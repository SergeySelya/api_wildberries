import pandas as pd
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Function for parser HTTP that return
from product_info_wb import parser_article


class FileUploadView(APIView):
    """
    Upload the .xlsx file or article.
    Then reads it and saves csv data to database.
    Endpoint: /api/product_info_wb/file_upload/
    """

    def post(self, request, *args, **kwargs):

        data = request.data["file"]
        if data is None:
            return Response(
                {"error": "No File Found"}, status=status.HTTP_400_BAD_REQUEST
            )

        if str(data).isdigit():
            res = parser_article.main([str(data)])
            return Response(res[0], status=status.HTTP_200_OK)

        elif str(data).endswith(".xlsx"):
            xl = pd.read_excel(data, header=None)
            res = parser_article.main(xl[0])
            return Response(res, status=status.HTTP_200_OK)
        else:
            return Response(
                data={"Incorrect format of request parameter: 'value'."},
                status=status.HTTP_400_BAD_REQUEST,
            )
