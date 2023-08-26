from django import forms

class VoltageForm(forms.Form):
    voltage = forms.FloatField()
    voltage.widget.attrs.update({
            'id' : 'voltage',
        })