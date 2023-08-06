from django.http import JsonResponse
from main.models import Sensor, SensorEvent
from django.db.models import Avg
from datetime import datetime
from django.db.models.functions import ExtractWeekDay
from django.db.models import Count, F
from datetime import datetime, timedelta


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
    if start_date > end_date:
        return JsonResponse({"error": "Wrong query date!"}, status=400)

    # Calculate count of each weekday
    days_count = {
        'Monday': 0,
        'Tuesday': 0,
        'Wednesday': 0,
        'Thursday': 0,
        'Friday': 0,
        'Saturday': 0,
        'Sunday': 0,
    }
    current_date = start_date
    while current_date <= end_date:
        # Gets the name of the day of the week for the current date
        day_of_week = current_date.strftime('%A')
        # Increase the count for the day of the week
        days_count[day_of_week] += 1
        current_date += timedelta(days=1)

    results = []
    for sensor_id in range(1, 11):
        counts = {i: 0 for i in range(1, 8)}
        sensor_events = (SensorEvent.objects.filter(
            event_datetime__date__range=(start_date, end_date),
            sensor_id=sensor_id)
                         # get work days Sunday = 1, Saturday = 7
                         .annotate(weekday=ExtractWeekDay('event_datetime'))
                         .values('weekday')
                         .annotate(count=Count('id')))

        for event in sensor_events:
            weekday = event['weekday']
            counts[weekday] = event['count']
        result = {
            'sensor_id': sensor_id,
            'sensor_name': str(sensor_id),
            'mon_avg_count': int(counts[2] / days_count['Monday'] if days_count['Monday'] else 0),
            'tue_avg_count': int(counts[3] / days_count['Tuesday'] if days_count['Tuesday'] else 0),
            'wed_avg_count': int(counts[4] / days_count['Wednesday'] if days_count['Wednesday'] else 0),
            'thu_avg_count': int(counts[5] / days_count['Thursday'] if days_count['Thursday'] else 0),
            'fri_avg_count': int(counts[6] / days_count['Friday'] if days_count['Friday'] else 0),
            'sat_avg_count': int(counts[7] / days_count['Saturday'] if days_count['Saturday'] else 0),
            'sun_avg_count': int(counts[1] / days_count['Sunday'] if days_count['Sunday'] else 0)
        }
        results.append(result)

    return JsonResponse({"results": results})
