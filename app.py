import streamlit as st
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import os
from falkordb import FalkorDB

st.set_page_config(page_title="GraphSentinel", page_icon="🛡️", layout="wide")
st.title("🛡️ GraphSentinel")
st.subheader("Graph-Based Security Threat Investigation")
st.caption("Investigate user-device-IP relationships to identify potential risks.")

# Demonstration data for cloud deployment
demo_data = [
    ["Alice", "high", "Unknown Laptop", "185.220.101.5"],
    ["David", "medium", "Office Computer", "192.168.1.50"],
    ["Priya", "low", "Work Laptop", "10.0.0.25"],
    ["Rahul", "high", "Unknown Phone", "45.155.205.233"],
]

def load_demo_data():
    return pd.DataFrame(
        demo_data,
        columns=["User", "Risk", "Device", "IP"]
    )

# Cloud mode uses sample data; local mode can connect to FalkorDB
if os.getenv("STREAMLIT_CLOUD") == "true":
    df = load_demo_data()
    st.info("Demo mode: displaying sample security records.")
else:
    try:
        db = FalkorDB(host="localhost", port=6379)
        graph = db.select_graph("GraphSentinel")
        result = graph.query("""
            MATCH (u:User)-[:USED]->(d:Device)-[:CONNECTED_FROM]->(i:IP)
            RETURN u.name, u.risk, d.name, i.address
        """).result_set

        if result:
            df = pd.DataFrame(
                result,
                columns=["User", "Risk", "Device", "IP"]
            )
        else:
            df = load_demo_data()
            st.warning("No graph records found. Showing sample data.")
    except Exception:
        df = load_demo_data()
        st.warning("FalkorDB unavailable. Showing sample data for demonstration.")

df["Risk"] = df["Risk"].str.lower()
df["Score"] = df["Risk"].map({"high": 90, "medium": 60, "low": 20})

a, b, c = st.columns(3)
a.metric("Users Investigated", df["User"].nunique())
b.metric("High-Risk Users", df.loc[df["Risk"] == "high", "User"].nunique())
c.metric("Connections", len(df))

st.subheader("📋 Security Investigation Records")
st.dataframe(df, use_container_width=True, hide_index=True)

st.subheader("🔎 Investigate a User")
selected = st.selectbox("Select user", sorted(df["User"].unique()))
user = df[df["User"] == selected].iloc[0]

st.write(f"**Risk level:** {user['Risk'].upper()} | **Demo score:** {user['Score']}/100")
st.write(f"**Device:** {user['Device']} | **IP:** {user['IP']}")

if user["Risk"] == "high":
    st.warning("Recommended action: Review authentication logs and verify the device/IP.")
elif user["Risk"] == "medium":
    st.info("Recommended action: Review recent activity for unusual access patterns.")
else:
    st.success("Recommended action: Continue routine monitoring.")

st.subheader("🕸️ User–Device–IP Relationship Graph")
G = nx.Graph()

for _, row in df.iterrows():
    G.add_edge(row["User"], row["Device"])
    G.add_edge(row["Device"], row["IP"])

fig, ax = plt.subplots(figsize=(12, 6))
nx.draw_networkx(G, ax=ax, with_labels=True, node_size=1800, font_size=8)
ax.axis("off")
st.pyplot(fig)
plt.close(fig)

st.caption(
    "Risk labels and scores are demonstration values, not verified threat intelligence."
)