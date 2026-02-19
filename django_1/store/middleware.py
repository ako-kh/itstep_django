import re

from django.shortcuts import render
from django.conf import settings

class MaintenanceModeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if (settings.MAINTENANCE_MODE
                and not request.user.is_staff
                and not re.match('/admin/', request.path)):

            return render(request, 'maintenance.html', status=503)

        response = self.get_response(request)

        return response