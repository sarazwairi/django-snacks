from django.urls import path
# from django.urls.resolvers import URLResolver

from .views import HomePageView,AboutPageView

urlpatterns=[
    path('',HomePageView.as_view(),name='home'),
    path('about/',AboutPageView.as_view(),name='about'),

]