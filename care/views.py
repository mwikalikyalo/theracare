from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from .models import Client, Therapist
from .serializers import ClientSerializer,TherapistSerializer

from django.core.files.storage import default_storage

# Create your views here.
@csrf_exempt
def clientApi(request,id=0):
    if request.method=='GET':
        clients = Client.objects.all()
        client_serializer = ClientSerializer(clients, many=True)
        return JsonResponse(client_serializer.data, safe=False)

    elif request.method=='POST':
        client_data=JSONParser().parse(request)
        client_serializer = ClientSerializer(data=client_data)
        if client_serializer.is_valid():
            client_serializer.save()
            return JsonResponse("Added Successfully!!" , safe=False)
        return JsonResponse("Failed to Add.",safe=False)
    
    elif request.method=='PUT':
        client_data = JSONParser().parse(request)
        clients=Client.objects.get(ClientId=client_data['ClientId'])
        client_serializer=ClientSerializer(clients,data=client_data)
        if client_serializer.is_valid():
            client_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)

    elif request.method=='DELETE':
        clients=Client.objects.get(ClientId=id)
        clients.delete()
        return JsonResponse("Deleted Succeffully!!", safe=False)

@csrf_exempt
def therapistApi(request,id=0):
    if request.method=='GET':
        therapists = Therapist.objects.all()
        therapist_serializer = TherapistSerializer(therapists, many=True)
        return JsonResponse(therapist_serializer.data, safe=False)

    elif request.method=='POST':
        therapist_data=JSONParser().parse(request)
        therapist_serializer = TherapistSerializer(data=therapist_data)
        if therapist_serializer.is_valid():
            therapist_serializer.save()
            return JsonResponse("Added Successfully!!" , safe=False)
        return JsonResponse("Failed to Add.",safe=False)
    
    elif request.method=='PUT':
        therapist_data = JSONParser().parse(request)
        therapists=Therapist.objects.get(TherapistId=therapist_data['TherapistId'])
        therapist_serializer=TherapistSerializer(therapist,data=therapist_data)
        if therapist_serializer.is_valid():
            therapist_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)

    elif request.method=='DELETE':
        therapist=Therapist.objects.get(TherapistId=id)
        therapist.delete()
        return JsonResponse("Deleted Succeffully!!", safe=False)


@csrf_exempt
def SaveFile(request):
    file=request.FILES['uploadedFile']
    file_name = default_storage.save(file.name,file)

    return JsonResponse(file_name,safe=False)