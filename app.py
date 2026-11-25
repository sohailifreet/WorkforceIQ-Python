# ==========================================
# WorkforceIQ - Employee Analytics Dashboard
# ==========================================

import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Configure the dashboard
st.set_page_config(
    page_title="WorkforceIQ",
    page_icon="👥",
    layout="wide"
)

# 2. Dashboard heading
st.title("👥 WorkforceIQ")
st.subheader("Employee Management & Analytics")
st.caption("Smart Workforce Management System")

# 3. Sample employee data
employee_data = {
    "Employee": ["Sohail", "Priya", "Amit", "Sneha",
                 "Arjun", "Neha"],
    "Department": ["IT", "HR", "IT", "Finance",
                   "HR", "Finance"],
    "Attendance": ["Present", "Present", "Absent",
                   "Present", "Present", "Absent"],
    "Salary": [40000, 35000, 45000, 38000, 32000, 42000]
}

# 4. Convert data into a Pandas DataFrame
df = pd.DataFrame(employee_data)

# 5. Calculate employee statistics
total_employees = len(df)
present = (df["Attendance"] == "Present").sum()
absent = (df["Attendance"] == "Absent").sum()
attendance_rate = (present / total_employees) * 100
total_payroll = df["Salary"].sum()

# 6. Display dashboard metrics
st.divider()

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Employees", total_employees)
col2.metric("Present Today", present)
col3.metric("Absent Today", absent)
col4.metric("Attendance Rate", f"{attendance_rate:.1f}%")

st.divider()

# 7. Display employee information
st.subheader("Employee Records")

st.dataframe(df, use_container_width=True)

# 8. Department-wise employee chart
st.subheader("Department-wise Workforce")

department_counts = df["Department"].value_counts().reset_index()
department_counts.columns = ["Department", "Employees"]

fig = px.bar(
    department_counts,
    x="Department",
    y="Employees",
    title="Employees by Department",
    color="Department"
)

st.plotly_chart(fig, use_container_width=True)

# 9. Payroll information
st.subheader("Payroll Overview")

st.metric("Total Monthly Payroll", f"₹{total_payroll:,.0f}")

st.success("WorkforceIQ Dashboard is running successfully!")
