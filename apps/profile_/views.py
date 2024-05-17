from django.shortcuts import redirect
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from apps.profile_.models import Profile
from apps.profile_.forms import ProfileForm


class ProfileCreateView(LoginRequiredMixin, CreateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'profile/profile_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('profile_detail', kwargs={'pk': self.object.pk})


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'profile/profile_form.html'

    def get_success_url(self):
        return reverse_lazy('profile_detail', kwargs={'pk': self.object.pk})


class ProfileDeleteView(LoginRequiredMixin, DeleteView):
    model = Profile
    template_name = 'profile/profile_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('profile_new')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.delete()
        return redirect(success_url)


class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'profile/profile_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile_pk'] = self.object.pk
        return context
