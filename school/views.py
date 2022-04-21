from django.shortcuts import render
from django.views.generic import (TemplateView, DetailView,
                                    ListView, CreateView,
                                    UpdateView, DeleteView, FormView,)
from .models import Category, Post, Comment, Reply

from django.urls import reverse_lazy
from .forms import CommentForm, ReplyForm, PostForm
from django.http import HttpResponseRedirect
from taggit.models import Tag
from django.contrib.auth.models import User
from users.models import Account

class TagMixin(object):
    def get_context_data(self, **kwargs):
        context = super(TagMixin, self).get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        return context


def search_results(request):
    posts = Post.objects.order_by('-created_at')
    categories = Category.objects.all()

    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            posts = posts.filter(description__icontains=keyword)

    data = {
        'posts': posts,
        'categories': categories,
    }
    return render(request, 'blog/search_results.html', data)


class CategoryListView(ListView):
    context_object_name = 'categories'
    model = Category
    template_name = 'blog/category_list_view.html'
    

class PostListView(TagMixin, DetailView):
    context_object_name = 'categories'
    model = Category
    template_name = 'blog/post_list_view.html'
    order_by = ['-created_at']


class TagIndexView(TagMixin, DetailView):
    model = Post
    template_name = 'blog/post_list_view.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(tags__slug=self.kwargs.get('tag_slug'))


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
        
class PostDetailView(DetailView,  FormView):
    context_object_name = 'posts'
    extra_context = {
        'categories': Category.objects.all()
    }
    model = Post
  
    template_name = 'blog/post_detail_view.html'
    form_class = CommentForm
    second_form_class = ReplyForm

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(request=self.request)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(request=self.request)
        # context['comments'] = Comment.objects.filter(id=self.object.id)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        if 'form' in request.POST:
            form_class = self.get_form_class()
            form_name = 'form'
        else:
            form_class = self.second_form_class
            form_name = 'form2'

        form = self.get_form(form_class)
        # print("the form name is : ", form)
        # print("form name: ", form_name)
        # print("form_class:",form_class)

        if form_name =='form' and form.is_valid():
            print("comment form is returned")
            return self.form_valid(form)
        elif form_name=='form2' and form.is_valid():
            print("reply form is returned")
            return self.form2_valid(form)
    
    def get_success_url(self):
            self.object = self.get_object()
            category = self.object.category
            name = self.object.name
            return reverse_lazy('school:post_detail', kwargs={'category':category.slug,
                                                                'name':name,
                                                                'slug':self.object.slug})

    def form_valid(self, form):
        self.object = self.get_object()
        fm = form.save(commit=False)
        fm.user = self.request.user
        fm.post_name = self.object.comments.name
        fm.post_name_id = self.object.id
        fm.save()
        return HttpResponseRedirect(self.get_success_url())

    def form2_valid(self, form):  
        self.object = self.get_object()
        fm = form.save(commit=False)
        fm.user = self.request.user
        fm.comment_name_id = self.request.POST.get('comment.id')
        fm.save()
        return HttpResponseRedirect(self.get_success_url())


    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)



class PostCreateView(CreateView):
    # fields = ('lesson_id','name','position','image','video','ppt','Notes')
    form_class = PostForm
    context_object_name = 'post'
    model = Post
    template_name = 'blog/post_create.html'

    def get_success_url(self):
        self.get_object()
        category = self.object.category
        return reverse_lazy('school:post_list', kwargs={'category':category.slug,
                                                        'slug':self.object.slug})

    def form_valid(self, form, *args, **kwargs):
        self.object = self.get_object()
        fm = form.save(commit=False)
        fm.created_by = self.request.user
        fm.Category = self.object.category
        fm.post = self.object
        fm.save()
        return HttpResponseRedirect(self.get_success_url())

class PostUpdateView(UpdateView):
    fields = ('name', 'position', 'video', 'filelink', 'ppt', 'Notes')
    model = Post
    template_name = 'blog/post_update.html'
    context_object_name = 'posts'


class PostDeleteView(DeleteView):
    model = Post
    context_object_name = 'posts'
    template_name = 'blog/post_delete.html'

    def get_success_url(self):
        print(self.object)
        category = self.get_object.Category
        post = self.object.post
        return reverse_lazy('school:post_list', kwargs={'category':category.slug, 'slug':post})










