# 🛡️ Telegram Anti-Scam & Anti-Spam Bot

[🔗 مستندات فارسی](PERSIONREADME.md)

A smart, multi-threaded Telegram bot developed using `pyTelegramBotAPI`. This bot automatically detects, manages, and blocks spam and scam users based on their message rates within specific timeframes.

---

## 🚀 Key Features

* **Smart Scam/Spam Detection:** Analyzes user message rates per second and applies a multi-level blacklist.
* **Multi-stage Punishment:** Automatically escalates repetitive offenders from Stage 1 to Stage 2 based on database records.
* **Background Worker:** Uses Python `threading` to continuously check blacklist expirations without interrupting the bot's main loop.
* **Advanced Message Listener:** Centrally logs various input formats (text, photos, documents, and voices).
* **Secure Configuration:** Protects sensitive data by loading tokens and database credentials via environment variables.

---

## 📂 Project Architecture

| File Name | Description |
| :--- | :--- |
| **`main.py`** | Core bot logic, listeners, background thread, and anti-spam enforcement. |
| **`config.py`** | Securely loads bot tokens and database configurations from the environment. |
| **`DDL.py`** | Database schema definition and initialization (Data Definition Language). |
| **`DML.py`** | Functions for inserting and updating blacklist records (Data Manipulation Language). |
| **`DQL.py`** | Functions for querying and validating offender statuses (Data Query Language). |

---

## 🗄️ Database Schema

This project utilizes a **MySQL** database to manage users and their restriction status.

### 1. `CUSTOMER` Table
* `ID` (BIGINT UNSIGNED, PK): Telegram Chat ID.
* `NAME` (VARCHAR): User's first name.
* `REGISTER_DATE` & `LAST_UPDATE` (DATETIME): Timestamps.

### 2. `BLACK_LIST` Table
* `CUSTOMER_ID` (BIGINT UNSIGNED, FK): References `CUSTOMER(ID)`.
* `STATUS` (VARCHAR): Current restriction status (`yes` / `no`).
* `STAGE` (INT): Punishment level (1 or 2).
* `TIME` (INT): Unix timestamp of the infraction.
* `DON` (VARCHAR): Action review status (`yes` / `no`).

---

## ⚙️ Installation & Setup

### 1. Install Dependencies
```bash
pip install -r requirements.txt