from django import forms
from .models import Visitor


class RegisterForm(forms.ModelForm):
    date_of_birth = forms.DateField(required=False, widget=forms.SelectDateWidget(
        years=range(1970, 2013),
        empty_label=("Year", "Month", "Date"),
        attrs={
            'class': 'form-control selectdatewidget-inline-select'
        }
    ))
    gender = forms.ChoiceField(required=False, choices=Visitor.GENDER_CHOICE, initial=0, widget=forms.RadioSelect())

    class Meta:
        model = Visitor
        fields = ('mobile_number', 'email', 'first_name', 'last_name', 'date_of_birth', 'gender')
