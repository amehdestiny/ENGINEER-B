def generate_report(tickets):
    total = len(tickets)

    statuses = ["open", "in_progress", "resolved"]
    priorities = ["critical", "high", "medium", "low"]
    categories = ["Network", "Hardware", "Software", "Other"]

    by_status = {
        s: sum(t["status"] == s for t in tickets)
        for s in statuses
    }

    by_priority = {
        p: sum(t["priority"] == p for t in tickets)
        for p in priorities
    }

    by_category = {
        c: sum(t["category"] == c for t in tickets)
        for c in categories
    }

    resolved = by_status["resolved"]

    return {
        "total": total,
        "by_status": by_status,
        "by_priority": by_priority,
        "by_category": by_category,
        "unresolved": by_status["open"] + by_status["in_progress"],
        "resolved": resolved,
        "resolution_percentage": round(resolved / total * 100, 2) if total else 0
    }


def display_report(tickets):
    report = generate_report(tickets)

    print("\n--- CAMPUSFLOW REPORT ---")
    print("Total tickets:", report["total"])
    print("By status:", report["by_status"])
    print("By priority:", report["by_priority"])
    print("By category:", report["by_category"])
    print("Unresolved:", report["unresolved"])
    print("Resolved:", report["resolved"])
    print("Resolution:", report["resolution_percentage"], "%")
