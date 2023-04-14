from drf_yasg.utils import swagger_auto_schema

from rest_framework import permissions, serializers, status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from .services import UserService


class CreateUserView(APIView):
    permission_classes = [permissions.AllowAny,]

    class CreateUserInputSerializer(serializers.Serializer):
        username = serializers.CharField()
        email = serializers.EmailField()
        password = serializers.CharField()

    @swagger_auto_schema(request_body=CreateUserInputSerializer)
    def post(self, request: Request) -> Response:
        serializer = self.CreateUserInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # user = UserService.create_user(**serializer.validated_data)

        return Response(status=status.HTTP_201_CREATED, data={'success': True, 'message': 'User created successfully'})
