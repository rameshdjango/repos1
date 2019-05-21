from django.conf.urls import url
#from taskapp import views
from taskapp.views import ImdbViewSet
from . import views
app_name= "taskapp"

from rest_framework import routers

router = routers.SimpleRouter()
#router.register(r'users', UserViewSet)
#router.register(r'accounts', AccountViewSet)
urlpatterns = router.urls

urlpatterns = [
    url(r'^$',ImdbViewSet.as_view({'get':'list'})),
   # url('admin', views.ListAdmin.as_view()),
   # url('<int:pk>/', views.DetailAdmin.as_view()),

]

#urlpatterns += routers.urls
#urlpatterns += routers.
