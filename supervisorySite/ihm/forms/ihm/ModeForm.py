from django import forms

class ModeForm(forms.Form):
    CHOICES = [
        ('M', 'Manual'),
        ('A', 'Automatic')
    ]
    mode = forms.ChoiceField(
        widget = forms.RadioSelect(),
        choices = CHOICES,
        label='',
    )
    mode.widget.attrs.update({
        'id' : 'mode',
    })