import rospy
from std_msgs.msg import Int32

class NodoOrdenes:
    def __init__(self):
        rospy.init_node('nodo_ordenes', anonymous=True)
        self.pub = rospy.Publisher('/consignas', Int32, queue_size=10)

    def run(self):
        while not rospy.is_shutdown():
            try:
                print("Hola, por favor ingrese un número para la acción a realizar:")
                print("1: Mover el robot a una pose")
                print("2: Mover el robot a una configuración")
                print("3: Mover el extremo del robot por una trayectoria dada")
                print("4: Añadir obstáculos a la escena de planificación")
                orden = int(input("Orden: "))
                if orden in [1, 2, 3, 4]:
                    self.pub.publish(orden)
                else:
                    print("Orden no válida")
            except ValueError:
                print("Por favor, ingrese un número válido")
            rospy.sleep(1)

if __name__ == '__main__':
    nodo = NodoOrdenes()
    nodo.run()
