#!/usr/bin/env python3
import csv, heapq, math

def dino_speed(stride_length, leg_length, g):
    return ((stride_length / leg_length) - 1) * math.sqrt(leg_length * g)

def dino(d1, d2):
    x, pq = {}, []
    with open(d1) as f:
        f_reader = csv.reader(f)
        for e in f_reader:
            x[e[0]] = [float(e[1]), e[2]]
    with open(d2) as f:
        f_reader = csv.reader(f)
        for e in f_reader:
            if e[0] in x:
                e_stats = x[e[0]]
                e_stats.append(e[-1])
                e_stats[0] = dino_speed(float(e[1]), e_stats[0], 9.8)
                x[e[0]] = e_stats
    for k,v in x.items():
        if v[-1] == 'bipedal':
            heapq.heappush(pq, (v[0], k))
    while pq:
        print(heapq.heappop(pq)[1])
    return 'done'

dino('ds1.csv', 'ds2.csv')