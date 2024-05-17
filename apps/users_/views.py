import requests
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse

from config.settings import API_ENDPOINT, API_TOKEN


def nutrition_menu(request):
    return render(request, 'users_/nutrition.html')

def upload_form(request):
    return render(request, 'users_/upload_form.html')


class ExcelUpload(APIView):
    """
     Chama o endpoint da api para fazer o upload da planilha Nutrition.

     Obrigatório fornecer:

     @File: Multipart/FormData {"file": arquivo.xlsx} (fornecer em body)
     @access_token: string (Bearer Token) (fornecer em header)
     """
    permission_classes = (IsAuthenticated,)

    @staticmethod
    def post(request):
        file = request.FILES.get('file')
        if not file:
            return JsonResponse(request, {"message": "Envie a planilha "
                                                          "para prosseguir."},
                                     status_code=400)
        files = {'file': file}

        url = f"{API_ENDPOINT}/nutrition/upload/"
        headers = {
            "Authorization": f"Bearer {API_TOKEN}"
        }
        response = requests.post(url, files=files, headers=headers)

        api_response = response.json()

        if response.status_code == 201:
            return JsonResponse({
                "message": "Upload realizado com sucesso!",
                "api_response": api_response
            }, status=201)
        else:
            return JsonResponse({
                "message": "Erro no upload do arquivo.",
                "api_response": api_response
            }, status=400)


class NutritionList(APIView):
    """
     Chama o endpoint da api para fazer a listagem páginada
     de Nutrition.

     Obrigatório fornecer:

     @access_token: string (Bearer Token) (fornecer em header)

     Opcional fornecer:

     parâmetros: ?page=1&size=10
     """

    permission_classes = (IsAuthenticated,)

    @staticmethod
    def get(request):
        page = request.query_params.get('page', 1)
        size = request.query_params.get('size', 10)

        url = f"{API_ENDPOINT}/nutrition/?page={page}&size={size}"
        headers = {
            "Authorization": f"Bearer {API_TOKEN}"
        }
        response = requests.get(url, headers=headers)

        api_response = response.json()

        if response.status_code == 200:
            return JsonResponse({
                "message": "Dados recuperados com sucesso!",
                "api_response": api_response
            }, status=200)
        else:
            return JsonResponse({
                "message": "Falha ao recuperar os dados",
                "api_response": api_response
            }, status=400)