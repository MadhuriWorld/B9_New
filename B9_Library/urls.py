"""
URL configuration for B9_Library project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include


from app import views 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('book/home/', views.welcome_page, name= 'home_page'),
    path('book/show-books/', views.show_books, name= 'show_books'),
    path('book/show-single-book/<int:id>/', views.show_single_book, name= 'show_single_book'),                    # when we have to access single book need id to access  
    path('book/add-book/', views.add_single_book, name= 'add_single_book'),                                       # adding a single book  
    path('book/edit-book/<int:id>/', views.edit_single_book, name= 'edit_single_book'),                           # edit delete a single book  
    path('book/delete-book/<int:id>/', views.delete_single_book, name= 'delete_single_book'),                     # hard delete a single book  
    path('book/soft-delete-book/<int:id>/', views.soft_delete_single_book, name= 'soft_delete_single_book'),          
    path('book/form-view/', views.form_view, name= 'form_view'),

    
    # path('view-a/', views.view_a, name= 'view_a'),
    

    # app user urls
    path('user/', include('app_user.urls'))
]




# patterns/url patterns/urls/endpoints
# http://127.0.0.1:8000/admin/
# http://127.0.0.1:8000/home/
# http://127.0.0.1:8000/show-books/
# http://127.0.0.1:8000/show-single-book/1/
# http://127.0.0.1:8000/add-book/
# http://127.0.0.1:8000/edit-single-book/1/
# http://127.0.0.1:8000/delete-single-book/1/
# http://127.0.0.1:8000/soft-delete-single-book/1/
# http://127.0.0.1:8000/form-view/
