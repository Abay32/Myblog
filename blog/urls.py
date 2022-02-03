#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from django.urls import path
from . import views

app_name = 'blog' 

urlpatterns = [
        path('', views.home, name = 'home'),
        path('articles/', views.articles, name = 'articles'),
        #path('article/', views.articles, name = 'article'),

        path('<slug:article>/', views.article, name='article'),        
        ]