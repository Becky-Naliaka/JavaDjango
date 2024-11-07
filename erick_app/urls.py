from django.urls import path

from erick_app import views

urlpatterns = [
    path('',views.home,name='my_home'),

    path('about/',views.about,name='my_about'),

    path('blog/',views.blog,name='my_blog'),

    path('contact/',views.contact,name='my_contact'),

    path('services/',views.services,name='my_services'),

    path('portfolio/',views.portfolio,name='my_portfolio'),

    path('testimonies/',views.testimonies,name='my_testimonies')
]