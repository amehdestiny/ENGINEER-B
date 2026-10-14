def search_tickets(tickets, title="", category="", status="", priority=""):
    results = []

    for ticket in tickets:
        if title.casefold() not in ticket["title"].casefold():
            continue
        if category and ticket["category"] != category:
            continue
        if status and ticket["status"] != status:
            continue
        if priority and ticket["priority"] != priority:
            continue

        results.append(ticket)

    return results


def sort_by_priority(tickets):
    order = {"critical": 1, "high": 2, "medium": 3, "low": 4}
    return sorted(tickets, key=lambda t: (order[t["priority"]], t["id"]))