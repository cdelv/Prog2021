import math

def R_perp(theta,ni=1.0, nt=1.7):
	theta = theta*(math.pi/180)
	thetat = math.asin(ni*math.sin(theta)/nt)
	return ((ni*math.cos(theta)-nt*math.cos(thetat))/(ni*math.cos(theta)+nt*math.cos(thetat)))**2

def R_par(theta,ni=1.0, nt=1.7):
	theta = theta*(math.pi/180)
	thetat = math.asin(ni*math.sin(theta)/nt)
	return ((nt*math.cos(theta)-ni*math.cos(thetat))/(nt*math.cos(theta)+ni*math.cos(thetat)))**2

def ang_vibra(theta, ni=1.0, nt=1.7):
	a = math.atan(math.sqrt(R_perp(60, ni, nt)/R_par(60, ni, nt)))
	return a*180/math.pi

print(ang_vibra(60))