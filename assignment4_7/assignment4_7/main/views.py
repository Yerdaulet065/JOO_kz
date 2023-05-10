from django.shortcuts import render, get_object_or_404, redirect
from .models import Review


def MainPage(request):
    reviews = Review.objects.all()

    count_of_reviews = reviews.count()
    rating = 0
    for review in reviews:
        rating += review.rating

    rating = float(str(round((rating / count_of_reviews), 1)))

    context = {
        'reviews': reviews,
        'rating': rating,
        'count_of_reviews': count_of_reviews
    }

    return render(request, 'main/home.html', context)


def CreatePage(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        rating = request.POST['rating']
        img = request.FILES['image']

        Review.objects.create(author=request.user, title=title, description=description, rating=rating, img=img).save()
        return redirect('/')

    return render(request, 'main/create.html')


def UpdatePage(request, pk):
    review = get_object_or_404(Review, id=pk)

    if request.POST:
        review.author = request.user
        review.title = request.POST.get('title')
        review.description = request.POST.get('description')
        review.rating = request.POST.get('rating')
        review.date = request.POST.get('date')
        review.img = request.FILES.get('image')
        review.save()
        return redirect('/')

    context = {
        'review': review,
    }

    return render(request, 'main/update.html', context)


def DeletePage(request, pk):
    review = get_object_or_404(Review, id=request.POST.get('review_id'))
    Review.objects.filter(id=review.id).delete()
    return redirect('/')