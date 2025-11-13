# Calenote
A lightweight calendar and notes application built with Flask, PostgreSQL, and React.

## Features
- Calendar view for selecting days  
- Notes linked to specific dates  
- Events with date, time, and description  
- User registration and login (JWT-based)  
- REST API built with Flask and SQLAlchemy  
- PostgreSQL for data storage  

## Tech Stack
**Frontend:** React (Vite), JSX  
**Backend:** Flask, SQLAlchemy, JWT  
**Database:** PostgreSQL  

## Setup

### Backend
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Run:
```
python server/app.py
```

### Frontend
```
cd client
npm install
npm run dev
```

## Project Structure
```
server/
    app.py
    __init__.py
    db.py
    controllers/
    services/
    repositories/
    models/

client/
    src/
```
