from django.shortcuts import render
from .forms import PostForm
from .models import Post
# Create your views here.
def index(request):
    recent_posts_list =Post.objects.order_by('-created')[:10]
    form = PostForm()
    user = request.user
    context = {'recent_posts_list': recent_posts_list,'form': form}
    
    if request.method =="POST":
        form =PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
    else:
        form = PostForm()
    return render(request,'index.html', context)
