from django.forms import ModelForm

from .models import Controller

class ControllerForm(ModelForm):
    class Meta:
        model = Controller
        fields = '__all__'

    def __init__(self, *args, **kwargs) -> None:
        super(ControllerForm, self).__init__(*args, **kwargs)
        self.fields['ki'].widget.attrs.update({
            'id' : 'ki',
        })
        self.fields['kp'].widget.attrs.update({
            'id' : 'kp',
        })
        self.fields['setPoint'].widget.attrs.update({
            'id' : 'setPoint',
        })