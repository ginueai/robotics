import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/hypark/Development/ros_ws1/install/my_sensor_pkg'
