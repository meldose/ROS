import rospy # import rospy modules

from turtlesim.msg import Pose # importing turtlesim.msgs from Pose
from geometry_msgs.msg import Twist # importing geometry_mgs from Twist


# defining the function for callback
def pose_callback(pose:Pose):
    cmd=Twist() # settig the Twist class
    if pose.x > 9.0 or pose.x < 2.0 or pose.y > 9.0 or pose.y<2.0: # setting the pose for x and y values 
        cmd.linear.x=1.0
        cmd.angular.z=1.4
    else:

        cmd.linear.x=5.0
        cmd.angular.z=0.0
    pub.publish(cmd) # setting the publisher

# calling the main function
if __name__=="__main__":
    rospy.init_node("turtle_controller") # settig the init_node
    
    pub=rospy.Publisher("/turtle1/cmd_vel",Twist,queue_size=10) # setting the Publisher
    sub=rospy.Subscriber("/turtle1/pose",Pose,callback=pose_callback) # setting the Sunscriber
    rospy.loginfo("Node has been started") # settig the logging info
    
    rospy.spin() # making tśure the program does not exit immediately
