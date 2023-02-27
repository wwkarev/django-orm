from django.urls import path

from library.views import AuthorApiView
from rest_framework.routers import SimpleRouter

from library.viewsets import AuthorModelView

urlpatterns = [
    path('author/', AuthorApiView.as_view()),
    path('author/<int:pk>/', AuthorApiView.as_view()),
]

router = SimpleRouter()
router.register("author_modelviewset", AuthorModelView)

urlpatterns += router.urls