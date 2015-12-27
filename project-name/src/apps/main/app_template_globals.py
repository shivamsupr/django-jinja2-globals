from datetime import datetime
import time
import pytz

def now():
    return datetime.utcnow().replace(tzinfo=pytz.utc)