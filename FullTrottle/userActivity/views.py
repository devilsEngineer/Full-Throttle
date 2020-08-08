from rest_framework import status, exceptions
from rest_framework import viewsets
from rest_framework.response import Response

from .models import User, ActivityPeriod
from .serializers import UserSerializer, ActivityPeriodSerializer
class UserView(viewsets.ModelViewSet):

    def getAllUsers(self, request):
        user_details=User.objects.all()
        user_serializer = UserSerializer(user_details, many=True)
        response = {"user_details": user_serializer.data}
        return Response(response, status=status.HTTP_200_OK)

    def getUserDetail(self, request):
        if 'id' in request.query_params and request.query_params is not None:
            try:
                user_details=User.objects.get(user_id=request.query_params['id'])
            except User.DoesNotExist:
                return Response(
                    data={"error":"User does not exist"},
                    status=status.HTTP_400_BAD_REQUEST
                )
            user_serializer = UserSerializer(user_details)
            response = {"user_details": user_serializer.data}
            return Response(response, status=status.HTTP_200_OK)

        return Response(
            data={"error": "id is required"},
            status=status.HTTP_400_BAD_REQUEST
            )

    def createUser(self, request):
        data = request.data
        data['user_id'] = data['id']
        del data['id']
        try:
            user_details=User.objects.get(user_id=data['user_id'])
        except User.DoesNotExist:
            serializer = UserSerializer(data=data)
            if serializer.is_valid():
                data = serializer.data
                user = User(**data)
                user.save()
                return Response(data, status=status.HTTP_200_OK)
            error = serializer.errors
            return Response(error, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"error":"User with id already exists"}, status=status.HTTP_400_BAD_REQUEST)

class UserActivityView(viewsets.ModelViewSet):
    
    def getUserAcivity(self, request):
        if 'id' in request.query_params and request.query_params is not None:
            user_activity=ActivityPeriod.objects(user_id=request.query_params['id'])
            activity_serializer = ActivityPeriodSerializer(user_activity,many=True)
            response = []
            for activity in activity_serializer.data:
                activity_period={}
                for key,value in activity.items():
                    if key in ['start_time','end_time']:
                        activity_period[key] = value
                response.append(activity_period)
            return Response({"activity_periods":response}, status=status.HTTP_200_OK)

        return Response(
            data={"error": "id is required"},
            status=status.HTTP_400_BAD_REQUEST
            )


    def createUserActivity(self, request):
        data = request.data
        data['user_id'] = data['id']
        del data['id']
        serializer = ActivityPeriodSerializer(data=data)
        if serializer.is_valid():
            activity_period = ActivityPeriod(**data)
            activity_period.save()
            response = serializer.data
            return Response(response, status=status.HTTP_200_OK)
        error = serializer.errors
        return Response(error, status=status.HTTP_400_BAD_REQUEST)

class UserAndActivityView(viewsets.ModelViewSet):

    def getAllUserAndActivity(self, request):
        """
        API to serve data as that of given Json file.
        """
        user_details=User.objects.all()
        user_data = UserSerializer(user_details,many=True).data
        
        for user in user_data:
            user_activity=ActivityPeriod.objects(user_id=user['user_id'])
            activity_serializer = ActivityPeriodSerializer(user_activity,many=True)
            activity_periods = []
            for activity in activity_serializer.data:
                del activity['id']
                del activity['user_id']
                activity_periods.append(activity)
            user["activity_periods"] = activity_periods
            user['id'] = user['user_id']
            del user['user_id']
        return Response({"ok":True,"members":user_data}, status=status.HTTP_200_OK)

    def getUserAndActivity(self, request):
        if 'id' in request.query_params and request.query_params is not None:
            try:
                user_details=User.objects.get(user_id=request.query_params['id'])
            except User.DoesNotExist:
                return Response(
                    data={"error":"User does not exist"},
                    status=status.HTTP_400_BAD_REQUEST
                )
            user_data = UserSerializer(user_details).data
            del user_data['id']
            user_activity=ActivityPeriod.objects(user_id=request.query_params['id'])
            activity_serializer = ActivityPeriodSerializer(user_activity,many=True)
            activity_periods = []
            for activity in activity_serializer.data:
                activity_period={}
                for key,value in activity.items():
                    if key in ['start_time','end_time']:
                        activity_period[key] = value
                activity_periods.append(activity_period)
            user_data["activity_periods"] = activity_periods
            return Response({"data":user_data}, status=status.HTTP_200_OK)

        return Response(
            data={"error": "id is required"},
            status=status.HTTP_400_BAD_REQUEST
            )

    def deleteUserAndActivity(self, request):
        if 'id' in request.query_params and request.query_params is not None:
            try:
                user = User.objects(user_id=request.query_params['id']).get()
            except User.DoesNotExist:
                return Response(
                    data={"error":"User does not exist"},
                    status=status.HTTP_400_BAD_REQUEST
                )
            user.delete()
            ActivityPeriod.objects(user_id=request.query_params['id']).delete()
            return Response("Delete Successfull",status=status.HTTP_200_OK)

        return Response(
            data={"error": "id is required"},
            status=status.HTTP_400_BAD_REQUEST
            )
