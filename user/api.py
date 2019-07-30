from django.core.cache import cache

from user.models import User

def submit_phone(request):
    '''提交手机号，发送验证码'''
    # phone = request.POST.get('phone')
    phone = request.GET.get('phone')
    print(phone)
    send_vcode(phone)
    return render_json(None)

