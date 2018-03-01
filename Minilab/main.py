#
# micropython i2c driver
#

import micropython
import mma845x as i2c


if __name__ == "__main__":
    '''Reads or Writes to i2c peripheral'''
    aye = pyb.I2C (1, pyb.I2C.MASTER)
    adr_list = []
    adr_list = pyb.I2C.scan (eye)


