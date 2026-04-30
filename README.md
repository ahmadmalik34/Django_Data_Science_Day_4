# Day 4: Blog App

This project is a simple blog application built with Django. It includes models for Posts and Categories, and views for displaying all posts and posts by category.

## Technology Stack
- Python
- Django

## Features

-   **Post Model**: Contains title, content, author, publication date, and a foreign key to the Category model.
-   **Category Model**: Contains a name and description for blog post categories.
-   **Views**:
    -   `all_posts`: Displays a list of all blog posts.
    -   `posts_by_category`: Displays posts belonging to a specific category.
-   **Templates**: Basic HTML templates for rendering the post list and category-specific posts.
-   **Admin**: Models are registered with the Django admin for easy content management.

## How to Run

1.  **Clone the repository.**
2.  **Navigate to the `Day_04_Blog_App` directory.**
3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    *(Create a requirements.txt file if one does not exist: `pip freeze > requirements.txt`)*
4.  **Apply migrations:**
    ```bash
    python manage.py migrate
    ```
5.  **Create a superuser to access the admin panel:**
    ```bash
    python manage.py createsuperuser
    ```
6.  **Run the development server:**
    ```bash
    python manage.py runserver
    ```
7.  Open your browser and go to `http://127.0.0.1:8000/` to see the blog.
8.  Access the admin panel at `http://127.0.0.1:8000/admin/` to create categories and posts.

## Screenshots
*(Add screenshots of your application here)*

