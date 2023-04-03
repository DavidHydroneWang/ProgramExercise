#!/usr/bin/env python
# coding=utf-8
import math
import random

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __lt__(self,other):
        self_mag = (self.x ** 2) + (self.y ** 2)
        other_mag = (other.x ** 2) + (other.y ** 2)
        return self_mag < other_mag

    def distance(self, other):
        res = math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)
        return res

class Element:
    def __init__(self, points=None, neighbors=None, edges=None):
        self.points = [] if points is None else points
        self.neighbors = [] if neighbors is None else neighbors
        self.edges = [] if edges is None else edges

    def add_point(self, point):
        self.points.append(point)

    def add_neighbor(self, neighbor):
        self.neighbors.append(neighbor)

    def get_edge(self):
        for x, y in zip(self.points, self.points[1:] + [self.points[0]]):
            if x > y:
                x, y = y, x
            self.edges.append((x, y))
        return self.edges


class Mesh:
    def __init__(self, points=None, elements=None):
        self.points = [] if points is None else points
        self.elements = [] if elements  is None else elements

    def add_point(self, point):
        self.points.append(point)

    def add_element(self, element):
        self.elements.append(element)


class ColorMesh:
    def __init__(self, points=None, elements=None):
        self.points = [] if points is None else points
        self.elements = [] if elements  is None else elements

    def add_point(self, point):
        self.points.append(point)

    def add_element(self, element):
        self.elements.append(element)


def find_neighbors(mesh):
    #all_elements = mesh.elements
    #print(all_elements)
    for e1 in mesh.elements:
        #temp = all_elements[:]
        #emp = temp.remove(e1)
        #print(temp)
        for e2 in mesh.elements:
            if e1 is not e2:
                #print(e1, e2)
                #print(set(e2.get_edge()))
                #print(set(e1.get_edge()) )
                if set(e1.get_edge()) & set(e2.get_edge()) != set():
                    e1.add_neighbor(e2)

def print_matrix(mesh):
    n = 10
    matrix = [[0] * n ] * n
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j:
                res = 0
                point = mesh.points[i - 1]
                for e in mesh.elements:
                    for t in e.get_edge():
                        if point in t:
                            res += 1
                            break
                #print(res)
                matrix[i - 1][i - 1] = res
            else:
                p1 = mesh.points[i - 1]
                p2 = mesh.points[j - 1]
                if p1 > p2 :
                    p1, p2 = p2, p1
                for e in mesh.elements:
                    if (p1, p2) in e.get_edge():
                        matrix[i - 1][j - 1] = p1.distance(p2)
    for i in range(n):
        for j in range(n):
            print(matrix[i][j])


def find_element_with_three_or_more_color(colormesh):
    res = []
    for element in colormesh.elements:
        temp = set()
        for point in element.points:
            temp.add(point.color)
        if len(temp) >= 3:
            res.append(element)
    return res


def two_to_line(point1, point2):
    x1 = point1.x
    y1 = point1.y
    x2 = point2.x
    y2 = point2.y

    if x1==x2:
        return (0, x1)
    if y1==y2:
        return (1, y1)
    else:
        k = (y1-y2)/(x1-x2)
        b = y1 - k*x1
        return (2, k, b)

def is_convex(element):

    convex = True
    length = len(element.points)

    for i in range(length):
        pre = i
        nex = (i+1) % length

        line = two_to_line(element.points[pre], element.points[nex])

        if line[0]==0:
            offset = [point.x - element.points[pre].x for point in element.points]
        elif line[0]==1:
            offset = [point.y - element.points[pre].y for point in element.points]
        else:
            k, b = line[1], line[2]
            offset = [k * point.x + b - point.y for point in element.points]

        for o in offset:
            for s in offset:
                if o*s < 0:
                    convex = False
                    break
            if convex == False:
                break

        if convex == False:
            break

    return convex

if __name__ == '__main__':
    P1 = Point(0.0, 4.0)
    P2 = Point(4.0, 4.0)
    P3 = Point(4.0, 2.0)
    P4 = Point(4.0, 0.0)
    P5 = Point(2.0, 0.0)
    P6 = Point(0.0, 0.0)
    P7 = Point(1.0, 1.0)
    P8 = Point(2.0, 2.0)
    P9 = Point(3.0, 1.0)
    P10 = Point(3.0, 3.1)
    E1 = Element(points=[P1, P2, P10, P8, P7, P6])
    E2 = Element(points=[P2, P3, P9, P10])
    E3 = Element(points=[P3, P4, P6, P7, P8, P9])
    E4 = Element(points=[P5, P6, P7])
    E5 = Element(points=[P8, P9, P10])
    # M = Mesh()
    M = Mesh(points=[P1, P2, P3, P4, P5, P6, P7, P8, P9, P10], elements=[E1, E2, E3, E4, E5])
#1.
    find_neighbors(M)
    print(M.elements)
    print(E1.neighbors)
    print(E2.neighbors)
    print(E3.neighbors)
    print(E4.neighbors)
    print(E5.neighbors)

# 2.
    print_matrix(M)

# 3.
    CM = ColorMesh(points=[P1, P2, P3, P4, P5, P6, P7, P8, P9, P10], elements=[E1, E2, E3, E4, E5])
    for point in CM.points:
        color = random.randint(1, 3)
        point.color = color
    for point in M.points:
        print(point.color)
    print(find_element_with_three_or_more_color(CM))
# 4.
    for element in M.elements:
        print(is_convex(element))
