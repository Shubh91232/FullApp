from django.urls import path

from . import views,admin
urlpatterns = [
    # path("admin/", admin.site.urls),
    path('tree/<int:pk>/',views.TreeAPI.as_view()),
]
