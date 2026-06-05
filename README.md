# Industrial Safety Surveillance Analytics Platform

## Overview

The Industrial Safety Surveillance Analytics Platform is an end-to-end safety monitoring and analytics solution developed to simulate, analyze, and visualize industrial surveillance events. The project leverages synthetic surveillance data to generate actionable safety insights, identify operational risks, monitor compliance, and support management-level decision-making through interactive dashboards and automated reporting.

The platform was developed as part of an industrial Data Analytics and AI internship project and demonstrates the application of analytics, visualization, and business intelligence techniques in industrial safety environments.

---

## Project Objectives

* Monitor industrial safety violations and incidents.
* Analyze surveillance event patterns across cameras and operational zones.
* Identify high-risk events and unsafe operational conditions.
* Measure safety compliance and false-positive detection rates.
* Generate executive-level safety insights and reports.
* Provide an interactive dashboard for operational monitoring.

---

## Dataset Overview

A synthetic industrial surveillance dataset was generated based on a MongoDB-inspired event schema.

### Dataset Statistics

* **Total Events:** 3,500+
* **Total Cameras:** 1,000
* **Multiple events per camera**
* Multiple operational zones and units
* Realistic timestamps and event durations

### Event Labels

* without_helmet
* without_boot
* without_goggle
* without_glove
* fall
* person
* no_ifr
* no_harness
* smoker
* license_plate
* no_extinguisher
* fire
* smoke
* cell_phone
* hairnet
* nohairnet
* mask
* nomask
* crowd
* loitering

---

## Exploratory Data Analysis (EDA)

The following analyses were performed:

### Data Quality Analysis

* Dataset overview
* Missing value analysis
* Descriptive statistics
* Data type validation

### Event Analytics

* Event distribution analysis
* Daily event trends
* Hourly event trends
* Camera-wise incident analysis
* Zone-wise incident analysis

### Safety Analytics

* Safety compliance analysis
* High-risk event monitoring
* False positive analysis
* Confidence score analysis
* Motion behavior analysis

### Risk Assessment

* Plant Risk Score calculation
* Incident severity classification
* Critical event monitoring
* Operational risk identification

---

## Dashboard Features

### Interactive Filters

* Zone Filter
* Violation Filter

### Executive KPI Section

* Total Events
* Total Cameras
* Total Zones
* Average Detection Confidence

### Risk & Compliance Monitoring

* Safety Compliance Rate
* High Risk Events
* False Positive Rate
* Plant Risk Score

### Incident Severity Classification

* Critical Events
* Major Events
* Minor Events

### Visual Analytics

#### Event Analytics

* Event Distribution
* Daily Event Trend
* Hourly Event Trend

#### Camera Analytics

* Top 10 Cameras by Violations
* Camera Performance Monitoring

#### Zone Analytics

* Zone-wise Incident Analysis
* Zone vs Violation Heatmap

#### Safety Analytics

* High Risk Event Analysis
* Detection Confidence Distribution
* Motion Behavior Analysis

### AI-Powered Recommendations

The dashboard provides automated safety recommendations based on the most frequently occurring violations and operational risk patterns.

### Executive Reporting

* Download Filtered Dataset (CSV)
* Executive PDF Report Generation
* Management-Level Safety Insights

---

## Technology Stack

### Programming & Analytics

* Python
* Pandas
* NumPy

### Visualization

* Plotly
* Matplotlib
* Seaborn

### Dashboard Development

* Streamlit

### Reporting

* ReportLab

---

## Key Performance Indicators (KPIs)

* Total Events
* Total Cameras
* Total Zones
* Average Confidence Score
* Safety Compliance Rate
* False Positive Rate
* High Risk Event Count
* Plant Risk Score
* Critical Incident Count
* Major Incident Count
* Minor Incident Count

---

## Dashboard Workflow

```text
Industrial Surveillance Event Data
                │
                ▼
Data Cleaning & Preprocessing
                │
                ▼
Exploratory Data Analysis
                │
                ▼
Risk Assessment & KPI Generation
                │
                ▼
Interactive Streamlit Dashboard
                │
                ▼
Executive Insights & Reporting
```

---

## How to Run

### Clone Repository

```bash
git clone <repository-link>
cd Industrial-Safety-Surveillance-Analytics
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Launch Dashboard

```bash
streamlit run dashboard.py
```

---

## Future Enhancements

### Data Engineering

* MongoDB Integration
* Real-Time Data Pipeline
* Automated Data Ingestion

### Artificial Intelligence

* AI-Powered Incident Summaries
* Predictive Risk Analytics
* Violation Forecasting
* Anomaly Detection

### Surveillance Enhancements

* Live CCTV Event Streaming
* Real-Time Alert System
* Camera Health Monitoring
* Safety Notification Engine

### Reporting

* Automated Daily Reports
* Email Alert Integration
* Scheduled Executive Reporting

---

## Project Outcomes

* Developed a realistic industrial surveillance dataset with 3,500+ events.
* Built a comprehensive safety analytics dashboard.
* Implemented operational risk monitoring and safety compliance tracking.
* Generated management-level safety insights and automated reports.
* Demonstrated practical applications of Data Analytics, Business Intelligence, and AI-driven decision support in industrial safety environments.

---

### Developed as part of a Data Analytics & AI Internship Project at Gotisheel Technologies LLP.
