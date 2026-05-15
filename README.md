# 🚧 Smart Toll Gate - ROS2 Humble Project
### Author: Marcel Kwiatkowski
**Project:** Intelligent Barrier in ROS2

An academic project demonstrating advanced node-to-node communication within the **ROS2 (Robot Operating System 2)** environment. The system simulates a real-world scenario of an automated toll gate and its interaction with an approaching vehicle (driver).

## 📑 Table of Contents
1. [Project Overwiev](#-project-overwiev)
2. [Implemented ROS2 Features](#-Implemented-ROS2-Features)
3. [File Structure & Code Explanation](#-File-Structure-&-Code-Explanation)
4. [Infrastructure as Code (Docker & DevContainers)](#-Infrastructure-as-Code-(Docker-&-DevContainers))
5. [Prerequisites](#-Prerequisites)
6. [Installation & Setup Guide](#-Installation-&-Setup-Guide)
7. [How to Run](#-How-to-Run)
8. [Results](#-results)

## 📌 Project Overview
The project implements two distinct nodes communicating in real-time:
1. **Gate Server (`szlaban_node`)**: Operates in the background, continuously broadcasting its status and awaiting service requests to open.
2. **Driver Client (`kierowca_node`)**: An interactive node that listens to the gate's broadcasts and allows the user to trigger the opening mechanism via keyboard input.

### Implemented ROS2 Features
* **Topics (Publisher/Subscriber)**: The gate continuously publishes its current physical state (`Zamkniety` [Closed] or `Otwarty` [Open]) on the `status_szlabanu` topic using standard `std_msgs/String` messages. The driver node subscribes to this topic to provide real-time updates to the user.
* **Services (Client/Server)**: The gate hosts an `otworz_szlaban` service (using the standard `std_srvs/Trigger` type). The driver acts as a service client, sending a trigger signal to open the gate.
* **Launch Files**: The server-side environment is initialized using a python-based launch file (`szlaban.launch.py`), allowing for node renaming and background execution.
* **Multithreading**: The driver node utilizes Python's `threading` library to simultaneously spin the ROS2 executor (listening to topics) and wait for standard user input (`stdin`) without blocking the execution thread.

---

## 📂 File Structure & Code Explanation

Here is a breakdown of the core files in this repository and their responsibilities:

*   **`projekt_szlaban/szlaban_node.py` (Gate Server Node)**
    *   Uses `create_publisher` to broadcast the gate's state every 1.0 second.
    *   Uses `create_service` to listen for trigger requests. Once triggered, it changes the state to `Otwarty` (Open) and initiates a 3-second timer (`create_timer`).
    *   When the timer expires, a callback automatically reverts the state to `Zamkniety` (Closed).

*   **`projekt_szlaban/kierowca_node.py` (Driver Client Node)**
    *   Uses `create_subscription` to listen to the gate's topic and log the physical state to the terminal.
    *   Implements a background thread (`threading.Thread`) to continuously read standard keyboard input (`stdin`). This ensures the ROS2 executor (`rclpy.spin`) is not blocked.
    *   When the user types `o`, it uses `create_client` to send an asynchronous service request to the gate.

*   **`launch/szlaban.launch.py` (Launch Configuration)**
    *   Automates the startup of the gate node. 
    *   Demonstrates ROS2 node renaming capabilities (remaps the node's name to `moj_szlaban` dynamically at runtime).

*   **`setup.py` (Build Configuration)**
    *   The configuration file for the `colcon` build system.
    *   Contains the `console_scripts` entry points, registering `szlaban` and `kierowca` as executable commands.
    *   Includes the `data_files` mapping, which ensures the `launch` directory is properly copied to the `install/share` path during the build process.

*   **`.devcontainer/` (Environment Config)**
    *   Contains the `Dockerfile` and `devcontainer.json` defining the isolated ROS2 Humble Linux environment.

---

## 🐳 Infrastructure as Code (Docker & DevContainers)
To ensure **100% reproducibility** and eliminate the "it works on my machine" problem, this project is entirely containerized. You do **not** need to install ROS2 or Ubuntu on your local machine.

The repository includes a `.devcontainer` configuration, which utilizes Docker to automatically build a complete Linux environment with **ROS2 Humble** pre-installed, along with all necessary build tools (like `colcon`).

### Prerequisites
To run this project, you will need:
* [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed and running.
* [Visual Studio Code](https://code.visualstudio.com/).
* The **[Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)** installed in VS Code.

---

## 🚀 Installation & Setup Guide

### 1. Clone the Repository
Clone this repository to your local machine:
~~~bash
git clone https://github.com/marcelkwiatkowski01/Intelligent-Barrier.git
cd Intelligent-Barrier
~~~

### 2. Start the Dev Container
1. Open the cloned folder in Visual Studio Code.
2. Press `F1` (or `Ctrl+Shift+P`) to open the command palette.
3. Type and select: **Dev Containers: Reopen in Container**.
4. VS Code will now build the Docker image and start the ROS2 container. (This may take a few minutes the first time).

### 3. Build the Workspace
Once inside the container (indicated by the terminal path `/workspace`), build the ROS2 package:
~~~bash
colcon build
source install/setup.bash
~~~

---

## 🎮 How to Run

Because the project features an interactive user interface (the driver's keyboard input), it is designed to run in a **Dual-Terminal Setup**.

### Terminal 1: Start the Gate Server
In your first VS Code terminal, launch the Gate Node using the provided launch file:
~~~bash
ros2 launch projekt_szlaban szlaban.launch.py
~~~
*Expected behavior: The terminal will begin logging the gate's closed status every second.*

### Terminal 2: Start the Driver Client
Open a **new terminal** inside VS Code (click the `+` icon). Source the environment and run the driver node directly:
~~~bash
source install/setup.bash
ros2 run projekt_szlaban kierowca
~~~
*Expected behavior: You will see an interactive prompt. The terminal will seamlessly display the gate's broadcasts while waiting for your input.*

### Interaction
In Terminal 2, simply type the letter `o` (case-insensitive) and press **Enter**.
1. The driver will send a Service request to the Gate.
2. The Gate will process the request, change its status to `Otwarty`, and hold the gate open.
3. After exactly 3 seconds, an internal timer within the Gate node will automatically close it, restoring the `Zamkniety` status.

## Results:


Project made by Kwiatkowski Marcel
