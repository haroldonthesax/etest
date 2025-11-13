from django.shortcuts import render, get_object_or_404, redirect
from .models import Pcb, TestSequence
from django.contrib import messages
from .forms import UpdateBoard

# Home page
def home(request):
    pcbs = Pcb.objects.all()
    context = {'pcbs':pcbs}
    return render(request, 'home.html', context)

# Login
def login_user(request):
    return render(request, 'login.html', {})

# Logout
def logout_user(request):
    pass

# Register
def register_user(request):
    return render(request, 'register.html', {})


# About page
def about(request):
    return render(request, 'about.html', {})

# Individaual board page:
def board(request, pk):
    # Set the record instance of board
    board = get_object_or_404(Pcb, id=pk) # Pass in the model, and the primary key 
    form=UpdateBoard(request.POST or None,  request.FILES or None, instance=board ) # Named after the forms.py definition. If you go to the page, it will fill out the form 
    # with the instance=board. If you are POSTing the page it will do the stuff in the "if is_valid" statemnt, otherwise it just displays the page. 
    #Save updated info
    if form.is_valid():
        form.save()
        messages.success(request, "The record has been updated.")
        return redirect('home')
    else:
        # Return the board's info into the board.html page and load it. 
        return render(request, 'board.html', {'board':board, 'form':form})

# Delete a board record
def delete_board(request, pk):
    board = get_object_or_404(Pcb, id=pk)
    # We deleted the record, so reload the home page showing the current records after deletion.
    board.delete()
    # Message
    messages.success(request, "The record has been deleted.")
    return redirect('home')

def add_board(request):
    form=UpdateBoard(request.POST or None,  request.FILES or None) #UpdateBoard in the forms.py file is reuseable because it has all of the model fields. 
    # Check for filled out form
    if form.is_valid():
        # Save the form
        form.save()
        messages.success(request, "The new board has been added.")
        return redirect('home')
    else:
        # Return the board's info into the board.html page and load it. 
        return render(request, 'add_board.html', {'board':board, 'form':form})





