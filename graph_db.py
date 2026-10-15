

from falkordb import FalkorDB

print("Starting GraphSentinel...")

db = FalkorDB(host="localhost", port=6379)
graph = db.select_graph("GraphSentinel")

graph.query("CREATE (:Person {name: 'Test User'})")

print("GraphSentinel connected to FalkorDB!")