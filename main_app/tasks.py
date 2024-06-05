from celery import shared_task
from celery.utils.log import get_task_logger
from .email import send_birthday_email
from datetime import datetime
from .models import FriendsModel

logger = get_task_logger(__name__)

@shared_task(name="send_birthday_wishes_task", bind=True)
def send_birthday_wishes_task(self):
    today = datetime.now().date()
    friends = FriendsModel.objects.filter(dob__month=today.month, dob__day=today.day)
    
    for friend in friends:
        send_birthday_email(friend.name, friend.email)
        
        logger.info(f"Sent birthday wishes to {friend.name} at {friend.email}")