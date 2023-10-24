from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _

from .models import EndPoint

class EndPointForm(ModelForm):
    class Meta:
        model = EndPoint
        fields = '__all__'
        labels = {
            "ipAddress": _("IP Address"),
            "port": _("Port"),
        }