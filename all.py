from time import sleep
from sense_hat import SenseHat


# setting IMUs and sensors
sense = SenseHat()
sense.set_imu_config(False, True, False)

# for stopping push "contorol + c"
while True:
    #getting sensors data
    humidity = sense.get_humidity()
    temp = sense.get_temperature()
    pressure = sense.get_pressure()
    orientation = sense.get_orientation_degrees()
    north = sense.get_compass()
    gyro_only = sense.get_gyroscope()
    accel_only = sense.get_accelerometer()
    event = sense.stick.get_events()
    print("Humidity: %s %%rH" % humidity)
    print("Temperature: %s C" % temp)
    print("Pressure: %s Millibars" % pressure)
    print("p: {pitch}, r: {roll}, y: {yaw}".format(**orientation))
    print("North: %s" % north)
    print("p: {pitch}, r: {roll}, y: {yaw}".format(**gyro_only))
    print("p: {pitch}, r: {roll}, y: {yaw}".format(**accel_only))
    #print(event)
    print("The joystick event was " + str(event))
    sleep(0.5)
