# Collaborations

This repository contains files related to colaborations with other organizations

<a href="https://github.com/CCSU-CS-Club/collaborations/tree/master/SistersInScience">Sisters in Science event</a>

## GoPiGo Python cheatsheet
Python Programming on GoPiGo
Each method is a clickable link

Motor control functions:
- fwd(): Move the GoPiGo forward with PID (better control)
- motor_fwd(): Move the GoPiGo forward without PID
- bwd(): Move the GoPiGo back with PID (better control)
- motor_bwd(): Move the GoPiGo back without PID
- left(): Turn GoPiGo Left slow (one motor off, better control)
- left_rot(): Rotate GoPiGo left in same position (both motors moving in the opposite direction)
- right(): Turn GoPiGo right slow (one motor off, better control)
- right_rot(): Rotate GoPiGo right in same position both motors moving in the opposite direction)
- stop(): Stop the GoPiGo

Motor speed Functions:
- increase_speed(): Increase the speed of the GoPiGo by 10
- decrease_speed(): Decrease the speed of the GoPiGo by 10
- set_left_speed(): Set speed of the left motor
- set_right_speed(): Set speed of the right motor
- set_speed(): Set speeds of both the motors

Encoder Functions:
- enc_tgt(): Set encoder target to move the GoPiGo to a set distance
- enable_encoders(): Enable the encoders
- disable_encoders(): Disable the encoders

Ultrasonic ranger read:
- us_dist(): Read distance from the ultrasonic sensor


LED control:
- led_on(): Turn LED on
- led_off(): Turn LED off
Servo control:
- enable_servo(): Enables the servo
- disable_servo(): Disables the servo
- servo(): Set servo position

Status from the GoPiGo:
- volt(): Read battery voltage in V
- fw_ver(): Get the firmware version of the GoPiGo
- enable_com_timeout(): Enable communication time-out(stop the motors if no command received in the specified time-out)
- disable_com_timeout(): Disable communication time-out
- read_status(): Read the status register on the GoPiGo
- read_enc_status(): Read encoder status
- read_timeout_status(): Read timeout status


