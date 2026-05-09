import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from std_srvs.srv import Trigger
import threading

class KierowcaNode(Node):
    def __init__(self):
        super().__init__('kierowca')
        
        # wysyla prosbe otwarcia
        self.client = self.create_client(Trigger, 'otworz_szlaban')
        
        # listener szlabanu
        self.subscription = self.create_subscription(String, 'status_szlabanu', self.wypisz_status, 10)

    def wypisz_status(self, msg):
        # wypisuje status szlabanu
        self.get_logger().info(f"Szlaban {msg.data}")

    def wyslij_o(self):
        # wysyla prosbe o otwarcie szlabanu
        if self.client.service_is_ready():
            self.get_logger().info("---> Wysylam prosbe o otwarcie szlabanu! <---")
            req = Trigger.Request()
            self.client.call_async(req)
        else:
            self.get_logger().info("Szlaban nie jest gotowy.")

def main(args=None):
    rclpy.init(args=args)
    node = KierowcaNode()

    # nasluchiwanie w osobnym watku, zeby moc jednoczesnie wpisywac komendy
    spin_thread = threading.Thread(target=rclpy.spin, args=(node,))
    spin_thread.start()

    print("\n=========================================")
    print(" KIEROWCA PODJECHAL!")
    print(" Wpisz 'o' i wcisnij Enter, zeby wyslac sygnal.")
    print("=========================================\n")

    try:
        # petla do wpisywania komend
        while True:
            klawisz = input()
            if klawisz.lower() == 'o':
                node.wyslij_o()
    except KeyboardInterrupt:
        pass

    rclpy.shutdown()
    spin_thread.join()

if __name__ == '__main__':
    main()