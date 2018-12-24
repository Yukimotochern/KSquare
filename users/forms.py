from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from .models import Profile
from allauth.account.forms import LoginForm
from django import forms
from django.utils.translation import pgettext, ugettext, ugettext_lazy as _
from allauth.account import app_settings
from allauth.account.app_settings import AuthenticationMethod
from allauth.utils import (
    build_absolute_uri,
    get_username_max_length,
    set_form_field_order,
)


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = UserCreationForm.Meta.fields


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('portfolio_site', 'profile_pic')


class PasswordField(forms.CharField):

    def __init__(self, *args, **kwargs):
        render_value = kwargs.pop('render_value',
                                  app_settings.PASSWORD_INPUT_RENDER_VALUE)
        kwargs['widget'] = forms.PasswordInput(render_value=render_value,
                                               attrs={'placeholder':
                                                      kwargs.get("label")})
        super(PasswordField, self).__init__(*args, **kwargs)


class CustomLoginForm(LoginForm):

    password = PasswordField(label=_("密碼"))

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(LoginForm, self).__init__(*args, **kwargs)
        if app_settings.AUTHENTICATION_METHOD == AuthenticationMethod.EMAIL:
            login_widget = forms.TextInput(attrs={'type': 'email',
                                                  'placeholder':
                                                  _('電子郵件'),
                                                  'autofocus': 'autofocus'})
            login_field = forms.EmailField(label=_("E-mail"),
                                           widget=login_widget)
        elif app_settings.AUTHENTICATION_METHOD \
                == AuthenticationMethod.USERNAME:
            login_widget = forms.TextInput(attrs={'placeholder':
                                                  _('帳號'),
                                                  'autofocus': 'autofocus'})
            login_field = forms.CharField(
                label=_("Username"),
                widget=login_widget,
                max_length=get_username_max_length())
        else:
            assert app_settings.AUTHENTICATION_METHOD \
                == AuthenticationMethod.USERNAME_EMAIL
            login_widget = forms.TextInput(attrs={'placeholder':
                                                  _('Username or e-mail'),
                                                  'autofocus': 'autofocus'})
            login_field = forms.CharField(label=pgettext("field label",
                                                         "Login"),
                                          widget=login_widget)
        self.fields["login"] = login_field
        set_form_field_order(self, ["login", "password", "remember"])
        if app_settings.SESSION_REMEMBER is not None:
            del self.fields['remember']

    def login(self, *args, **kwargs):

        # Add your own processing here.

        # You must return the original result.
        return super(CustomLoginForm, self).login(*args, **kwargs)


