import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.io as pio
import matplotlib.pyplot as plt
import seaborn as sns

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet

# =====================================
# PLOTLY THEME
# =====================================

pio.templates.default = "plotly_dark"

# =====================================
# PAGE CONFIG
# =====================================

st.set_page_config(
    page_title="Industrial Safety Dashboard",
    layout="wide"
)

# =====================================
# CUSTOM CSS
# =====================================

st.markdown("""
<style>

[data-testid="metric-container"] {
    background-color: #1e293b;
    border: 1px solid #334155;
    padding: 20px;
    border-radius: 15px;
    text-align: center;
    box-shadow: 0px 4px 10px rgba(0,0,0,0.3);
}

[data-testid="metric-container"] label {
    font-size: 18px !important;
    font-weight: 600 !important;
}

[data-testid="metric-container"] div {
    font-size: 28px !important;
}

</style>
""", unsafe_allow_html=True)

# =====================================
# TITLE
# =====================================

st.title(
    "Industrial Safety Surveillance Analytics | Gotisheel Technologies"
)

st.markdown("""
AI-powered industrial safety monitoring dashboard
for surveillance analytics, compliance monitoring,
and operational risk assessment.
""")

# =====================================
# LOAD DATA
# =====================================

df = pd.read_csv(
    "industrial_safety_events_dataset_updated.csv"
)

df['created_at'] = pd.to_datetime(df['created_at'])

# =====================================
# SIDEBAR FILTERS
# =====================================

st.sidebar.header("Dashboard Filters")

selected_zone = st.sidebar.selectbox(
    "Select Zone",
    ["All"] + list(df['zone'].unique())
)

selected_label = st.sidebar.selectbox(
    "Select Violation",
    ["All"] + list(df['label'].unique())
)

# =====================================
# FILTER DATA
# =====================================

filtered_df = df.copy()

if selected_zone != "All":
    filtered_df = filtered_df[
        filtered_df['zone'] == selected_zone
    ]

if selected_label != "All":
    filtered_df = filtered_df[
        filtered_df['label'] == selected_label
    ]

# =====================================
# BUSINESS CALCULATIONS
# =====================================

safe_labels = [
    'mask',
    'hairnet',
    'person'
]

compliant = filtered_df[
    filtered_df['label'].isin(safe_labels)
]

compliance_percentage = (
    len(compliant)
    /
    len(filtered_df)
) * 100

high_risk_count = len(
    filtered_df[
        filtered_df['label'].isin(
            ['fire', 'smoke', 'fall']
        )
    ]
)

false_positive_rate = (
    filtered_df['false_positive'].mean()
) * 100

top_violation = (
    filtered_df['label']
    .value_counts()
    .idxmax()
)

top_zone = (
    filtered_df['zone']
    .value_counts()
    .idxmax()
)

top_camera = (
    filtered_df['camera']
    .value_counts()
    .idxmax()
)

peak_hour = (
    filtered_df['created_at']
    .dt.hour
    .value_counts()
    .idxmax()
)

# =====================================
# RISK SCORE
# =====================================

fire_count = len(
    filtered_df[
        filtered_df['label'] == 'fire'
    ]
)

smoke_count = len(
    filtered_df[
        filtered_df['label'] == 'smoke'
    ]
)

fall_count = len(
    filtered_df[
        filtered_df['label'] == 'fall'
    ]
)

risk_score = (
    fire_count * 5 +
    smoke_count * 4 +
    fall_count * 5
)

# =====================================
# SEVERITY CLASSIFICATION
# =====================================

critical = [
    'fire',
    'smoke',
    'fall'
]

major = [
    'without_helmet',
    'without_glove',
    'without_boot',
    'without_goggle',
    'no_harness'
]

critical_count = len(
    filtered_df[
        filtered_df['label'].isin(critical)
    ]
)

major_count = len(
    filtered_df[
        filtered_df['label'].isin(major)
    ]
)

minor_count = (
    len(filtered_df)
    - critical_count
    - major_count
)


# =====================================
# PDF REPORT FUNCTION
# =====================================

