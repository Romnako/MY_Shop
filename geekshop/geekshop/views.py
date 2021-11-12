from django.shortcuts import render
from mainapp.models import Product
from basketapp.models import Basket
from django.views.generic.base import TemplateView

from django.dispatch import receiver
from allauth.socialaccount.signals import pre_social_login

def main(request):
    title = 'Магазин'
    products = Product.objects.all()[1:4]

    context = {
        'title': title,
        'products': products,
    }
    return render(request, 'geekshop/index.html', context=context)


def contacts(request):
    title = 'Контакты'
    context = {
        'title': title,
    }
    return render(request, 'geekshop/contact.html', context=context)



def populate_profile(sociallogin, user, **kwargs):

    if sociallogin.account.provider == 'facebook':
        user_data = user.socialaccount_set.filter(provider='facebook')[0].extra_data
        picture_url = "http://graph.facebook.com/" + sociallogin.account.uid + "/picture?type=large"
        email = user_data['email']
        first_name = user_data['first_name']

    if sociallogin.account.provider == 'linkedin':
        user_data = user.socialaccount_set.filter(provider='linkedin')[0].extra_data
        picture_url = user_data['picture-urls']['picture-url']
        email = user_data['email-address']
        first_name = user_data['first-name']

    if sociallogin.account.provider == 'twitter':
        user_data = user.socialaccount_set.filter(provider='twitter')[0].extra_data
        picture_url = user_data['profile_image_url']
        picture_url = picture_url.rsplit("_", 1)[0] + "." + picture_url.rsplit(".", 1)[1]
        email = user_data['email']
        first_name = user_data['name'].split()[0]

    user.profile.avatar_url = picture_url
    user.profile.email_address = email
    user.profile.first_name = first_name
    user.profile.save()

class ErrorPage(TemplateView):
    template_name = 'error.html'