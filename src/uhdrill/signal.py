from datetime import timedelta, datetime
from django.utils.timezone import make_aware
from django.db.models.signals import post_save
from django.conf import settings
from django.dispatch import receiver
from base import views
from base.models import Order, User
from django.core.mail import send_mail


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def publish_activate_token(sender, instance, **kwargs):
    if not instance.is_active:
        user_activate_token = views.UserActivateTokens.objects.create(
            user=instance,
            expired_at=make_aware(datetime.now()+timedelta(days=settings.ACTIVATION_EXPIRED_DAYS)),
        )
        subject = 'Please Activate Your Account'
        message = f'URLにアクセスしてユーザーアクティベーション。\n {settings.MY_URL}/activate/{user_activate_token.activate_token}/'
    if instance.is_active:
        subject = 'Activated! Your Account!'
        message = 'ユーザーが使用できるようになりました'
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [
        instance.email,
    ]
    send_mail(subject, message, from_email, recipient_list)


@receiver(post_save, sender=Order)
def order_complate_mail(sender, instance, **kwargs):
    if instance.is_confirmed:

        # Userテーブルからメールアドレスを抽出
        queryset = User.objects.filter(id=instance.user_id)
        email = queryset[0].email

        subject = 'ご注文ありがとうございました。'
        message = f'ご注文ありがとうございました。\n 注文履歴はこちらから見ることができます。 \n {settings.MY_URL}/orders/{instance.id}/'
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = [
            email,
        ]
        send_mail(subject, message, from_email, recipient_list)
