import csv
import random
import math 




def get_places_csv(file):
    places = []
    with open(file) as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            places.append(row)
    return places
    
def get_random_places(n):
    places = []
    for i in range(n):
        places.append(["place{}".format(i), random.uniform(-90, 90), random.uniform(-180, 180)])
    return places    
    
def get_distances(places):
    distances = []
    for i, place1 in enumerate(places):
        for j, place2 in enumerate(places[i+1:]):
            if place1 == place2:
                continue
            distances.append((google_formula(float(place1[1]), float(place1[2]), float(place2[1]), float(place2[2])), place1[0], place2[0]))
    return distances
    
def google_formula(lat1, lon1, lat2, lon2): #used google to get the formula 
    R = 6371  
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
    dlat = int(lat2 - lat1)
    dlon = int(lon2 - lon1)
    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.asin(math.sqrt(a))
    return R * c

def distances_order(distances):
        for distance, place1, place2 in sorted(distances, key=lambda x: x[0]):
            print("{} - {} {:.1f} km\n".format(place1, place2, distance))


def main (n=None):
    if n!=None:
       places = get_random_places(n)
    else:
         places = get_places_csv("places.csv")
   
    distances = get_distances(places)
    total_distance = sum(d[0] for d in distances)
    avg_distance = total_distance / len(distances)
    closest_pair = min(distances, key=lambda x: abs(x[0] - avg_distance))
    order = distances_order(distances)
    
   
    print("Average distance: {:.1f} km. Closest pair: {} - {} {:.1f} km.".format(
            avg_distance, closest_pair[1], closest_pair[2], closest_pair[0]
        ))
    

if __name__ == "__main__":
    main()
    