# Crypto_Price_Predictor
This repository contains a Python script that demonstrates the process of predicting Crypto prices using various Python models. The script utilizes the 'pandas', 'numpy' 'matplotlib' 'Tensorflow' and 'SK learn kit' packages for data processing, visualization, and text customization
## Why CryptoPredictions?
This library offers a wide range of services you may not find anywhere else. The exclusive benefits of CryptoPredictions are:
* some models may perform exceptionally well in terms of accuracy, they often require a well-defined strategy for successful trading. Our backtester can help you determine the effectiveness of your model in real-world scenarios.
* **Investment decisions**: Many people invest in cryptocurrencies, and they need to make informed decisions based on current market trends and future projections. Crypto predictions can give investors an idea of which cryptocurrencies are likely to perform well in the future, allowing them to make better investment decisions.
* **Risk management**: Cryptocurrency markets are highly volatile, and predicting future price movements can help investors manage their risks. By understanding where the market is headed, investors can make informed decisions about when to buy, sell, or hold their crypto assets.
* **Innovation and development**: Crypto predictions can help identify emerging trends in the cryptocurrency industry, allowing developers and entrepreneurs to create new products and services that meet the needs of the market.
* **Market analysis**: Cryptocurrency predictions can help analysts and researchers understand the current state of the market and make forecasts about future trends. This information can be useful for businesses, policymakers, and other stakeholders who want to stay informed about the cryptocurrency industry.
* At CryptoPredictions, we do not fetch indicators from different websites, because it leads to problems such as null rows and the lack of information on indicators for all cryptocurrencies. Instead, CryptoPredictions calculates them in a way that doesn't carry the mentioned problems and could be generalized to other datasets.
## Overview
* **Dataset Collection**: we have Collected data in the form of CSV files from reputed websites. Also, those Datasets are posted in this repository named:
 1.  Bitcoinprice_dataset.csv
 2.  ripple_dataset.csv
 3.  ETH_Dataset.csv
* **Prediction Model**: Firstly we have imported all necessary packages such as 'Pandas', 'Tensorflow', 'sk learn', 'Numpy' and 'Matplotlib' to preprocess data after that train_test_split function is used for training and testing of data (80% of data is used for Training and remaining 20% of data is used for Testing )for that SVR (Support Vector Regression) function is used as it helps to reduce the prediction error and allows SVR to handle non-linear relationships between input variables and the target variable using a kernel function, at last, we predict function from sklearn is used for final prediction of cryptocurrencies.
* **Web Development** : We have used HTML, CSS, and some Python modules to develop a web page. The home page of our web page consists of books, news, videos, blogs, and some text box regarding Cryptocurrencies. We have appended our prediction table into a CSV file then using pandas we created a HTML web page so that we can link it with our home page.
## Outcome
