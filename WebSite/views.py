from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Sum, Avg, Max, Min, Count, Q
from .models import Soda, Mugs, Figurines, Toys, Order, StudentProfile, EducationalProgram, ProgramManagement, Classmate
from .forms import OrderForm


def home(request):
    return render(request, "home.html")


def character_list(request):
    return render(request, "characters_list.html")


def get_anime(request):
    return render(request, "show_anime.html")


def get_manga(request):
    return render(request, "show_manga.html")


def get_shop(request):
    toy_name = request.GET.get('toy_name', '')
    toy_max_price = request.GET.get('toy_max_price', '')
    toy_sort = request.GET.get('toy_sort', '')
    toys = Toys.objects.all()
    if toy_name:
        toys = toys.filter(name__icontains=toy_name)
    if toy_max_price:
        toys = toys.filter(price__lte=toy_max_price)
    if toy_sort == 'asc':
        toys = toys.order_by('price')
    elif toy_sort == 'desc':
        toys = toys.order_by('-price')


    fig_name = request.GET.get('fig_name', '')
    fig_max_price = request.GET.get('fig_max_price', '')
    fig_sort = request.GET.get('fig_sort', '')
    figurines = Figurines.objects.all()
    if fig_name:
        figurines = figurines.filter(name__icontains=fig_name)
    if fig_max_price:
        figurines = figurines.filter(price__lte=fig_max_price)

    if fig_sort == 'asc':
        figurines = figurines.order_by('price')
    elif fig_sort == 'desc':
        figurines = figurines.order_by('-price')


    mug_name = request.GET.get('mug_name', '')
    mug_max_price = request.GET.get('mug_max_price', '')
    mug_sort = request.GET.get('mug_sort', '')
    mugs = Mugs.objects.all()
    if mug_name:
        mugs = mugs.filter(name__icontains=mug_name)
    if mug_max_price:
        mugs = mugs.filter(price__lte=mug_max_price)
    if mug_sort == 'asc':
        mugs = mugs.order_by('price')
    elif mug_sort == 'desc':
        mugs = mugs.order_by('-price')

    soda_name = request.GET.get('soda_name', '')
    soda_max_price = request.GET.get('soda_max_price', '')
    soda_sort = request.GET.get('soda_sort', '')
    soda = Soda.objects.all()
    if soda_name:
        soda = soda.filter(name__icontains=soda_name)
    if soda_max_price:
        soda = soda.filter(price__lte=soda_max_price)
    if soda_sort == 'asc':
        soda = soda.order_by('price')
    elif soda_sort == 'desc':
        soda = soda.order_by('-price')

    context = {
        'data': {
            'toys': toys,
            'figurines': figurines,
            'mugs': mugs,
            'soda': soda,
            'filters': {
                'toy_name': toy_name,
                'toy_max_price': toy_max_price,
                'toy_sort': toy_sort,
                'fig_name': fig_name,
                'fig_max_price': fig_max_price,
                'fig_sort': fig_sort,
                'mug_name': mug_name,
                'mug_max_price': mug_max_price,
                'mug_sort': mug_sort,
                'soda_name': soda_name,
                'soda_max_price': soda_max_price,
                'soda_sort': soda_sort,
            }
        }
    }
    return render(request, 'shop.html', context)


def get_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            product = request.POST.get('product')
            price = request.POST.get('price')

            if product and price:
                Order.objects.create(
                    customer_name=form.cleaned_data['customer_name'],
                    email=form.cleaned_data['email'],
                    product=product,
                    price=price
                )
                form = OrderForm()
                message = "Спасибо! Ваш заказ успешно оформлен."

    product = request.GET.get('product') or request.POST.get('product')
    price = request.GET.get('price') or request.POST.get('price')

    if request.method == 'GET' and not product and not request.GET.get('email') and not request.GET.get('sort'):
        return redirect('WebSite:get_shop')

    sort = request.GET.get('sort', '-created_at')
    orders = Order.objects.all().order_by(sort)

    if request.GET.get('email'):
        orders = orders.filter(email__icontains=request.GET['email'])

    if request.GET.get('customer_name'):
        orders = orders.filter(customer_name__icontains=request.GET['customer_name'])

    if request.GET.get('email'):
        orders = orders.filter(email__icontains=request.GET['email'])

    initial_data = {}
    if request.method == 'GET':
        initial_data = {
            'product': product,
            'price': price
        }

    order_stats = {
        'total_orders': orders.count(),
        'total_revenue': orders.aggregate(Sum('price'))['price__sum'] or 0,
        'avg_order': orders.aggregate(Avg('price'))['price__avg'] or 0,
        'max_order': orders.aggregate(Max('price'))['price__max'] or 0,
        'min_order': orders.aggregate(Min('price'))['price__min'] or 0,
    }


    context = {
        'product': product,
        'price': price,
        'form': OrderForm(initial=initial_data),
        'orders': orders,
        'order_stats': order_stats,
        'message': locals().get('message', '')
    }

    return render(request, 'order.html', context)

def hse_studies_main(request):
    return render(request, 'hse_studies.html')

def my_profile(request):
    profile = get_object_or_404(StudentProfile, pk=1)  # or use your logic to get the profile
    return render(request, 'my_profile.html', {'profile': profile})

def educational_program(request):
    program = get_object_or_404(EducationalProgram, pk=1)
    return render(request, 'educational_program.html', {'program': program})

def program_management(request):
    program = get_object_or_404(EducationalProgram, pk=1)
    management = ProgramManagement.objects.filter(program=program)

    return render(request, 'program_management.html', {
        'program': program,
        'management': management
    })

def classmates(request):
    program = get_object_or_404(EducationalProgram, pk=1)
    classmates = Classmate.objects.filter(program=program)
    search_query = request.GET.get('search', '')
    if search_query:
        classmates = classmates.filter(
            Q(full_name__icontains=search_query[0:1].upper()) |
            Q(email__icontains=search_query[0:1].upper()) |
            Q(phone__icontains=search_query[0:1].upper())
        )

    sort = request.GET.get('sort', 'full_name')
    valid_sorts = ['full_name', '-full_name', 'email', '-email']
    sort = sort if sort in valid_sorts else 'full_name'
    classmates = classmates.order_by(sort)

    context = {
        'program': program,
        'classmates': classmates,
        'search_query': search_query,
        'current_sort': sort,
    }
    return render(request, 'classmates.html', context)


#-----------------------------------------------------------------------------------------------

def objects_arrays(request):
    return render(request, 'objects_array.html')

def artworks_within_budget(artworks, budget):
    affordable_artworks = []

    for artwork in artworks:
        name_price = artwork.rsplit(' - ', 1)
        if len(name_price) != 2:
            continue

        name, price = name_price
        try:
            price = int(price)

        except ValueError:
            continue

        if price % budget == 0:
            affordable_artworks.append(name.strip())

    return sorted(affordable_artworks)


def get_affordable_artworks(request, artworks, budget):
    artworks_list = artworks.split(',')
    affordable_artworks = artworks_within_budget(artworks_list, budget)

    return render(request, 'task.html', {
        'affordable_artworks': affordable_artworks,
        'budget': budget})
