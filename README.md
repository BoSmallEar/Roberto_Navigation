1. roscore

2. Start rviz, gazebo environment

roslaunch roberto_test_navigation start_navigation.launch

3. Start localization 

roslaunch roberto_test_navigation initialize_navigation.launch

4. Edit data/path.txt, complete the path

roslaunch roberto_test_navigation goal_publisher.launch
