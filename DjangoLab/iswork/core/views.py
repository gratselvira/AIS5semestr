from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, DetailView,CreateView, UpdateView,DeleteView
from django.views.generic.edit import FormMixin
from .models import Advantage, Like
from .forms import AdvantageForm, AuthUserForm, RegisterUserForm, CommentForm
from django.urls import reverse, reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect

# файл содержит функции, которые обрабатывают HTTP-запросы и возвращают HTTP-ответы.
# Функции в этом файле часто взаимодействуют с моделями данных.
class CustomSuccessMessageMixin:
    @property
    def success_msg(self):
        return False
        
    def form_valid(self,form):
        messages.success(self.request, self.success_msg)
        return super().form_valid(form)
    def get_success_url(self):
        return '%s?id=%s' % (self.success_url, self.object.id)

class HomeListView(ListView):
    model = Advantage
    template_name = 'index.html'
    context_object_name = 'list_articles'

    def get_queryset(self):
        queryset = super().get_queryset()
        filter_type = self.request.GET.get('filter')

        if filter_type == 'date':
            queryset = queryset.order_by('-create_date')  # Сортировка по дате создания
        elif filter_type == 'title':
            queryset = queryset.order_by('name')  # Сортировка по заголовку
        else:
            queryset = queryset.order_by('-create_date')  # По умолчанию сортировка по дате создания

        return queryset
    


class LikeView(View):
    def post(self, request, pk):
        article = Advantage.objects.get(pk=pk)
        like, created = Like.objects.get_or_create(user=request.user, article=article)
        if created:
            messages.success(request, 'Вы понравились статью!')
        else:
            messages.info(request, 'Вы уже понравились этой статье.')
        return redirect('detail_page', pk=article.pk)


class HomeDetailView(CustomSuccessMessageMixin, FormMixin, DetailView):
    model = Advantage
    template_name = 'detail.html'
    context_object_name = 'get_article'
    form_class = CommentForm
    success_msg = 'Комментарий создан!'

    def get_success_url(self, **kwargs):
        return reverse_lazy('detail_page', kwargs={'pk':self.get_object().id})

    def post(self,request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
        
    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.article = self.get_object()
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)

class ArticleCreateView(LoginRequiredMixin, CustomSuccessMessageMixin, CreateView):
    login_url = reverse_lazy('login_page')
    model = Advantage
    template_name = 'edit_page.html'
    form_class = AdvantageForm
    success_url = reverse_lazy('edit_page')
    success_msg = 'Запись создана'
    def get_context_data(self,**kwargs):
        kwargs['list_articles'] = Advantage.objects.all().order_by('-id')
        return super().get_context_data(**kwargs)
    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)

class ArticleUpdateView(LoginRequiredMixin, CustomSuccessMessageMixin,UpdateView):
    model = Advantage
    template_name = 'edit_page.html'
    form_class = AdvantageForm
    success_url = reverse_lazy('edit_page')
    success_msg = 'Запись успешно обновлена'
    def get_context_data(self,**kwargs):
        kwargs['update'] = True
        return super().get_context_data(**kwargs)
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if self.request.user != kwargs['instance'].author:
            return self.handle_no_permission()
        return kwargs

def delete_page(request, pk):
     get_article = Advantage.objects.get(pk=pk)
     get_article.delete()
     return redirect(reverse('edit_page'))

class MyprojectLoginView(LoginView):
    template_name = 'login.html'
    form_class = AuthUserForm
    success_url = reverse_lazy('edit_page')
    def get_success_url(self):
        return self.success_url

class RegisterUserView(CreateView):
    model = User
    template_name = 'register_page.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('edit_page')
    success_msg = 'Пользователь успешно создан'
    def form_valid(self,form):
        form_valid = super().form_valid(form)
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]
        aut_user = authenticate(username=username,password=password)
        login(self.request, aut_user)
        return form_valid
    

class MyProjectLogout(LogoutView):
    next_page = reverse_lazy('edit_page')
