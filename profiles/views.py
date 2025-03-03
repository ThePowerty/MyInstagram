from django.contrib import messages
from django.views.generic.edit import FormView
from django.utils.decorators import method_decorator
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView
from profiles.models import UserProfile
from django.views.generic.edit import UpdateView
from django.views.generic import ListView
from .forms import ProfileFollow
from profiles.models import Follow

@method_decorator(login_required, name='dispatch')
class ProfileDetailView(DetailView, FormView):
    model = UserProfile
    template_name = "profile/profile_detail.html"
    context_object_name = "profile"
    form_class = ProfileFollow

    def get_initial(self):
        self.initial['profile_pk'] =  self.get_object().pk
        return super().get_initial()

    def form_valid(self, form):
        profile_pk = form.cleaned_data.get('profile_pk')
        following = UserProfile.objects.get(pk=profile_pk)

        if Follow.objects.filter(
              follower=self.request.user.profile,
              following=following
        ).count():
            Follow.objects.filter(
                  follower=self.request.user.profile,
                  following=following
              ).delete()
            messages.add_message(self.request, messages.SUCCESS, f"Se ha dejado de seguir a {following.user.username}")
        else:
            Follow.objects.get_or_create(
              follower=self.request.user.profile,
              following=following
            )
            messages.add_message(self.request, messages.SUCCESS, f"Se empieza a seguir a {following.user.username}")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('profile:detail', args=[self.get_object().pk])
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        following = Follow.objects.filter(follower=self.request.user.profile, following=self.get_object()).exists()
        context['following'] = following
        return context

@method_decorator(login_required, name='dispatch')
class ProfileUpdateView(UpdateView):
    model = UserProfile
    template_name = "profile/profile_update.html"
    context_object_name = "profile"
    fields = ['profile_picture', 'bio', 'birth_date']

    def dispatch(self, request, *args, **kwargs):
        user_profile = self.get_object()
        if user_profile.user != self.request.user:
            return HttpResponseRedirect(reverse('home'))
        return super().dispatch(request, *args, **kwargs)
    
    def form_valid(self, form):
        messages.add_message(self.request, messages.SUCCESS, "Perfil editado correctamente.")
        return super(ProfileUpdateView, self).form_valid(form)
    
    def get_success_url(self):
        return reverse('profile:detail', args=[self.object.pk])

class ProfileListView(ListView):
    model = UserProfile
    template_name = "profile/profile_list.html"
    context_object_name = "profiles"

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return UserProfile.objects.all().order_by('user__username').exclude(user=self.request.user)
        return UserProfile.objects.all().order_by('user__username')
