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

| Marker ID | Dictionary | Command |
|-----------|------------|---------|
| 8         | 4x4        | Ascend  |
| 37        | 4x4        | Land    |
| 1         | 4x4        | Move Forward |
| 2         | 4x4        | Move Backward |
| 3         | 4x4        | Turn Right |
| 4         | 4x4        | Turn Left |

> **Note:** The images in the `markers/` folder correspond to these IDs. Ensure the images are printed/scaled correctly for reliable detection.

---

## 📁 Project Structure

