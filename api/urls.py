from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name="api-verview"),
    path('book-list', views.ShowAll, name="list"),
    path('book-detail/<int:id>', views.ShowOne, name="list-one"),
    path('book-create', views.Create, name="create"),
    path('book-update/<int:pk>', views.Update, name="update"),
    path('book-delete/<int:pk>', views.Delete, name="delete"),
    path('recommend-book-title/<str:genre>/<str:title>', views.recommend_by_title, name="recommend-by-title"),
    path('recommend-book-desc/<str:genre>/<str:title>', views.recommend_by_desc, name="recommend-by-desc"),
    path('top-rated/', views.top_rated, name="top-rated"),
    path('longest/', views.longest, name="longest"),
]
