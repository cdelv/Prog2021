import math as m

def f(x, y, A, B, C):
	return (x - A)**2 + (y - B)**2 + C * m.exp(- (x + A)**2 - (y + B)**2)
	
def gradient(x, y, A, B, C, dt):
	df_dx = (f(x + dt, y, A, B, C) - f(x, y, A, B, C)) / dt
	df_dy = (f(x, y + dt, A, B, C) - f(x, y, A, B, C)) / dt
	return df_dx, df_dy

def gradient_direnction(x, y, A, B, C, dt = 1e-9):
    df_dx, df_dy = gradient(x, y, A, B, C, dt)
    angle = m.atan2(-df_dy, -df_dx)
    if angle < 0:
        angle += 2 * m.pi
    return round(m.degrees(angle))

N, A, B, C = map(float, input().split())
answer = []

for i in range(int(N)):
	x, y = map(float, input().split())
	answer.append(gradient_direnction(x, y, A, B, C))

print(' '.join([str(x) for x in answer]))
