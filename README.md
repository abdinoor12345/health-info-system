🏥 Health Information System
This project is a basic Health Information Management System where a doctor (system user) can:

Create health programs (e.g., TB, Malaria, HIV, etc.)

Register new clients

Enroll clients into one or more health programs

Search for clients

View a client's profile including enrolled programs

Expose client profile data via a public API

🛠️ Tech Stack
Frontend | Backend | Styling | Other
Vue.js | Django REST Framework (DRF) | TailwindCSS | MYSQL

📦 Project Structure
/```python
backend (Django + DRF)
/frontend (Vue.js + Tailwind)

```
/backend ➔ Django REST Framework project containing APIs for clients, health programs, and enrollments

/frontend ➔ Vue.js project using Tailwind CSS for styling the UI and consuming the backend APIs

## 🚀 Getting Started

**1. Clone the repository
**`https://github.com/abdinoor12345/health-info-system
` 
2**. Setup Backend (Django)**
`cd backend
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate     # Windows
pip install mysqlclient
pip install djangorestframework
pip install django-cors-headers
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

`
The backend server will start at:
` http://localhost:8000/
` 
**3. Setup Frontend (Vue.js)
**cd frontend
`npm install
npm run dev`

The frontend will start at:
`http://localhost:5173/
`

** 📋 API Endpoints (Backend)
**
Method | Endpoint |           Description
POST | /register/ |           Register a doctor (user)
POST | /login/ |              Login and get auth token
GET | /health_programs/ |      List all health programs
POST | /health_programs/ |      Create a new health program
GET | /clients/ |                 List all registered clients
POST | /clients/ |                Register a new client
GET | /profile/<client_id>/ |      View a client's full profile
GET | /clients/search/?query=name | Search clients by name
POST | /enrollments/ |              Enroll a client into a program

program

**🖥️ Frontend Features**

Dashboard for programs and clients

Forms for client registration and health program creation

Client search functionality

Profile view for each client

Fully responsive design with TailwindCSS

**✨ Extra Features
**Token-based authentication (DRF tokens)

Proper error handling

Validation on both backend and frontend

Reusable Vue components

Clean and responsive UI


**🧪 Future Improvements
**Unit tests and API tests

JWT Authentication instead of simple tokens

Pagination for clients list

Profile editing for clients

Client photo uploads

Deployment on Vercel (Frontend) and Railway/Render (Backend)

![dashboard 
](screenshots/dashboard.png)

![ enrollments
](screenshots/enrollments.png)

![formclients
](screenshots/FORMCLIENTS.PNG)

![PROGRAMFORM
](screenshots/programform.png)


 🧑‍⚕️ Clients and Programs Management
In this system, both listing and creation of Clients and Health Programs are seamlessly handled on the same page.

✅ Integrated Views

For Clients, the system displays a list of all registered clients along with an option to add a new client without leaving the page.

For Health Programs, users can view all existing programs and create a new program in the same interface.

✅ Dynamic Form Visibility

A toggle button is available to show or cancel the creation forms for both Clients and Programs.

This keeps the pages clean, minimal, and focused until the user explicitly wants to perform a creation action.

✅ Enhanced User Workflow

Doctors (users) can quickly view, create, and manage data from a single page without navigating between multiple sections.

This improves speed, reduces clicks, and provides a better user experience.

✅ Demo Available

The behavior of the Client and Program management pages is shown clearly in the PowerPoint presentation with screenshots and a video demonstration.

