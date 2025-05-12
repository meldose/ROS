#!/usr/bin/env python3 

import rospy

if __name__=="__main__":
    rospy.init_node("test_node")
    
    rospy.loginfo("frst node")
    
    rate=rospy.Rate(10)
    
    while not rospy.is_shutdown():
        
        rospy.logwarn("this is warning")
        rospy.logerr("This is an error")

        rospy.sleep(1.0)

        rospy.loginfo("End of the Program")




