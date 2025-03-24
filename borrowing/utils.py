from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string

def send_notification_email(subject, recipient, message=None, template=None, context=None, fail_silently=True):
    """
    Generic email sending utility that supports both direct messages and templates
    
    """
    try:
        # If template and context are provided, render the template
        if template and context:
            message = render_to_string(template, context)
        elif not message:
            raise ValueError("Either message or template+context must be provided")

        return send_mail(
            subject=subject,
            message=message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[recipient],
            fail_silently=fail_silently
        )
    except Exception as e:
        print(f"Email sending failed: {str(e)}")
        return False