def generate_pdf():

    pdf_file = "Executive_Safety_Report.pdf"

    doc = SimpleDocTemplate(pdf_file)

    styles = getSampleStyleSheet()

    content = []

    content.append(
        Paragraph(
            "Industrial Safety Executive Report",
            styles['Title']
        )
    )

    content.append(Spacer(1, 12))

    content.append(
        Paragraph(
            "Generated from Industrial Safety Surveillance Analytics Dashboard",
            styles['Normal']
        )
    )

    content.append(Spacer(1, 12))

    content.append(
        Paragraph(
            f"<b>Total Events:</b> {len(filtered_df)}",
            styles['Normal']
        )
    )

    content.append(
        Paragraph(
            f"<b>Total Cameras:</b> {filtered_df['camera'].nunique()}",
            styles['Normal']
        )
    )

    content.append(
        Paragraph(
            f"<b>Total Zones:</b> {filtered_df['zone'].nunique()}",
            styles['Normal']
        )
    )

    content.append(
        Paragraph(
            f"<b>Average Confidence:</b> {filtered_df['score'].mean():.2f}",
            styles['Normal']
        )
    )

    content.append(
        Paragraph(
            f"<b>Compliance Rate:</b> {compliance_percentage:.2f}%",
            styles['Normal']
        )
    )

    content.append(
        Paragraph(
            f"<b>High Risk Events:</b> {high_risk_count}",
            styles['Normal']
        )
    )

    content.append(
        Paragraph(
            f"<b>Plant Risk Score:</b> {risk_score}",
            styles['Normal']
        )
    )

    content.append(Spacer(1, 20))

    content.append(
        Paragraph(
            "Executive Insights",
            styles['Heading2']
        )
    )

    content.append(
        Paragraph(
            f"Most Recurring Violation: {top_violation}",
            styles['Normal']
        )
    )

    content.append(
        Paragraph(
            f"Highest Risk Zone: {top_zone}",
            styles['Normal']
        )
    )

    content.append(
        Paragraph(
            f"Most Active Camera: {top_camera}",
            styles['Normal']
        )
    )

    content.append(
        Paragraph(
            f"Peak Unsafe Hour: {peak_hour}:00 hrs",
            styles['Normal']
        )
    )
    content.append(Spacer(1, 20))

    content.append(
        Paragraph(
            "Recommended Action:",
            styles['Heading2']
        )
    )

    content.append(
        Paragraph(
            f"""
            Focus monitoring efforts in {top_zone}.
            Conduct additional training related to {top_violation}.
            Review safety procedures for high-risk incidents.
            Monitor camera {top_camera} closely as it has generated the highest number of alerts.
            """,
            styles['Normal']
        )
    )

    doc.build(content)

    return pdf_file


# =====================================
# EXECUTIVE KPI SECTION
# =====================================

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
    "Total Zones",
    filtered_df['zone'].nunique()
)

col4.metric(
    "Average Confidence",
    round(
        filtered_df['score'].mean(),
        2
    )
)

# =====================================
# RISK & COMPLIANCE SUMMARY
# =====================================

st.markdown("## Risk & Compliance Overview")

c1,c2,c3,c4 = st.columns(4)

with c1:
    st.info(
        f"""
        ### Compliance Rate

        **{compliance_percentage:.2f}%**
        """
    )

with c2:
    st.warning(
        f"""
        ### High Risk Events

        **{high_risk_count}**
        """
    )

with c3:
    st.error(
        f"""
        ### False Positive Rate

        **{false_positive_rate:.2f}%**
        """
    )

with c4:
    st.success(
        f"""
        ### Plant Risk Score

        **{risk_score}**
        """
    )


# =====================================
# INCIDENT SEVERITY OVERVIEW
# =====================================

st.markdown("## Incident Severity Overview")

severity_data = pd.DataFrame({
    "Severity": [
        "Critical",
        "Major",
        "Minor"
    ],
    "Count": [
        critical_count,
        major_count,
        minor_count
    ]
})

fig_severity = px.pie(
    severity_data,
    values="Count",
    names="Severity",
    hole=0.55,
    color="Severity",
    color_discrete_map={
        "Critical": "#ef4444",
        "Major": "#f59e0b",
        "Minor": "#22c55e"
    },
    title="Incident Severity Distribution"
)

fig_severity.update_layout(
    template="plotly_dark",
    height=450
)

st.plotly_chart(
    fig_severity,
    use_container_width=True
)


# =====================================
# KEY INSIGHTS
# =====================================

st.markdown("## Key Insights")

st.success(
    f"Most Recurring Violation: {top_violation}"
)

st.warning(
    f"Highest Risk Zone: {top_zone}"
)

st.info(
    f"Most Active Camera: {top_camera}"
)

# =====================================
# EVENT DISTRIBUTION
# =====================================

st.divider()

st.subheader(
    "Event Distribution"
)

label_counts = (
    filtered_df['label']
    .value_counts()
)

fig1 = px.pie(
    values=label_counts.values,
    names=label_counts.index,
    title="Violation Distribution"
)

fig1.update_layout(
    template="plotly_dark"
)

st.plotly_chart(
    fig1,
    use_container_width=True
)

# =====================================
# DAILY EVENT TREND
# =====================================

st.divider()

st.subheader(
    "Daily Event Trend"
)

daily_events = filtered_df.groupby(
    filtered_df['created_at'].dt.date
).size()

fig2 = px.line(
    x=daily_events.index,
    y=daily_events.values,
    markers=True
)

