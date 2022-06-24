from rest_framework import routers

from posts.views import PostViewSet

router = routers.SimpleRouter()
router.register('', PostViewSet)

urlpatterns = router.urls
