<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Bangalore House Price Prediction</title>
</head>
<body>

<h1>Bangalore House Price Prediction</h1>
<p>This project aims to predict house prices in Bangalore using machine learning. It leverages various features such as location, availability, size, total square footage, bathrooms, and balconies to predict the approximate price of houses.</p>

<h2>Table of Contents</h2>
<ul>
  <li><a href="#introduction">Introduction</a></li>
  <li><a href="#project-overview">Project Overview</a></li>
  <li><a href="#dataset">Dataset</a></li>
  <li><a href="#data-preprocessing">Data Preprocessing</a></li>
  <li><a href="#feature-engineering">Feature Engineering</a></li>
  <li><a href="#modeling">Modeling</a></li>
  <li><a href="#evaluation">Evaluation</a></li>
  <li><a href="#how-to-use">How to Use</a></li>
  <li><a href="#results">Results</a></li>
  <li><a href="#future-enhancements">Future Enhancements</a></li>
  <li><a href="#acknowledgments">Acknowledgments</a></li>
</ul>

<h2 id="introduction">Introduction</h2>
<p>With Bangalore's rapid urbanization and real estate demand, predicting property prices can be challenging due to various factors like location, availability, and property features. This project applies machine learning techniques to predict the prices of properties in Bangalore based on historical data.</p>

<h2 id="project-overview">Project Overview</h2>
<p>The project involves:</p>
<ol>
  <li><strong>Data Cleaning</strong>: Handling missing values and standardizing data formats.</li>
  <li><strong>Feature Engineering</strong>: Creating meaningful features to improve model accuracy.</li>
  <li><strong>Model Training</strong>: Training multiple regression models to identify the best-performing model.</li>
  <li><strong>Evaluation</strong>: Evaluating models based on performance metrics like Mean Absolute Error (MAE) and Root Mean Squared Error (RMSE).</li>
  <li><strong>GUI Interface</strong>: Creating a user-friendly GUI to allow users to input property details and receive price predictions.</li>
</ol>

<h2 id="dataset">Dataset</h2>
<p>The dataset includes details on various properties in Bangalore, with features such as:</p>
<ul>
  <li><strong>Location</strong>: Area/location of the property.</li>
  <li><strong>Availability</strong>: Availability status of the property.</li>
  <li><strong>Size</strong>: Number of bedrooms.</li>
  <li><strong>Total Sqft</strong>: Total square footage of the property.</li>
  <li><strong>Bath</strong>: Number of bathrooms.</li>
  <li><strong>Balcony</strong>: Number of balconies.</li>
  <li><strong>Price</strong>: Target variable (price of the property).</li>
</ul>

<h2 id="data-preprocessing">Data Preprocessing</h2>
<ol>
  <li><strong>Handling Missing Values</strong>: Imputation strategies for missing entries.</li>
  <li><strong>Encoding Categorical Variables</strong>: Location data was transformed using a method based on average property prices.</li>
  <li><strong>Scaling</strong>: Applied MinMaxScaler to numerical columns for normalization.</li>
</ol>

<h2 id="feature-engineering">Feature Engineering</h2>
<ol>
  <li><strong>Location Aggregation</strong>: Reduced locations by grouping areas with low data frequency.</li>
  <li><strong>Custom Encoding</strong>: Used mean encoding on location features.</li>
  <li><strong>Feature Scaling</strong>: Normalized numerical features to enhance model performance.</li>
</ol>

<h2 id="modeling">Modeling</h2>
<p>Models used:</p>
<ul>
  <li><strong>Linear Regression</strong></li>
  <li><strong>Random Forest Regressor</strong></li>
  <li><strong>Gradient Boosting Regressor</strong></li>
  <li><strong>XGBoost Regressor</strong></li>
</ul>

<h2 id="evaluation">Evaluation</h2>
<p>The models were evaluated using:</p>
<ul>
  <li><strong>Mean Absolute Error (MAE)</strong></li>
  <li><strong>Root Mean Squared Error (RMSE)</strong></li>
</ul>

<h2 id="how-to-use">How to Use</h2>
<h3>Prerequisites</h3>
<p>Python 3.x</p>
<p>Libraries: <code>pandas</code>, <code>numpy</code>, <code>scikit-learn</code>, <code>matplotlib</code>, <code>seaborn</code>, <code>customtkinter</code> for GUI</p>

<h3>Running the Project</h3>
<ol>
  <li>Clone this repository:
    <pre><code>git clone https://github.com/yourusername/Bangalore-House-Price-Prediction.git</code></pre>
  </li>
  <li>Install required libraries:
    <pre><code>pip install -r requirements.txt</code></pre>
  </li>
  <li>Run the <code>main.py</code> file to start the GUI:
    <pre><code>python main.py</code></pre>
  </li>
</ol>

<h3>Using the GUI</h3>
<p>Enter details such as location, size, availability, total sqft, bathrooms, and balconies. Click on "Predict" to see the estimated house price.</p>

<h2 id="results">Results</h2>
<p>After comparing models, the <strong>Random Forest Regressor</strong> and <strong>XGBoost</strong> gave the most accurate results for the test dataset with the lowest error scores.</p>

<h2 id="future-enhancements">Future Enhancements</h2>
<ol>
  <li><strong>Model Tuning</strong>: Hyperparameter tuning for improved accuracy.</li>
  <li><strong>Advanced Feature Engineering</strong>: Incorporating additional location-based features.</li>
  <li><strong>Deployment</strong>: Deploying the model as a web application.</li>
</ol>

<h2 id="acknowledgments">Acknowledgments</h2>
<p>Special thanks to Kaggle and other open data sources for providing real estate data used in this project.</p>

</body>
</html>
