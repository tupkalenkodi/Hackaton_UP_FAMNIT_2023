from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django_user_agents.utils import get_user_agent
from Home.gpt import get_response
from Character.models import Character
from Home.models import HistoryItem


@login_required(login_url='login')
def process_gpt_request(request):
    if request.method == 'POST':
        character_name = request.POST.get('character')
        character = Character.objects.get(name=character_name)
        theme = request.POST.get('theme')

        if theme == '':
            theme = 'Any theme'
            result = get_response(character=character, theme=theme)
            HistoryItem(user=request.user, character=character,
                        theme=theme, text=result).save()

            return JsonResponse({'output': result})
        elif character is not None and theme is not None:
            result = get_response(character=character, theme=theme)
            HistoryItem(user=request.user, character=character,
                        theme=theme, text=result).save()

            return JsonResponse({'output': result})

        else:
            return JsonResponse({'output': 'Invalid character or theme.'})

    else:
        return JsonResponse({'output': 'Invalid request.'})


def homepage(request):
    user_agent = get_user_agent(request)

    if request.user.is_authenticated:
        template_name = 'Home/Logged_pages/create_content.html'
        user_characters = Character.objects.filter(user=request.user)
        context = {'user_characters': user_characters}
        if user_agent.is_mobile:
            layout_name = 'Home/Logged_pages/layout_mobile_logged.html'
        else:
            layout_name = 'Home/Logged_pages/layout_desktop_logged.html'
    else:
        template_name = 'Home/Homepages/homepage.html'
        context = {}
        if user_agent.is_mobile:
            layout_name = 'Home/Homepages/layout_mobile_homepages.html'
        else:
            layout_name = 'Home/Homepages/layout_desktop_homepages.html'

    context['layout_name'] = layout_name

    return render(request, template_name, context)


def faq(request):
    if get_user_agent(request).is_mobile:
        layout_name = 'Home/Homepages/layout_mobile_homepages.html'
    else:
        layout_name = 'Home/Homepages/layout_desktop_homepages.html'

    return render(request, 'Home/Homepages/faq.html', {'layout_name': layout_name})


def developers(request):
    if get_user_agent(request).is_mobile:
        layout_name = 'Home/Homepages/layout_mobile_homepages.html'
    else:
        layout_name = 'Home/Homepages/layout_desktop_homepages.html'

    return render(request, 'Home/Homepages/developers.html', {'layout_name': layout_name})


@login_required(login_url='login')
def history(request):
    user_characters = Character.objects.filter(user=request.user)
    history_items = reversed(sorted(HistoryItem.objects.filter(user=request.user),
                                    key=lambda x: x.created_at))

    chosen_character = request.POST.get('chosen_character')
    print(chosen_character)
    if request.method == 'POST':
        if chosen_character == 'None':
            history_items = reversed(sorted(HistoryItem.objects.filter(user=request.user),
                                            key=lambda x: x.created_at))
        else:
            history_items = reversed(sorted(HistoryItem.objects.filter(character__name=chosen_character),
                                            key=lambda x: x.created_at))

    if get_user_agent(request).is_mobile:
        layout_name = 'Home/Logged_pages/layout_mobile_logged.html'
    else:
        layout_name = 'Home/Logged_pages/layout_desktop_logged.html'

    return render(request, 'Home/Logged_pages/history.html', {'history_items': history_items,
                                                              'user_characters': user_characters,
                                                              'chosen_character': chosen_character,
                                                              'layout_name': layout_name})
