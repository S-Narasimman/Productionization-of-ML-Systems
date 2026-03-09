# Capstone_Project_Productionization_of_ML_Systems


# Project Title:
**Voyage Analytics: Integrating MLOps in Travel
Productionization of ML Systems**

## Business Context

In the realm of travel and tourism, the intersection of data analytics and machine learning presents an opportunity to revolutionize the way travel experiences are curated and delivered. This capstone project revolves around a trio of datasets - users, flights, and hotels - each providing a unique perspective on travel patterns and preferences. The goal is to leverage these datasets to build and deploy sophisticated machine learning models, serving a dual purpose: enhancing predictive capabilities in travel-related decision-making and mastering the art of MLOps through hands-on application.

## Brief overview of each datasets
#### **Users Dataset:**
- code: User identifier.
- company: Associated company.
- name: Name of the user.
- gender: Gender of the user.
- age: Age of the user.

#### **Flights Dataset:**
- travelCode: Identifier for the travel.
- userCode: User identifier(linked to the Users dataset)
- from: Origin of the flight.
- to: Destination of the flight.
- flightType: Type of flight (e.g., first class).
- price: Price of the flight.
- time: Flight duration.
- distance: Distance of the flight.
- agency: Flight agency.
- date: Date of the flight.

#### **Hotels Dataset:**
- travelCode: Identifier for the travel, similar to the Flights dataset.
- userCode: User identifier(linked to the Users dataset)
- name: Name of the hotel.
- place: Location of the hotel.
- days: Number of days of the hotel stay.
- price: Price per day.
- total: Total price for the stay.
- date: Date of the hotel booking.

## Project Objectives
Build a regression model to predict the price of a flight using the flights.csv dataset. Focus on feature selection, model training, and validation to ensure accuracy and reliability.


## Solution Overview:
- Machine Learning Model: Multiple ML model trained on historical flight data (Selected Random Forest Model).
- Web Application: A Flask app for interacting with users and making predictions.
- Experiment Tracking: MLflow is used to track experiments, version models, and log metrics.
- Deployment: Docker is used to containerize the Flask application for easy deployment and scalability.



# Conclusion:


In this project, titled "Voyage Analytics: Integrating MLOps in Travel Productionization of ML Systems," I explored the power of machine learning in the travel and tourism industry, with a specific focus on flight price prediction. The project aimed to integrate data analytics and machine learning with MLOps practices to predict flight prices and offer valuable business insights that could enhance decision-making, pricing strategies, and operational efficiency for travel-related organizations. The project was carried out using datasets from three primary sources—users, flights, and hotels—allowing for an in-depth analysis of travel patterns and preferences.


Data Preprocessing and Feature Engineering:
The initial stages of the project involved significant data preprocessing to ensure high-quality, usable data for model training. The raw dataset had no missing values or duplicates, making it a clean starting point. I extracted critical date-related features, such as year, month, and day, from the `date` column to enable time-based analysis. Furthermore, I engineered the `year_index` feature, which helped in understanding year-over-year trends and made the dataset more suitable for predictive modeling. 
One-hot encoding was applied to categorical features, such as flight type and agency, which helped in preserving the categorical nature of these variables. Outlier detection was done using the z-score method, ensuring that extreme values did not skew the model predictions. The data was then split into training and testing sets with a 20% test size, ensuring sufficient data for both training and evaluation.


Exploratory Data Analysis (EDA) and Insights:
Through various visualizations, such as box plots, scatter plots, count plots, and heatmaps, I gained valuable insights into the dataset's underlying patterns. Some key findings include:


- Flight Pricing Trends: The analysis revealed that first-class flights tend to have higher prices, while economy flights are more affordable. This insight can inform airlines’ pricing strategies, allowing them to optimize revenue and attract customers.
  
- Flight Distance vs. Price: The scatter plot showed a positive correlation between flight distance and price, suggesting that longer flights typically command higher prices. This information can help airlines set prices based on the distance of routes.


- Agency Popularity: The count plot illustrated the frequency of flights associated with different agencies, highlighting key partnerships and helping businesses identify which agencies to collaborate with for targeted marketing efforts.


- Seasonal and Geographic Trends: Insights into how flight prices change over time and across different origins provided valuable information on demand cycles and regional price differences. Understanding these trends can help in devising promotional strategies and planning marketing campaigns tailored to specific seasons or regions.


Machine Learning Models and Evaluation:
I implemented and evaluated four distinct machine learning models to predict flight prices: Decision Tree Regression, Random Forest Regression, Gradient Boosting Regression, and Linear Regression. After training and hyperparameter tuning using GridSearchCV, I assessed each model's performance using key metrics—Mean Absolute Error (MAE), Mean Squared Error (MSE), and R-squared (R²).


- The Decision Tree model performed reasonably well but lacked the robustness needed for accurate predictions, especially on unseen data.
- The Random Forest model, an ensemble technique, demonstrated the highest performance across evaluation metrics, achieving a good balance between model complexity and accuracy. It provided strong results in both training and testing phases, making it a suitable candidate for production deployment.
- The Gradient Boosting model also showed good predictive power, but it was more computationally intensive than Random Forest, which made the latter more efficient for large-scale data.
- Linear Regression was simple and interpretable but was less effective compared to the ensemble models due to its assumption of linear relationships, which did not fully capture the complexities of the flight price prediction.


The Random Forest Regression model was ultimately selected as the final model due to its strong predictive performance, flexibility, and ability to handle both numerical and categorical data. Additionally, Random Forest provided insights into feature importance, helping identify which features most strongly influence flight prices, such as `flight type`, `distance`, and `agency`.


Business Impact and Practical Implications:
The insights derived from the data and the machine learning models hold significant business value for the travel and tourism industry:


- Pricing Optimization: By understanding how factors like flight distance, type, and agency affect prices, airlines can develop dynamic pricing strategies to optimize revenue. For example, flights with longer distances can be priced higher, while economy-class flights can be made more competitive to attract budget-conscious travelers.


- Demand Forecasting and Seasonal Adjustments: The seasonal trends identified through EDA can help airlines predict periods of high or low demand, allowing them to adjust pricing and promotional campaigns accordingly to maximize bookings during peak times.


- Customer Targeting: The insights into which agencies offer the most flights or have the best pricing can guide travel agencies and airlines in forming strategic partnerships and targeting their marketing campaigns more effectively.


- Operational Efficiency: The predictive models could be integrated into a real-time production environment, allowing airlines and travel agencies to predict prices dynamically, automate pricing decisions, and enhance customer satisfaction.
Future Steps and Recommendations:
While the Random Forest model has shown promising results, there are several avenues for future improvements:


1. Model Interpretability: Exploring model interpretability tools such as SHAPE or LIME would provide deeper insights into how individual features influence predictions, which could help in gaining stakeholder trust and transparency.


2. Advanced Models: Exploring more sophisticated models, such as Neural Networks, could further improve prediction accuracy, especially if the dataset is expanded to include additional features such as customer behavior, weather, or competitor prices.


3. Cross-domain Integration: Expanding the analysis to include data from hotels, transportation, and user preferences could provide a more holistic view of the travel experience and lead to even better prediction models for the broader travel industry.


This project not only demonstrated the power of machine learning in the travel industry but also provided valuable insights into the various factors affecting flight pricing. The integration of MLOps practices ensures that the solution is scalable, maintainable, and ready for deployment. By leveraging machine learning and MLOps, the travel industry can make data-driven decisions, improve customer satisfaction, and optimize revenue.

