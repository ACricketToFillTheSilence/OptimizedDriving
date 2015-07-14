# OptimizedDriving

Short Python script designed to return the shortest detour distance if one driver needed to pick up another driver before 
starting his/her route.

In the scenario for this function, Driver 1 is driving between points A and B. Driver 2 is driving between points C and D. 
The function returns the shorter of the two distances if one driver must detour to pick up and drop off the other driver 
before finishing his/her trip.

This is not strictly a shortest distance function because the starting point must either be point A or C and the ending point
must either be Point B or D. For this reason, the function only calculates the general pick-up (between points A and B), 
general drop-off (between points C and D), then compares the distance between A-B and C-D. The shorter of the two pairs will
give the optimal route, proven by Dijkstra's Algorithm. The function then adds pick-up, drop-off, and shortest pair together 
to give the shortest total detour time.
