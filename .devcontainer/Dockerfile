FROM osrf/ros:humble-desktop

# aktualizacja i instalacja narzedzi
RUN apt-get update && apt-get install -y \
    python3-colcon-common-extensions \
    nano \
    && rm -rf /var/lib/apt/lists/*

# zautomatyzowanie ladowania srodowiska ROS2 przy otwarciu terminala
RUN echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc
