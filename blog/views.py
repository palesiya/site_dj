from django.views.generic import ListView
from blog.models import Post


class BlogView(ListView):
    paginate_by = 3
    model = Post
    template_name = 'blog.html'
