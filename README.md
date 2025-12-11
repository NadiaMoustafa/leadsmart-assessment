# LeadSmart Assessment – Overview & Navigation Guide

## Overview

This repository contains my complete end-to-end solution for the LeadSmart Data Science Assessment.  
The project covers six major components: data exploration, business intelligence, predictive modeling, strategic decision systems, AI agent design, and production engineering.

Across the submission, I approached the problem as the sole data hire—prioritizing real-world decision-making, production readiness, business value, and stakeholder alignment.

### Part 1 – Data Discovery & Exploration
A full exploratory analysis of the four provided datasets, identifying data quality issues, validating completeness, and extracting insights that influence BI dashboards and predictive models.  
The notebook includes the questions I would ask stakeholders to clarify ambiguities and ensure correct data interpretation.

### Part 2 – Business Intelligence

A production-ready Streamlit dashboard built in VS Code, designed to give business users clear visibility into their campaign performance.

The dashboard supports multi-level filtering (business user, project, and date range) and provides a rich set of insights including:

- Key KPIs (Spend, Impressions, Clicks, Reach, Leads, CTR, CPL)
- Campaign-level performance tables
- Trends over time for spend and lead generation
- Lead status distribution and status-change analysis
- Segmentation insights such as CPL and CTR by project
- CSV export of filtered leads

This provides users with a complete view of spend efficiency, lead quality, and campaign outcomes—helping them understand whether their money is being invested effectively and where performance bottlenecks exist.


### Part 3 – Predictive Intelligence (Lead Conversion Model)
A Random Forest model predicting which leads are most likely to convert.  
Includes feature engineering (lead-level + campaign-level), model evaluation, assumptions, and practical application for prioritizing sales efforts.

### Part 4 – Strategic Decision System (Campaign Success Model)
A Random Forest model that evaluates whether a campaign is performing well enough to continue.  
The system predicts campaign success based on conversion rate and performance metrics such as CTR, CPM, spend, impressions, and clicks.  
Delivered with documentation covering thresholds, practical workflow integration, and stakeholder questions.

### Part 5 – Agentic AI Design
A full design document describing an AI lead-qualification agent.  
Includes architecture, sample conversation flows, business case, system components, assumptions, and open questions.

### Part 6 – Production Engineering
A complete production deployment plan (for Part 3), including:  
tech stack, cloud architecture, CI/CD pipelines, monitoring, cost estimates, operational risks, and remediation strategies.

---

## How to Navigate This Submission


The repository follows the required structure. Below is a guide to what each folder/file contains and how to navigate the submission.

<img width="767" height="591" alt="Screenshot 2025-12-11 141728" src="https://github.com/user-attachments/assets/cfb72c89-9d7e-4681-8f20-cc722d3cf649" />


---

## What to Review :

- **For data foundation:**  
  Open `part1_exploration.ipynb`

- **For BI experience:**  
  Open `part2_dashboard/app.py`  
  and read `part2_dlcumentaion/README.md`

- **For predictive intelligence:**  
  - Lead Conversion → `part3_model.ipynb`  
  - Campaign Success → `part4_model.ipynb`

- **For design thinking / product strategy:**  
  - AI Agent → `part5_ai_agent_design/`  
  - Production Deployment → `part6_production_plan/`

- **For a quick executive overview:**  
  Open `SUMMARY.md` 

---

###### Environment Setup. only required in part 2 and it explained in details in the part2/readme.md file

**
