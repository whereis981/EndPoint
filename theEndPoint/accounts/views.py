from django.contrib.auth import login, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView

from theEndPoint.accounts.forms import EditProfileForm, RegisterUserForm
from theEndPoint.accounts.models import Profile

UserModel = get_user_model()


class RegisterUserView(CreateView):
    form_class = RegisterUserForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        response = super().form_valid(form)

        user = self.object
        login(self.request, user)

        return response


class DetailProfileView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'profile/profile_details.html'
    context_object_name = 'profile'

    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk')

        if pk:
            return Profile.objects.get(pk=pk)

        else:
            return self.request.user.profile


class EditProfileView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = EditProfileForm
    template_name = 'profile/profile_edit.html'

    def get_success_url(self):
        return reverse('profile_details', kwargs={'pk': self.object.pk})


class DeleteProfileView(LoginRequiredMixin, DeleteView):
    model = UserModel
    template_name = 'profile/profile_delete.html'
    success_url = reverse_lazy('home')
