# Lunch Voting System

## Description
This application is designed for voting on lunch menus in a company. Employees can register, log in, and vote for the menu available on the current day. After 1 PM, the menu with the highest number of votes is displayed.

## Technologies
- Django
- Django REST Framework
- PostgreSQL (or SQLite for development)
- JWT for authentication
- Docker
- PyTests

## Installation
### Requirements
- Python 3.x
- pip
- Docker (for containerization)

### Running the Project
1. **Clone the repository:**
   ```bash
   git clone <YOUR_REPOSITORY_URL>
   cd <project_folder>
2. **Create a virtual environment (optional, but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # for Linux/Mac
   venv\Scripts\activate  # for Windows
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
4. **Run the server:**
   ```bash
   python manage.py migrate  # Apply migrations
   python manage.py runserver  # Start the server

### Running with Docker
1. **Build the containers:**
   ```bash
   docker-compose build
2. **Run the containers:**
   ```bash
   docker-compose up

## Usage
- To register a new user, send a POST request to `/api/employees/register/` with the necessary data.
- For authentication, use `/api/token/`, providing the username and password.
- Retrieve the current menu by sending a GET request to `/api/menus/`.
- Vote for a menu by sending a POST request to `/api/votes/` with the desired `menu_id`.

## Testing
- To run the tests, use:
   ```bash
   pytest
