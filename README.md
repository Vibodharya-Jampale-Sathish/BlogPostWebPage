# 📝 BlogPostWebPage

A responsive web application to **create, read, update, and delete blog posts**, built using **Flask** and **PostgreSQL**. Ideal for personal blogging, company news pages, or content-driven sites.

---

## 🌟 Features

- User-friendly CRUD interface for blog posts
- Create, view list, read details, edit, and delete posts
- Clean, minimal design using HTML/CSS (optionally Bootstrap)
- Simple navigation and intuitive user experience
- Lightweight and easy to customize

---

## 🛠️ Technologies Used

| Technology       | Purpose                                              |
|------------------|------------------------------------------------------|
| **Flask**        | Web framework for building Python routes and views   |
| **Jinja2**       | Templating engine for HTML rendering                |
| **PostgreSQL**   | Relational database to store blog entries           |
| **psycopg2**     | Python adapter for PostgreSQL                       |
| **Bootstrap**    | Responsive, mobile-first CSS framework (optional)   |

---

### 📥 Installation

1. **Clone the repo**
   ```bash
   git clone https://github.com/Vibodharya-Jampale-Sathish/BlogPostWebPage.git
   cd BlogPostWebPage
---

## 🧠 Architecture
```mermaid


```mermaid


```mermaid
flowchart TD
    subgraph User Interface (Browser)
        A1[Login Form (/login)]
        A2[Registration Form (/register)]
        A3[Blog Post Form (/blog)]
        A4[Logout Link (/logout)]
    end

    subgraph Flask Application
        B1[Route: /login]
        B2[Route: /register]
        B3[Route: /blog]
        B4[Route: /logout]
        B5[Session Management]
        B6[Flash Messaging]
        B7[Templates: login.html, register.html, blog.html]
        B8[Validation & Redirect Logic]
    end

    subgraph PostgreSQL Database
        C1[(users Table)]
        C2[(blogs Table)]
    end

    A1 --> B1
    A2 --> B2
    A3 --> B3
    A4 --> B4

    B1 --> C1
    B2 --> C1
    B3 --> C2

    B1 --> B5
    B2 --> B6
    B3 --> B6
    B4 --> B5
    B1 --> B7
    B2 --> B7
    B3 --> B7
    B1 --> B8
    B2 --> B8
    B3 --> B8

```
