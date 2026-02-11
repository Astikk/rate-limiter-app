from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import FileUploaderSerializer, OrderSerializer
from .excelReader import handleExcelUpload
from django.conf import settings
from .models import Order, FileUploader
from .rate_limiter import rate_limit
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .permission_checker import check_permission

# Create your views here.
class loginAPI(APIView):
    def post(self, request):
        data = request.data
        username = data.get('username')
        password = data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({
                "status": True,
                "message": "token created",
                "data": str(token)
            })
        return Response({
            "status": False,
            "message": "In valid",
            "data": {}
        })



class ExcelUploadAPI(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    @check_permission("POST", FileUploader)
    def post(self, request):
        data = request.data
        serializer = FileUploaderSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            file_path = serializer.data['file']
            # handleExcelUpload(f"{settings.BASE_DIR}/{file_path}")
            return Response({
                "status":True,
                "message": "File uploaded"
            })
        return Response({
            "status": False,
            "message": "File not uploaded",
            "data": serializer.errors
        })

class OrderAPI(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    @check_permission('GET', Order)
    @rate_limit(max_request=5, time_window=60)
    def get(self, request):
        orders = Order.objects.all()[:10]
        serializer = OrderSerializer(orders, many=True)
        return Response({
            "status": True,
            "message": "orders",
            "data": serializer.data
        })
