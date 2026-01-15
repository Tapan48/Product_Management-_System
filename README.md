# Product Management System

A full-stack product management system built with FastAPI and React.

## Features

- CRUD operations for products
- PostgreSQL database integration
- RESTful API endpoints
- React frontend with modern UI

## Setup

### Backend

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install fastapi sqlalchemy psycopg2-binary python-dotenv uvicorn
```

3. Create a `.env` file based on `.env.example`:
```bash
cp .env.example .env
```

4. Update the `.env` file with your database credentials.

5. Run the FastAPI server:
```bash
uvicorn main:app --reload
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

## API Endpoints

- `GET /` - Welcome message
- `GET /products` - Get all products
- `GET /product/{id}` - Get product by ID
- `POST /products` - Create a new product
- `PUT /products/{id}` - Update a product
- `DELETE /products/{id}` - Delete a product

## Database Schema

**Product**
- id (Integer, Primary Key)
- name (String)
- description (String)
- price (Float)
- quantity (Integer)
