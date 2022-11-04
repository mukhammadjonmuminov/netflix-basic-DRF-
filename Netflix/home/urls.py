from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ActorViewSet, MovieViewSet, MovieActorAPIView, CommentAdd, CommentListAPIView, CommentDeleteAPIView
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register('actors', ActorViewSet)
router.register('movies', MovieViewSet)
# router.register('comment', AddComment, "comment")

urlpatterns = [
    path('', include(router.urls)),
    path('movies/<int:id>/actors', MovieActorAPIView.as_view()),
    path('auth/', obtain_auth_token),
    path('add_comment/', CommentAdd.as_view(), name="add-comment"),
    path('comments/', CommentListAPIView.as_view(), name="list-comments"),
    path('delete/', CommentDeleteAPIView.as_view(), name="delete-comment")
]
