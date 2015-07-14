import math

def calc_distance(origin, end):
	#calculates the distance between two tuples that represent 
	#Cartesian points
	x1, y1 = origin[0], origin[1]
	x2, y2 = end[0], end[1]

	dist = math.sqrt(float(pow(x1-x2,2)+pow(y1-y2,2)))

	return dist


def find_faster_route(first_or, first_dest, second_or, second_dest):
	#This function takes advantage of the fact that the distance
	#between both drivers' origins and their destinations will be the
	#same; all that differs is the length between each one's origin and
	#destination.

	#Note: all four variables must be 2-tuples representing the
	#Latitude/Longitude pairs of the starting and ending points for the
	#two drivers.

	pick_up = calc_distance(first_or, second_or)
	drop_off = calc_distance(second_dest, first_dest)

	first_distance = calc_distance(first_or, first_dest)
	second_distance = calc_distance(second_or, second_dest)

	shortest_path = (min(first_distance, second_distance))

	shortest_path += pick_up
	shortest_path += drop_off

	return shortest_path



#Test case

# d1_origin = (1,6)
# d1_destination = (9,0)

# d2_origin = (0,3)
# d2_destination = (3,8)


# print "faster route: ", find_faster_route(d1_origin, d1_destination, d2_origin, d2_destination)