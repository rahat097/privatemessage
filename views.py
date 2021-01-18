from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from . models import PrivateMessage
from .forms import MessageForm,MessageFormWithUsername
from django.contrib import messages


def messagedialog(request,id):
	user = User.objects.get(id = id)

	allmessage1 = PrivateMessage.objects.filter(pmsender = request.user, pmreciever = user)
	allmessage2 = PrivateMessage.objects.filter(pmsender = user, pmreciever = request.user)

	allmessage3 = allmessage1 | allmessage2

	allmessage4 = allmessage3.order_by('id')

	context = {
	'allmessage4' : allmessage4,
	}
	return render(request,'messagehistory.html', context)



def messagedetailoutbox(request,id):
	message = PrivateMessage.objects.get(id = id)
	if request.user != message.pmsender:
		messages.info(request, "You cant see this message.")
		return redirect('messagehome')

	context = {
	'message' : message,
	}
	return render(request, 'messagedetailoutbox.html', context)




def messageoutbox(request):
	allmessage = PrivateMessage.objects.filter(pmsender = request.user).order_by('-id')
	if request.method == 'POST':
		if not User.objects.filter(username = request.POST['pmreciever'] ).exists():
			messages.info(request, "User dont exist, Write correct username")
			return redirect('messageoutbox')
		elif request.user == User.objects.get(username = request.POST['pmreciever'] ):
			messages.info(request, "You cant send Message to yourself")
			return redirect('messageoutbox')

		else:
			user = User.objects.get(username = request.POST['pmreciever'] )
			message_form = MessageFormWithUsername()
			new_message = PrivateMessage(pmsender=request.user,pmreciever=user, pmbody=request.POST['pmbody'])
			new_message.save()
			messages.info(request, "Message Sent Succesfully")
			return redirect('messageoutbox')

	else:
		message_form = MessageFormWithUsername()




	context = {
	'allmessage' : allmessage,
	'message_form' : message_form,
	}
	return render(request, 'messageoutbox.html',context)



def messageinbox(request):
	allmessage = PrivateMessage.objects.filter(pmreciever = request.user).order_by('-id')


	context = {
	'allmessage' : allmessage,
	}
	return render(request, 'messagehomepage.html',context)


def messagedetailinbox(request,id):
	message = PrivateMessage.objects.get(id = id)
	if request.user != message.pmreciever:
		messages.info(request, "You cant see this message.")
		return redirect('messageinbox')
	message.is_seen = True
	message.save()
	if request.method == 'POST':
		message_form = MessageForm(data=request.POST)
		if message_form.is_valid():
			new_meassge = message_form.save(commit=False)
			new_meassge.pmreciever = message.pmsender
			new_meassge.pmsender = message.pmreciever
			if new_meassge.pmsender == new_meassge.pmreciever:
				messages.info(request, "Sorry")
				return redirect('messageinbox')
			else:
				new_meassge.save()
				messages.info(request, "Message Sent Succesfully")
				return redirect('messageinbox')

	else:
		message_form = MessageForm()

	context = {
	'message' : message,
	'message_form' : message_form,
	}
	return render(request, 'messagedetail.html', context)
