from django.contrib import messages
from django.shortcuts import redirect, render
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.http import require_http_methods

from .forms import ContactForm


@ensure_csrf_cookie
def home(request):
    return render(request, "website/home.html", {"contact_form": ContactForm()})


@require_http_methods(["POST"])
def contact(request):
    submitted_data = request.POST.copy()
    submitted_data["full_name"] = submitted_data.get("name", "")
    label_to_value = {label: value for value, label in ContactForm.INQUIRY_CHOICES}
    submitted_data["inquiry_type"] = label_to_value.get(submitted_data.get("inquiry", ""), "")
    form = ContactForm(submitted_data)
    if form.is_valid():
        # This is intentionally not persisted or emailed until a support service is configured.
        messages.info(request, "Your message is valid, but message delivery has not been connected yet.")
    else:
        messages.error(request, "Please correct the highlighted contact fields.")
    return redirect("home")


def coming_soon(request, page):
    content = {
        "login": ("Login is coming soon", "Your PICKCAM account portal will be available with the platform launch."),
        "register": ("Join PICKCAM", "Customer registration will be available when the PICKCAM app launches."),
        "company": ("Partner with PICKCAM", "Company registration will be available when the partner portal launches. Please use the contact form for partnership inquiries."),
    }
    title, description = content[page]
    return render(request, "website/coming_soon.html", {"title": title, "description": description, "page": page})


def legal(request, page):
    content = {
        "privacy": ("Privacy Policy", "PICKCAM's privacy policy will be published before the platform begins collecting user information."),
        "terms": ("Terms & Conditions", "PICKCAM's terms and conditions will be published before the platform launches."),
    }
    title, description = content[page]
    return render(request, "website/legal.html", {"title": title, "description": description})
