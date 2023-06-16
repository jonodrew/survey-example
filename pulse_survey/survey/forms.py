
from django import forms
from django.core.exceptions import ValidationError

CABINET_OFFICE_DOMAINS = ("digital.cabinet-office.gov.uk", "cabinetoffice.gov.uk", "no10.gov.uk")


def is_cabinet_office_email(email_address: str) -> bool:
    """
    This function checks whether the email address given ends in a Cabinet Office domain. If there are changes to the
    business units in the Cabinet Office, the constant CABINET_OFFICE_DOMAINS should be updated. This does not confirm
    whether the address is actually valid; whether it's connected to a person; or anything else: only that it is a
    possible Cabinet Office email address
    """
    if not email_address.lower().split("@")[-1] in CABINET_OFFICE_DOMAINS:
        raise ValidationError("Please enter a Cabinet Office email address")
    return True


class FeedbackForm(forms.Form):
    template_name = "feedback.html"
    email = forms.EmailField(required=False, validators=[is_cabinet_office_email])
    content = forms.TextInput()

