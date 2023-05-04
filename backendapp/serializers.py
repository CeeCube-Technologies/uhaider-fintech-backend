from rest_framework import serializers
from .models import *


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'

class ApplicationPDFsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicationPDFs
        fields = '__all__'

class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = "__all__"

    def create(self, validated_data):
        pdf_files = validated_data.pop('pdf_files', None)
        application = super().create(validated_data)

        if pdf_files:
            for pdf_file in pdf_files:
                unique_info = pdf_file.name  # Replace this with your own unique information
                pdf = application.pdf_files.create(
                    file=pdf_file, unique_info=unique_info)
        return application

    def update(self, instance, validated_data):
        pdf_files_data = validated_data.pop('pdf_files', [])
        instance = super().update(instance, validated_data)
        for pdf_file_data in pdf_files_data:
            ApplicationPDFs.objects.create(application=instance, **pdf_file_data)
        return instance
