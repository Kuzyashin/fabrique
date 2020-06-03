import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'json', views.JsonPayloadViewSet, base_name='json-payload')
router.register(r'xml', views.XmlPayloadViewSet, base_name='xml-payload')

urlpatterns = router.urls
