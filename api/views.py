from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PaintingSerializer
from paintings.models import Painting, Review, Tag

@api_view(["GET"])
def getRoutes(request):
    routes = [
        {"GET": "/api/paintings"},
        {"GET": "/api/paintings/id"},
        {"POST": "/api/paintings/id/vote"},
        {"POST": "/api/users/token"},
        {"POST": "/api/users/token/refresh"},
    ]

    return Response(routes)

@api_view(["GET"])
def getPaintings(request):
    paintings = Painting.objects.all()
    serializer = PaintingSerializer(paintings, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def getPainting(request, pk):
    painting = Painting.objects.get(id=pk)
    serializer = PaintingSerializer(painting, many=False)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def paintingVote(request, pk):
    painting = Painting.objects.get(id=pk)
    user = request.user.profile
    data = request.data

    review, created = Review.objects.get_or_create(
        owner = user,
        painting = painting,
    )

    review.value = data['value']
    review.save()
    painting.getVoteScore()
    serializer = PaintingSerializer(painting, many=False)
    return Response(serializer.data)

@api_view(['DELETE'])
# @permission_classes([IsAuthenticated])
def removeTag(request):
    tagID = request.data['tag']
    paintingID = request.data['painting']

    painting = Painting.objects.get(id = paintingID)
    tag = Tag.objects.get(id = tagID)
    painting.tags.remove(tag)
    
    return Response("Tag was deleted.")