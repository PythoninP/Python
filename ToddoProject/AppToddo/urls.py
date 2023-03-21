from. import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    # path('details/', views.details, name='detail'),
    path('delete/<int:taskid>/', views.delete, name='dlt'),
    path('update/<int:id>/', views.update, name="update"),
    path('cv/', views.Tasklistview.as_view(), name="view"),
    path('cvd/<int:pk>/', views.TaskDetailView.as_view(), name="detail"),
    path('cvu/<int:pk>/', views.TaskUpdateView.as_view(), name='updatev'),
    path('cvdlt/<int:pk>/', views.TaskDeleteView.as_view(), name="dlt")
]