from django import forms

class StudentForm(forms.Form):
    Nom = forms.CharField(max_length=10)
    Prenom = forms.CharField(max_length=30)
    Matricule = forms.CharField(max_length=30)
    Naissance = forms.DateField()
    Telephone = forms.CharField(max_length=14)
    Ville = forms.CharField(max_length=20)
    Niveau = forms.CharField(max_length=20)
