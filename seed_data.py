from falkordb import FalkorDB

db = FalkorDB(host="localhost", port=6379)
graph = db.select_graph("GraphSentinel")

graph.query("""
CREATE (u:User {name: 'Alice', risk: 'high'})
-[:USED]->(d:Device {name: 'Unknown Laptop'})
-[:CONNECTED_FROM]->(i:IP {address: '185.220.101.5'})
""")

graph.query("""
CREATE (u:User {name: 'David', risk: 'medium'})
-[:USED]->(d:Device {name: 'Office Computer'})
-[:CONNECTED_FROM]->(i:IP {address: '192.168.1.50'})
""")

print("Alice and David added successfully!")