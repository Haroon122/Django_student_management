from django import forms
from .models import Student

class StudentForm(forms.ModelForm):  # Form ka naam sahi hai
    class Meta:
        model = Student
        fields = ["name", "roll_number", "student_class", "gender"]
        widgets = {
            'gender': forms.Select(attrs={'class': 'form-select'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
        
        # Add placeholders
        self.fields['name'].widget.attrs['placeholder'] = 'Enter student name'
        self.fields['roll_number'].widget.attrs['placeholder'] = 'Enter roll number'
        self.fields['student_class'].widget.attrs['placeholder'] = 'Enter class'

    def clean_roll_number(self):
        roll_number = self.cleaned_data.get('roll_number')
        if not roll_number.isalnum():
            raise forms.ValidationError("Roll number must contain only letters and numbers")
        return roll_number
