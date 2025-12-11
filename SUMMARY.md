# Project Summary

## 1. What I Built

This assessment required delivering an end‑to‑end data function for Leadsmart. I completed all six parts:

### **Part 1 – Data Exploration**

Performed a full EDA on all four datasets (campaigns, leads, insights, status changes). Identified data quality issues, inconsistencies, missing values, and structural problems. Documented clarifying questions and insights.

### **Part 2 – Business Intelligence Dashboard (Streamlit)**

Built a production‑ready **Streamlit dashboard** showing campaign performance, spend efficiency, lead funnel KPIs, and ad metrics. Included data cleaning logic, interactive filters, automated insights, and user‑friendly visualizations.

### **Part 3 – Predictive Intelligence (Lead Scoring Model)**

Developed a **Random Forest classifier** to predict the likelihood a lead will progress to a qualified/conversion stage. Included feature engineering, evaluation, and a practical prioritization strategy for sales teams.

### **Part 4 – Strategic Decision System (Campaign Success Model)**

Designed and implemented a **Random Forest regression/classifier hybrid logic** for scoring campaign performance and recommending actions (continue, pause, increase budget). Defined a clear success framework based on conversion rate, ROAS, and CPC efficiency.

### **Part 5 – AI Agent Design**

Produced a design document for a full AI agent that handles lead qualification phone calls, with architecture, conversation flows, business case, build‑vs‑buy analysis, and integration with the existing CRM workflow.

### **Part 6 – Production Engineering Plan**

Delivered a complete production deployment plan for the predictive model: architecture, API design, monitoring, retraining pipeline, cost estimates, DevOps workflow, and risk mitigation.

---

## 2. Key Findings (Top 3–5 Insights)

1. **Only 0.4% of campaigns are successful** — Out of 7,364 campaigns analyzed, just 32 met all success criteria (conversion rate >5%, cost per conversion <$500, CTR >1%), highlighting a severe performance imbalance and the urgent need for strategic intervention.
2. 98.3% of the total daily budget ($12.4M) is currently allocated to campaigns recommended to be stopped or paused. **This represents a massive opportunity for reallocation**.
3. ROI Estimate is the most important predictor (64%), followed by Total Leads (16%) and Impressions (4%). **This suggests focusing on campaigns with strong ROI signals rather than just high spend**.
4. The top 5 campaigns have 95–97% success probability but represent only a tiny fraction of the total budget.
5. Many campaigns generate leads but fail to convert them efficiently, draining budget without ROI.

---

## 3. Recommendations (What Leadsmart Should Prioritize)

### **1. Implement lead scoring across all accounts**

This will help sales teams focus on high‑value leads and reduce wasted time.

### **2. Build a unified campaign health score**

This gives business users a clear signal on which campaigns to pause or scale.

### **3. focusing on campaigns with strong ROI signals rather than just high spend.**

Make it her priority by focusing on big deal

### **4. should be scaled immediately with increased budget.**

Focusing on Top campaigns

### **5. Prioritize agentic AI for qualification**

A qualification agent can reduce sales workload by 40–60% and improve response time.

---

## 4. What’s Next (If Given More Time)

1. **Introduce time‑series forecasting** for spend allocation and expected campaign performance.
2. **Automate the ML model retraining pipeline** with real‑time ingestion.
3. **Implement a feature store** to standardize feature computation for leads and campaigns.
4. **Add uplift modeling** to estimate which campaigns improve after budget increases.
5. **Run A/B tests** to measure the impact of lead scoring on actual sales productivity.

---

## 5. Assumptions & Questions for Stakeholders

### **Assumptions & Questions for Week 1**

1. **How does each client define a conversion?** (Booking? Visit? Down payment?)
2. **What does a “qualified lead” mean to the sales teams?**
3. **What are acceptable response‑time SLAs for lead follow‑ups?**
4. **Do campaigns have custom goals?** (Brand awareness vs. lead quality)
5. **What additional fields can we collect from Facebook to improve accuracy?**
6. **How do sales teams currently prioritize leads?**

---

