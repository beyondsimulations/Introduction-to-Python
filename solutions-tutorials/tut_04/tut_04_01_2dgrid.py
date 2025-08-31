# TODO: Calculate distances in 2 dimensions
# - You are working with tuples representing points in 2D space (x, y).
# - Write a function that takes a tuple and returns the distance from the origin (0, 0).
# - Create a list of 5 tuples representing multiple points and calculate the distance for each point.
# - Create a function that takes a list of tuples and returns the point that is farthest from the origin.
# - Print the result to the console.

def calculate_distance(point):
    x, y = point
    return (x**2 + y**2)**0.5

def find_farthest_point(points):
   max_distance = 0
   farthest_point = None
   for point in points:
       distance = calculate_distance(point)
       if distance > max_distance:
           max_distance = distance
           farthest_point = point
   return farthest_point

points = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]

farthest_point = find_farthest_point(points)
print(f"The point farthest from the origin is {farthest_point}")
