from .models.movie import Movie
from .models.actor import Actor
from rest_framework import status
from rest_framework import filters
from .models.comment import Comment
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.pagination import LimitOffsetPagination
# from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import TokenAuthentication
from .serializers import ActorSerializer, MovieSerializer, CommentSerializer

class ActorViewSet(ReadOnlyModelViewSet):
    serializer_class = ActorSerializer
    queryset = Actor.objects.all()

class MovieViewSet(ReadOnlyModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    pagination_class = LimitOffsetPagination
    # filter_backends = [filters.SearchFilter]
    # # filter_backends = [DjangoFilterBackend]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    ordering_fields = ["-imdb"]
    search_fields = ["name", "actor__name"]

    @action(detail=True, methods=['GET'])
    def actor(self, request, *args, **kwargs):
        movie = self.get_object()
        seriarizer = ActorSerializer(movie.actor.all(), many=True)
        return Response(seriarizer.data)

    @action(detail=True, methods=['POST'])
    def watch(self, request, *args, **kwargs):
        movie = self.get_object()
        movie.watched += 1
        movie.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=True, methods=['POST'])
    def add_actor(self, request, *args, **kwargs):
        movie = self.get_object()
        actor_id = request.data['id']
        actor = Actor.objects.get(id=actor_id)
        movie.actor.add(actor)
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=True, methods=['POST'])
    def remove_actor(self, request, *args, **kwargs):
        movie = self.get_object()
        actor_id = request.data["id"]
        actor = Actor.objects.get(id=actor_id)
        movie.actor.remove(actor)
        movie.save()
        return Response(status=status.HTTP_200_OK)

class MovieActorAPIView(APIView):

    @staticmethod
    def get(request, id, *args, **kwargs):
        movie = Movie.objects.get(id=id)
        seriarizer = ActorSerializer(movie.actor.all(), many=True)
        return Response(seriarizer.data)

class CommentAdd(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    @staticmethod
    def post(request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CommentListAPIView(ListAPIView):
    serializer_class = CommentSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return Comment.objects.filter(user=self.request.user)

class CommentDeleteAPIView(APIView):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication, ]

    @staticmethod
    def delete(request, pk):
        comment = Comment.objects.get(pk=pk)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# """
#     ModelViewSet uchun
# """

# class AddComment(ModelViewSet):
#     serializer_class = CommentSerializer
#     authentication_classes = (TokenAuthentication,)
#     permission_classes = (IsAuthenticated,)
#     queryset = Comment.objects.all()
#
#     # def get_queryset(self):
#     #     return Comment.objects.filter(user=self.request.user)
#
#     def perform_create(self, serializer):
#         serializer.validated_data["user"] = self.request.user
#         serializer.save()