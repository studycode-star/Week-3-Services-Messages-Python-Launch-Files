import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/khoi/robocon_ws/src/robocon_basics/install/robocon_basics'
