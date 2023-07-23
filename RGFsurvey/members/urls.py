from django.urls import path

from . import views,admin
urlpatterns = [
    # path("admin/", admin.site.urls),
    path('details/',views.members),
    path('details/tree/<int:id>',views.detailes,name='viewDatiles'),
]
