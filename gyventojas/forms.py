from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from gyventojas.models import Resident


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = Resident
        fields = ('username', 'email')  # Naudojame 'username' ir 'email' laukus iš modelio

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = Resident
        fields = ('username', 'email')  # Naudojame 'username' ir 'email'

    