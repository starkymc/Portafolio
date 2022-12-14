import datetime
from ipware import get_client_ip
from django.http import HttpResponse
from portafoliopersonal.models import IpAddress

BLACK_LIST = [
    
]

class saveip_address():
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        ip, is_routable = get_client_ip(request)
        print( ip)
        direccionesIpe = IpAddress.objects.filter(ip_address = ip ).exists()
        if direccionesIpe:
            return self.get_response(request)
        if is_routable:
         pass
        IpAddress.objects.create(pub_date = datetime.date.today(), ip_address = ip)
        return self.get_response(request)
        
