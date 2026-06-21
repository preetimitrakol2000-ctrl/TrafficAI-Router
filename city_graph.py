class SmartCityGrid:
    def __init__(self, total_intersections=4):
        self.vertices = total_intersections
        # Adjacency Matrix tracking latency weights (0 = No Link, Value = Traversal Time in Seconds)
        self.matrix = [
            [0, 5, 12, 0],   # Intersection 0 links to 1 and 2
            [5, 0, 2, 25],   # Intersection 1 links to 0, 2, and 3
            [12, 2, 0, 4],   # Intersection 2 links to 0, 1, and 3
            [0, 25, 4, 0]    # Intersection 3 links to 1 and 2
        ]
