

def finalize(request):
    shopping_url = request.REQUEST.get('shopping')
    try:
        appshop_session = appshop.Session(shopping_url)
        request.session['appshop'] = {
            "shopping_url": shopping_url,
            "access_token": appshop_session.request_token(request.REQUEST)
        }

    except Exception:
        messages.error(request, "Could not log in to Appshop store.")
        return redirect(reverse('appshop_app.views.login'))

    messages.info(request, "Logged in to Appshop store.")

    response = redirect(_return_address(request))
    request.session.pop('return_to', None)
    return response