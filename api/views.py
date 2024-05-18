from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from api.serializers import GroupSerializer, GroupItemSerializer, ChapterSerializer, SubchapterSerializer
from api.models import *


@api_view(['GET'])
@permission_classes([AllowAny])
def index(request):
    serializer = GroupSerializer(Group.objects.all(), many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([AllowAny])
def groups(request):
    serializer = GroupSerializer(Group.objects.all(), many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([AllowAny])
def group(request, pk):
    serializer = GroupSerializer(Group.objects.get(pk=pk))
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([AllowAny])
def chapters(request, group_item):
    serializer = ChapterSerializer(Chapter.objects.filter(parent_id=group_item), many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([AllowAny])
def chapter(request, pk):
    if pk == 0 or pk == '0':
        serializer = None
        return Response(serializer)
    serializer = ChapterSerializer(Chapter.objects.get(pk=pk))
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([AllowAny])
def group_items(request, pk):
    serializer = GroupItemSerializer(GroupItem.objects.filter(group=pk), many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([AllowAny])
def group_item(request, pk):
    if pk == 0 or pk == '0':
        serializer = None
        return Response(serializer)
    serializer = GroupItemSerializer(GroupItem.objects.get(pk=pk))
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([AllowAny])
def subchapters(request, chapter):
    serializer = SubchapterSerializer(Subchapter.objects.filter(parent_id=chapter), many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([AllowAny])
def subchapter(request, pk):
    if pk == 0 or pk == '0':
        serializer = None
        return Response(serializer)
    serializer = SubchapterSerializer(Subchapter.objects.get(pk=pk))
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([AllowAny])
def search(request):
    q = str(request.data.get('q')).lower()

    if q:
        group_items = GroupItemSerializer(GroupItem.objects.filter(title__icontains=q), many=True)
        chapters = ChapterSerializer(Chapter.objects.filter(title__icontains=q), many=True)
        subchapter = SubchapterSerializer(Subchapter.objects.filter(title__icontains=q), many=True)
        serializer = group_items.data + chapters.data + subchapter.data
        return Response(serializer)
    return Response([])