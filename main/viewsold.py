@login_required
def contacts(request):
    contacts = Contact.objects.all().order_by('-id')
   
    return render(request, "contacts.html", {
        'contacts' : contacts,
        'form' : ContactForm()
    }) 

@login_required
def search_contacts(request):
    import time 
    time.sleep(2)
    query = request.GET.get('search_contacts', '')

    contacts = request.user.contacts.filter(
        Q(name__icontains=query) | Q(email__icontains=query)
    )

    return render(request, "partials/contacts-list.html", { 'contacts' : contacts } )

@login_required
@require_http_methods(['POST'])
def create_contact(request):
    form = ContactForm(request.POST, request.FILES, initial={'user': request.user})
    if form.is_valid():
        new_contacts = form.save(commit=False)
        new_contacts.user = request.user
        new_contacts.save()
        contacts= Contact.objects.filter(user=request.user).order_by('-id')
        context = { 'contacts' : contacts }
        response = render(request, "partials/contacts-list.html", context )
        response['HX-Trigger'] = 'success'
        return response
    else:
        response = render(request, "partials/add-modal.html", {'form' : form} )
        response['HX-Retarget'] = '#my_modal_1'
        response['HX-Reswap'] = 'outerHTML'
        response['HX-Trigger-After-Settle'] = 'fail'
        return response 


@login_required
def edit_contact(request, id):
    # 1. डेटा निकालें
    contact_obj = get_object_or_404(Contact, id=id)

    if request.method == 'POST':
        # 2. सेव करने का लॉजिक
        form = ContactForm(request.POST, request.FILES, instance=contact_obj)
        if form.is_valid():
            form.save()
            contacts = Contact.objects.filter(user=request.user).order_by('-id')
            response =  render(request, "partials/contacts-list.html", {'contacts': contacts})
            response['HX-Trigger'] = json.dumps({"success" : "true"})
            return response
    
    # 3. GET रिक्वेस्ट: यहाँ 'x' या 'contact' वही नाम भेजो जो तुम टेम्पलेट में यूज़ कर रहे हो
    form = ContactForm(instance=contact_obj)
    context = {
        'editform': form, 
        'instance': contact_obj  # मैंने यहाँ 'instance' नाम दिया है
    }
    return render(request, "partials/editform.html", context)


@login_required
def delete_contact(request, id):
    # 1. डेटा निकालें
    contact_obj = get_object_or_404(Contact, id=id)
    contact_obj.delete()
    contacts = Contact.objects.filter(user=request.user).order_by('-id')
    response = render(request, "partials/contacts-list.html", {'contacts': contacts})
    response['HX-Trigger'] = 'contact_deleted'
    return response
 


''''
def edit_contact(request, id):
    print(f"Checking ID: {id}")
    contacts = get_object_or_404(Contact, id=id)

    if request.method == 'POST':
        #contacts = get_object_or_404(Contact, id=id)
        editform = ContactForm(request.POST, request.FILES, instance=contacts)
        if editform.is_valid():
            editform.save()
            messages.success(request, "Profile updated")
            ucontacts = Contact.objects.filter(user=request.user).order_by('id')
            return render(request, "partials/contact-row.html", {'ucontacts': ucontacts})
            response['HX-Trigger'] = 'show_success_toast'
            response.write('<div id="editform" hx-swap-oob="outerHTML"></div>')
            return response
        else:
            print("FORM INVALID ❌")
            print(form.errors)
    else:
        editform = ContactForm(instance=contacts)
        context = {'editform': editform, 'contacts': contacts }
    
    return render(request, "partials/editform.html", context)
'''            


'''
def schemeread(request, slug):
    scheme = Scheme.objects.get(slug=slug)

    return render(request, "schemeread.html", {
        'scheme' : scheme,
    }) 
def register(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        #form = RegistrationForm(request.POST)
        user = User.objects.create_user(
            username=username,
            password=password
        )

        SrijanProfile.objects.create(user=user)
        return render(request, "welcome.html")
#        return render(request, "welcome.html", {'user' : user_obj })
        
        
        if form.is_valid():
            user_obj = form.save()
            messages.success(request, "आपका रजिस्ट्रेशन सफल रहा!")
            #return redirect('welcome') # अपनी लॉगिन URL का नाम लिखें
        
        else:
            #messages.error(request, "कृपया त्रुटियों को ठीक करें।")
            # यहाँ जादू है: फॉर्म की हर एरर को Toastr मैसेज में बदलें
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field.capitalize()}: {error}")
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})
        '''

'''
def login_view(request):
    if request.method == "POST":
        u = request.POST.get('username')
        p = request.POST.get('password')
        user = authenticate(username=u, password=p)
        
        if user is not None:
            auth_login(request, user)
            return redirect('dashboard')
        else:
            return HttpResponse("गलत जानकारी!")
            
    return render(request, 'login.html')
'''


def pandas(request):
    area = None
    if request.method == "POST":
        radius = request.POST.get("radius")
        radius = float(radius)
        area = 3.14 * radius * radius 
    
    return render(request, "pandas.html", { 'area' : area })



