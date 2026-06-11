from django import forms
from .models import Patient

class PatientForm(forms.ModelForm):
    class Meta:
        model=Patient
        fields=[
            "name",
            "age",
            "disease"
        ]
    def clean(self):
        cleaned_data=super().clean()
        age=cleaned_data.get("age")
        disease=cleaned_data.get("disease")
        if age <35 and disease.lower()=="heart attack":
            raise forms.ValidationError("patient is too young to undergo heart surgery")
        return cleaned_data

    def clean_age(self):
        age=self.cleaned_data["age"]
        if age<0:
            raise forms.ValidationError("age cannot be negative")
        return age
    def clean_name(self):
        name=self.cleaned_data["name"]
        if len(name)<3:
            raise forms.ValidationError("name is too short")
        return name
    def clean_disease(self):
        disease=self.cleaned_data["disease"]
        if len(disease)<4:
            raise forms.ValidationError("disease name is too short ")
        return disease