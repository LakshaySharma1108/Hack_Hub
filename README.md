
🚀 HackHub
HackHub is a dynamic web platform built with Django that helps users discover, track, and explore hackathons across the globe. Whether you're a student, developer, or enthusiast, HackHub makes it easy to stay informed about upcoming, ongoing, and past tech events.

🧩 Features
📅 Hackathon Categorization — See events grouped into upcoming, ongoing, and past.

🔎 Search & Filter — Search events by title, tech stack, mode, and more.

📝 Event Details — View complete information like dates, links, prize pool, location, etc.

🔧 Admin Panel — Easily manage events using Django's built-in admin interface.

🛠 Tech Stack
Layer	Technology
Frontend	HTML5, CSS3, JavaScript
Backend	Django (Python)
Database	SQLite (default) or PostgreSQL
Hosting	GitHub Pages (static) / PythonAnywhere / Render / Vercel (via API)

🚀 Setup Instructions
1. Clone the Repository
   bash
   Copy
   Edit
   git clone https://github.com/LakshaySharma1108/Hack_Hub.git
   cd HackHub
2. Create & Activate Virtual Environment
   bash
   Copy
   Edit
   python -m venv env
   source env/bin/activate    # On Windows use `env\Scripts\activate`
3. Install Dependencies
   bash
   Copy
   Edit
   pip install -r requirements.txt
4. Apply Migrations
   bash
   Copy
   Edit
   python manage.py migrate
5. Create Superuser (for Admin access)
   bash
   Copy
   Edit
   python manage.py createsuperuser
6. Run Development Server
   bash
   Copy
   Edit
   python manage.py runserver
   Open your browser and visit: http://127.0.0.1:8000

🧠 Possible Future Features
User Registration & Login

Bookmarking / Submitting Hackathons

Email Notifications

API for fetching external hackathon listings

👥 Contributing
Feel free to fork this project, make improvements, and submit a PR!

Fork the repo

Create a new branch (git checkout -b feature-name)

Commit your changes (git commit -m "Added feature")

Push and create a Pull Request

🤝 Acknowledgements
Built using Django and open-source love ❤️

UI inspired by the hackathon community

