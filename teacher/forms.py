from django import forms

class TeacherForm(forms.Form):
    Nom = forms.CharField(max_length=10)
    Prenom = forms.CharField(max_length=30)
    Genre = forms.CharField(max_length=30)
    Matière = forms.CharField(max_length=30)
    Matricule = forms.CharField(max_length=30)
    Age = forms.CharField(max_length=30)
    Telephone = forms.CharField(max_length=14)
    Ville = forms.CharField(max_length=20)
    