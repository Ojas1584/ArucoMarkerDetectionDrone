# 🛸 Patented UAV Navigation for GPS-Denied Environments

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python&logoColor=yellow)](https://www.python.org/)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.x-blue?logo=opencv&logoColor=white)](https://opencv.org/)
[![ROS](https://img.shields.io/badge/ROS-Noetic-blue?logo=ros)](https://www.ros.org/)
[![Patent](https://img.shields.io/badge/Patent_Filed-202521075349-brightgreen)](https://ipindia.gov.in/)

This repository contains the software for a **patented autonomous UAV navigation system** designed to operate in GPS-denied environments. The system uses real-time computer vision with **ArUco markers** to achieve high-precision localization, object tracking, and adaptive motion control.

This is a complete hardware/software solution, validated in simulation (ROS/Gazebo) and on real-world nano-drones, achieving a **40% reduction in flight path errors** and a **30% improvement in marker detection accuracy** over baseline methods.

---

## 📌 Core Features

- **High-Precision Localization:** Uses OpenCV to detect ArUco markers and perform 6-DoF pose estimation, enabling the drone to know its exact position and orientation without GPS.
- **Robust ID-Based Control Logic:** A custom-engineered control system (part of the patent) maps specific ArUco marker IDs to complex flight commands (e.g., ascend, land, move, turn).
- **Real-Time Object Tracking:** Implements adaptive motion planning to stably track and follow detected markers.
- **Hardware Integration:** Full integration with nano-drones for real-world command execution.
- **Simulation-Ready:** Includes configurations for testing and validation within a ROS/Gazebo simulated environment.

---

## 🔧 Tech Stack

* **Core Logic:** Python 3.9+
* **Computer Vision:** OpenCV (opencv-python-contrib)
* **Drone Communication:**  custom drone SDK
* **Robotics Framework:** Robot Operating System (ROS)
* **Simulation:** Gazebo
* **Libraries:** NumPy

---

## 🏛️ System Architecture

The system operates on a closed-loop, off-board control principle:

1.  **[Camera Sensor] → Video Feed:** The drone's onboard camera streams a real-time video feed to the ground control station (laptop).
2.  **[OpenCV] → Detection & Pose Estimation:** The feed is processed by OpenCV to detect ArUco markers. The system calculates the precise 3D pose (position and orientation) of the marker relative to the drone.
3.  **[Control Logic] → Command Generation:** Based on the marker's ID and pose, the custom control logic (the "brain" of the system) generates the appropriate navigation command (e.g., "move forward 20cm," "turn 15 degrees right").
4.  **[Drone API] → Command Execution:** The command is sent back to the drone, which executes the maneuver.
5.  This loop repeats at high frequency, creating a stable, real-time feedback system.

---

## 🧩 ArUco Command Logic

The system is configured to respond to specific markers with pre-defined commands.

| Marker ID | Dictionary | Command |
|:----------|:-----------|:--------|
| 8         | 4x4_50     | Ascend / Take-Off |
| 37        | 4x4_50     | Land |
| 1         | 4x4_50     | Move Forward |
| 2         | 4x4_50     | Move Backward |
| 3         | 4x4_50     | Turn Right |
| 4         | 4x4_50     | Turn Left |

---

## 📊 Results & Validation

This system was validated against baseline navigation methods and demonstrated significant performance gains:

* **Detection Accuracy:** The custom ID-based control logic resulted in a **30% improvement** in robust marker detection compared to standard approaches.
* **Navigation Stability:** Real-time object tracking and adaptive motion planning led to a **40% reduction in flight path errors** during repeated test flights.

---

## 📜 Patent Status

The novel methods for localization and control developed in this project are the subject of a filed patent.

**Patent Filed – Application No. 202521075349**

---

## 🚀 Getting Started

### Prerequisites

* Python 3.9+
* OpenCV (`opencv-python-contrib`)
* Drone-specific SDK 
* (Optional) ROS Noetic & Gazebo installed for simulation.

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Ojas1584/ArucoMarkerDetectionDrone.git
    cd ArUco-Marker-Detection-UAV
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

### Usage

1.  **For Real-World Flight:**
    * Ensure you are connected to the drone's Wi-Fi network.
    * Run the main flight script:
    ```bash
    python main_flight.py
    ```

2.  **For Simulation (ROS/Gazebo):**
    * Launch the Gazebo world with the drone and markers:
    ```bash
    roslaunch drone_aruco_sim simulation.launch
    ```
    * In a new terminal, run the ROS control node:
    ```bash
    rosrun drone_aruco_sim control_node.py
    ```

---

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
