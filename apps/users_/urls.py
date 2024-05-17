from django.urls import path

from apps.users_.views import ExcelUpload, NutritionList
from . import views


urlpatterns = [
    path('excel/upload/', ExcelUpload.as_view(), name='excel_upload'),
    path('nutrition/list/', NutritionList.as_view(), name='nutrition_list'),
    path('nutrition/menu/', views.nutrition_menu, name='nutrition_menu'),
    path('upload/form/', views.upload_form, name='upload_form'),

]