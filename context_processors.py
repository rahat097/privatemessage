from . models import PrivateMessage



def add_variable_to_context(request):
	if request.user.is_authenticated:
		lastmessage = request.user.privatemessage.filter(is_seen = False).last()
		unreadmessagecount = PrivateMessage.objects.filter(pmreciever = request.user, is_seen = False).count()
	else:
		lastmessage = 0
		unreadmessagecount = 0
	return {
        'unreadmessagecount': unreadmessagecount,
        'lastmessage' : lastmessage
    }