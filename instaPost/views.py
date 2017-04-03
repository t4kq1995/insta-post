from django.http import JsonResponse
import os.path
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from splinter import Browser


""" Global variables """
BASE = os.path.dirname(os.path.abspath(__file__))
LOGIN = "t4kq"
PASSWORD = "pro100vladpro100vlad"


@api_view(['GET'])
@permission_classes((permissions.IsAuthenticated,))
def upload_photo(request):
    if request.method == 'GET':
        from InstagramAPI import InstagramAPI
        inst_api = InstagramAPI(LOGIN, PASSWORD)
        inst_api.login()
        inst_api.uploadPhoto(os.path.join(BASE, "../images/image.jpg"), 'Hello')
        return JsonResponse({'status': True})


@api_view(['GET'])
@permission_classes((permissions.IsAuthenticated,))
def splinter_parse(request):
    if request.method == 'GET':
        with Browser('chrome') as browser:
            # Visit URL
            url = "http://www.google.com"
            browser.visit(url)
            browser.fill('q', 'splinter - python acceptance testing for web applications')
            # Find and click the 'search' button
            button = browser.find_by_name('btnG')
            # Interact with elements
            button.click()
            if browser.is_text_present('splinter.readthedocs.io'):
                print("Yes, the official website was found!")
            else:
                print("No, it wasn't found... We need to improve our SEO techniques")
        return JsonResponse({'status': True})
