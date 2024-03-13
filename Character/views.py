from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django_user_agents.utils import get_user_agent
from .forms import CharacterForm


@login_required(login_url='login')
def create_character(request):
    if request.method == 'POST':
        form = CharacterForm(request.POST)
        if form.is_valid():
            character = form.save(commit=False)
            character.user = request.user
            character.save()

            return redirect('homepage')
    else:
        form = CharacterForm()

    if get_user_agent(request).is_mobile:
        layout_name = 'Home/Logged_pages/layout_mobile_logged.html'
    else:
        layout_name = 'Home/Logged_pages/layout_desktop_logged.html'

    return render(request, 'Character/create_character.html', {'form': form, 'layout_name': layout_name})
