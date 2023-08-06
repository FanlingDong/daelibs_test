from django.http import JsonResponse
from main.models import Sensor, SensorEvent
from django.db.models import Avg
from datetime import datetime
from django.db.models.functions import ExtractWeekDay
from django.db.models import Count, F


# Create your views here.

def day_of_week_average_count(request):
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    if start_date:
        start_date = datetime.strptime(start_date, '%Y-%m-%d')
    if end_date:
        end_date = datetime.strptime(end_date, '%Y-%m-%d')
    print('start_date', start_date)
    print('end_date', end_date)

    # sensor_data = SensorEvent.objects.filter(event_datetime__date__range=(start_date, end_date))
    results = []

    for sensor_id in range(1, 11):
        counts = {i: 0 for i in range(1, 8)}
        sensor_events = SensorEvent.objects.filter(
            event_datetime__date__range=(start_date, end_date),
            sensor_id=sensor_id
        ).annotate(
            weekday=ExtractWeekDay('event_datetime')  # 提取工作日
        ).values('weekday').annotate(
            count=Count('id')  # 计算每个工作日的事件数
        )
        for event in sensor_events:
            weekday = event['weekday']
            counts[weekday] = event['count']
        result = {
            'sensor_id': sensor_id,
            'sensor_name': str(sensor_id),
            'mon_avg_count': counts[2],
            'tue_avg_count': counts[3],
            'wed_avg_count': counts[4],
            'thu_avg_count': counts[5],
            'fri_avg_count': counts[6],
            'sat_avg_count': counts[7],
            'sun_avg_count': counts[1]
        }
        results.append(result)

    return JsonResponse({"results": results})
