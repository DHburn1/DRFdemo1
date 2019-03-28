from django.views import View
from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from stuapp.models import Actor, Movie
from rest_framework.viewsets import ModelViewSet

from stuapp.serializers import ActorSerializer,MovieSerializer


# class ActorListView(APIView):
#     """
#     查询所有演员信息、增加演员信息、修改、删除操作
#     """
#     def get(self,request):
#         actors = Actor.objects.all()
#
#         ac = ActorSerializer(instance=actors,many=True)
#         return Response(data=ac.data)

class ActorListView(ListAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

class ActorDetailView(GenericAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

    def get(self,request,pk):
        actor = self.get_object()
        ac = self.get_serializer(instance=actor)
        return Response(data=ac.data)

class MovieListView(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


