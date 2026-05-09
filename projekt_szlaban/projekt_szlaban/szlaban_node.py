import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from std_srvs.srv import Trigger

class SzlabanNode(Node):
    def __init__(self):
        super().__init__('szlaban_node')
        
        self.publisher_ = self.create_publisher(String, 'status_szlabanu', 10)
        self.timer = self.create_timer(1.0, self.publikuj_status)
        self.srv = self.create_service(Trigger, 'otworz_szlaban', self.otworz_callback)
        
        self.czy_otwarty = False
        self.timer_zamykania = None

    def publikuj_status(self):
        # wybor tekstu
        stan = 'Otwarty' if self.czy_otwarty else 'Zamkniety'
        
        # szlaban wypisuje stan
        self.get_logger().info(f'Szlaban: {stan}')
        
        # wysyla go do subscribera
        msg = String()
        msg.data = stan
        self.publisher_.publish(msg)

    def otworz_callback(self, request, response):
        self.get_logger().info('---> Otrzymano wiadomosc "O" od kierowcy! Otwieram!')
        self.czy_otwarty = True
        
        if self.timer_zamykania is not None:
            self.timer_zamykania.cancel()
        # zamyka szlaban po 3 s
        self.timer_zamykania = self.create_timer(3.0, self.zamknij_szlaban)

        response.success = True
        return response

    def zamknij_szlaban(self):
        self.czy_otwarty = False
        self.timer_zamykania.cancel()

def main(args=None):
    rclpy.init(args=args)
    node = SzlabanNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()