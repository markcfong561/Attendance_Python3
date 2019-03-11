"""
Program that puts sign in and sign out data onto firebase
"""

from django.shortcuts import render
from firebase import firebase
import datetime

firebase = firebase.FirebaseApplication('https://linworth-attendance-testing.firebaseio.com/', None)
now = datetime.datetime.now()
date = now.strftime("%Y-%m-%d")

def signIn(request):

    return render(request, "signIn.html")

def signOut(request):

    return render(request, "signOut.html")

def postsign(request):
    student_id = request.POST.get('Student_ID')

    now = datetime.datetime.now()
    time = now.strftime("%H:%M")
    url = '/' + student_id + '/' + date + '/' + 'Signed Out'

    if firebase.get(student_id, None) == None or firebase.get(url, None) == None:
        
        return render(request, "invalidID.html")

    else:

        firebase.put(url, 'Signed In', time)
        return render(request, "signedIn.html")

def postsign_signOut(request):
    student_id = request.POST.get('Student_ID')
    location = request.POST.get('Location')

    now = datetime.datetime.now()
    time = now.strftime("%H:%M")

    if firebase.get(student_id, None) == None:

        return render(request, "invalidID.html")

    else:

        period = request.POST.get('Period')
        url = '/' + student_id + '/' + date + '/' + 'Signed Out'
        firebase.put(url, 'Location',  location)
        firebase.put(url, 'Time', time)
        return render(request, "signedOut.html")
