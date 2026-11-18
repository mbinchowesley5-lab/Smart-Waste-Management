# PICKCAM Django Website

PICKCAM is now a Django-powered landing website, structured so that customer accounts, company onboarding, and a REST API can be added without replacing the frontend.

## Run locally

```powershell
python manage.py migrate
python manage.py runserver
```

Then open `http://127.0.0.1:8000/`.

## Structure

- `pickcam/` — Django project configuration and root URLs.
- `website/` — landing-page views, routes, and contact form validation.
- `templates/website/` — Django templates for the landing, legal, and coming-soon pages.
- `css/` and `js/` — source static assets, served as `/static/css/` and `/static/js/`.

The current contact endpoint validates submitted data but deliberately does not store or email it until PICKCAM's support/backend integration is configured.

For production, set a secure `SECRET_KEY`, turn `DEBUG` off, configure `ALLOWED_HOSTS`, and serve collected static files through the deployment platform.
