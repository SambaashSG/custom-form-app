from .models import ExtraInfo
from django.forms import ModelForm

class ExtraInfoForm(ModelForm):
    """
    The fields on this form are derived from the ExtraInfo model in models.py.
    """
    def __init__(self, *args, **kwargs):
        super(ExtraInfoForm, self).__init__(*args, **kwargs)
        self.fields['pre_employment_card_no'].error_messages = {
            "required": u"Type in your pre-employment card number",
            "invalid": u"Pre-employment card number is not correct",
        }
        self.fields['mobile_phone_number'].error_messages = {
            "required": u"Type in your mobile number",
            "invalid": u"Mobile number is not correct",
        }
        self.fields['voucher_code'].error_messages = {
            "required": u"Type in your voucher code",
            "invalid": u"Voucher code is not correct",
        }

    class Meta(object):
        model = ExtraInfo
        fields = ('pre_employment_card_no', 'mobile_phone_number', 'voucher_code')
