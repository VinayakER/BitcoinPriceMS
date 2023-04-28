# BitcoinPriceMS
This project fetch Bitcoin prices in USD from a public api https://api.coindesk.com/v1/bpi/currentprice.json and save to local MySQL database. 
Then we can fetch this saved data with an another API with endpoint **/bitcoin/prices**.

## To install the project simply run these commands.
Assuming that you have already installed MySQL and created new database.
```
> git clone https://github.com/VinayakER/BitcoinPriceMS
> cd BitcoinPriceMS
> pip install -r requirements.txt

**Create new file .env and paste your database uri it it with variable name DATABASE_URL.**

> bash run.sh
```
Your project will be running on your local machine and you will see output something link this. 
```
INFO:     Will watch for changes in these directories: ['/home/vinayak/dev/additional/BitCoinTest']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [61699] using StatReload
INFO:     Started server process [61701]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

Now you need to go to http://127.0.0.1:8000/bitcoin/prices.

You will get records added to database. 

This project will fetch new price in every 5 minutes automaticaly. 
