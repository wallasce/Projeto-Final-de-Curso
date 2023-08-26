from django import forms

class ModeForm(forms.Form):
    CHOICES = [
        ('M', 'Manual'),
        ('A', 'Automático')
    ]
    mode = forms.ChoiceField(
        widget = forms.RadioSelect,
        choices = CHOICES,
    )
    mode.widget.attrs.update({
            'id' : 'mode',
        })