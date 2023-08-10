def calc_speed(r, vel):
    if   r[0] <= 0 and vel[0] < 0:
        return (-vel[0], vel[1])
    elif r[0] + Length >= Width and vel[0] > 0:
        return (-vel[0], vel[1])
    elif r[1] <= 0 and vel[1] < 0:
        return (vel[0], -vel[1])
    elif r[1] + 1 >= Height and vel[1] > 0:
        return (vel[0], -vel[1])
    else:
        return vel

Width, Height, Length = [int(x) for x in input().split()]
vel = (1,1)
r = (0,0)
steps = 100
positions = [r[0],r[1]]

for i in range(steps):
    r = (r[0] + vel[0], r[1] + vel[1])
    vel = calc_speed(r, vel)
    positions.append(r[0])
    positions.append(r[1])


print(' '.join([str(x) for x in positions]))

