from falkordb import FalkorDB

db = FalkorDB(host="localhost", port=6379)
graph = db.select_graph("GraphSentinel")


def investigate():
    result = graph.query("""
        MATCH (u:User)-[:USED]->(d:Device)-[:CONNECTED_FROM]->(i:IP)
        RETURN u.name, u.risk, d.name, i.address
    """)

    print("\n=== GraphSentinel Investigation Report ===")

    if not result.result_set:
        print("No connections found.")
        return

    for row in result.result_set:
        user, risk, device, ip = row

        score = {"high": 90, "medium": 60, "low": 20}.get(
            risk.lower(), 10
        )

        print(f"\nUser: {user}")
        print(f"Risk Level: {risk.upper()}")
        print(f"Risk Score: {score}/100")
        print(f"Device: {device}")
        print(f"IP Address: {ip}")

        if score >= 80:
            print("Alert: High priority investigation.")
            print("Reason: User is marked high-risk.")
        elif score >= 50:
            print("Alert: Further review recommended.")
            print("Reason: User has a medium-risk classification.")
        else:
            print("Alert: Low priority.")

if __name__ == "__main__":
    investigate()