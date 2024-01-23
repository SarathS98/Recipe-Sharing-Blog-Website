from django.contrib import admin
from django.urls import path
from secapp import views
from secapp import views as user_view
from .views import ArticleDetailView, PostDeleteView, PostUpdateView


from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    
    path("homepage/", views.front_page, name='hmepg'),
    path("aboutpage/", views.about, name='abtpg'),
    path("login/", views.log_in, name='lgin'),
    path("joinpage/", user_view.join_pg, name='jnpg'),
    path("explore/", user_view.explore_pg, name='explr'),
    path("profile/", user_view.profile_pg, name='prfpg'),
    path("account/", user_view.account_pg, name='accnt'),
    path("article/<int:pk>", ArticleDetailView.as_view(), name='article-detail'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)