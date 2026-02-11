Bank Marketing Analytics – SQL, Python & Power BI
Bank telemarketing campaign analysis for term-deposit subscriptions using SQL, Python and Power BI.
Dataset: Portuguese bank marketing campaign (11,162 customers, multiple contact campaigns).

🔍 Business Problem
The bank wants to improve its telemarketing campaign by:

Increasing term-deposit subscription rate

Reducing wasted calls to low‑probability customers

Understanding which customer segments, months, and call frequencies work best

🧱 Data & Tools
Data source: Bank marketing dataset (term deposit campaign)

Row count: 11,162 customers

Target: Campaign success (poutcome = 'success')

Tech stack:

SQL (MySQL) – data extraction & aggregation

Python (pandas, scikit‑learn) – modeling

Power BI – visual dashboard

🗄️ SQL Analysis
Main SQL questions answered:

Overall campaign performance

Total customers contacted

Number of successful outcomes

Overall success rate (%)

Top jobs to target

Success rate by job (job)

Top segments (e.g. students, management)

Age group performance

Age grouped in decades (20s, 30s, 40s…)

Success rate by age group

Campaign call optimization

Success rate vs. number of calls (campaign)

Identifies point where extra calls reduce effectiveness

Best months to call

Success rate by month

Highlights high‑performing periods

Exported result tables are used directly in Power BI.


🤖 Python Model (Bank_Marketing_Model.py)
A classification model predicts probability of campaign success:

Target variable: poutcome mapped to target (1 = success, 0 = other)

Features used:

age, job, marital, education, default, housing, loan, campaign, pdays, previous, month

Model: Logistic Regression

Key steps:

Label encoding for categorical variables

Train/test split (80/20)

Model training and evaluation (classification report)

Export predictions to bank_predictions.csv with:

actual_success

predicted_success

success_probability

Model performance: around 89.3% accuracy on the test set.


📊 Power BI Dashboard
The Power BI report combines SQL outputs and model results:

KPIs:

Total customers

Overall success rate (%)

Visuals:

Bar chart: success rate by job

Campaign & Customer Insights

Line chart: success rate vs. number of campaign calls

Column chart: success rate by age group

Table: success rate by month (best months to run campaigns)

The dashboard is designed for marketing and business stakeholders to quickly answer:

“How many times should we call?”

“Which months are worth investing more budget?”

📁 Repository Structure
├── sql_queries.sql                 # All SQL used for analysis
├── overview.csv                    # Overall KPIs
├── top_jobs.csv                    # Job-level performance
├── age_analysis.csv                # Age group success rates
├── campaign_length.csv             # Calls vs success
├── monthly_performance.csv         # Month-level success rates
├── Bank_Marketing_Model.py         # Python model (logistic regression)
├── bank_predictions.csv            # Model predictions and probabilities
├── bank_marketing.pbix             # Power BI report 
└── README.md

🧩 Key Learnings & Impact
Identified high‑potential customer segments and time periods for marketing.

Showed that success rate drops after too many calls, helping optimize campaign cost.

Built an end‑to‑end data pipeline:

SQL data prep → Python modeling → Power BI dashboard.

This project demonstrates practical skills in data management, SQL, Python modeling, and BI storytelling for banking/marketing analytics roles.
