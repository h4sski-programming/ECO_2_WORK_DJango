from django import forms

from .models import Activity

# class ActivityForm(forms.Form):
#     date = forms.DateField(required=True)
#     distance = forms.IntegerField(required=True)
#     vehicle = forms.CharField(max_length=100, required=True)


class TestingForm(forms.ModelForm):

    name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))

    class Meta:
        model = Activity
        fields = ['date', 'distance', 'vehicle', 'name']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['date'].widget.attrs.update({
            'class': 'form-control',
        })
        self.fields['distance'].widget.attrs.update({
            'class': 'form-control',
            'min': '0',
        })
        self.fields['vehicle'].widget.attrs.update({
            'class': 'custom-select',
        })
