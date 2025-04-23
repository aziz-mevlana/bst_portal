from django.shortcuts import render
from django.utils import timezone

def coming_soon(request):
    current_date = timezone.now()
    context = {
        'title': 'Yakında Buradayız!',
        'message': 'Web sitemiz çok yakında yayında olacak!',
        'year': current_date.year,
    }
    return render(request, 'coming_soon/index.html', context)
