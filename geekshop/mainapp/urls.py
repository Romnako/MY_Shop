from django.urls import path
from .views import products, product
from django.views.decorators.cache import cache_page


app_name = 'mainapp'


urlpatterns = [
    path('', products, name='main'),
    path('category/<int:pk>', cache_page(3)(products), name='category'),
    path('product/<int:pk>', cache_page(3)(product), name='detail'),
    path('category/<int:pk>/page/<int:page>/', products, name='page'),
    # path('users/delete/<int:pk>/', user_delete, name='user_delete'),

]
