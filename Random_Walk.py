import random

#1.Solution for random walk:
def random_walk_1(n):
    """Returns coordiantes after 'n' block random walk."""
    x = 0
    y = 0
    for i in range(n):
        step = random.choice(["N","S","E","W"])
        if step == "N":
            y += 1
        elif step == "S":
            y -= 1
        elif step == "E":
            x += 1
        else:
            x -= 1
    return (x,y)

for i in range(25):
    walk = random_walk_1(10)
    print(walk, "Distance from home = ", abs(walk[0]) + abs(walk[1]))

#2.Solution for random walk:
def random_walk_2(n):
    """Returns coordiantes after 'n' block random walk."""
    x, y = 0, 0
    for i in range(n):
        (dx, dy) = random.choice([(0,1), (0,-1), (1,0), (-1,0)])
        x += dx
        y += dy
    return (x,y)

for i in range(25):
    walk = random_walk_2(10)
    print(walk, "Distance from home = ", abs(walk[0]) + abs(walk[1]))

#Monte Carlo for finding out what are the chances to end up 4 blocks away or less:
number_of_walks = 10000

for walk_length in range(1, 31):
    no_transport = 0 #Number of walks 4 blocks or fewer from home
    for i in range(number_of_walks):
        (x, y) = random_walk_2(walk_length)
        distance = abs(x) + abs(y)
        if distance <= 4:
            no_transport += 1
    no_transport_percentage = float(no_transport / number_of_walks)
    print("Walk size = ", walk_length, " / % of no transport = ", 100*no_transport_percentage)
