from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import FileUploaderSerializer, OrderSerializer
from .excelReader import handleExcelUpload
from django.conf import settings
from .models import Order
from .rate_limiter import rate_limit

# Create your views here.
class ExcelUploadAPI(APIView):
    def post(self, request):
        data = request.data
        serializer = FileUploaderSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            file_path = serializer.data['file']
            handleExcelUpload(f"{settings.BASE_DIR}/{file_path}")
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
    @rate_limit(max_request=5, time_window=60)
    def get(self, request):
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response({
            "status": True,
            "message": "orders",
            "data": serializer.data
        })
