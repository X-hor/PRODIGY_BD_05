# Hotel Booking Platform - Backend API

A backend REST API for a Hotel Booking Platform developed using **Django** and **Django REST Framework**.

The API allows customers to register, browse hotel rooms, make reservations, and manage their bookings. It also provides role-based access control for administrators and receptionists to manage hotel operations securely.

---

## Features

### Authentication & Authorization

- User registration
- JWT authentication
- User profile endpoint
- Role-based access control
- Three user roles:
  - Admin
  - Receptionist
  - Customer

---

### Room Management

- Create new rooms (Admin only)
- Update room information
- Delete rooms
- List all rooms
- View room details
- Search and filter rooms
- View available rooms for a specific date range

---

### Booking Management

- Create bookings
- View personal bookings
- Cancel bookings
- Prevent overlapping bookings
- Validate booking dates
- Prevent booking inactive rooms

---

## Technologies Used

- Python 3
- Django
- Django REST Framework
- PostgreSQL
- Simple JWT
- drf-spectacular (Swagger/OpenAPI)
- django-filter

---

## Project Structure

```
PRODIGY_BD_05/
│
├── accounts/
│
├── rooms/
│
├── bookings/
│
├── config/
│
├── postman/
│
├── requirements.txt
├── README.md
├── .env.example
└── manage.py
```

---

## API Endpoints

### Authentication

| Method | Endpoint |
|---------|----------|
| POST | /api/auth/register/ |
| POST | /api/auth/login/ |
| POST | /api/auth/refresh/ |
| GET | /api/auth/profile/ |

---

### Rooms

| Method | Endpoint |
|---------|----------|
| GET | /api/rooms/ |
| GET | /api/rooms/{id}/ |
| POST | /api/rooms/ |
| PUT | /api/rooms/{id}/ |
| DELETE | /api/rooms/{id}/ |
| GET | /api/rooms/available/ |

---

### Bookings

| Method | Endpoint |
|---------|----------|
| GET | /api/bookings/ |
| POST | /api/bookings/ |
| DELETE | /api/bookings/{id}/ |

---

## Installation

Clone the repository:

```bash
git clone https://github.com/X-hor/PRODIGY_BD_05.git
```

Move into the project directory:

```bash
cd PRODIGY_BD_05
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment:

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project root.

Example:

```env
SECRET_KEY=your_secret_key

DEBUG=True

DB_NAME=hotel_booking_db
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
```

---

## Database Migration

```bash
python manage.py makemigrations

python manage.py migrate
```

---

## Create an Admin User

```bash
python manage.py createsuperuser
```

---

## Run the Server

```bash
python manage.py runserver
```

The API will be available at:

```
http://127.0.0.1:8000/
```

---

## API Documentation

Swagger UI:

```
http://127.0.0.1:8000/api/docs/
```

OpenAPI Schema:

```
http://127.0.0.1:8000/api/schema/
```

---

## Business Rules

- Only authenticated users can access protected endpoints.
- Only Admin users can create, update, or delete rooms.
- Customers can only manage their own bookings.
- Bookings cannot overlap for the same room.
- Check-out date must be after the check-in date.
- Inactive rooms cannot be booked.

---

## Future Improvements

- Email verification
- Password reset
- Automatic booking completion
- Room images
- Payment integration
- Booking history
- Dashboard and analytics
- Docker support
- Automated tests
- CI/CD pipeline

---

## Repository

https://github.com/X-hor/PRODIGY_BD_05

---

