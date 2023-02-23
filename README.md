# Interactive Brokers TWS with Tradingview Webhook

## Setup
This setup assumes, you run TWS on your desktop and use Ngrok service to publish the webhook endpoint

### Prepare environment
- Clone the repository: `git clone https://github.com/zdytch/ib-tws-tradingview.git`
- Switch to the project folder: `cd /path/to/project/directory`
- Create a copy of environment file from the sample: `cp .env.sample .env`
- Open .env file with any text editor, e.g.: `nano .env`
- You will see variables with sample values. Replace the values with your own ones

### Environment variables explained
- WEBHOOK_TOKEN: a string to identify your requests from TravingView. Use any string you want. For example, you can use a 32-char hex number from [this online generator](https://codebeautify.org/generate-random-hexadecimal-numbers)

- NGROK_TOKEN: token generated from [Ngrok account](#Setup-Ngrok-account)
- NGROK_REGION: region from [Ngrok account](#Setup-Ngrok-account)
- NGROK_DOMAIN: domain from [Ngrok account](#Setup-Ngrok-account)

- TIME_ZONE: timezone name. Affects timestamps in logging. All TZ names are available [here](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)

- COMPOSE_PROJECT_NAME: used by docker engine to label images, doesn't affect the application

### Setup Ngrok account
- Register new account on [Ngrok page](https://ngrok.com)
- Upgrade to Personal plan
- Get your ngrok token from [here](https://dashboard.ngrok.com/get-started/your-authtoken)
- Add ngrok subdomain in "Domains" section. Use domain and region for your choice

### Setup Tradingview Alert
- In Message field, insert text in format:
```
{"token": "WEBHOOK_TOKEN_FROM_ENV_FILE", "symbol": "{{ticker}}", "exchange": "{{exchange}}", "close": "{{close}}"}
```
- In Webhook URL field, insert address in format: `https://domain-from-ngrok.com/webhook`

### Setup TWS Application
- Run the TWS application from your desktop
- Login with your username, password and trading mode
- From menu, open 'File' - 'Global Configuration...'
- 'API' - 'Settings' section: 'Enable activex and socket clients' -> ENABLE, 'API readonly' -> DISABLE, 'Socket port' -> 7497
- 'API' - 'Precautions' section: set -> ENABLE for all precautions
- Press 'Apply', then 'Ok'
- Close the application using 'X' button in the corner. That will upload application settings from desktop to IB server

### Setup Docker
- Install [Docker Desktop](https://www.docker.com/products/docker-desktop)

## Run
- Run TWS application
- Switch to the project folder: `cd /path/to/project/directory`
- Run: `docker compose up --build`
