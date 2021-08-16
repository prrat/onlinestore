from django.shortcuts import render, get_object_or_404
from .models import Post
from django.views import generic
from .models import Post
from .forms import CommentForm

# Create your views here.

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 3

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

    def post_detail(request, slug):

        template_name = 'post_detail.html'
        post = get_object_or_404(Post, slug=slug)
        comments = post.comments.filter(active=True)
        new_comment = None
        # Comment posted
        if request.method == 'POST':
            comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
        else:
            comment_form = CommentForm()

        return render(request, template_name, {'post': post,
                                            'comments': comments,
                                           'new_comment': new_comment,'comment_form': comment_form})
def currency(request):
      template = 'currency.html'
      return render(request, template)

# def base(request):
#       template1 = 'base.html'
#       return render(request, template1)


# def post_detail(request):
#       template2 = 'post_detail.html'
#       return render(request, template2)

# def sidebar(request):
#       template3 = 'sidebar.html'
#       return render(request, template3)