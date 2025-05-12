#!/usr/bin/env python3 

import rospy # importing the rospy module

if __name__=="__main__": # runnig the main function
    rospy.init_node("test_node") # setting the init node
    
    rospy.loginfo("frst node") # logging info
    
    rate=rospy.Rate(10) # setting the rospy rate (no of loop)
    
    while not rospy.is_shutdown():
        
        rospy.logwarn("this is warning") # setitng the logginwarning 
        rospy.logerr("This is an error") # setting the logging error

        rospy.sleep(1.0) # setting the time sleep

        rospy.loginfo("End of the Program") # logging info




