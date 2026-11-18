from django import forms


class ContactForm(forms.Form):
    INQUIRY_CHOICES = [
        ("general", "General Inquiry"),
        ("support", "Customer Support"),
        ("partnership", "Company Partnership"),
        ("registration", "Business Registration"),
        ("other", "Other"),
    ]

    full_name = forms.CharField(max_length=120)
    email = forms.EmailField()
    phone = forms.CharField(max_length=30, required=False)
    inquiry_type = forms.ChoiceField(choices=INQUIRY_CHOICES)
    subject = forms.CharField(max_length=180)
    message = forms.CharField(widget=forms.Textarea, max_length=4000)
