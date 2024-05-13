# Django Notes App

Welcome to the Django Notes App repository!

This application allows users to create, manage, and organize their notes effectively using Django.

![app_logo](./static/images/python_django_logo.jpg)

## Features

- Create, edit, and delete notes with ease.
- Organize notes into different categories or tags.
- User authentication and authorization for secure access to notes.
- Search functionality to quickly find specific notes.

## Installation

1. Clone this repository to your local machine.
2. Install the required dependencies:
    ```
    pip install -r requirements.txt
    ```
3. Apply migrations to set up the database: 
    ```
    python manage.py migrate
    ```
4. Create a superuser account to access the admin panel:
    ```
    python manage.py createsuperuser
    ```
5. Start the development server:
    ```
    python manage.py runserver
    ```
6. Visit `http://localhost:8000` in your web browser to access the application.

## Usage

1. Log in with your superuser account or register a new account.
2. Create notes by clicking on the "New Note" button.
3. Edit or delete notes as needed.
4. Organize notes by adding tags or categories.
5. Use the search bar to find specific notes quickly.

## Contributing

Contributions are welcome! If you'd like to add new features, improve existing ones, or fix any issues, feel free to open a pull request.

## Acknowledgements

Special thanks to the [Letícia Portell](https://www.linkedin.com/in/leportella/) for clear instructions and guidance to develop this app and to the Django community for creating such a powerful and versatile web framework.
