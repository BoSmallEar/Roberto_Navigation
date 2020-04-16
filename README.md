0. Clone roberto_navigation and roberto-arm-pickup under the same catkin workspace, source setup.sh, run catkin_make

1. roscore

2. Start rviz, gazebo environment

roslaunch roberto_test_navigation start_navigation.launch

3. Start localization & ik_planner

roslaunch roberto_test_navigation initialize_navigation.launch

4. Edit data/path.txt, complete the path

roslaunch roberto_test_navigation goal_publisher.launch

5. Give goal to robot arm (replace x,y,z with values such as 0.4 -0.3 0.5)

rosrun roberto_ik_planner talker.py x y z 0 0 0      
