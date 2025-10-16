import streamlit as st
import requests
import pandas as pd

# ---- CONFIG ----
API_URL = "https://your-fastapi-url.repl.co"  # 👈 Replace with your FastAPI URL

st.set_page_config(page_title="Aged Care Roster System", layout="wide")
st.title("👩‍⚕️ Aged Care Roster Dashboard")

# ---- SIDEBAR ----
st.sidebar.header("Navigation")
option = st.sidebar.radio("Go to:", ["Staff", "Leave", "Shifts", "Reports"])

# ---- STAFF PAGE ----
if option == "Staff":
    st.subheader("Staff List")
    try:
        response = requests.get(f"{API_URL}/staff")
        if response.status_code == 200:
            data = pd.DataFrame(response.json())
            st.dataframe(data)
        else:
            st.error("Could not fetch staff data.")
    except Exception as e:
        st.error(f"Error: {e}")

# ---- LEAVE PAGE ----
elif option == "Leave":
    st.subheader("Staff Leave Requests")
    try:
        response = requests.get(f"{API_URL}/leave")
        if response.status_code == 200:
            data = pd.DataFrame(response.json())
            st.dataframe(data)
        else:
            st.warning("No leave data found.")
    except Exception as e:
        st.error(f"Error: {e}")

# ---- SHIFTS PAGE ----
elif option == "Shifts":
    st.subheader("Shift Allocations")
    try:
        response = requests.get(f"{API_URL}/shift")
        if response.status_code == 200:
            data = pd.DataFrame(response.json())
            st.dataframe(data)
        else:
            st.warning("No shift data available.")
    except Exception as e:
        st.error(f"Error: {e}")

# ---- REPORTS PAGE ----
elif option == "Reports":
    st.subheader("Reports & Exports")
    st.info("Download upcoming PDF and Excel reports here.")
