from django import forms
from .models import Position, Employee


class StaffForm(forms.ModelForm):
    date_of_employment = forms.DateField(label='Дата трудоустройства',
                                         widget=forms.DateInput(format='%d-%m-%Y', attrs={'type': 'date'}),
                                         required=False)

    class Meta:
        model = Employee
        fields = ('surname', 'name', 'patronymic', 'position', 'date_of_employment' )


class PositionForm(forms.ModelForm):
    class Meta:
        model = Position
        fields = ('name',)
