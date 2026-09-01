from django import forms

from .models import ContactMessage


class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage

        fields = [
            "name",
            "email",
            "subject",
            "message",
        ]

        widgets = {
            "name": forms.TextInput(
                attrs={
                    "placeholder": "Your Name",
                    "autocomplete": "name",
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    "placeholder": "Your Email",
                    "autocomplete": "email",
                }
            ),
            "subject": forms.TextInput(
                attrs={
                    "placeholder": "Subject",
                }
            ),
            "message": forms.Textarea(
                attrs={
                    "placeholder": "Your Message",
                    "rows": 6,
                }
            ),
        }

    def clean_name(self):
        name = self.cleaned_data["name"].strip()

        if len(name) < 2:
            raise forms.ValidationError(
                "Name must contain at least 2 characters."
            )

        return name

    def clean_message(self):
        message = self.cleaned_data["message"].strip()

        if len(message) < 10:
            raise forms.ValidationError(
                "Message must contain at least 10 characters."
            )

        return message