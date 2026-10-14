QUESTIONS = [
    ("An unassigned ticket moves to in_progress.",
     ["Accept", "Reject and preserve data", "Resolve it", "Delete it"], "B"),

    ("What is the resolution percentage with zero tickets?",
     ["Crash", "100%", "0%", "Divides by one"], "C"),

    ("How should combined search filters work?",
     ["Match any filter", "Match all filters", "Network only", "Open only"], "B"),

    ("What happens when a resolved ticket receives a new note?",
     ["Append it", "Delete old notes", "Reject until reopened", "Change status"], "C"),

    ("What happens when JSON contains duplicate ticket IDs?",
     ["Keep both", "Replace memory", "Rejects the load", "Rename IDs"], "C"),

    ("A PR changes validation but has no negative tests.",
     ["Approved immediately", "Request focused tests", "Merge immediately", "Ask AI to approve"], "B")
]


def calculate_score(answers):
    return sum(
        answer == question[2]
        for question, answer in zip(QUESTIONS, answers)
    )


def run_quiz():
    answers = []

    for number, (question, options, correct) in enumerate(QUESTIONS, 1):
        print(f"\nQ{number}. {question}")

        for letter, option in zip("ABCD", options):
            print(f"{letter}. {option}")

        while True:
            answer = input("Your answer (A/B/C/D): ").strip().upper()

            if answer in "ABCD" and len(answer) == 1:
                answers.append(answer)
                break

            print("Invalid choice. Enter A, B, C, or D.")

    print(f"\nYour score: {calculate_score(answers)}/6")

    for number in (1, 2):
        explanation = input(
            f"Please explain why your answer to Q{number} is correct: "
        ).strip()

        print("Your explanation:", explanation)
