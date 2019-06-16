from django.shortcuts import render

# Create your views here.
def land_redirect(request):
    # if request.user.is_authenticated:
    #     return redirect(reverse('home:home'))
    # else:
    #     feed_list = UserFeedback.objects.all()
        return render(request, 'index.html')