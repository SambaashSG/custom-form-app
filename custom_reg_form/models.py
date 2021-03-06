from django.conf import settings
from django.db import models
from django.core.validators import RegexValidator
# Backwards compatible settings.AUTH_USER_MODEL
USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')


class ExtraInfo(models.Model):
    """
    This model contains two extra fields that will be saved when a user registers.
    The form that wraps this model is in the forms.py file.
    """
    user = models.OneToOneField(USER_MODEL, null=True, on_delete=models.CASCADE)



    pre_employment_card_no = models.CharField(
        verbose_name="Pre-employment Card No",
        max_length=50,
    )

    mobile_phone_number = models.CharField(
        verbose_name="Mobile phone number",
        max_length=15,
    )

    voucher_code = models.CharField(
        verbose_name="Voucher Code",
        max_length=14,
    )
