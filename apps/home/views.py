from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView


def index(request):

    # Page from the theme 
    return render(request, 'pages/index.html')


class CustomLoginView(LoginView):
    def get_success_url(self):
        if self.request.user.is_authenticated:
            if self.request.user.profile:
                profile_pk = self.request.user.profile.pk
                return reverse_lazy('profile_detail', kwargs={'pk': profile_pk})
            else:
                return reverse_lazy('profile_create')
        else:
            return reverse_lazy('login')

LOGIN_REDIRECT_URL = CustomLoginView()