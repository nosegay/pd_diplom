from django.conf import settings
from django.core.mail.message import EmailMultiAlternatives

from pd_diplom.celery import celery_app

from users.models import ConfirmEmailToken


@celery_app.task()
def send_verification_email(user_id, **kwargs):
    """
    отправляем письмо с подтрердждением почты
    """
    # send an e-mail to the user
    token, _ = ConfirmEmailToken.objects.get_or_create(user_id=user_id)
    
    msg = EmailMultiAlternatives(
        # title:
        f"User verification for {token.user.email}",
        # message:
        token.key,
        # from:
        settings.EMAIL_HOST_USER,
        # to:
        [token.user.email]
    )
    msg.send()
