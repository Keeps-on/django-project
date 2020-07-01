from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    # ...
]

router = DefaultRouter()  # 可以处理视图的路由器
router.register('books', views.BookInfoViewSet)  # 向路由器中注册视图集
router.register('heros',views.HeroInfoViewSet)

urlpatterns += router.urls  # 将路由器中的所以路由信息追到到django的路由列表中