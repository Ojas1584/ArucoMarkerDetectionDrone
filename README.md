# 🛸 ArUco Marker Detection UAV

This project enables a **Nano Drone / UAV** to detect ArUco markers using OpenCV and perform navigation commands accordingly. It supports both 4x4 and 5x5 ArUco markers with custom IDs for drone movement control.

---

## 📌 Features

- Detects multiple ArUco marker dictionaries (4x4 and 5x5) in real-time  
- Maps marker IDs to UAV navigation commands (ascend, land, move forward/backward, turn)  
- Displays detected markers and commands on live camera feed  
- Compatible with Nano Drone / UAV for autonomous navigation  

---

## 🧩 ArUco Marker Details

| Marker ID | Dictionary | Command | Image |
|-----------|------------|---------|-------|
| 8         | 4x4        | Ascend  | ![Marker 8](markers/aruco.png) |
| 37        | 4x4        | Land    | ![Marker 37](markers/aruco1.png) |
| 1         | 4x4        | Move Forward | ![Marker 1](markers/aruco2.png) |
| 2         | 4x4        | Move Backward | ![Marker 2](markers/aruco3.png) |
| 3         | 4x4        | Turn Right | ![Marker 3](markers/aruco5.jpeg) |
| 4         | 4x4        | Turn Left | ![Marker 4](markers/aruco4.png) |

> **Note:** Make sure the marker images exist in the `markers/` folder inside the repo.

---

## 📁 Project Structure

