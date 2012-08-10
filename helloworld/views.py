from django.shortcuts import render
from django.shortcuts import render_to_response

from widgets import GreetingForm

def sayhello(request):


    if request.method == 'POST': # If the form has been submitted...
        form = GreetingForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
            return render_to_response('greet.html', {'form': form.cleaned_data} )
    else:
        form = GreetingForm() # An unbound form

    return render(request, 'hello.html', { 'form': form, })

