import rospy
from sensor_msgs.msg import JointState
from std_msgs.msg import Header
from math import sin

def talker():
    pub = rospy.Publisher('joint_states', JointState, queue_size=20)
    rospy.init_node('joint_state_publisher]')
    rate = rospy.Rate(10)

    left_to_link_1 = -1.9
    link_1_to_hidden_link = -1.9
    hidden_link_to_link_2 = 0
    link_2_to_left_gripper = 0
    link_2_to_right_gripper = 0
    dt = 0

    hello_str = JointState()
    hello_str.header = Header()
    hello_str.header.stamp = rospy.Time.now()
    hello_str.name = ['left_to_link_1', 'link_1_to_hidden_link', 'hidden_link_to_link_2',
     'link_2_to_left_gripper', 'link_2_to_right_gripper']
    hello_str.position = [left_to_link_1, link_1_to_hidden_link, hidden_link_to_link_2,
     link_2_to_left_gripper, link_2_to_right_gripper]
    hello_str.velocity = [1000, 1000, 1000, 1000, 1000]
    hello_str.effort = [0.5, 0.5, 0.5, 0.5, 0.5]

    pub.publish(hello_str)
    rate.sleep()

    while not rospy.is_shutdown():
        dt += 0.1
        hello_str = modify(hello_str, dt)

        pub.publish(hello_str)
        rate.sleep()

def modify(msg, dt):
    msg.position[0] = 1.9 * sin(dt)
    msg.position[1] = 1.9 * sin(dt)
    msg.position[2] = 2 * sin(dt) + 2
    msg.position[3] = (1.57075 * sin(dt) + 1.57075) /2
    msg.position[4] = (1.57075 * sin(dt) + 1.57075) /2
    msg.header.stamp = rospy.Time.now()
    return msg

if __name__ == "__main__":
    try:
        talker()
    except rospy.ROSInterruptException:
        pass