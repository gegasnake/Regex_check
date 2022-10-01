from django.urls import path

from .views import RegexFormView, RegexMatchesView, RegexDoesNotMatchView

urlpatterns = [
    path('', RegexFormView.as_view(), name='home'),
    path('matches/', RegexMatchesView.as_view(), name='matches'),
    path('doesnotmatch/', RegexDoesNotMatchView.as_view(), name='doesnotmatch'),
]
