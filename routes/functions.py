from .models import Airport, AirportRoute
from .models import AirportRoute


def find_nth_node(airport_code, direction, n):
    """
    Find Nth left or right child from a given airport
    """
    try:
        current_airport = Airport.objects.get(code=airport_code)
    except Airport.DoesNotExist:
        return None

    for _ in range(n):
        route = AirportRoute.objects.filter(
            parent_airport=current_airport,
            position=direction
        ).select_related('child_airport').first()

        if not route:
            return None

        current_airport = route.child_airport

    return current_airport

def get_longest_route():
    """
    Find route with maximum duration
    """
    return AirportRoute.objects.order_by('-duration').first()


def find_shortest_path(start_airport, end_airport, visited=None):
    """
    DFS-based shortest path
    """
    if visited is None:
        visited = set()

    if start_airport == end_airport:
        return 0

    visited.add(start_airport)
    shortest_distance = None

    routes = AirportRoute.objects.filter(parent_airport=start_airport)

    for route in routes:
        if route.child_airport not in visited:
            sub_distance = find_shortest_path(
                route.child_airport, end_airport, visited
            )
            if sub_distance is not None:
                total = route.duration + sub_distance
                if shortest_distance is None or total < shortest_distance:
                    shortest_distance = total

    return shortest_distance



def build_route_tree():
    """
    Builds a tree-like structure of airport routes
    """
    routes = AirportRoute.objects.select_related(
        'parent_airport', 'child_airport'
    )

    tree = {}

    for route in routes:
        parent = route.parent_airport.code
        child = route.child_airport.code

        if parent not in tree:
            tree[parent] = []

        tree[parent].append({
            'child': child,
            'position': route.position,
            'duration': route.duration
        })

    return tree
