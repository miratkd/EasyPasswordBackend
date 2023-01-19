from mainApp import models, exceptions

def save_password(account, request):
    try:
        request.data['site']
    except:
        raise exceptions.NoSiteException
    try:
        request.data['password']
    except:
        raise exceptions.NoPasswordException
    if len(request.data['site']) > 50 or len(request.data['password']) > 50:
        raise exceptions.MaxSizeException
    return models.Password.objects.create(
        account = account,
        site = request.data['site'],
        password = request.data['password']
    )

def get_all_passwords (account):
    return models.Password.objects.filter(account = account)
