from campusflow.tickets import (
    create_ticket, assign_ticket, change_status,
    add_note, view_notes, open_work_queue
)
from campusflow.storage import load_tickets, save_tickets
from campusflow.search import search_tickets, sort_by_priority
from campusflow.reports import display_report
from campusflow.understanding_check import run_quiz


FILE = "tickets.json"


def show_tickets(tickets):
    for t in tickets:
        print(
            f'T{t["id"]:03} | {t["title"]} | {t["category"]} | '
            f'{t["priority"]} | {t["status"]} | {t["assigned_to"]}'
        )


def search_menu(tickets):
    title = input("Title search (Enter to skip): ").strip()

    categories = ["Network", "Hardware", "Software", "Other"]
    statuses = ["open", "in_progress", "resolved"]
    priorities = ["critical", "high", "medium", "low"]

    def choose_filter(label, options):
        while True:
            value = input(f"{label} {options} (Enter to skip): ").strip()

            if not value or value in options:
                return value

            print("Invalid option. Try again.")

    category = choose_filter("Category", categories)
    status = choose_filter("Status", statuses)
    priority = choose_filter("Priority", priorities)

    results = search_tickets(tickets, title, category, status, priority)

    if input("Sort results by priority? (y/n): ").strip().lower() == "y":
        results = sort_by_priority(results)

    if results:
        show_tickets(results)
    else:
        print("No matching tickets.")


def main():
    try:
        tickets = load_tickets(FILE)
        print("Tickets loaded.")
    except FileNotFoundError:
        tickets = []
        print("Starting with an empty ticket list.")
    except (ValueError, OSError) as error:
        print("Could not load tickets:", error)
        return

    while True:
        print("""
--- CAMPUSFLOW NEXT ---
1. Create ticket
2. Open work queue
3. Assign ticket
4. Change ticket status
5. Search tickets
6. Reports
7. Add follow-up note
8. View ticket notes
9. Engineering understanding check
10. Save and exit
""")

        choice = input("Choose an option: ").strip()

        try:
            if choice == "1":
                title = input("Title: ")
                category = input("Category (Network/Hardware/Software/Other): ")
                urgency = input("Urgency (low/medium/high): ")
                users = int(input("Affected users: "))

                create_ticket(tickets, title, category, urgency, users)
                print("Ticket created.")

            elif choice == "2":
                show_tickets(open_work_queue(tickets))

            elif choice == "3":
                ticket_id = int(input("Ticket ID: "))
                staff = input("Staff name: ")
                assign_ticket(tickets, ticket_id, staff)
                print("Ticket assigned.")

            elif choice == "4":
                ticket_id = int(input("Ticket ID: "))
                status = input("New status (open/in_progress/resolved): ")
                change_status(tickets, ticket_id, status)
                print("Status updated.")

            elif choice == "5":
                search_menu(tickets)

            elif choice == "6":
                display_report(tickets)

            elif choice == "7":
                ticket_id = int(input("Ticket ID: "))
                author = input("Author: ")
                message = input("Note: ")
                add_note(tickets, ticket_id, author, message)
                print("Note added.")

            elif choice == "8":
                ticket_id = int(input("Ticket ID: "))
                for note in view_notes(tickets, ticket_id):
                    print(note["note_id"], note["author"], note["message"])

            elif choice == "9":
                run_quiz()

            elif choice == "10":
                save_tickets(FILE, tickets)
                print("Tickets saved. Goodbye!")
                break

            else:
                print("Choose a number from 1 to 10.")

        except (ValueError, KeyError, TypeError) as error:
            print("Action failed:", error)


if __name__ == "__main__":
    main()
