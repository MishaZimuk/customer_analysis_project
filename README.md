# Customer Analysis Project

FastAPI service for customer analytics: key metrics, visualizations, and simple dashboards built with **Pandas**, **Matplotlib**, and **Jinja2**.

## 🚀 Features
- Customer metrics (activity, segments, repeat orders, revenue trends)
- Visualization (PNG charts via Matplotlib)
- REST API + HTML reports (FastAPI + Jinja2 templates)
- Clean modular structure (routers / logic / utils)

## 🗂️ Project Structure
```
analysis
api_logic
routers
templates
static
charts
utils
data
main.py
requirements.txt
.gitignore
```

## ⚙️ Installation
```bash
git clone https://github.com/your-username/customer_analysis_project.git
cd customer_analysis_project

python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux/macOS
source .venv/bin/activate

pip install -r requirements.txt
```

## ▶️ Run
```bash
uvicorn main:app --reload
# then open http://127.0.0.1:8000
```

## 📡 API Endpoints
| Method | Endpoint |
|---|---|
| GET | `/` |
| GET | `/avg_days_between_orders` |
| GET | `/avg_days_between_orders_chart` |
| GET | `/avg_days_between_orders_report` |
| GET | `/avg_order_value_by_hour` |
| GET | `/avg_order_value_by_hour_chart` |
| GET | `/avg_order_value_by_hour_report` |
| GET | `/basic_stats` |
| GET | `/churn_status` |
| GET | `/churn_status_chart` |
| GET | `/churn_status_report` |
| GET | `/cohort` |
| GET | `/cohort_chart` |
| GET | `/cohort_report` |
| GET | `/customer_lifecycle` |
| GET | `/customer_lifecycle_chart` |
| GET | `/customer_lifecycle_report` |
| GET | `/customer_lifetime` |
| GET | `/customer_lifetime_chart` |
| GET | `/customer_lifetime_report` |
| GET | `/docs` |
| GET | `/docs/oauth2-redirect` |
| GET | `/first_second_delay` |
| GET | `/first_second_delay_chart` |
| GET | `/first_second_delay_report` |
| GET | `/health` |
| GET | `/images/{image_name}` |
| GET | `/ltv` |
| GET | `/ltv_chart` |
| GET | `/ltv_report` |
| GET | `/monthly_growth` |
| GET | `/monthly_growth_chart` |
| GET | `/monthly_growth_report` |
| GET | `/monthly_stats` |
| GET | `/new_vs_returning` |
| GET | `/new_vs_returning_chart` |
| GET | `/new_vs_returning_report` |
| GET | `/openapi.json` |
| GET | `/orders_by_day_of_month` |
| GET | `/orders_by_day_of_month_chart` |
| GET | `/orders_by_day_of_month_report` |
| GET | `/orders_by_day_of_week` |
| GET | `/orders_by_day_of_week_chart` |
| GET | `/orders_by_day_of_week_report` |
| GET | `/orders_by_hour` |
| GET | `/orders_by_hour_chart` |
| GET | `/orders_by_hour_report` |
| GET | `/orders_by_month` |
| GET | `/orders_by_month_chart` |
| GET | `/orders_by_month_report` |
| GET | `/orders_heatmap` |
| GET | `/orders_heatmap_chart` |
| GET | `/orders_heatmap_report` |
| GET | `/redoc` |
| GET | `/repeat_rate` |
| GET | `/repeat_rate_chart` |
| GET | `/repeat_rate_report` |
| GET | `/retention` |
| GET | `/retention_chart` |
| GET | `/retention_report` |
| GET | `/revenue_by_hour` |
| GET | `/revenue_by_hour_chart` |
| GET | `/revenue_by_hour_report` |
| GET | `/rfm` |
| GET | `/rfm_chart` |
| GET | `/rfm_report` |
| GET | `/segment` |
| GET | `/segment_chart` |
| GET | `/segment_report` |

## 📁 Data
Place your input CSV/Parquet in `data/` (or update paths in code). Document the expected columns here.

## 🏗️ Roadmap
- [ ] Define data schema & validators
- [ ] Add more endpoints and tests
- [ ] Build dashboards with multiple charts
- [ ] Optional: Dockerfile / CI

## 📄 License
MIT 
