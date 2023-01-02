from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name="api-verview"),
    path('book-list', views.ShowAll, name="list"), # List all the books in the database
    path('book-detail/<int:id>', views.ShowOne, name="list-one"), # List one book in the database having the id
    path('book-create', views.Create, name="create"), # Create a new book in the database
    path('book-update/<int:pk>', views.Update, name="update"), # Update a book in the database having the id
    path('book-delete/<int:pk>', views.Delete, name="delete"), # Delete a book in the database having the id
    path('recommend-book-title/<str:genre>/<str:title>', views.recommend_by_title, name="recommend-by-title"), # Recommend a book by title
    path('recommend-book-desc/<str:genre>/<str:title>', views.recommend_by_desc, name="recommend-by-desc"), # Recommend a book by description
    path('top-rated/', views.top_rated, name="top-rated"), # List top rated books
    path('longest/', views.longest, name="longest"), # List books with longest description
]
