#from EmulatorGUI import GPIO
import RPi.GPIO as GPIO
import time

class Hx711:
    def __init__(self, pin_dout, pin_slk):
        self._pin_dout = pin_dout
        self._pin_slk = pin_slk

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self._pin_slk, GPIO.OUT)
        GPIO.setup(self._pin_dout, GPIO.IN)

        GPIO.output(self._pin_slk, GPIO.HIGH)
        time.sleep(0.0001)
        GPIO.output(self._pin_slk, GPIO.LOW)

        self.averageValue()
        self.setOffset(self.averageValue())
        self.setScale()

    def averageValue(self, times=32):
        sumation = 0
        for i in range(times):
            sum += self.getValue()

        return sumation / times

    def getValue(self):
        data = [0, 0, 0]

        while GPIO.input(self._pin_dout):
            pass

        for j in range(2, -1, -1):
            for i in range(7, -1, -1):
                GPIO.output(self._pin_slk, GPIO.HIGH)
                data[j] |= (GPIO.input(self._pin_dout) << i)
                GPIO.output(self._pin_slk, GPIO.LOW)

        GPIO.output(self._pin_slk, GPIO.HIGH)
        GPIO.output(self._pin_slk, GPIO.LOW)

        data[2] ^= 0x80

        return (data[2] << 16) | (data[1] << 8) | data[0]

    def setOffset(self, offset):
        self._offset = offset

    def setScale(self, scale=1.0):
        self._scale = scale

    def getGram(self, times=32):
        val = self.averageValue(times) - self._offset
        return float(val) / self._scale

    def __del__(self):
        GPIO.cleanup()
