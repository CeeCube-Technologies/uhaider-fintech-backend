# myenv\Scripts\activate
# source myenv/Scripts/activate
# mongodb+srv://devcent:JPifHZQhFtShsa0Y@fintechapicluster0.t1cpxfd.mongodb.net/test


# from django.shortcuts import render
from rest_framework import viewsets, parsers
from .models import *
from .serializers import *



class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    parser_classes = [parsers.MultiPartParser, parsers.FormParser]

    def create(self, request, *args, **kwargs):
        serializer = ApplicationSerializer(data=request.data)

        if serializer.is_valid():
            # Save the application object
            application = serializer.save()

            # Save the uploaded PDF files
            pdf_files = request.FILES.getlist('pdf_files')
            for pdf_file in pdf_files:
                ApplicationPDFs.objects.create(application=application, file=pdf_file)

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    # def perform_create(self, serializer):
    #     pdf_files = self.request.FILES.getlist('pdf_files')
    #     unique_infos = self.request.POST.getlist('unique_infos')
    #     application = serializer.save()
    #     if pdf_files:
    #         for i, pdf_file in enumerate(pdf_files):
    #             unique_info = unique_infos[i] if i < len(
    #                 unique_infos) else pdf_file.name
    #             application.pdf_files.create(
    #                 file=pdf_file, unique_info=unique_info)

# Create your views here.

class StatusViewSet(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer


class ApplicationPDFsViewSet(viewsets.ModelViewSet):
    queryset = ApplicationPDFs.objects.all()
    serializer_class = ApplicationPDFsSerializer


# getData ---
# queryset = Application.objects.all()
# serializer = ApplicationSerializer(queryset, many=True)
# json_data = serializer.data

# addData ---
# json_data = '{"application_id": 1, "name_of_business": "ABC Corporation", ... }'
# serializer = ApplicationSerializer(data=json_data)
# if serializer.is_valid():
#     serializer.save()
