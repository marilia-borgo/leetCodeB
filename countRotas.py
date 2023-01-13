# https://leetcode.com/problems/count-all-possible-routes/


def rotas_possiveis(curr_city, destination, curr_fuel, cities):
    if curr_fuel < 0:
        return 0
    route_count = 0
    if curr_city == destination:
        route_count =+1
    
    for next_city in range(len(cities)):
        if next_city != curr_city:
            cost = abs(cities[curr_city] - cities[next_city])
            route_count += rotas_possiveis(next_city, destination,curr_fuel-cost, cities)
    return route_count

def solution_1(cities, start,destination, fuel):
    return rotas_possiveis(start, destination, fuel, cities)

solution_1([2,3,6,8,4],0,2,10)   


