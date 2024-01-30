from mail_templated import send_mail

from celery import shared_task

from .models import Product


@shared_task
def send_mails_about_favourites(product_int):

    product = Product.objects.get(pk=product_int)

    user_emails = [str(user.email) for user in product.favourite_by.all()]

    send_mail(
        'favourite_user_product.html', {'product': product},
        'oleksandr.hnylosyr@gmail.com', user_emails
    )


