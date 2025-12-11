# Part 2: Business Intelligence Dashboard Documentation

## 1. Overview

This dashboard was developed using **Streamlit** to provide business users with actionable insights on campaign performance, lead outcomes, and advertising efficiency. The goal is to help users understand whether their marketing spend is effective and to make informed decisions regarding campaigns and leads.

The dashboard integrates multiple cleaned datasets:
- `campaigns_cleaned.csv` – campaign metadata (project, user, start/stop times)
- `campaign_leads_cleaned.csv` – leads data for each campaign
- `insights_cleaned.csv` – ad performance metrics (spend, impressions, clicks, reach)
- `lead_status_changes_cleaned.csv` – lead status transitions over time

---

## 2. User Value

The dashboard provides the following key functionalities for business users:

1. **Overview of Key Metrics (KPIs)**  
   - Total Spend, Impressions, Clicks, Reach, Leads  
   - CTR (Click-Through Rate) and CPL (Cost Per Lead)  
   - Quick snapshot to evaluate campaign performance at a glance

2. **Campaign-Level Insights**  
   - Table of all campaigns with spend, impressions, clicks, reach, CTR, and CPL  
   - Helps identify high-performing and low-performing campaigns

3. **Trends Over Time**  
   - Line charts showing:
     - Leads added over time
     - Ad spend over time
     - Lead status changes over time  
   - Enables monitoring of campaign performance dynamics and lead funnel progression

4. **Lead Outcome Analysis**  
   - Pie chart of lead status distribution  
   - Helps understand the quality and conversion potential of leads

5. **Segmentation Analysis**  
   - Average CPL and CTR by project  
   - Assists in prioritizing campaigns/projects with better ROI

6. **Data Export**  
   - Download filtered leads as CSV for further offline analysis or reporting

---

## 3. Approach and Methodology

1. **Data Preparation**  
   - Used pre-cleaned datasets to ensure high data quality  
   - Converted date fields safely to `datetime` objects for accurate filtering and aggregation  

2. **Filtering Mechanism**  
   - Sidebar filters allow dynamic exploration:
     - Business User
     - Project
     - Date Range  
   - Filters applied across all tables and charts for consistency

3. **Aggregation & Metrics Calculation**  
   - Aggregated campaign-level metrics using `groupby`  
   - Calculated CTR and CPL per campaign and overall  
   - Trend charts aggregated daily for leads, spend, and status changes

4. **Visualization**  
   - Used Plotly for interactive line and bar charts, and pie charts  
   - Metrics displayed using Streamlit `metric` widgets for immediate insights

5. **Production-Readiness Considerations**  
   - Dashboard updates dynamically based on filters  
   - Downloadable CSV allows offline analysis  
   - Code structured for maintainability and scalability

---

## 4. Key Insights

Based on the sample data and dashboard functionality:

1. **Campaign Efficiency**  
   - CPL varies significantly across projects; some campaigns spend more without generating proportionally more leads  
   - CTR also varies, helping identify campaigns with low engagement

2. **Lead Quality and Conversion**  
   - Lead status distribution reveals the percentage of leads that convert vs. remain unqualified  
   - Monitoring status changes over time helps identify bottlenecks in lead nurturing

3. **Trends**  
   - Tracking leads and spend over time highlights periods of high ROI and low performance  
   - Seasonal trends or campaign timing effects can be observed

---

## 5. Assumptions

- Users care primarily about:
  - Spend efficiency (CPL, CTR)
  - Lead outcomes and trends
  - Project-level segmentation
- Cleaned datasets are accurate and up-to-date
- Users will use the dashboard to monitor campaigns both in real-time and periodically

---

## 6. Next Steps / Questions for Stakeholders

1. **Additional Metrics**  
   - Are there any other KPIs users care about, e.g., ROI per campaign, cost per click (CPC), or conversion rate?

2. **Granularity**  
   - Should trends be shown daily, weekly, or monthly for easier interpretation?

3. **Advanced Segmentation**  
   - Are users interested in demographic or channel-level breakdowns?

4. **Alerts and Thresholds**  
   - Should the dashboard notify users when campaigns exceed spend thresholds or CPL benchmarks?

5. **Integration**  
   - Should this dashboard be integrated into the main platform for seamless access?

---

## 7. Technical Notes

- Built using **Streamlit** and **Plotly** for interactivity  
- Python 3.9+ recommended  
- Requires the cleaned datasets in a `data/` folder  
- Run using:
  ```bash
  streamlit run app.py
