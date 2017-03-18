cmake_minimum_required(VERSION 2.8.3)
project(motion_camera_ros)

# add_definitions(-std=c++11)

find_package(catkin REQUIRED COMPONENTS
  rospy
  roslint
)

## System dependencies are found with CMake's conventions
# find_package(Boost REQUIRED COMPONENTS system)

catkin_python_setup()

# add_message_files(
#   FILES
#   Message1.msg
# )

## Generate services in the 'srv' folder
# add_service_files(
#   FILES
#   Service1.srv
# )

## Generate actions in the 'action' folder
# add_action_files(
#   FILES
#   Action1.action
# )

## Generate added messages and services with any dependencies listed here
# generate_messages(
#   DEPENDENCIES
#   std_msgs  # Or other packages containing msgs
# )

## Generate dynamic reconfigure parameters in the 'cfg' folder
# generate_dynamic_reconfigure_options(
#   cfg/DynReconf1.cfg
# )

catkin_package(
    CATKIN_DEPENDS
        rospy
)

roslint_python()

## Install ##
install(PROGRAMS
    ros/scripts/motion_camera_node
    DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

## Testing ##

