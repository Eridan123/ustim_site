from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.views.generic import ListView

from .models import Post


class HomePageView(ListView):
    model = Post
    template_name = 'home.html'


class ViewFunctions:
    def home(request):
        template = loader.get_template('home.html')
        context = {
            "posts": Post.objects.all().order_by("created_on")
        }
        return HttpResponse(template.render(context, request))
    def about(request):
        template = loader.get_template('about.html')
        context = {
        }
        return HttpResponse(template.render(context, request))

    def partner(request):
        template = loader.get_template('partners.html')
        context = {
        }
        return HttpResponse(template.render(context, request))

    def staff(request):
        template = loader.get_template('staff.html')
        context = {
        }
        return HttpResponse(template.render(context, request))

    def news(request):
        template = loader.get_template('news.html')
        context = {
            "posts": Post.objects.all().order_by("created_on")
        }
        return HttpResponse(template.render(context, request))

    def services(request):
        template = loader.get_template('services.html')
        context = {
        }
        return HttpResponse(template.render(context, request))

    def contact(request):
        template = loader.get_template('contact.html')
        context = {
        }
        return HttpResponse(template.render(context, request))
