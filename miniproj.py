import cv2
import cv2.aruco as aruco
import numpy as np
from cflib.crazyflie import Crazyflie
from cflib.crazyflie.syncCrazyflie import SyncCrazyflie
from cflib.positioning.motion_commander import MotionCommander
import cflib.crtp

# Initialize Crazyflie communication
uri = 'radio://0/45/2M/E7E7E7E7E7'  # Update with your actual Crazyflie URI

# Initialize webcam
cap = cv2.VideoCapture(0)  # For Linux
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
cap.set(cv2.CAP_PROP_FPS, 60)

if not cap.isOpened():
    print("Error: Could not open video stream.")
    exit()

# Define ArUco dictionaries for 4x4 and 5x5
aruco_dict_4x4 = aruco.getPredefinedDictionary(aruco.DICT_4X4_50)
aruco_dict_5x5 = aruco.getPredefinedDictionary(aruco.DICT_5X5_50)

parameters = aruco.DetectorParameters()
parameters.adaptiveThreshWinSizeMin = 5
parameters.adaptiveThreshWinSizeMax = 23
parameters.adaptiveThreshWinSizeStep = 10
parameters.minMarkerPerimeterRate = 0.03
parameters.maxMarkerPerimeterRate = 4.0
parameters.polygonalApproxAccuracyRate = 0.05
parameters.minDistanceToBorder = 3




# Example dictionary to map marker IDs to Crazyflie commands
navigation_commands = {
    8: 'ascend',
    37: 'land',
    1: 'move_forward',
    2: 'move_backward',
    3: 'turn_right',
    4: 'turn_left'
}

# Connect to Crazyflie and initialize motion control
cflib.crtp.init_drivers(enable_debug_driver=False)
with SyncCrazyflie(uri, cf=Crazyflie(rw_cache='./cache')) as scf:
    with MotionCommander(scf) as mc:
        while True:
            # Capture frame-by-frame
            ret, frame = cap.read()
            if not ret:
                break

            # Convert frame to grayscale
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Detect ArUco markers from both dictionaries
            corners_4x4, ids_4x4, rejected_img_points_4x4 = aruco.detectMarkers(gray, aruco_dict_4x4, parameters=parameters)
            corners_5x5, ids_5x5, rejected_img_points_5x5 = aruco.detectMarkers(gray, aruco_dict_5x5, parameters=parameters)

            detected_commands = []

            # If markers are detected in either dictionary
            if ids_4x4 is not None or ids_5x5 is not None:
                if ids_4x4 is not None:
                    aruco.drawDetectedMarkers(frame, corners_4x4, ids_4x4)
                    print(f"Detected {len(ids_4x4)} 4x4 markers")  # Debugging: print how many 4x4 markers were detected
                    for i in range(len(ids_4x4)):
                        marker_id = ids_4x4[i][0]
                        if marker_id in navigation_commands:
                            command = navigation_commands[marker_id]
                            detected_commands.append(f"{marker_id}: {command}")
                            if command == 'ascend':
                                mc.up(0.4)
                            elif command == 'land':
                                mc.stop()
                            elif command == 'move_forward':
                                mc.forward(0.2)
                            elif command == 'move_backward':
                                mc.forward(-0.2)
                            elif command == 'turn_right':
                                mc.turn_right(90)
                            elif command == 'turn_left':
                                mc.turn_left(90)

                if ids_5x5 is not None:
                    aruco.drawDetectedMarkers(frame, corners_5x5, ids_5x5)
                    print(f"Detected {len(ids_5x5)} 5x5 markers")  # Debugging: print how many 5x5 markers were detected
                    for i in range(len(ids_5x5)):
                        marker_id = ids_5x5[i][0]
                        if marker_id in navigation_commands:
                            command = navigation_commands[marker_id]
                            detected_commands.append(f"{marker_id}: {command}")
                            if command == 'ascend':
                                mc.up(0.4)
                            elif command == 'land':
                                mc.stop()
                            elif command == 'move_forward':
                                mc.forward(0.2)
                            elif command == 'move_backward':
                                mc.forward(-0.2)
                            elif command == 'turn_right':
                                mc.turn_right(90)
                            elif command == 'turn_left':
                                mc.turn_left(90)

            else:
                print("No markers detected.")  # Debugging: print if no markers are detected

            # Display the frame with marker overlays
            cv2.imshow('ArUco Marker Detection', frame)

            # Overlay the detected marker commands in the top-right corner
            y_offset = 20  # Vertical position of text starting point
            for command in detected_commands:
                cv2.putText(frame, command, (frame.shape[1] - 200, y_offset), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                y_offset += 30  # Move the text down for each command

            # Exit on pressing 'q'
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

# Release resources
cap.release()
cv2.destroyAllWindows()