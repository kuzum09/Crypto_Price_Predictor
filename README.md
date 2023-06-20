# Crypto Price Predictor
This repository contains a Python script that demonstrates the process of predicting Crypto prices using various Python models. The script utilizes the 'pandas', 'numpy' 'matplotlib' 'Tensorflow' and 'SK learn kit' packages for data processing, visualization, and text customization
## Why CryptoPredictions?
This library offers a wide range of services you may not find anywhere else. The exclusive benefits of CryptoPredictions are:
* some models may perform exceptionally well in terms of accuracy, they often require a well-defined strategy for successful trading. Our backtester can help you determine the effectiveness of your model in real-world scenarios.
* **Investment decisions**: Many people invest in cryptocurrencies, and they need to make informed decisions based on current market trends and future projections. Crypto predictions can give investors an idea of which cryptocurrencies are likely to perform well in the future, allowing them to make better investment decisions.
* **Risk management**: Cryptocurrency markets are highly volatile, and predicting future price movements can help investors manage their risks. By understanding where the market is headed, investors can make informed decisions about when to buy, sell, or hold their crypto assets.
* **Innovation and development**: Crypto predictions can help identify emerging trends in the cryptocurrency industry, allowing developers and entrepreneurs to create new products and services that meet the needs of the market.
* **Market analysis**: Cryptocurrency predictions can help analysts and researchers understand the current state of the market and make forecasts about future trends. This information can be useful for businesses, policymakers, and other stakeholders who want to stay informed about the cryptocurrency industry.
* At CryptoPredictions, we do not fetch indicators from different websites, because it leads to problems such as null rows and the lack of information on indicators for all cryptocurrencies. Instead, CryptoPredictions calculates them in a way that doesn't carry the mentioned problems and could be generalized to other datasets.
## Workflow
### Webpage
![Screenshot 2023-05-21 163114](https://github.com/kuzum09/Crypto_Price_Predictor/assets/126418779/6ce9d2fd-7899-48ba-b1fa-b93975f0d99d)
### Prediction Model
![Screenshot 2023-05-21 201429](https://github.com/kuzum09/Crypto_Price_Predictor/assets/126418779/afdb0950-6f98-4450-86d0-23ec97ff1728)
### Dataflow Design
![Screenshot 2023-06-20 170309](https://github.com/kuzum09/Crypto_Price_Predictor/assets/126418779/6239273e-1579-4f8d-bc4a-e951cb953d1e)
## Overview
* **Dataset Collection**: we have Collected data in the form of CSV files from reputed websites. Also, those Datasets are posted in this repository named:
 1.  Bitcoinprice_dataset.csv
 2.  ripple_dataset.csv
 3.  ETH_Dataset.csv
* **Prediction Model**: Firstly we have imported all necessary packages such as 'Pandas', 'Tensorflow', 'sk learn', 'Numpy' and 'Matplotlib' to preprocess data after that train_test_split function is used for training and testing of data (80% of data is used for Training and remaining 20% of data is used for Testing )for that SVR (Support Vector Regression) function is used as it helps to reduce the prediction error and allows SVR to handle non-linear relationships between input variables and the target variable using a kernel function, at last, we predict function from sklearn is used for final prediction of cryptocurrencies.

  ![image](https://github.com/kuzum09/Crypto_Price_Predictor/assets/126418779/cddcb589-aac6-4f0e-b775-7efac4044eac)
  
* **Web Development** : We have used HTML, CSS, and some Python modules to develop a web page. The home page of our web page consists of books, news, videos, blogs, and some text box regarding Cryptocurrencies. We have appended our prediction table into a CSV file then using pandas we created a HTML web page so that we can link it with our home page.
*  **Recomendation Engine**: We integrate news.api data for making a recommendation engine which will help our user to stay updated on the latest news about the crypto market.
  
## Result
### Webpage
![Screenshot 2023-06-20 163510](https://github.com/kuzum09/Crypto_Price_Predictor/assets/126418779/7820e6bc-040d-4147-a72a-fdae047932f1)
![Screenshot 2023-06-20 014212](https://github.com/kuzum09/Crypto_Price_Predictor/assets/126418779/c988beb0-ebe8-4322-ac35-0c185181126a)
## Pridiction Model
### Bitcoin
![image](https://github.com/kuzum09/Crypto_Price_Predictor/assets/126418779/90e94481-08d9-4fab-b6a0-cda7c828c35f)
### Etherium
![image](https://github.com/kuzum09/Crypto_Price_Predictor/assets/126418779/4c088755-8ec5-4086-a1cb-91d03766ce6a)
### Ripple
![image](https://github.com/kuzum09/Crypto_Price_Predictor/assets/126418779/99d75eb1-3ed8-4fce-89f0-44c809479f13)
### Recomendation Engine
![Screenshot 2023-06-20 163558](https://github.com/kuzum09/Crypto_Price_Predictor/assets/126418779/7d143258-0e80-4066-9dbf-01bfa658ed0b)




