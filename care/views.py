from cProfile import Profile
from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from .models import Client, Therapist, Profile
from .serializers import ClientSerializer,TherapistSerializer
from django.core.files.storage import default_storage
from .forms import ClientForm,ProfileForm,TherapistForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    clients = Client.objects.all()
    therapist = Therapist.objects.all()
    profile = Profile.objects.all()
    return render(request, 'home.html', {'clients':clients, 'therapist':therapist, 'profile':profile})


@login_required(login_url='/accounts/login/')
def create_profile(request):
    current_user = request.user
    
    if request.method=='POST':
        form = ProfileForm(request.POST,request.FILES)
        if request.current_user.is_authenticated:
            form.instance.user = request.user
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user

            profile.save()
        return redirect('home')
    else:
        form=ProfileForm()

    return render(request,'create_profile.html',{"form":form})

@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    profile =Profile.objects.get(user=current_user)

    return render(request,'profile.html',{"profile":profile})




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