from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .forms import AirportRouteForm, NthNodeSearchForm, ShortestPathForm, AirportForm
from .models import Airport
from .services import (
    find_nth_node,
    get_longest_route,
    find_shortest_path,
    build_route_tree,
    
)

# def add_airport_route(request):
#     form = AirportRouteForm(request.POST or None)

#     if form.is_valid():
#         form.save()

#     return render(request, 'add_route.html', {'form': form})

def add_airport_route(request):
    form = AirportRouteForm(request.POST or None)

    if form.is_valid():
        form.save()

    tree = build_route_tree()

    return render(request, 'add_route.html', {
        'form': form,
        'tree': tree
    })

def nth_node_view(request):
    result = None
    form = NthNodeSearchForm(request.POST or None)

    if form.is_valid():
        result = find_nth_node(
            form.cleaned_data['airport_code'],
            form.cleaned_data['direction'],
            form.cleaned_data['n']
        )

    return render(request, 'nth_node.html', {
        'form': form,
        'result': result
    })


def longest_node_view(request):
    route = get_longest_route()
    return render(request, 'longest_node.html', {'route': route})


def shortest_path_view(request):
    distance = None
    form = ShortestPathForm(request.POST or None)

    if form.is_valid():
        start = Airport.objects.get(code=form.cleaned_data['source'])
        end = Airport.objects.get(code=form.cleaned_data['destination'])
        distance = find_shortest_path(start, end)

    return render(request, 'shortest_path.html', {
        'form': form,
        'distance': distance
    })


def add_airport(request):
    form = AirportForm(request.POST or None)

    if form.is_valid():
        form.save()
        form = AirportForm()  # reset form after save

    return render(request, 'add_airport.html', {
        'form': form
    })
