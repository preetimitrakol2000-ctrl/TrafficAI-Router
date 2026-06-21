from city_graph import SmartCityGrid
from dijkstra_core import PathOptimizer
from traffic_updater import inject_camera_congestion_feed

if __name__ == "__main__":
    print("🚦 Launching Dense Adjacency Matrix SmartCity-Router Core...\n")

    city = SmartCityGrid(total_intersections=4)
    engine = PathOptimizer(intersections_count=4)

    print("🔍 Calculating Baseline Routing Time Map from Node [0]...")
    baseline_latencies = engine.calculate_optimal_route(city.matrix, starting_point=0)
    print(f"   👉 Standard Time Vector to Targets: {baseline_latencies}")

    # Simulate heavy traffic camera feed congestion updates between nodes 1 and 2
    print("\n📥 IoT Camera Notification: High Congestion Detected on Lane Link [1 <-> 2]!")
    inject_camera_congestion_feed(city, source=1, target=2, updated_latency=30)

    updated_latencies = engine.calculate_optimal_route(city.matrix, starting_point=0)
    print(f"   🔮 Recalculated Dynamic Time Vector: {updated_latencies}")
