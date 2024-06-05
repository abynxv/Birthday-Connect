from . models import FriendsModel
from . serilaizers import FriendsSerializer
from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

class FriendView(APIView):
    def post(self, request):
        serializer = FriendsSerializer(data=request.data)
        if serializer.is_valid():
            friend = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def get(self, request, *args, **kwargs):
        friends = FriendsModel.objects.all()
        serializer = FriendsSerializer(friends, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class FriendDetailView(APIView):
    def  get(self, request, pk):
        friend = get_object_or_404(FriendsModel, pk=pk)
        serializer = FriendsSerializer(friend)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        friend = get_object_or_404(FriendsModel, pk=pk)
        serializer = FriendsSerializer(friend, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request,pk):
        friend = get_object_or_404(FriendsModel, pk=pk)
        friend.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

    