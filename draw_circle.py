import rospy # importing rospy modules

from geometry_msgs.msg import Twist # importing geometry_msgs

if __name__=="__main_": # running the main function
    rospy.init_node("draw_circle") # setting the init node 
    rospy.loginfo("Node has beeen started") # getting the logging info
    
    pub=rospy.Publisher("/turtle1/cmd_vel",Twist,queue_size=10) # setting up the publisher
    
    rate=rospy.Rate(2) # setting the rospy Rate
    
    while not rospy.is_shutdown():
        msg=Twist()
        msg.linear.x=2.0 # setting the linear x
        msg.angular.z=1.0 # settig the angular z
        pub.publish(msg) # publish the publisher
        rate.sleep() # rate the sleep
        


