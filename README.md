# LanguageRecognition

 Tomato Harvester Robot to automate agricultural work 



# Table of Contents
 
 <img src="https://github.com/Youssef-Assbaghi/LanguageRecognition/blob/main/demo/Grafcos.png" align="right" width="300" alt="header"/>

   * [What is this?](#1)
   * [Requeriments](#R)
   * [Description](#2)
   * [Models](#3)
   * [Results](#4)
   * [Testing and results](#5)

   * [Authors](#6)



# What is this? <a name="1"></a>
This project is related to the subject of the third-year computing mention at the UAB of "Robotics, Language and Planning" . In it, a project of the creation of a robot through simulations has been carried out. In this repository you can find everything you need to run and test the robot. It includes all the Python code and the CoppeliaSim scenes to test Matt-Omato. The point of that project is we have to create a robot with a budget  of approximately 100€. To see more detailed information about the project, please read the report carefully.
# Requeriments <a name="R"></a>
For running each sample code:

- Python 3.7

- numpy <a fref="www.google.es"></a>

- math
- Jupyter Notebook

- matplotlib

- sklearn

- seaborn


# Description <a name="2"></a>
Matt-Omato is a robot capable of harvesting tomatoes autonomously through different growing lines and deposit them in a box attached to the base.

The main mechanical component is a anthropomorphic 5-axis robotic arm plus clamp which allows you a sufficient range to harvest tomatoes you have on the growing lines on each side.  At the end of the arm it has a special 3-finger gripper which allows us to take the tomatoes more easily and correctly.

 Matt-Omato's movement through the tomato plants is linear. Moves back and forth through rails so you don't lose straight line  and thus avoid possible shock with the tomateras. Matt-Omato has two proximity sensors which allow him to change direction if he detects any object.
 
 The other most important part of Matt-Omato is the RGB-D camera that has built-in. Thanks to it it is able to detect the tomatoes and obtain the coordinates of them.  This will also allow us to define a threshold that types of tomatoes we agree to harvest and which we do not.
 
  Generally speaking Matt-Omato is able to:
  -  Detect tomato coordinates using a 3D point cloud.
  -  Calculate the angles of rotation of the arm motors in order to move the manipulator through inverse kinematics.
  -   Move autonomously through the tomato plants thanks to the rails and proximity sensors

# Models <a name="3"></a>



# Results <a name="4"></a>

<img src="https://github.com/Youssef-Assbaghi/LanguageRecognition/blob/main/demo/Grafcos.png"  alt="header"/>
