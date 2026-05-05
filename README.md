# 🎨 Blog Admin & Templates

<div align="center">

**Build a Public Blog with Django Admin**

[![Django](https://img.shields.io/badge/Django-5.0%2B-darkgreen?style=flat-square&logo=django)](https://www.djangoproject.com/)
[![SQLite](https://img.shields.io/badge/Database-SQLite-blue?style=flat-square&logo=sqlite)](https://www.sqlite.org/)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=flat-square&logo=python)](https://www.python.org/)

[Features](#-features) • [Installation](#-installation) • [Usage](#-quick-start)

</div>

---

## 🎯 Overview

Build a powerful admin interface to manage blog posts + a public-facing blog that displays posts to site visitors.

**Django admin is genuinely one of the best features in any web framework.**

---

## ✨ Features

| Feature | Details |
|---------|---------|
| 🔐 **Django Admin** | Built-in CMS to manage posts, authors, categories |
| 📖 **Blog List View** | Display all posts with metadata |
| 📄 **Post Detail View** | Individual post pages with full content |
| 🎨 **Custom Styling** | Beautiful CSS theme for public blog |
| 🔗 **Navigation** | Links between list and detail views |
| 👤 **Author Info** | Display author details with each post |

---

## 📦 Tech Stack

- **Framework:** Django 5.0+
- **Database:** SQLite3
- **Frontend:** HTML5 + CSS3 (custom theme)
- **Language:** Python 3.8+

---

## 🚀 Quick Start

### Installation

```bash
# Create virtual environment
python -m venv venv

# Activate it
.\venv\Scripts\activate  # Windows
source venv/bin/activate  # macOS/Linux

# Install dependencies
pip install django python-decouple

# Apply migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser
```

### Run Locally

```bash
python manage.py runserver
```

Access:
- **Blog:** `http://127.0.0.1:8000/`
- **Admin:** `http://127.0.0.1:8000/admin/`

---

## 🔧 Django Admin Setup

### Register Models

```python
# blog/admin.py
from django.contrib import admin
from .models import Author, Category, Post

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    search_fields = ['name', 'bio']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    search_fields = ['name']

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created_at']
    search_fields = ['title', 'content']
    list_filter = ['categories', 'created_at']
    filter_horizontal = ['categories']
```

### Admin Features

✅ List view with filtering and searching  
✅ Custom columns in list display  
✅ Inline editing  
✅ Many-to-many management  
✅ Date/time filtering  
✅ Bulk actions  

---

## 📄 Public Blog Views

### List View

```python
def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'blog/post_list.html', {'posts': posts})
```

### Detail View

```python
def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
```

---

## 🎨 Templates

### base.html
Shared layout with navigation, header, footer.

### post_list.html
Shows all posts in a card grid with excerpts.

### post_detail.html
Full post content with author info and categories.

---

## 📂 Project Structure

```
Day_04_Blog_App/
├── manage.py
├── config/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── blog/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   ├── migrations/
│   └── templates/
│       ├── base.html
│       ├── post_list.html
│       └── post_detail.html
└── static/
    └── css/
        └── style.css
```

---

## 🔑 Key Concepts

### Django Admin
Pre-built interface for CRUD operations. Saves hours of development time.

### Template Rendering
`render()` function passes data to templates and returns HTML.

### Django Template Language (DTL)
`{{ variable }}` and `{% for item in items %}` for dynamic content.

### URL Patterns
`path('posts/<int:pk>/', views.post_detail)` with dynamic parameters.

---

## 📖 What You'll Learn

✅ Register models in Django admin  
✅ Customize admin display and filtering  
✅ Create function-based views  
✅ Render templates with context data  
✅ Django Template Language basics  
✅ URL routing with path parameters  
✅ Connect views to templates  
✅ Static files and CSS styling  

---

## 🔄 Next Steps

- **Day 5:** Add authentication, user profiles, and post creation forms

---

<div align="center">

**Day 4 of 50 — Django × Data Science Challenge**

Building the public interface and admin panel.

</div>

