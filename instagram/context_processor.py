from datetime import datetime
from django.conf import settings


def get_current_year(request):
  current_year = datetime.now().year
  return {
    'current_year': current_year
  }
