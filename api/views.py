from django.http import JsonResponse
from rest_framework.decorators import api_view , permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import ProjectSerializer
from projects.models import Project ,Review ,Tag


@api_view(['GET'])    
def getRoutes(request):
    routes = [
        {'method': 'GET', 'path': '/api/projects'},
        {'method': 'GET', 'path': '/api/projects/id'},
        {'method': 'GET', 'path': '/api/projects/id/vote'},
        {'method': 'POST', 'path': '/api/users/token'},
        {'method': 'POST', 'path': '/api/users/token/refresh'},
    ]
    return Response(routes)

@api_view(['GET'])
def getProjects(request):
    
    projects = Project.objects.all()
    serializer = ProjectSerializer(projects , many=True)
    return Response(serializer.data)    

@api_view(['GET'])
def getProject(request , pk):
    
    projects = Project.objects.get(id=pk)
    serializer = ProjectSerializer(projects , many=False)
    return Response(serializer.data)    

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def ProjectVote(request,pk):
    project = Project.objects.get(id=pk)
    user = request.user.profile
    data = request.data
    
    review , created = Review.objects.get_or_create(
        owner = user,
        project = project,
        
    )
    review.value = data['value']
    review.save()
    project.getVoteCount
    
    serializer = ProjectSerializer(project,many=False)
    return Response(serializer.data)

@api_view(['DELETE'])
def removeTag(request):
    tagId = request.data['tag']
    projectId = request.data['project']

    project = Project.objects.get(id=projectId)
    tag = Tag.objects.get(id=tagId)

    project.tags.remove(tag)

    return Response('Tag was deleted!')