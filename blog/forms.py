from django import forms
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User
from .models import Post, Comment


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)


class UserRegistrationForm(UserCreationForm):
  email = forms.EmailField(required=True)
  password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
  password2 = forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput)
  class Meta: #Esto es para que el formulario sepa que campos tiene que mostrar
    model = User
    fields = ['username', 'email', 'password1', 'password2']
    help_texts={k:"" for k in fields} #Esto es para que el formulario no muestre los mensajes de ayuda

class UserEditForm(UserCreationForm):
  email = forms.EmailField(required=False)
  password1 = forms.CharField(label="Modificar contraseña", widget=forms.PasswordInput)
  password2 = forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput)
  last_name = forms.CharField(label="Apellido", required=False)
  first_name = forms.CharField(label="Nombre", required=False)
  age = forms.IntegerField(label="Edad", required=False)


  class Meta: #Esto es para que el formulario sepa que campos tiene que mostrar
    model = User
    fields = ['username', 'email', 'first_name', 'last_name','age', 'password1', 'password2']
    help_texts={k:"" for k in fields} #Esto es para que el formulario no muestre los mensajes de ayuda
