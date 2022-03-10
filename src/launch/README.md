Launch file
	1) move.launch
	This file represents the code for running:
		a) Turtlebot3 Burger running in Gazebo in circles of defined radius
		b) Turtlebot3 Burger running in Gazebo an open loop square of defined side length
	The file launches the turtlebot burger in an empty gazebo world as written in the following command: "<include file="$(find turtlebot3_gazebo)/launch/turtlebot3_empty_world.launch"/>"
	
	To run the turtlebot in circles, the following command should be used in terminal window:
	"roslaunch assignment3_turtlebot3 move.launch code:=circle"
	Where assignment3_turtlebot3 is the package inside which we have move.launch file which will run code circle.py once circle is entered in the code
	
	To run the turtlebot in the square, the following command should be used in terminal window:
	"roslaunch assignment3_turtlebot3 move.launch code:=square"
	Where assignment3_turtlebot3 is the package inside which we have move.launch file which will run code square_openloop.py once "square" is entered in the code
	
	
	2) Obstacle.launch
	
	This file represents the launch code for stopping a running turtlebot once it reaches to a safe distance before the wall
	The command to execute it is:
	"roslaunch assignment3_turtlebot3 obstacle.launch"
	Where assignment3_turtlebot3 is the package inside which obstacle.launch file will run the code obs.py which would ultimately run turtlebot in a straight line until a safe distance to the wall is reached
