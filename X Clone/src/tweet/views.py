from django.shortcuts import render, redirect
from .models import Tweet
from .forms import TweetForm
from django.shortcuts import get_object_or_404 

# Create your views here.

def index(request):
    return render(request, 'apps/index.html')

# tweet list (main tweet page)
def tweet_list(request):
    tweets = Tweet.objects.all().order_by('-created_at') # get all the tweets from the database and order them by the created_at field in descending order . 
    return render(request, 'apps/tweet_list.html', {'tweets': tweets}) # pass the tweets to the templates. 

# create tweet 
def tweet_create(request):
    if request.method == 'POST':
        form = TweetForm(request.POST, request.FILES)
        if form.is_valid():
            tweet = form.save(commit=False) # commit=False means that we don't want to save the form to the database yet. We want to add the user first. 
            tweet.user = request.user # request.user is the user that is currently logged in. every request has a user attribute that is the user that is currently looged in. 
            tweet.save() # now we save the tweet to the detabase. 
            return redirect('tweet_list') # its redirect the user to the tweet_list page after the tweet is created successfully. 
    else:
        form = TweetForm()
    return render(request, 'apps/tweet_form.html', {'form': form})

# edit tweet
def tweet_edit(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user=user.request.user) # get the tweet that we want to edit by using the get_object_or_404 function that takes the model and the primary key of the object the we want to get and it will return the object if it exists or return a 404 page of it doesn't exits  pk=tweet_id is the primary key of the tweet that we want to edit. user=request.user is used to make sure that the user that is currenlty logged in is the user that created the tweet. 
    if request.method == 'POST':
        form = TweetForm(request.POST, request.FILES, instance=tweet) # instance=tweet is used to populate the form with the tweet that we want to edit. 
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweet_list')
    else:
        form = TweetForm(instance=Tweet) # instance=tweet is used to populate the form with the tweet that we want to edit. 
    return render(request, 'apps/tweet_form.html', {'form': form})

# delete tweet
def tweet_delete(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user = request.user) # if form was not filled its give 404 error
    if request.method == 'POST':
        tweet.delete()
        return redirect('tweet_list')
    return render(request, 'apps/tweet_confirm_delete.html', {'tweet': tweet})

