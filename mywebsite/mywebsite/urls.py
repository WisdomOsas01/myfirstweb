from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
from users import views as user_views
from django.conf import settings
from django.conf.urls.static import static
from .views import PostListView ,PostDetailView,PostCreateView , PostUpdateView , PostDeleteView , UserPostListView

urlpatterns = [path('time',views.current_datetime),
               path('admin/', admin.site.urls),
               path('plus({1,2})hours/',views.hours_ahead),
               path('',PostListView.as_view(),name='mywebsite-home'),
               path('user/<str:username>', UserPostListView.as_view(), name='user-post'),
               path('about',views.about,name='mywebsite-about'),
               path('music',views.music),
               path('register/', user_views.register, name='register'),
               path('login/', auth_views.LoginView.as_view(template_name='users/login.html'),name='login'),
               path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
               path('profile/', user_views.profile, name='profile'),
               path('post/<int:pk>',PostDetailView.as_view(), name='post-detail'),
               path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
               path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
               path('post/new/',PostCreateView.as_view(),name='post-create'),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)