from django.shortcuts import render
from django.http import JsonResponse
from .models import HealthProgram, Client, Enrollment
from .Serializers import HealthProgramSerializer, ClientSerializer, EnrollmentSerializer,EnrollmentCreateSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404

from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from django.views.decorators.csrf import csrf_exempt
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login
from rest_framework import filters
class HealthProgramViewSet(viewsets.ModelViewSet):
    queryset = HealthProgram.objects.all()
    serializer_class = HealthProgramSerializer
    permission_classes = [AllowAny]
    
class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    # Custom search action
    @action(detail=False, methods=['get'], url_path='search')
    def search_clients(self, request):
        search_query = request.query_params.get('search', '')
        if search_query:
            clients = Client.objects.filter(
                Q(first_name__icontains=search_query) |
                Q(last_name__icontains=search_query) |
                Q(contact_number__icontains=search_query) |
                Q(email__icontains=search_query)
            )
        else:
            clients = Client.objects.all()

        serializer = self.get_serializer(clients, many=True)
        return Response(serializer.data) 
    
class EnrollmentViewSet(viewsets.ModelViewSet):
    queryset = Enrollment.objects.all()
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return EnrollmentCreateSerializer
        return EnrollmentSerializer
     
User = get_user_model()

@api_view(["POST"])
@permission_classes([AllowAny])
def register_user(request):
    username = request.data.get("username")
    password = request.data.get("password")
    first_name = request.data.get("first_name", "")
    last_name = request.data.get("last_name", "")
    email = request.data.get("email", "").lower()   

    if not all([username, password, first_name, last_name, email]):
        return Response({"error": "All fields are required"}, status=status.HTTP_400_BAD_REQUEST)
    try:
        validate_email(email)
    except ValidationError:
        return Response({"error": "Invalid email format"}, status=status.HTTP_400_BAD_REQUEST)

    if User.objects.filter(username__iexact=username).exists():
        return Response({"error": "Username already taken"}, status=status.HTTP_400_BAD_REQUEST)

    if User.objects.filter(email__iexact=email).exists():
        return Response({"error": "Email already in use"}, status=status.HTTP_400_BAD_REQUEST)

    user = User.objects.create_user(
        username=username,
        password=password,
        first_name=first_name,
        last_name=last_name,
        email=email,
    )
    return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
  
@api_view(['POST'])
@permission_classes([AllowAny])
def login_user(request):
    username = request.data.get('username')
    password = request.data.get('password')

    if not username or not password:
        return Response({'error': 'Username and password required'}, status=status.HTTP_400_BAD_REQUEST)

    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)   
        return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['GET'])
@permission_classes([AllowAny])
def client_profile(request, client_id):
    try:
        client = Client.objects.get(pk=client_id)
    except Client.DoesNotExist:
        return Response({'error': 'Client not found'}, status=status.HTTP_404_NOT_FOUND)
    
    client_serializer = ClientSerializer(client)
    
    enrollments = Enrollment.objects.filter(client=client)
    programs = [enrollment.program for enrollment in enrollments]
    programs_serializer = HealthProgramSerializer(programs, many=True)
    
    return Response({
        'client': client_serializer.data,
        'programs_enrolled': programs_serializer.data
    }, status=status.HTTP_200_OK)
class ClientSearchView(generics.ListAPIView):
    serializer_class = ClientSerializer
    pagination_class = PageNumberPagination
    
    def get_queryset(self):
        queryset = Client.objects.all()
        search_query = self.request.query_params.get('search', None)
        
        if search_query:
            queryset = queryset.filter(
                Q(first_name__icontains=search_query) |
                Q(last_name__icontains=search_query) |
                Q(contact_number__icontains=search_query) |
                Q(email__icontains=search_query) |
                Q(address__icontains=search_query)
            )
        return queryset 
    
@api_view(['POST'])
def enroll_client(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    program_id = request.data.get('program_id')

    if not program_id:
        return Response({'error': 'Program ID is required.'}, status=status.HTTP_400_BAD_REQUEST)
    
    program = get_object_or_404(HealthProgram, pk=program_id)
    enrollment = Enrollment.objects.create(client=client, program=program)
    
    return Response({
        'message': f'{client} successfully enrolled in {program}.',
        'enrollment_id': enrollment.id
    }, status=status.HTTP_201_CREATED) 