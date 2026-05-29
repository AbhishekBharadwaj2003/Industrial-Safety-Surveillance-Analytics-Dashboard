import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.io as pio

# PLOTLY THEME
pio.templates.default = "plotly_dark"

# PAGE CONFIG
st.set_page_config(
    page_title="Industrial Safety Dashboard",
    layout="wide"
)

# CUSTOM CSS
st.markdown("""
<style>

/* Main background */
.main {
    background-color: #0f172a;
}

/* Metric cards */
[data-testid="metric-container"] {
    background-color: #1e293b;
    border: 1px solid #334155;
    padding: 15px;
    border-radius: 12px;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background-color: #111827;
}

/* Titles */
h1, h2, h3 {
    color: #f8fafc;
}

/* Dataframe */
[data-testid="stDataFrame"] {
    border-radius: 10px;
}

</style>
""", unsafe_allow_html=True)

# TITLE
st.title("Industrial Safety Surveillance Analytics | Gotisheel Technologies")

st.markdown("""
AI-powered industrial safety monitoring dashboard for surveillance analytics, compliance monitoring, and operational risk assessment.
""")

# LOAD DATA
df = pd.read_csv(
    r"E:\PERSONAL\EXTRA\GOTISHEEL TECHNOLOGIES\industrial_safety_events_dataset.csv"
)

# DATE CONVERSION
df['created_at'] = pd.to_datetime(df['created_at'])

# SIDEBAR
st.sidebar.header("Dashboard Filters")

selected_zone = st.sidebar.selectbox(
    "Select Zone",
    ["All"] + list(df['zone'].unique())
)

selected_label = st.sidebar.selectbox(
    "Select Violation",
    ["All"] + list(df['label'].unique())
)

# FILTERING
filtered_df = df.copy()

if selected_zone != "All":
    filtered_df = filtered_df[
        filtered_df['zone'] == selected_zone
    ]

if selected_label != "All":
    filtered_df = filtered_df[
        filtered_df['label'] == selected_label
    ]

# KPI SECTION
st.markdown("## Executive Safety Summary")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Events",
    len(filtered_df)
)

col2.metric(
    "Total Cameras",
    filtered_df['camera'].nunique()
)

col3.metric(
    "Zones",
    filtered_df['zone'].nunique()
)

col4.metric(
    "Average Confidence",
    round(filtered_df['score'].mean(), 2)
)

# SAFETY COMPLIANCE
safe_labels = ['mask', 'hairnet', 'person']

compliant = filtered_df[
    filtered_df['label'].isin(safe_labels)
]

compliance_percentage = (
    len(compliant) / len(filtered_df)
) * 100

# HIGH RISK EVENTS
high_risk_count = len(
    filtered_df[
        filtered_df['label'].isin(['fire', 'smoke', 'fall'])
    ]
)

# FALSE POSITIVE RATE
false_positive_rate = (
    filtered_df['false_positive'].mean()
) * 100

st.success(
    f"Safety Compliance Rate: {compliance_percentage:.2f}%"
)

st.warning(
    f"High Risk Events Detected: {high_risk_count}"
)

st.info(
    f"False Positive Rate: {false_positive_rate:.2f}%"
)

# INSIGHTS
st.markdown("## Key Insights")

top_violation = filtered_df['label'].value_counts().idxmax()

top_zone = filtered_df['zone'].value_counts().idxmax()

top_camera = filtered_df['camera'].value_counts().idxmax()

st.write(
    f"Most recurring violation: {top_violation}"
)

st.write(
    f"Highest risk zone: {top_zone}"
)

st.write(
    f"Most active camera: {top_camera}"
)

# EVENT DISTRIBUTION
st.divider()
st.subheader("Event Distribution")

label_counts = filtered_df['label'].value_counts()

fig1 = px.pie(
    values=label_counts.values,
    names=label_counts.index
)

fig1.update_layout(
    template="plotly_dark"
)

st.plotly_chart(fig1, use_container_width=True)

# DAILY EVENT TREND
st.divider()
st.subheader("Daily Event Trend")

daily_events = filtered_df.groupby(
    filtered_df['created_at'].dt.date
).size()

fig2 = px.line(
    x=daily_events.index,
    y=daily_events.values
)

fig2.update_layout(
    template="plotly_dark"
)

st.plotly_chart(fig2, use_container_width=True)

# CAMERA ANALYSIS
st.divider()
st.subheader("Camera-wise Violations")

camera_counts = filtered_df['camera'].value_counts().head(10)

fig3 = px.bar(
    x=camera_counts.index,
    y=camera_counts.values,
    color=camera_counts.values
)

fig3.update_layout(
    template="plotly_dark"
)

st.plotly_chart(fig3, use_container_width=True)

# ZONE ANALYSIS
st.divider()
st.subheader("Zone-wise Incidents")

zone_counts = filtered_df['zone'].value_counts()

fig4 = px.bar(
    x=zone_counts.index,
    y=zone_counts.values,
    color=zone_counts.values
)

fig4.update_layout(
    template="plotly_dark"
)

st.plotly_chart(fig4, use_container_width=True)

# HOURLY ANALYSIS
st.divider()
st.subheader("Hourly Violation Trend")

filtered_df['hour'] = filtered_df['created_at'].dt.hour

hourly_events = filtered_df.groupby('hour').size()

fig5 = px.line(
    x=hourly_events.index,
    y=hourly_events.values
)

fig5.update_layout(
    template="plotly_dark"
)

st.plotly_chart(fig5, use_container_width=True)


# HIGH RISK ANALYSIS

st.divider()
st.subheader("High Risk Events")

high_risk = filtered_df[
    filtered_df['label'].isin(['fire', 'smoke', 'fall'])
]

risk_counts = high_risk['label'].value_counts()

if len(risk_counts) > 0:

    fig6 = px.bar(
        x=risk_counts.index,
        y=risk_counts.values,
        color=risk_counts.values
    )

    fig6.update_layout(
        template="plotly_dark"
    )

    st.plotly_chart(fig6, use_container_width=True)

else:
    st.warning(
        "No high risk events available for selected filters."
    )

# DATA TABLE
st.divider()
st.subheader("Event Data")

st.dataframe(filtered_df.head(50))

# EXECUTIVE INSIGHTS
st.divider()
st.markdown("## Executive Insights")

peak_hour = filtered_df['created_at'].dt.hour.value_counts().idxmax()

st.write(
    f"Most recurring violation detected: {top_violation}"
)

st.write(
    f"Highest risk operational zone: {top_zone}"
)

st.write(
    f"Most active surveillance camera: {top_camera}"
)

st.write(
    f"Peak unsafe activity observed around: {peak_hour}:00 hrs"
)

# DOWNLOAD BUTTON
csv = filtered_df.to_csv(index=False)

st.download_button(
    label="Download Filtered Data",
    data=csv,
    file_name="filtered_safety_data.csv",
    mime="text/csv"
)

# FOOTER
st.divider()

st.caption(
    "Industrial Safety Surveillance Analytics Dashboard | Gotisheel Technologies"
)