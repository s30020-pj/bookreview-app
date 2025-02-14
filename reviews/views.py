from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Book, Category, Review
from django.http import JsonResponse
from django.db.models import Q

def add_book_form(request):
    categories = Category.objects.all()
    return render(request, 'reviews/add_book.html', {'categories': categories})

def book_list(request):
    books = Book.objects.all().order_by('title')
    categories = Category.objects.all()
    selected_category = request.GET.get('category')
    search = request.GET.get('search')
    
    if selected_category:
        books = books.filter(categories__id=selected_category)

    if search:
        books = books.filter(
        Q(title__icontains=search) |
        Q(author__icontains=search)
        )
    
    paginator = Paginator(books, 6)  # Show 6 books per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'books': page_obj,
        'categories': categories,
        'selected_category': selected_category
    }
    return render(request, 'reviews/book_list.html', context)

def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    reviews = book.review_set.all().order_by('-created_at')
    
    # Add pagination
    paginator = Paginator(reviews, 4)  # Show 5 reviews per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'book': book,
        'reviews': page_obj
    }
    return render(request, 'reviews/book_detail.html', context)

def login(request):
    return render(request, 'registration/login.html')

@login_required
def add_review(request, book_id):
    if request.method == 'POST' and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        # Process the review
        review = Review.objects.create(
            book_id=book_id,
            user=request.user,
            rating=request.POST.get('rating'),
            text=request.POST.get('text')
        )
        
        # Calculate new average
        book = Book.objects.get(id=book_id)
        new_average = book.average_rating()
        
        return JsonResponse({
            'success': True,
            'user': request.user.username,
            'rating': review.rating,
            'text': review.text,
            'new_average': float(new_average)
        })
    
    return JsonResponse({'success': False})

@login_required
def add_book_submit(request):
    if request.method == 'POST':

        book = Book.objects.create(
            title=request.POST.get('title'),
            author=request.POST.get('author'),
            author_bio=request.POST.get('author_bio'),
            description=request.POST.get('description'),
        )

        categories = request.POST.getlist('categories')
        book.categories.set(categories)

        return redirect('reviews:book_list')
    
    else:
    
        return redirect('reviews:add_book_form')
