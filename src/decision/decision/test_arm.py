from hiwonder_sdk import Board
import time

actions = (
    (90, 90, 90, 90),
    (90, 180, 120, 45),
    (90, 90, 120, 45),
    (0, 90, 120, 45),
    (0, 180, 120, 45)
)

for action in actions:
    Board.setPWMServoAngle(2, action[0])
    time.sleep(1)
    Board.setPWMServoAngle(5, action[1])
    time.sleep(1)
    Board.setPWMServoAngle(4, action[2])
    time.sleep(1)
    Board.setPWMServoAngle(3, action[3])
    time.sleep(1)