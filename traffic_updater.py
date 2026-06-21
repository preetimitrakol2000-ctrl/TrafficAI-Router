def inject_camera_congestion_feed(city_grid, source, target, updated_latency):
    city_grid.matrix[source][target] = updated_latency
    city_grid.matrix[target][source] = updated_latency
