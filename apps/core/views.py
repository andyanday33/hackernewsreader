from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)

            return HttpResponseRedirect('frontpage')
    else:
        form = UserCreationForm()

    return render(request, 'core/signup.html', {'form': form})