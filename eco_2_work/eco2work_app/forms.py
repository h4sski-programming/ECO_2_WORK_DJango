from django import forms

from .models import Activity

# class ActivityForm(forms.Form):
#     date = forms.DateField(required=True)
#     distance = forms.IntegerField(required=True)
#     vehicle = forms.CharField(max_length=100, required=True)


class TestingForm(forms.Form):

    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'special'}))

    class Meta:
        model = Activity
        fields = ['date', 'distance', 'vehicle', 'name']
