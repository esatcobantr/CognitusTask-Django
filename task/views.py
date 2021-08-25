from task.models import AlgorithmModel
from rest_framework.generics import UpdateAPIView, ListAPIView, DestroyAPIView
from task.serializers import CreateSerializer, UpdateSerializer, ListSerializer, DeleteSerializer, PredictionSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
import requests
import os



class TaskCreateView(APIView):
    serializer_class = CreateSerializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data, context={"request": request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"status": "True"})



class TaskUpdateView(UpdateAPIView):
    queryset = AlgorithmModel.objects.all()
    serializer_class = UpdateSerializer
    lookup_field = 'id'



class TaskListView(ListAPIView):
    queryset = AlgorithmModel.objects.all()
    serializer_class = ListSerializer



class TaskDeleteView(DestroyAPIView):
    queryset = AlgorithmModel.objects.all()
    serializer_class = DeleteSerializer
    lookup_field = 'id'



class TrainView(APIView):
    def post(self, request):
        requests.post(os.getenv("train_url"))
        return Response({"status": "True"})



class PredictionView(APIView):
    serializer_class = PredictionSerializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data, context={"request": request})
        serializer.is_valid(raise_exception=True)
        response = serializer.prediction()
        return Response({"response": response})