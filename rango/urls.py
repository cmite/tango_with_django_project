#!/usr/bin/python
# coding=utf-8

# Base Python File (urls.py)
# Created: jeu. 18 août 2016 16:46:48 CEST
# Version: 1.0
#
# This Python script was developped by François-Xavier Thomas.
# You are free to copy, adapt or modify it.
# If you do so, however, leave my name somewhere in the credits, I'd appreciate it ;)
#
# (ɔ) François-Xavier Thomas <fx.thomas@gmail.com>


from django.conf.urls import url
from rango import views


urlpatterns = [url(r'^$', views.index, name='index'),
               url(r'^about/$', views.about, name='about'),
               url(r'^add_category/$', views.add_category, name='add_category'),
               url(r'^add_page/$', views.add_page, name='add_page'),
               url(r'^category/(?P<category_name_slug>[\w\-]+)/$',
                   views.category, name='category')]
