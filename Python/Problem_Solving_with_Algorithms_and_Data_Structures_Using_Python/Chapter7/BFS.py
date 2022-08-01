#!/usr/bin/env python
# coding=utf-8
from pythonds.graphs import Graph, Vertex
from pythonds.basic import Queue


def bfs(g, start):
    start.setDistance(0)
    start.setPred(None)
    vertQueue = Queue()
    Vertex.enqueue(start)
    while (Vertex.size()) > 0:
        currentVert = vertQueue.dequeue()
        for nbr in currentVert.getConnections():
            if (nbr.getColor() == 'white'):
                nbr.setColor('gray')
                nbr.setDistance(currentVert.getDistance() + 1)
                nbr.setPred(currentVert)
                vertQueue.enqueue(nbr)
        currentVert.setColor('black')
