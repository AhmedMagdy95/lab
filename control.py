#!/usr/bin/env python3
import rclpy 
from rclpy.node import Node
from example_interfaces.srv import Firstsr
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from math import pow, atan2, sqrt

class my_node (Node):
   
    def __init__(self):
        super().__init__("Node_name")
        self.create_service(Firstsr, "srv_name", self.srv_call)
        self.service_client(8,9)
        self.service_client(10,20)
        
    def service_client(self,a,b):
        client=self.create_client(AddTwoInts,"First_server")
        while client.wait_for_service(0.25)==False:
            self.get_logger().warn("wating for server")

        request=AddTwoInts.Request()
        request.a=a
        request.b=b
        futur_obj=client.call_async(request)
        futur_obj.add_done_callback(self.future_call)

    def future_call(self,future_msg):
        self.get_logger().info(str(future_msg.result().sum))
        


def update_pose(self,data):
    self.pose =data
    self.pose.x=round(self.pose.x , 4)
    self.pose.y=round(self.pose.y , 4)

def euclidean_distance(self, goal_pose):
    return sqrt(pow((goal_pose.x - self.pose.x), 2) +
    pow((goal_pose.y - self.pose.y), 2))
   
def linear_vel(self, goal_pose, constant=1.5):
  return constant * self.euclidean_distance(goal_pose)
   
def steering_angle(self, goal_pose):
  return atan2(goal_pose.y - self.pose.y, goal_pose.x - self.pose.x)
   
def angular_vel(self, goal_pose, constant=6):
 return constant * (self.steering_angle(goal_pose) - self.pose.theta)

def move_turtle(self):
    goal_pose = Pose()
    # Get the input from the user.
    goal_pose.x = float(input("Set your x goal: "))
    goal_pose.y = float(input("Set your y goal: "))
   



def main(args=None):
    rclpy.init(args=args)
    node=my_node()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__=="__main__":
    main()