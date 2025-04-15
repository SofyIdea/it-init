from django.urls import path
from . import views
from users import views as users
from feedback import views as feedback
from requisitions import views as requisitions

urlpatterns = [
    path('', views.list, name='main_page'),
    path('news/<int:id>', views.paper, name='paper'),
    path('register/', users.user_register, name='register'),
    path('login/', users.user_login, name='login'),
    path('logout/', users.user_logout, name='user_logout'),
    path('reviews/', feedback.reviews_view, name='reviews'),
    path('add_feedback/', feedback.add_feedback, name='add_feedback'),
    path('add_response/', feedback.add_response, name='add_response'),
    path('add_article/', views.add_article, name='add_article'),
    path('create_request/', requisitions.create_request, name='create_request'),
    path('profile/', users.user_profile, name='user_profile'),
    path('add_response_reply/', feedback.add_response_reply, name='add_response_reply'),
]