import pandas as pd
from falkordb import FalkorDB

CSV_FILE = "security_logs.csv"

db = FalkorDB(host="localhost", port=6379)
graph = db.select_graph("GraphSentinel")

df = pd.read_csv(CSV_FILE)

required = {"user", "device", "ip", "risk"}
if not required.issubset(df.columns):
    raise ValueError(
        "CSV must contain columns: user, device, ip, risk"
    )

for _, row in df.iterrows():
    user = str(row["user"]).strip().replace("'", "")
    device = str(row["device"]).strip().replace("'", "")
    ip = str(row["ip"]).strip().replace("'", "")
    risk = str(row["risk"]).strip().lower()

    if not all([user, device, ip]) or risk not in {"high", "medium", "low"}:
        print(f"Skipping invalid row: {row.to_dict()}")
        continue

    graph.query("""
        MERGE (u:User {name: $user})
        SET u.risk = $risk
        MERGE (d:Device {name: $device})
        MERGE (i:IP {address: $ip})
        MERGE (u)-[:USED]->(d)
        MERGE (d)-[:CONNECTED_FROM]->(i)
    """, {
        "user": user,
        "device": device,
        "ip": ip,
        "risk": risk
    })

print(f"Imported {len(df)} CSV rows.")