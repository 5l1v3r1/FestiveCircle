from django.contrib.auth import update_session_auth_hash
def fill(backend, strategy, details, response,
        user=None, *args, **kwargs):
    if user:
        print("YEH REGISTERED HAI")
        return
    
    print("YE LA WARIS HAI")
    url = None
    first_name = None
    last_name = None
    profile = user.profile
    print(response)
    if backend.name == 'google-oauth2':
        url = response['picture']
        first_name = response['name']
        last_name = response['name']
        ext = url.split('.')[-1]

    last_name = first_name.split(" ")[1]
    first_name = first_name.split(" ")[0]
    
    user.first_name = first_name
    user.last_name = last_name
    profile.profile_picture = url
    
    user.save()
    profile.save()
    update_session_auth_hash(strategy.request, user)
