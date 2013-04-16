from point.models import Point

points=Point.objects.all().order_by('position')
for point in points:
    print point.position
