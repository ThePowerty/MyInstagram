from django.views.generic.edit import CreateView
from posts.models import Post
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.detail import DetailView
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required
from .forms import CommentCreateForm
from .forms import PostCreateForm

from django.http import JsonResponse

@method_decorator(login_required, name='dispatch')
class PostCreateView(CreateView):
    template_name = "posts/post_create.html"
    model = Post
    form_class = PostCreateForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.add_message(self.request, messages.SUCCESS, "Publicación creada correctamente.")
        return super(PostCreateView, self).form_valid(form)
    
class PostDetailView(DetailView, CreateView):
    template_name = "posts/post_detail.html"
    model = Post
    context_object_name = 'post'
    form_class = CommentCreateForm

    def form_valid(self, form):
      form.instance.user = self.request.user
      form.instance.post = self.get_object()
      return super(PostDetailView, self).form_valid(form)

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Comentario añadido correctamente.")
        return reverse('post_detail', args=[self.get_object().pk])


@login_required
def like_post_ajax(request, pk):
    post = Post.objects.get(pk=pk)
    if request.user in post.likes.all():
        request.user.profile.unlike_post(post)
        return JsonResponse(
          {
              'message': 'Ya no te gusta esta publicación.',
              'liked': False,
              'nlikes': post.likes.all().count()
            }
        )
    else:
        # post.like(request.user)
        request.user.profile.like_post(post)
        return JsonResponse(
          {
              'message': 'Te gusta esta publicación.',
              'liked': True,
              'nlikes': post.likes.all().count()
            }
        )