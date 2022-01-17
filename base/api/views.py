from django.core.checks import messages
from rest_framework.decorators import api_view
from rest_framework import viewsets,status
from rest_framework.response import Response
from app.models import Members
from .serializers import MemberSerializer

@api_view(['GET','POST'])
def getMembers(request):
    if request.method == 'GET':
        members = Members.objects.all()
        serializer = MemberSerializer(members,many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = MemberSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

@api_view(['GET','PUT','DELETE','PATCH'])
def getMember(request,id):
    try:
        member = Members.objects.get(id=id)
        if request.method == 'GET':
            serializer = MemberSerializer(member)
            return Response(serializer.data)
        if request.method == 'PUT':
            member = Members.objects.get(id=id)
            serializer = MemberSerializer(instance=member,data=request.data)
            print(serializer.is_valid())
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data)
        if request.method == 'PATCH':
            member = Members.objects.get(id=id)
            data = request.data
            member.name = data.get("name",member.name)
            member.email = data.get("email",member.email)
            member.level = data.get("level",member.level)
            member.save()
            serializer = MemberSerializer(member)
            return Response(serializer.data)
        if request.method == 'DELETE':
            member = Members.objects.get(id=id)
            member.delete()
            return Response('Deleted')
    except:
        message = "Resource does not exists"
        return Response(data=message, status=status.HTTP_404_NOT_FOUND)