fig2.update_layout(
    template="plotly_dark"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

# =====================================
# HOURLY EVENT TREND
# =====================================

st.divider()

st.subheader(
    "Hourly Violation Trend"
)

filtered_df['hour'] = (
    filtered_df['created_at']
    .dt.hour
)

hourly_events = (
    filtered_df
    .groupby('hour')
    .size()
)

fig3 = px.line(
    x=hourly_events.index,
    y=hourly_events.values,
    markers=True
)

fig3.update_layout(
    template="plotly_dark"
)

st.plotly_chart(
    fig3,
    use_container_width=True
)


# =====================================
# CAMERA ANALYTICS
# =====================================

st.divider()

st.subheader("Top 10 Cameras by Violations")

top10 = (
    filtered_df['camera']
    .value_counts()
    .head(10)
)

fig_top = px.bar(
    x=top10.index,
    y=top10.values,
    color=top10.values,
    title="Top 10 Cameras"
)

st.plotly_chart(
    fig_top,
    use_container_width=True
)


# =====================================
# ZONE ANALYTICS
# =====================================

st.divider()

st.subheader(
    "Zone-wise Incidents"
)

zone_counts = (
    filtered_df['zone']
    .value_counts()
)

fig6 = px.bar(
    x=zone_counts.index,
    y=zone_counts.values,
    color=zone_counts.values,
    title="Zone-wise Incident Count"
)

fig6.update_layout(
    template="plotly_dark"
)

st.plotly_chart(
    fig6,
    use_container_width=True
)

# =====================================
# ZONE VS VIOLATION HEATMAP
# =====================================

st.divider()

st.subheader(
    "Zone vs Violation Heatmap"
)

heatmap_data = pd.crosstab(
    filtered_df['zone'],
    filtered_df['label']
)

fig, ax = plt.subplots(
    figsize=(14, 6)
)

sns.heatmap(
    heatmap_data,
    annot=True,
    fmt='d',
    cmap='YlOrRd',
    ax=ax
)

st.pyplot(fig)

# =====================================
# HIGH RISK ANALYSIS
# =====================================

st.divider()

st.subheader(
    "High Risk Event Analysis"
)

high_risk = filtered_df[
    filtered_df['label'].isin(
        ['fire', 'smoke', 'fall']
    )
]

risk_counts = (
    high_risk['label']
    .value_counts()
)

if len(risk_counts) > 0:

    fig7 = px.bar(
        x=risk_counts.index,
        y=risk_counts.values,
        color=risk_counts.values,
        title="Critical Safety Events"
    )

    fig7.update_layout(
        template="plotly_dark"
    )

    st.plotly_chart(
        fig7,
        use_container_width=True
    )

else:

    st.warning(
        "No high risk events available."
    )

# =====================================
# CONFIDENCE DISTRIBUTION
# =====================================

st.divider()

st.subheader(
    "Detection Confidence Distribution"
)

fig8 = px.histogram(
    filtered_df,
    x='score',
    nbins=20,
    title="Confidence Score Distribution"
)

fig8.update_layout(
    template="plotly_dark"
)

st.plotly_chart(
    fig8,
    use_container_width=True
)

# =====================================
# MOTION ANALYSIS
# =====================================

st.divider()

st.subheader(
    "Motion Analysis"
)

fig9 = px.scatter(
    filtered_df,
    x='motionless_count',
    y='position_changes',
    color='label',
    title="Motion Behaviour Analysis"
)

st.plotly_chart(
    fig9,
    use_container_width=True
)

# =====================================
# AI RECOMMENDATIONS
# =====================================

st.divider()

st.markdown(
    "## AI Safety Recommendations"
)

if top_violation == "without_helmet":

    st.warning(
        """
        Recommendation:
        
        Conduct PPE awareness training,
        strengthen helmet compliance checks,
        and increase monitoring frequency.
        """
    )

elif top_violation == "fire":

    st.warning(
        """
        Recommendation:
        
        Review fire safety protocols,
        inspect extinguishers,
        and conduct emergency drills.
        """
    )

elif top_violation == "smoke":

    st.warning(
        """
        Recommendation:
        
        Investigate smoke sources,
        improve ventilation systems,
        and perform safety inspections.
        """
    )

else:

    st.info(
        """
        Recommendation:
        
        Continue routine monitoring and
        maintain current safety practices.
        """
    )

# =====================================
# EXECUTIVE INSIGHTS
# =====================================

st.divider()

st.markdown(
    "## Executive Insights"
)

st.success(
    f"Most recurring violation detected: {top_violation}"
)

st.warning(
    f"Highest risk operational zone: {top_zone}"
)

st.info(
    f"Most active surveillance camera: {top_camera}"
)

st.error(
    f"Peak unsafe activity observed around: {peak_hour}:00 hrs"
)

# =====================================
# EVENT DATA
# =====================================

st.divider()

st.subheader(
    "Event Data Preview"
)

st.dataframe(
    filtered_df.head(50)
)

# =====================================
# DOWNLOAD SECTION
# =====================================

st.divider()

st.markdown(
    "## Export Reports"
)

csv = filtered_df.to_csv(
    index=False
)

st.download_button(
    label="⬇ Download Filtered Dataset",
    data=csv,
    file_name="filtered_safety_data.csv",
    mime="text/csv"
)

pdf_file = generate_pdf()

with open(pdf_file, "rb") as pdf:

    st.download_button(
        label="📄 Download Executive PDF Report",
        data=pdf,
        file_name="Executive_Safety_Report.pdf",
        mime="application/pdf"
    )

# =====================================
# FOOTER
# =====================================

st.divider()

st.caption(
    "Industrial Safety Surveillance Analytics Dashboard | Gotisheel Technologies LLP"
)

