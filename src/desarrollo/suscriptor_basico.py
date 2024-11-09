#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32
from geometry_msgs.msg import Pose
from control_robot import ControlRobot

class NodoControlRobot:
    def __init__(self):
        rospy.init_node('suscriptor_basico', anonymous=True)
        self.control_robot = ControlRobot()
        rospy.Subscriber('/consignas', Int32, self.callback)

    def callback(self, data):
        orden = data.data
        if orden == 1:
            self.mover_pose()
        elif orden == 2:
            self.mover_configuracion()
        elif orden == 3:
            self.ejecutar_trayectoria()
        elif orden == 4:
            self.anadir_obstaculo()
        else:
            rospy.logwarn("Orden no reconocida")

    def mover_pose(self):
        rospy.loginfo("Moviendo el robot a una pose específica")
        pose_goal = Pose()
        pose_goal.position.x = 0.5
        pose_goal.position.y = 0.0
        pose_goal.position.z = 0.5
        pose_goal.orientation.w = 1.0
        resultado = self.control_robot.move_to_pose(pose_goal)
        rospy.loginfo(f"Resultado de mover a una pose: {'Exitoso' if resultado else 'Fallido'}")

    def mover_configuracion(self):
        rospy.loginfo("Moviendo el robot a una configuración específica")
        joint_goal = self.control_robot.get_motor_angles()
        joint_goal[0] += 0.5  
        resultado = self.control_robot.move_motors(joint_goal)
        rospy.loginfo(f"Resultado de mover a una configuración: {'Exitoso' if resultado else 'Fallido'}")

    def ejecutar_trayectoria(self):
        rospy.loginfo("Ejecutando una trayectoria")
        pose1 = Pose()
        pose1.position.x = 0.5
        pose1.position.y = 0.0
        pose1.position.z = 0.5
        pose1.orientation.w = 1.0

        pose2 = Pose()
        pose2.position.x = 0.6
        pose2.position.y = 0.1
        pose2.position.z = 0.5
        pose2.orientation.w = 1.0

        trayectoria = [pose1, pose2]
        resultado = self.control_robot.move_trajectory(trayectoria)
        rospy.loginfo(f"Resultado de ejecutar trayectoria: {'Exitoso' if resultado else 'Fallido'}")

    def anadir_obstaculo(self):
        rospy.loginfo("Añadiendo obstáculo a la escena")
        pose_caja = Pose()
        pose_caja.position.x = 0.3
        pose_caja.position.y = 0.0
        pose_caja.position.z = 0.2
        self.control_robot.add_box_to_planning_scene(pose_caja, "caja_obstaculo")

if __name__ == '__main__':
    nodo = NodoControlRobot()
    rospy.spin()

