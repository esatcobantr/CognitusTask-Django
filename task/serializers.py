from rest_framework import serializers
from task.models import AlgorithmModel
import pandas as pd
import requests
import os


class CreateSerializer(serializers.Serializer):

    file = serializers.FileField(required=True)

    def save(self):
        file = self.validated_data.get('file')
        df = pd.read_excel(file)
        text = df.get('text').tolist()
        label = df.get('label').tolist()
        
        for index in range(len(label)):
            AlgorithmModel.objects.create(text=text[index], label=label[index])



class UpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlgorithmModel
        fields = ['id', 'text', 'label']



class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlgorithmModel
        fields = ['id', 'text', 'label']



class DeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlgorithmModel
        fields = ['id', 'text', 'label']



class PredictionSerializer(serializers.Serializer):
    text = serializers.CharField(required=True)
    def prediction(self):
        text = self.initial_data.get('text')
        response = requests.post(os.getenv("prediction_url"), json={"text": text})
        return response