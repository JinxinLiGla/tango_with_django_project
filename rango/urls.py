from django.urls import path
from rango import views

app_name = 'rango'

urlpatterns = [
    path(r'',views.index,name='index'),
    path(r'rango/about/', views.about, name='about'),
    path(r'rango/', views.index, name='index'),
    # path(r'rango/category/(?P<category_name_slug>[\w\-]+)/$', views.show_category, name='show_category'),
    path(r'rango/category/<slug:category_name_slug>/',views.show_category, name='show_category'),
]
