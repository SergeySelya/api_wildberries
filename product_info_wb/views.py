from rest_framework.parsers import (
    MultiPartParser,
    FormParser
)
import pandas as pd
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class FileUploadView(APIView):
    """
            Upload the .xlsx file or int values.
            Then reads it and saves csv data to database.
            Endpoint: /api/product_info_wb/file_upload/
    """

    parser_classes = (MultiPartParser, FormParser,)

    def post(self, request, *args, **kwargs):

        # _dict_file_obj = request.data['file']
        # # xl = pd.read_excel(_dict_file_obj)
        # return Response(_dict_file_obj.isdigit(),
        #                     status=status.HTTP_400_BAD_REQUEST)

        if request.data['file'] is None:
            return Response({"error": "No File Found"},
                            status=status.HTTP_400_BAD_REQUEST)

        try:
            if request.data['file'].isdigit() is True:
                return Response(request.data['file'],
                                status=status.HTTP_200_OK)
            else:
                return Response({"The article must have only numbers"},
                                     status=status.HTTP_400_BAD_REQUEST
                               )

        except :
            return Response('file',
                            status=status.HTTP_200_OK)
