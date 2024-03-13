from django.urls import path
from . import views
from register import views as views2
from Character import views as views3


urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('faq', views.faq, name="faq"),
    path('developers', views.developers, name="developers"),
    path('register', views2.register_user, name="register"),
    path('login', views2.login_user, name="login"),
    path('logout', views2.logout_user, name="logout"),
    path('create_character', views3.create_character, name="create_character"),
    path('history', views.history, name="history"),
    path('process_gpt_request', views.process_gpt_request, name='process_gpt_request'),
]
