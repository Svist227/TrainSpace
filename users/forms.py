from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator

from Chuvash_Workout.forms import MyValidator
from Chuvash_Workout.models import MyUsers


class Autoriz(forms.Form):
    username = forms.CharField(max_length=255, label='Логин')
    password = forms.CharField(max_length=255, label='Пароль')

class classAutoriz(AuthenticationForm):
    username = forms.CharField(max_length=255, label='Логин',widget=forms.TextInput(attrs={'class':'form-input'}))
    password = forms.CharField(max_length=255, label='Пароль',widget=forms.PasswordInput(attrs={'class':'form-input'}))
    class Meta:
        model = get_user_model()
        fields = ['username', 'password']
class Register2(forms.Form):
    gender_choise = (
        ('1', 'man'),
        ('2', 'woman')
    )
    name = forms.CharField(max_length=255, label='имя', min_length=5,validators=[MyValidator()],
                           error_messages={
                               'min_lenth': "слишком короткий заголовок",
                               'required':'Поле должно быть заполнено'},

                           )
    surname = forms.CharField(max_length=255, label='фамилия' ,
                              validators=[MinLengthValidator(5, message='Мин 5 сим'),MyValidator()])
    logins = forms.CharField(max_length=255,  label='логин')
    passwords = forms.CharField(max_length=255, label='пароль')
    gender = forms.ChoiceField(choices=gender_choise)


class Register(UserCreationForm):
     username = forms.CharField(max_length=255, label='Логин', min_length=5,widget=forms.TextInput(attrs={'class':'form-input'}))
     password1 = forms.CharField(max_length=255, label='Пароль', min_length=5,widget=forms.PasswordInput(attrs={'class':'form-input',}))
     password2 = forms.CharField(max_length=255, label='Повтор пароля', min_length=5,widget=forms.PasswordInput(attrs={'class':'form-input',}))
     class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'first_name', 'last_name','password1']
        labels = {
        'username':'Логин',
        'password1':'Пароль',
        'first_name':'Имя',
        'email':'E-mail'
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-input'}),
            'last_name': forms.TextInput(attrs={'class': 'form-input'}),
            'email': forms.TextInput(attrs={'class': 'form-input'})}


    # def clean_password2(self):
    #     cd = self.cleaned_data
    #     if cd['password'] != cd['password2']:
    #         raise forms.ValidationError('Пароли не совпадают')
    #      return cd['password']


     def clean_email(self):
        email = self.cleaned_data['email']
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError('Еmail уже зарегестрирован')
        return email

class AddRegister(forms.ModelForm):
    class Meta:
        model = MyUsers
        fields = ['photo', 'date_bitrh']
        widgets = {
            'date_bitrh': forms.TextInput(attrs={'class': 'form-input'})}
        labels = {
            'date_bitrh': "Дата рождения",
            'photo': "Фото"
        }

class UpdateProfile(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'first_name', 'last_name']

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-input'}),
            'last_name': forms.TextInput(attrs={'class': 'form-input'}),
            'email': forms.TextInput(attrs={'class': 'form-input'}),
            'username': forms.TextInput(attrs={'class': 'form-input'})}


class MyformChangePass(PasswordChangeForm):
    old_password = forms.CharField(max_length=255, label='Старый пароль', min_length=5,
                               widget=forms.TextInput(attrs={'class': 'form-input'}))
    new_password1 = forms.CharField(max_length=255, label='Новый пароль', min_length=5,
                                widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    new_password2 = forms.CharField(max_length=255, label='Подтверждение пароля', min_length=5,
                                widget=forms.PasswordInput(attrs={'class': 'form-input'}))