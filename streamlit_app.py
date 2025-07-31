import streamlit as st
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Title
st.title('📦 Shipment by Product Type')

# Connect to SQLite DB
conn = sqlite3.connect('app.db')
query = "SELECT product_type, SUM(shipment_count) as total FROM shipments GROUP BY product_type"
df = pd.read_sql_query(query, conn)
conn.close()

# Plotting Bar Chart
fig, ax = plt.subplots()
ax.bar(df['product_type'], df['total'], color='orange')
ax.set_xlabel('Product Type')
ax.set_ylabel('Total Shipments')
ax.set_title('Total Shipments by Product Type')
ax.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()

# Show Chart in Streamlit
st.pyplot(fig)