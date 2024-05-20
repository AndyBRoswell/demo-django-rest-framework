from django.urls import include, path
from rest_framework import routers

from _tutorial.quickstart import views  # add the project root to PYTHONPATH to make this symlink work. this is to disambiguate the import statement.

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing. Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),  # intercepted by built-in auth mechanism
    # path('', include('snippets.urls')),
    path('api-auth/', include('rest_framework.urls'))
]
