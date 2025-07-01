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
flowchart TD
    %% User-facing routes
    A1[Login Page (/login)]
    A2[Register Page (/register)]
    A3[Blog Page (/blog)]
    A4[Logout Link (/logout)]

    %% Flask routes and logic
    B1[Flask Route: /login]
    B2[Flask Route: /register]
    B3[Flask Route: /blog]
    B4[Flask Route: /logout]
    B5[Session & Flash Logic]
    B6[Jinja2 Templates]
    B7[Validation & Redirects]

    %% Database
    C1[(users Table)]
    C2[(blogs Table)]

    %% Flow
    A1 --> B1 --> C1
    A2 --> B2 --> C1
    A3 --> B3 --> C2
    A4 --> B4

    B1 --> B5
    B2 --> B5
    B3 --> B5
    B4 --> B5

    B1 --> B6
    B2 --> B6
    B3 --> B6

    B1 --> B7
    B2 --> B7
    B3 --> B7

```
