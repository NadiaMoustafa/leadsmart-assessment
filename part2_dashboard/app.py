import streamlit as st
import pandas as pd
import plotly.express as px

# I'm already cleaned the datasets before so i can now use it directly

# 1. LOAD CLEANED DATASETS
campaigns = pd.read_csv("data/campaigns_cleaned.csv")
campaign_leads = pd.read_csv("data/campaign_leads_cleaned.csv")
insights = pd.read_csv("data/insights_cleaned.csv")
lead_status_changes = pd.read_csv("data/lead_status_changes_cleaned.csv")

# 2. CONVERT DATES SAFELY -- just to make sure
campaigns['start_time'] = pd.to_datetime(campaigns['start_time'], errors='coerce')
campaigns['stop_time'] = pd.to_datetime(campaigns['stop_time'], errors='coerce')
campaign_leads['added_date'] = pd.to_datetime(campaign_leads['added_date'], errors='coerce')
insights['created_at'] = pd.to_datetime(insights['created_at'], errors='coerce')
lead_status_changes['created_at'] = pd.to_datetime(lead_status_changes['created_at'], errors='coerce')

# 3. SIDEBAR FILTERS
st.sidebar.header("Filters")
user_filter = st.sidebar.selectbox("Select Business User", ["All"] + list(campaigns['user_id'].unique()))
project_filter = st.sidebar.selectbox("Select Project", ["All"] + list(campaigns['project_name'].unique()))
date_range = st.sidebar.date_input(
    "Select Date Range",
    [insights['created_at'].min().date(), insights['created_at'].max().date()]
)

# Apply filters
filtered_campaigns = campaigns.copy()
if user_filter != "All":
    filtered_campaigns = filtered_campaigns[filtered_campaigns['user_id'] == user_filter]
if project_filter != "All":
    filtered_campaigns = filtered_campaigns[filtered_campaigns['project_name'] == project_filter]

filtered_insights = insights[insights['campaign_id'].isin(filtered_campaigns['id'])]
filtered_insights = filtered_insights[
    (filtered_insights['created_at'].dt.date >= date_range[0]) &
    (filtered_insights['created_at'].dt.date <= date_range[1])
]

filtered_leads = campaign_leads[campaign_leads['campaign_id'].isin(filtered_campaigns['id'])]
filtered_leads = filtered_leads[
    (filtered_leads['added_date'].dt.date >= date_range[0]) &
    (filtered_leads['added_date'].dt.date <= date_range[1])
]

# 4. KPIs / Overview
st.title("📊 Campaign Performance Dashboard")
st.header("Key Metrics Overview")

total_spend = filtered_insights['spend'].sum()
total_impressions = filtered_insights['impressions'].sum()
total_clicks = filtered_insights['clicks'].sum()
total_reach = filtered_insights['reach'].sum()
total_leads = filtered_leads.shape[0]
ctr = (total_clicks / total_impressions * 100) if total_impressions > 0 else 0
cpl = (total_spend / total_leads) if total_leads > 0 else 0

col1, col2, col3, col4, col5, col6 = st.columns(6)
col1.metric("Total Spend", f"${total_spend:,.2f}")
col2.metric("Total Impressions", f"{total_impressions:,}")
col3.metric("Total Clicks", f"{total_clicks:,}")
col4.metric("Total Reach", f"{total_reach:,}")
col5.metric("Total Leads", f"{total_leads}")
col6.metric("CPL (Cost per Lead)", f"${cpl:.2f}")

# 5. Campaign Performance Table
st.header("Campaign Performance")
campaign_summary = filtered_insights.groupby('campaign_id').agg({
    'spend':'sum',
    'impressions':'sum',
    'clicks':'sum',
    'reach':'sum'
}).reset_index()

campaign_summary = campaign_summary.merge(
    filtered_campaigns[['id','project_name','user_id']], 
    left_on='campaign_id', 
    right_on='id', 
    how='left'
)

# Calculate CTR and CPL per campaign
leads_count = filtered_leads.groupby('campaign_id')['id'].count().reindex(campaign_summary['campaign_id']).fillna(0)
campaign_summary['CTR (%)'] = (campaign_summary['clicks'] / campaign_summary['impressions'] * 100).round(2)
campaign_summary['CPL'] = (campaign_summary['spend'] / leads_count).round(2)

st.dataframe(campaign_summary[['project_name','user_id','spend','impressions','clicks','reach','CTR (%)','CPL']])

# 6. Trend Analysis
st.header("Trends Over Time")

# Leads over time
leads_time = filtered_leads.groupby('added_date').size().reset_index(name='Leads')
fig_leads = px.line(leads_time, x='added_date', y='Leads', title="Leads Over Time")
st.plotly_chart(fig_leads)

# Spend over time
spend_time = filtered_insights.groupby('created_at')['spend'].sum().reset_index()
fig_spend = px.line(spend_time, x='created_at', y='spend', title="Spend Over Time")
st.plotly_chart(fig_spend)

# 7. Lead Outcome Analysis
st.header("Lead Outcomes")
lead_outcomes = filtered_leads['lead_status'].value_counts().reset_index()
lead_outcomes.columns = ['Status','Count']
fig_outcome = px.pie(lead_outcomes, names='Status', values='Count', title="Lead Status Distribution")
st.plotly_chart(fig_outcome)

# Lead status changes over time
status_changes_filtered = lead_status_changes[lead_status_changes['lead_id'].isin(filtered_leads['id'])]
status_time = status_changes_filtered.groupby('created_at')['status'].count().reset_index()
fig_status_time = px.line(status_time, x='created_at', y='status', title="Lead Status Changes Over Time")
st.plotly_chart(fig_status_time)

# 8. Segmentation Analysis
st.header("Segmentation Analysis")

# CPL by Project
cpl_project = campaign_summary.groupby('project_name')['CPL'].mean().reset_index()
fig_cpl_proj = px.bar(cpl_project, x='project_name', y='CPL', title="Average CPL by Project")
st.plotly_chart(fig_cpl_proj)

# CTR by Project
ctr_project = campaign_summary.groupby('project_name')['CTR (%)'].mean().reset_index()
fig_ctr_proj = px.bar(ctr_project, x='project_name', y='CTR (%)', title="Average CTR by Project")
st.plotly_chart(fig_ctr_proj)

# 9. Export Filtered Data
st.download_button(
    label="Download Filtered Leads CSV",
    data=filtered_leads.to_csv(index=False).encode('utf-8'),
    file_name='filtered_leads.csv',
    mime='text/csv'
)
