from django.fo 
from .models import MyUser

class MyUserForm(ModelForm):
    class Meta:
        model= MyUser
        