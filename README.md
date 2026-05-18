
---


# Scam Detector Bot

This project is a Telegram bot built with Python that monitors user behavior based on message frequency in a short time window.  
If a user sends too many messages too quickly, they are marked as suspicious and added to a blacklist in the database.

## Features

- Detect suspicious behavior based on message frequency
- Store users in a MySQL database
- Automatically add suspicious users to the blacklist
- Connect to Telegram using `telebot`
- Save customer information in the `CUSTOMER` table

## Tech Stack

- **Programming Language:** Python
- **Database:** MySQL
- **Libraries:**
  - `mysql.connector` for MySQL connection
  - `pyTelegramBotAPI` / `telebot` for Telegram bot development
  - `time` for time tracking

## Project Structure
```bash
.
├── config.py         # Database settings and bot token
├── DML.py            # Database operations such as blacklisting users
├── main.py           # Bot logic and scam detection
└── requirements.txt  # Required Python packages
