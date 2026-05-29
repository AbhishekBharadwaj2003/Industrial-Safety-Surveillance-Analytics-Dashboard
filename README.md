# Industrial Safety Surveillance Analytics Dashboard

## Overview

This project simulates and analyzes industrial safety surveillance events using synthetic event data generated in a MongoDB-inspired schema. The dashboard provides insights into safety compliance, operational risks, camera-wise incidents, zone-wise monitoring, and high-risk safety events.

## Features

* Interactive Streamlit dashboard
* Event distribution analysis
* Camera-wise violation monitoring
* Zone-wise incident analysis
* Hourly event trend visualization
* Safety compliance tracking
* High-risk event monitoring (Fire, Smoke, Fall)
* False positive analysis
* Downloadable filtered datasets

## Technology Stack

* Python
* Pandas
* Plotly
* Streamlit
* NumPy
* Matplotlib
* Seaborn

## Key Metrics

* Total Events
* Total Cameras
* Total Zones
* Average Detection Confidence
* Safety Compliance Rate
* False Positive Rate
* High Risk Events



## How to Run

```bash
pip install -r requirements.txt
python -m streamlit run dashboard.py
```

## Future Enhancements

* Real-time MongoDB integration
* Live CCTV event streaming
* AI-powered incident summaries
* Predictive risk analytics
* Alert notification system



