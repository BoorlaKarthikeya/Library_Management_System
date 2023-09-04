# Library Management System (Django)

## Overview

The Library Management System is a web-based application developed using the Django framework. It serves as a comprehensive platform for managing various aspects of a library, including cataloging books, handling book circulation, managing user accounts, and generating reports.



## Features

- **Book Cataloging**: Easily add and manage books in the library's collection, including details such as title, author, genre, and availability status.

- **Circulation Management**: Streamline book borrowing and returning processes, ensuring accurate records of book loans.

- **User Account Management**: Manage user accounts, track book reservations, and provide online access to patrons for searching and reserving books.

- **Report Generation**: Generate detailed reports and analytics to aid library administrators in decision-making, including insights into book usage and overdue books.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/BoorlaKarthikeya/Library_Management_System
   cd LMS
   ```

2 . create a virtual environment and install dependencies

```bash
  python -m venv venv
  source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

3 .Migrate the database:

```bash
   python manage.py migrate
```

4. Create a superuser (admin):

```bash

   python manage.py createsuperuser
```

5 . Run the development server:

```bash

   python manage.py runserver
```

<h1>Usage</h1>
Log in as an administrator using the superuser credentials created during installation.
Start by adding books to the library's collection and managing user accounts.
Explore the various features to handle book circulation and generate reports.
Patrons can access the system to search for books, make reservations, and manage their accounts.
Technologies Used
Django framework
HTML, CSS, JavaScript for the frontend
PostgreSQL (or your preferred database) for data storage
Integration with barcode scanners and RFID systems for efficient book tracking.
Contributing
Contributions are welcome! Please fork the repository and create a pull request with your changes. Be sure to follow the code of conduct.

Demo:
Home page;

![Home page](<images/Screenshot%20(165).png>)
Login Page:

![Login page](<images/Screenshot%20(164).png>)
Add Student Page :

![Add Student page](<images/Screenshot%20(166).png>)
Add Book Page : 

![Add Book page](<images/Screenshot%20(168).png>)
Add Book Instance Page :

![Add Book Intance page](<images/Screenshot%20(167).png>)
Issue Book page :

![Issue Book page](<images/Screenshot%20(169).png>)
List Of Issued Books :
![Issued Books page](<images/Screenshot%20(172).png>)
List of Students :
![Students List page](<images/Screenshot%20(171).png>)

