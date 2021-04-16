states_needed = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])

stations = {}
stations["kone"] = set(["id", "nv", "ut"])
stations["ktwo"] = set(["wa", "id", "mt"])
stations["kthree"] = set(["or", "nv", "ca"])
stations["kfour"] = set(["nv", "ut"])
stations["kfive"] = set(["ca", "az"])

final_stations = set()

while len(states_needed) > 0:
    best_station = None
    states_covered = set()
    
    #поиск лучшей станции
    for key, value in stations.items():
        covered_by_station = states_needed & value
        if len(covered_by_station) > len(states_covered):
            best_station = key
            states_covered = value
        
    states_needed = states_needed - states_covered
    final_stations.add(best_station)

print(final_stations)