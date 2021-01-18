from . models import PrivateMessage



def add_variable_to_context(request):
	if request.user.is_authenticated:
		unreadmessagecount = PrivateMessage.objects.filter(pmreciever = request.user, is_seen = False).count()
	else:
		unreadmessagecount = 0
	return {
        'unreadmessagecount': unreadmessagecount
    }