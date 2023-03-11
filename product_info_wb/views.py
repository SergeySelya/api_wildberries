from rest_framework.parsers import (
    MultiPartParser,
    FormParser
)
import pandas as pd
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from product_info_wb import parser_article

class FileUploadView(APIView):
    """
            Upload the .xlsx file or int values.
            Then reads it and saves csv data to database.
            Endpoint: /api/product_info_wb/file_upload/
    """

    parser_classes = (MultiPartParser, FormParser,)

    def post(self, request, *args, **kwargs):

        data = request.data['file']
        if data is None:
            return Response({"error": "No File Found"},
                            status=status.HTTP_400_BAD_REQUEST)

        try:
            if request.data['file'].isdigit() is True:
                return Response(parser_article.get_product(data),
                         status=status.HTTP_200_OK
                         )
            else:
                return Response({"The article must have only numbers"},
                                status=status.HTTP_400_BAD_REQUEST
                                )
        except:
            _dict_file_obj = request.data['file'].__dict__
            _excel = _dict_file_obj['_name'].endswith('.xlsx')

            if _excel is True:
                a = []
                xl = pd.read_excel(data,header=None).to_dict()

                for value in xl[0].values():

                    a.append(parser_article.get_product(str(value)))
                return Response(a,
                                status=status.HTTP_400_BAD_REQUEST
                                )

            else:
                return Response(data={"Upload File must have *.xlsx format."},
                                status=status.HTTP_400_BAD_REQUEST
                                )
