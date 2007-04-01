from django.shortcuts import redirect, render, get_object_or_404
from voiture.models import Voiture, Reviews
from .forms import ReviewsForm
from voiture.models import Reviews
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def createreview(request, voiture_id):
    voiture = get_object_or_404(Voiture,pk=voiture_id)
    if request.method == 'GET':
        return render(request, 'Reviews/create.html', {'form':ReviewsForm(), 'voiture': voiture})
    else:
        try:
            form = ReviewsForm(request.POST)
            newReview = form.save(commit=False)
            newReview.user = request.user
            newReview.voiture = voiture
            newReview.save()
            return redirect('voiture:detail', newReview.voiture.id)
        except ValueError:
            return render(request, 'Reviews/create.html', {'form':ReviewForm()})


@login_required
def updatereview(request, review_id):
    review = get_object_or_404(Reviews,pk=review_id,user=request.user)
    if request.method == 'GET':
        form = ReviewsForm(instance=review)
        return render(
            request, 
            'Reviews/create.html', 
            {'review': review,'form':form}
        )
    else:
        try:
            form = ReviewsForm(request.POST,
            instance=review)
            form.save()
            return redirect(
                'voiture:detail', 
                review.voiture.id
            )
        except ValueError:
            return render(
                request, 
                'Reviews/create.html',
                {'review': review,'form':form, 'error':'Bad data in form'}
            )


@login_required
def deletereview(request, review_id):
    review = get_object_or_404(Reviews, pk=review_id, user=request.user)
    review.delete()
    return redirect('voiture:detail', review.voiture.id)