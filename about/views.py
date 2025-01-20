from django.shortcuts import render
from django.contrib import messages
from .models import About
from .forms import CollaborateForm
# Create your views here.


def about_me(request):
    """
    Renders the most recent information about the website owner. 
    And also handles the form for collaboration requests.
    Displays an individual instance of :model:'about.About'.
    **Context**
    ``about``
        An instance of :model:'about.About'.
    ``collaborate_form``
        An instance of :form:'about.forms.CollaborateForm'.
    **Template:**
    :template:'about/about.html'
    """
    if request.method == 'POST':
        collaborate_form = CollaborateForm(request.POST)
        if collaborate_form.is_valid():
            collaborate_form.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                'Collaboration request received! I endeavour to respond '
                'within 2 working days.'
            )
    about = About.objects.all().order_by('-updated_on').first()
    collaborate_form = CollaborateForm()

    return render(
        request,
        'about/about.html',
        {
            'about': about,
            'collaborate_form': collaborate_form,
        },
    )
