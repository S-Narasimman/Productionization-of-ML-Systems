# Voyage Analytics: Integrating MLOps in Travel

### *Productionization of Machine Learning Systems*

---

## 📌 Project Overview

**Voyage Analytics** is an end-to-end MLOps solution designed to revolutionize how travel experiences are analyzed and priced. By synthesizing multi-dimensional datasets—**Users, Flights, and Hotels**—this project builds a high-performance predictive ecosystem.

The primary focus is the development and deployment of a sophisticated **Flight Price Prediction** model, integrated into a professional MLOps pipeline to ensure scalability, reproducibility, and real-time utility.

---

## 📊 Data Architecture

The project leverages three interconnected data streams to capture the full traveler journey:

### 1. Users Dataset

* **Demographics:** Name, Gender, Age.
* **Professional Context:** Company association and unique User Identifiers (`code`).

### 2. Flights Dataset

* **Logistics:** Origin (`from`), Destination (`to`), and Flight Type (e.g., First Class).
* **Metrics:** Price, Duration (`time`), Distance, and Agency details.
* **Temporal:** Specific flight dates linked to users.

### 3. Hotels Dataset

* **Stay Details:** Hotel name, location (`place`), and duration of stay (`days`).
* **Financials:** Price per day and total booking cost.

---

## 🛠️ Technical Solution Stack

* **Modeling:** Scikit-learn (Random Forest Regressor, Gradient Boosting, Linear Regression).
* **Experiment Tracking:** **MLflow** for versioning models and logging hyperparameters/metrics.
* **Web Framework:** **Flask** for serving the model via a user-friendly REST API.
* **Containerization:** **Docker** for environment consistency and seamless deployment.
* **Visualization:** Matplotlib, Seaborn, and Canva for advanced EDA and reporting.

---

## 🚀 Methodology & Insights

### 1. Data Engineering

* **Feature Extraction:** Transformed raw `date` strings into granular features (Year, Month, Day) and engineered a `year_index` to track inflation and seasonal trends.
* **Categorical Handling:** Implemented One-Hot Encoding for `flightType` and `agency`.
* **Robustness:** Applied Z-score outlier detection to ensure model stability against pricing anomalies.

### 2. Exploratory Data Analysis (EDA)

* **Price Dynamics:** Confirmed that First Class bookings and flight distance are the strongest predictors of total cost.
* **Agency Trends:** Identified market-dominant agencies, providing a roadmap for strategic partnerships.
* **Demand Cycles:** Uncovered seasonal fluctuations that inform high-traffic marketing strategies.

### 3. Model Selection

After rigorous benchmarking using **MAE, MSE, and $R^2$**, the **Random Forest Regressor** was selected as the production model due to its superior ability to handle non-linear relationships and its robustness against overfitting.

---

## 💼 Business Impact

* **Revenue Optimization:** Enables dynamic pricing strategies based on distance and class demand.
* **Strategic Marketing:** Uses demand forecasting to optimize promotional spending during peak travel windows.
* **Operational Efficiency:** The MLOps framework allows for automated deployment and monitoring, reducing the "time-to-insight."

---

## 🏁 Conclusion

This project demonstrates the transformative power of integrating Machine Learning with MLOps in the travel sector. By moving beyond static analysis to a containerized, tracked, and deployed solution, we have created a tool that not only predicts flight costs with high accuracy but also provides a scalable blueprint for future travel tech innovations.

The transition from raw data exploration to a live **Flask** application—backed by **Docker** and **MLflow**—ensures that the insights derived are actionable, maintainable, and ready for real-world production environments.

---

## 🔮 Future Roadmap

* **Explainability:** Integrate **SHAP** or **LIME** to provide transparency in pricing decisions.
* **Neural Networks:** Explore Deep Learning architectures as the dataset scales.
* **Holistic Analytics:** Expand the model to include hotel and transport data for "Total Trip Cost" forecasting.