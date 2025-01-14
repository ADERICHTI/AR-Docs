from django.urls import path
from . import views

#docs: categories of document
#document: documents in each category

urlpatterns = [
    path('', views.home_page, name='home'),
    path('docs/<int:pk>/', views.documents_page, name='docs'),
    path('docs/document/<int:pk>/<int:pk2>/', views.document_page, name='document'),
    path('docs/document/<int:pk>/edit/', views.DocumentEditView.as_view(), name='document_edit'),
    path('docs/document/<int:pk>/delete/', views.DocumentDeleteView.as_view(), name='document_delete'),
    path('search_result/', views.search_result, name='search_result'),
    path('login/', views.log_in, name='login'),
    path('logout/', views.log_out, name='logout'),
]
