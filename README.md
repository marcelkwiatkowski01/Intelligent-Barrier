# 🚧 Smart Toll Gate - ROS2 Humble Project

An academic project demonstrating advanced node-to-node communication within the **ROS2 (Robot Operating System 2)** environment. The system simulates a real-world scenario of an automated toll gate and its interaction with an approaching vehicle (driver).

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

## 🐳 Infrastructure as Code (Docker & DevContainers)
To ensure **100% reproducibility** and eliminate the "it works on my machine" problem, this project is entirely containerized. You do **not** need to install ROS2 or Ubuntu on your local machine.

The repository includes a `.devcontainer` configuration, which utilizes Docker to automatically build a complete Linux environment with **ROS2 Humble** pre-installed, along with all necessary build tools (like `colcon`).

### Prerequisites
To run this project, you will need:
* [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed and running.
* [Visual Studio Code](https://code.visualstudio.com/).
* The **Dev Containers** extension installed in VS Code.

---

## 🚀 Installation & Setup Guide

### 1. Clone the Repository
Clone this repository to your local machine:
```bash
git clone [https://github.com/marcelkwiatkowski01/Intelligent-Barrier.git](https://github.com/marcelkwiatkowski01/Intelligent-Barrier.git)
cd Intelligent Barrier
