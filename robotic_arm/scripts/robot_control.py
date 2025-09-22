import sys
import rospy
import moveit_commander
import moveit_msgs.msg
from math import pi

moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node('move_robot', anonymous=True)

robot = moveit_commander.RobotCommander()
scene = moveit_commander.PlanningSceneInterface()

def move_robot_arm(joint1, joint2, joint3, joint4, joint5, joint6):
    group_name = "robot_arm"  # Replace with your arm's group name
    group = moveit_commander.MoveGroupCommander(group_name)

    joint_goal = group.get_current_joint_values()
    joint_goal[0] = joint1
    joint_goal[1] = joint2
    joint_goal[2] = joint3
    joint_goal[3] = joint4
    joint_goal[4] = joint5
    joint_goal[5] = joint6

    group.go(joint_goal, wait=True)
    group.stop()

def move_end_effector(joint1, joint2):
    group_name = "hand_ee"  # Replace with your end effector's group name
    group = moveit_commander.MoveGroupCommander(group_name)

    joint_goal = group.get_current_joint_values()
    joint_goal[0] = joint1
    joint_goal[1] = joint2

    group.go(joint_goal, wait=True)
    group.stop()


def main():
	move_end_effector(-0.1243,0.2075)
	rospy.sleep(1)
	move_robot_arm(-0.6849,-0.5,0.1758,1.5377,-0.8722,-1.4085)
	rospy.sleep(1)
	move_end_effector(0.2709,-0.2501)
	rospy.sleep(1)
	move_robot_arm(-1.1759,0.1985,-3.0685,1.3568,-1.57,-1.2534)
	rospy.sleep(1)
	
if __name__ == '__main__':
    while True:
        main()

