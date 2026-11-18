from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("contact/", views.contact, name="contact"),
    path("login/", views.coming_soon, {"page": "login"}, name="login"),
    path("register/", views.coming_soon, {"page": "register"}, name="register"),
    path("companies/register/", views.coming_soon, {"page": "company"}, name="company_register"),
    path("privacy/", views.legal, {"page": "privacy"}, name="privacy"),
    path("terms/", views.legal, {"page": "terms"}, name="terms"),
    # Compatibility routes preserve the original static-page URLs during the migration.
    path("pages/login.html", views.coming_soon, {"page": "login"}),
    path("pages/register.html", views.coming_soon, {"page": "register"}),
    path("pages/company-register.html", views.coming_soon, {"page": "company"}),
    path("pages/privacy.html", views.legal, {"page": "privacy"}),
    path("pages/terms.html", views.legal, {"page": "terms"}),
]
