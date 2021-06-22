from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Hall


def home(req):
    return render(req, 'halls/home.html')


def dashboard(req):
    return home(req)


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('home')
    
    def form_valid(self, form):
        view = super().form_valid(form)
        data = form.cleaned_data
        user = authenticate(username=data['username'], password=data['password1'])
        login(self.request, user)
        return view


class CreateHall(LoginRequiredMixin, generic.CreateView):
    login_url = reverse_lazy('login')
    model = Hall
    fields = ('title',)
    template_name = 'halls/hall_update.html'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        form.instance.user = self.request.user
        super().form_valid(form)
        return redirect('home')


class DetailHall(generic.DetailView):
    model = Hall
    template = 'halls/hall_detail.html'


class UpdateHall(generic.UpdateView):
    model = Hall
    fields = ('title',)
    template_name = 'halls/hall_update.html'
    extra_context = { 'edit': True }
    success_url = reverse_lazy('dashboard')


class DeleteHall(generic.DeleteView):
    # this can render a template if called with get and also if post-ed removes the obj
    model = Hall
    template_name = 'halls/hall_update.html'
    extra_context = { 'delete': True }
    success_url = reverse_lazy('dashboard')







