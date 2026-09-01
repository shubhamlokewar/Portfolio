# 🚀 Deploying the Portfolio

The portfolio can be deployed as a live Django application without purchasing a domain.

This project can be hosted on Render using:

- Django
- Gunicorn
- WhiteNoise
- PostgreSQL
- GitHub

Render provides a free `onrender.com` URL for the deployed web service.

---

## Deployment Architecture

```text
GitHub Repository
       │
       │ Git Push
       ↓
    Render
       │
       ├── Django Web Service
       │
       └── PostgreSQL Database
       │
       ↓
Public HTTPS Website
