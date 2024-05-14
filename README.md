# Paltech-Challenge

## Part 1

### Initial thinking

Need to stich images, determine angle of one, determine distance (know distance to something with z, but what?)
Using a point we can determine angle from there, assuming images stiched together, if groups need a point in each group
To calc angle from angle->if images stiched together can treat pixels as equal distance, if can treat pixels as equal distance then it's just a sphere, counting pixels gives arc length, if have distance (radius) then we have angle from simple math

How do I know distance? drone goes down slowly until it reaches the ground, we know z of this place
Images not in same place->drone moves between images but me know where it took the image in each case.
Let's say we know for one image the angle and distance, using simple math we can determine everything.
For image img->img pos is known, img0 angle and img0 pos are known. movement between pos can be modeled as a straight line, from a triangle->dist to img, dist to img0 and pos_mov, two are known,  I can use angle0 and pos_mov to determine an angle of the triangle, this allows the use of cosines to determine the other side, if we can determine the dist to the second image we have the angle through cosines. Through the stich I have a pixel distance from one image to the next.

### Solution

Image stitching is mostly unchanged from what would normally be done, this includes the fact that a homography matrix can be computed without the rotation (see [5](https://www.cse.psu.edu/~rtc12/CSE486/lecture16.pdf)). The orientation is calculated by assigning the rotation matrix I to one image and solving for the other rotation matrix iteratively in each pair of images.

### Details to consider

Image orientation is from one image, which has been arbitrarily assigned a direction.

### Files

design_question.md includes detailed information of what steps to execute to solve the problem. It is divided in three steps:

1. Extracting information to find common points in images.
2. Identifying common points, transforming images and stiching them together.
3. Calculatin image orientation.

## Part 2

### Initial thinking

First step->are they numbers?
Second step->checking if/where the ray intersects the 'plane'
For step two->get equation, if any point of the plane satisfies the equation then they intersect. Binary search could work if I can use it to determine where I am in relation to the ray. Given the center->ray towards the center, compare with the one I have, compare orientation, I now know the direction to reach it, binary search in that direction, if angles match then we have found the point, if I reach the end and it's away they don't intersect.

### Solution

Using binary search on points sorted according to the sum of their x and y points, we compare the vector between the origin point and a point in the plane with the vector, using this comparison to determine where to search next.

### Assumptions

The DEM data does not have a high gradient. This means we don't have a very steep wall rising suddenly.

For cases that do not meet this assumption it might be possible to add z to the size comparison and sorting.

Points not specified in DEM are not considered to be valid answers, if we want to add this we could simply add an error range to the comparison between vectors, allowing the method to return True if the vectors are close enough to one another.

### Details to consider

Checking if the ray can intersect with the plane was considered the same as checking if there was an intersection with the plane. We cannot eliminate a vector if it is parallel as it could quite simply be part of the plain or have a common height.

Only library used is sys, as it is required to read inputs, however this library is included in Python installations.

Expected range was not considered as I don't know what the expected range was.

### Files

terrain_mapping.py is the Python code which solves the problem.
