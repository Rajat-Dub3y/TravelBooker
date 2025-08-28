# TravelBooker - Travel Booking Web Application

**TravelBooker** is a Django-based web application that allows users to browse travel options (Flights, Trains, Buses), make bookings, and manage their bookings. The application uses MySQL for the database and is deployed on PythonAnywhere.

**Deployed App:** \https://raja1dub3y.pythonanywhere.com/

---

## Features

### User Management

* Register, login, and logout using Django’s authentication system.
* Update user profile information.

### Travel Options

* TravelOption model includes: Type, Source, Destination, Date/Time, Price, Available Seats.
* Users can filter travel options by type, source, destination, and date.

### Booking

* Users can book travel options, specifying the number of seats.
* Each booking includes: Booking ID, User, Travel Option, Number of Seats, Total Price, Booking Date, Status.
* View current and past bookings.
* Cancel bookings.

### Frontend

* User-friendly interface built with Django templates and **Bootstrap 5**.
* Responsive design for desktop and mobile devices.

---

## Tech Stack

* **Backend:** Django 5.2+
* **Database:** MySQL
* **Frontend:** Django Templates + Bootstrap 5
* **Deployment:** PythonAnywhere

---

## Installation (Local Setup)

1. Clone the repository:

   ```bash
   git clone [Your GitHub Link]
   cd TravelBooker
   ```
2. Create and activate a virtual environment:

   ```bash
   python -m venv myenv
   source myenv/bin/activate    # Linux/Mac
   myenv\Scripts\activate     # Windows
   ```
3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```
4. Configure MySQL database:

   * Create a database and user.
   * Update `settings.py` with credentials.
5. Apply migrations:

   ```bash
   python manage.py migrate
   ```
6. Create a superuser:

   ```bash
   python manage.py createsuperuser
   ```
7. Run the development server:

   ```bash
   python manage.py runserver
   ```
8. Open in browser: `http://127.0.0.1:8000/`

---

## Deployment (PythonAnywhere)

1. Upload project files or clone repository.
2. Set working directory to `/home/username/TravelBooker/`.
3. Create and activate a virtualenv, then install dependencies:

   ```bash
   pip install -r requirements.txt
   ```
4. Update `settings.py` for PythonAnywhere MySQL database.
5. Configure WSGI file to point to Django project.
6. Reload the web app.
7. Access via your PythonAnywhere URL.

---

## Usage

1. Register or login as a user.
2. Browse available travel options.
3. Book travel by selecting options and confirming.
4. View and manage current/past bookings.
5. Cancel bookings if needed.

---

## Additional Features

* Input validation for booking seats.
* Search and filter travel options.
* Unit tests for key features.
* MySQL database integration.

---
