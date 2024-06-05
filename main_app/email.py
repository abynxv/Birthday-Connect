from django.core.mail import send_mail

def send_birthday_email(name, email):
    subject = f'Happy Birthday, {name}!'
    message = f"Dear {name},\n\nWishing you a very happy birthday!\n\nBest regards,\nAbhinav"
    from_email = 'abhinavabi001@email.com'
    
    send_mail(subject, message, from_email, [email])