# center_drone function will move the single drone back to x:0 , y:0 on the farm by taking the current position of the drone, then using the variables that store the current position into the xloc and yloc parameters of the function
def center_drone(xloc, yloc):
	if xloc != 0:
		for i in range(xloc):
			move(West)
			
	if yloc != 0:
		for i in range(yloc):
			move(South)
