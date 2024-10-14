Given a box of particle we want to find the minimum distance between 2 of them. 
Standard algorithm would be to compute al the distances between couples of 
particles and sort them. This scales as O(N^2). 

Another approach is to compute for every particle only the neighbors who are inside a specific 
distance. This approach scales again as O(N^2), but has a much smaller prefactor as can be seen in the plot. 
