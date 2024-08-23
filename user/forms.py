from django import forms

class UserForm(forms.Form):
    Admin = forms.CharField(max_length=10)
    Ancien_mot_de_passe = forms.CharField(max_length=30)
    Nouveau_mot_de_passe = forms.CharField(max_length=30)
    Confirmer_le_nouveau_mot_de_passe = forms.CharField(max_length=30)
    
class UserAdd(forms.Form):
    Pseudo = forms.CharField(max_length=30)
    mot_de_passe = forms.CharField(max_length=30)
    Confirmer_mot_de_passe = forms.CharField(max_length=30)