from datetime import datetime

def get_current_year(request):
  current_year = datetime.now().year
  return {
    'current_year': current_year
  }
