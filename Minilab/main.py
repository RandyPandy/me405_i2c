#
# micropython i2c driver
#

import micropython
import bno055 as imu
accel_range = b'00000000' ##accel = 2g
accel_range = b'00000001' ##accel = 4g care if not in fusion mode. top 8 bits impact power and BW


if __name__ == "__main__":
    '''Reads or Writes to i2c peripheral'''
    aye = pyb.I2C (1, pyb.I2C.MASTER)
    nerd = BNO055(aye, 0x28, accel_range)
    x_data = nerd.get_ax_bits()

    def scan_list()
        aye = pyb.I2C (1, pyb.I2C.MASTER)
        adr_list = []
        adr_list = pyb.I2C.scan(aye)
        return adr_list
