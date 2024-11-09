import sys
import copy
import rospy
from moveit_commander import MoveGroupCommander, RobotCommander, roscpp_initialize, PlanningSceneInterface
import moveit_msgs.msg
from math import pi, tau, dist, fabs, cos
from std_msgs.msg import String
from moveit_commander.conversions import pose_to_list
from typing import List
from geometry_msgs.msg import Pose, PoseStamped
from control_msgs.msg import GripperCommandAction, GripperCommandGoal, GripperCommandResult
from actionlib import SimpleActionClient

class ControlRobot:
    def __init__(self) -> None:
        roscpp_initialize(sys.argv)
        ##rospy.init_node("control_robot", anonymous=True)
        self.robot = RobotCommander()
        self.scene = PlanningSceneInterface()
        self.group_name = "robot"
        self.move_group = MoveGroupCommander(self.group_name)
        self.gripper_action_client = SimpleActionClient("rg2_action_server", GripperCommandAction)
        self.add_floor()

    def get_motor_angles(self) -> list:
        return self.move_group.get_current_joint_values()
    
    def move_motors(self, joint_goal: List[float], wait: bool= True) -> bool:
        return self.move_group.go(joint_goal, wait=wait)
    
    def get_pose(self) -> Pose:
        return self.move_group.get_current_pose().pose
    
    def move_to_pose(self, pose_goal: Pose, wait: bool=True) -> bool:
        self.move_group.set_pose_target(pose_goal)
        return self.move_group.go(wait=wait)
    
    def add_box_to_planning_scene(self, pose_caja: Pose, name: str,
                                  tamaño: tuple = (.1,.1,.1)) -> None:
        box_pose = PoseStamped()
        box_pose.header.frame_id = "base_link"
        box_pose.pose = pose_caja
        box_name = name
        self.scene.add_box(box_name, box_pose, size=tamaño)

    def move_trajectory(self, poses: List[Pose], wait: bool = True) -> bool:
        poses.insert(0, self.get_pose())
        (plan, fraction) = self.move_group.compute_cartesian_path(poses, 0.01, 0.0)

        if fraction != 1.0:
            return False
        
        return self.move_group.execute(plan, wait=wait)

    def add_floor(self) -> None:
        pose_suelo = Pose()
        pose_suelo.position.z = -0.026
        self.add_box_to_planning_scene(pose_suelo,"suelo",(2,2,.05))
        
    def mover_pinza(self, anchura_dedos: float, fuerza: float) -> bool:
        goal = GripperCommandGoal()
        goal.command.position = anchura_dedos
        goal.command.max_effort = fuerza
        self.gripper_action_client.send_goal(goal)
        self.gripper_action_client.wait_for_result()
        result = self.gripper_action_client.get_result()
        
        return result.reached_goal

if __name__ == '__main__':
    control = ControlRobot()
    #control.mover_pinza(100,10)
    pose_act = control.get_pose()
    pose_act.position.z -= 0.1
    print(pose_act)
    control.move_to_pose(pose_act)
    # configuracion_act = control.get_motor_angles()
    # configuracion_act[0] += pi
    # control.move_motors(configuracion_act)



