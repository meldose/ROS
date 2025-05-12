import rospy # importing the rospy modules

from turtlesim.msg import Pose # importing Pose turtlesim_msgs from Pose <


# defining function for callback
def pose_callback(msg):
    rospy.loginfo("("+str(msg.x)+","+str(msg.y)+")")
    

if __name__=="__main__": # calling the main function
    rospy.init_node("turtle_pose_subscriber") # setting the 
    
    sub=rospy.Subscriber("/turtle1/pose",Pose,callback=pose_callback) # setting the subscriber
    
    rospy.loginfo("Node has been started") # setting the logging info
    
    rospy.spin() # blocking program from exiting ,allows callback (else program ight exit immediately)
    
    