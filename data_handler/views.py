from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from data_handler.models import RSSIData
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.views import APIView
from django.views.generic import View
import matplotlib.pyplot as plt
import json
        
def root_view(request):
    # 루트 URL에 대한 요청을 처리하는 로직을 작성합니다.
    return HttpResponse("Welcome to the root page!")

@csrf_exempt
def data_receiver(request):
    if request.method == 'POST':
        received_data = int(request.POST.get('data'))
        # 데이터 처리 작업 수행
        print("Received data:", received_data)
        
        # 받은 데이터를 데이터베이스에 저장
        rssi_data = RSSIData(rssi_value=received_data)
        rssi_data.save()
        
        # 받은 데이터를 HTML 페이지에 표시
        return JsonResponse({'status': 'Data received and saved successfully'})
        #return JsonResponse({'status': 'Data received successfully'})
    else:
        return JsonResponse({'error': 'Invalid request method'})

@csrf_exempt    
def graph_data_view(request):
    # 데이터베이스에서 최신 데이터 가져오기
    recent_data = RSSIData.objects.order_by("-id")[:100000]
    
    # 그래프에 사용할 데이터 포맷으로 변환
    labels = [obj.id for obj in recent_data]
    values = [obj.rssi_value for obj in recent_data]
    chart_data = {"labels": labels, "values": values}
    
    chart_data_json = json.dumps(chart_data)
    
    return render(request, 'graph_template.html', {"chart_data_json": chart_data_json})

@csrf_exempt
def graph_distance_view(request):
    #데이터베이스에서 거리 값 가져오기
    recent_distance = RSSIData.objects.order_by("-id")[:1000000]
    
    # 그래프에 사용할 거리 포맷으로 변환
    labels = [obj.id for obj in recent_distance]
    distance = [obj.dist_data for obj in recent_distance]
    graph_data = {"labels": labels, "values":distance}
    
    graph_data_json = json.dumps(graph_data)
    
    return render(request, 'distance_template.html', {"distance_data_json": graph_data_json})