from django.shortcuts import render, redirect
from .forms import RegistrationForm
from .models import CustomUser, Profile
import uuid

def index(request):
    if request.method == 'POST':
        return redirect('register')
    return render(request, 'index.html')

def get_random_id():
    return str(uuid.uuid4())[:10]

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            profile = Profile(user=user, random_id=get_random_id())
            profile.save()
            return redirect('profile', pk=user.pk)
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

def profile(request, pk):
    user = CustomUser.objects.get(pk=pk)
    return render(request, 'profile.html', {'user': user})
