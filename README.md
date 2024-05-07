# Paltech-Challenge

## Part 1
Need to stich images, determine angle of one, determine distance (know distance to something with z, but what?)
Using a point we can determine angle from there, assuming images stiched together, if groups need a point in each group
To calc angle from angle->if images stiched together can treat pixels as equal distance, if can treat pixels as equal distance then it's just a sphere, counting pixels gives arc length, if have distance (radius) then we have angle from simple math

How do I know distance? drone goes down slowly until it reaches the ground, we know z of this place
Images not in same place->drone moves between images but me know where it took the image in each case.
Let's say we know for one image the angle and distance, using simple math we can determine everything.
For image img->img pos is known, img0 angle and img0 pos are known. movement between pos can be modeled as a straight line, from a triangle->dist to img, dist to img0 and pos_mov, two are known,  I can use angle0 and pos_mov to determine an angle of the triangle, this allows the use of cosines to determine the other side, if we can determine the dist to the second image we have the angle through cosines. Through the stich I have a pixel distance from one image to the next.

## Part 2
First step->are they numbers?
Second step->checking if/where the ray intersects the 'plane'
For step two->get equation, if any point of the plane satisfies the equation then they intersect. Binary search could work if I can use it to determine where I am in relation to the ray. Given the center->ray towards the center, compare with the one I have, compare orientation, I now know the direction to reach it, binary search in that direction, if angles match then we have found the point, if I reach the end and it's away they don't intersect.
