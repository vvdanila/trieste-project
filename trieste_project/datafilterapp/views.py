from django.shortcuts import render_to_response
from datafilterapp.models import Visits
from django.db.models import Count
import datetime


def index(request):
    if request.method == 'GET':    
        context = {}
        checked = 'checked'
        keywords = request.GET.getlist('keywords')
        start_date = request.GET.get('start_date')
        end_date = request.GET.get('end_date')
        count = request.GET.get('count')
        db_data = Visits.objects.filter()

        if start_date and end_date:
            start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d").date()
            end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d").date()
            db_data = db_data.filter(date__range=(start_date, end_date))
            context['start_date'] = start_date.isoformat()
            context['end_date'] = end_date.isoformat()

        for keyword in keywords:
            db_data = db_data.filter(long_url__contains=keyword)
            context[keyword] = checked

        if count:
            count = int(count)
            db_data = db_data.values('short_url').annotate(count=Count('short_url')).order_by('-count')[0:count]
            context['count'] = count
        else:
            db_data = db_data.values('short_url').annotate(count=Count('short_url')).order_by('-count')

        context['data'] = db_data

        return render_to_response('index.html', context)
