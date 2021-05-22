from .models import MyUUIDCreator
from .serializers import MyUUIDCreatorSerializer
import uuid
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

# Create your views here.


class MyUUIDCreatorView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        # create new MyUUIDCreator instance
        MyUUIDCreator.objects.create(generated_id=uuid.uuid4())
        # get all MyUUIDCreator instances
        uuids = MyUUIDCreator.objects.all()
        data_serializer = MyUUIDCreatorSerializer(uuids, many=True)
        good_api_status = status.HTTP_200_OK
        return Response(
            {
                "status": True,
                "message": "Successful",
                "data": data_serializer.data,
            },
            status=good_api_status,
        )
