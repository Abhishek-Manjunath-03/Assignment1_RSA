# Group 6 - Boolean Logic Simulator
by Amogh Hemanth Likith Naresh Abhishek

## Description
The Boolean Logic Simulator is a simple tool that allows users to input different types of logic gates (AND, OR, NOT, XOR) and compute the output based on the given inputs. This project demonstrates fundamental concepts in electronics engineering and programming.

## Problem Statement
The task is to develop a Boolean Logic Simulator that allows users to compute outputs based on various logic gates, including AND, OR, NOT, and XOR. The simulator should feature a user-friendly interface for inputting gate types and boolean values, along with robust input validation to ensure correct data entry. It should involve implementing basic logic gate functions, creating a simple command-line or web interface, and writing comprehensive tests to verify the functionality of the logic gates. 

## Objective
Task is to implement the core functionality for basic logic gates: AND, OR, NOT, and XOR. These gates perform the fundamental operations used in digital circuits.

AND Gate:
The AND gate takes two binary inputs (0 or 1). It returns 1 if both inputs are 1; otherwise, it returns 0.
Example: For inputs (1, 1), the output will be 1. For inputs (1, 0), the output will be 0.

OR Gate:
The OR gate also takes two binary inputs. It returns 1 if at least one of the inputs is 1; otherwise, it returns 0.
Example: For inputs (1, 0), the output will be 1. For inputs (0, 0), the output will be 0.

NOT Gate:
The NOT gate takes only one input. It inverts the input, so if the input is 1, the output will be 0, and if the input is 0, the output will be 1.
Example: For input 1, the output will be 0. For input 0, the output will be 1.

XOR Gate:
The XOR (Exclusive OR) gate takes two binary inputs. It returns 1 if the inputs are different (i.e., one is 1 and the other is 0); otherwise, it returns 0.
Example: For inputs (1, 0), the output will be 1. For inputs (1, 1), the output will be 0.

## Steps
Repository Creation:
The first step was to create a GitHub repository named "Assignment1_RSA". This repository will serve as the central location for storing all project-related code, documentation, and resources. It ensures that all team members can easily access and collaborate on the project.

Granting Access to Team Members:
Once the repository was created, access was granted to all group members by adding them as contributors. This step is crucial for team collaboration, as it allows each member to contribute to the project by pushing code, creating branches, and submitting pull requests.

Task Assignment:
After setting up the repository, we divided the project into specific tasks and assigned each team member a responsibility:
Team 1: Responsible for implementing the basic logic gate functions (AND, OR, NOT, XOR). This involves writing the core logic that powers the Boolean Logic Simulator.
Team 2: Tasked with developing the input validation and user interface, ensuring that users can easily input the correct data (0 or 1) and interact with the simulator. This also includes creating a simple CLI or web interface for user interaction.
Team 3: Focuses on writing test cases, usage examples, and documentation. This step ensures that the logic gate functions are thoroughly tested, and users understand how to use the simulator through detailed examples and clear instructions.

## Project Development Process for the Boolean Logic Simulator
The first step in the project was to create a GitHub repository named "Assignment1_RSA," which serves as the central location for storing all project-related code, documentation, and resources, ensuring easy access and collaboration among team members.

Once the repository was created, access was granted to all group members by adding them as contributors, which is crucial for collaboration as it allows each member to contribute by pushing code, creating branches, and submitting pull requests.

After setting up the repository, the project was divided into specific tasks. Team 1 was responsible for implementing the basic logic gate functions (AND, OR, NOT, XOR), which involved writing the core logic for the Boolean Logic Simulator. Team 2 was tasked with developing input validation and a user interface, ensuring that users could easily input the correct data (0 or 1) and interact with the simulator through a simple command-line or web interface. Team 3 focused on writing test cases, usage examples, and documentation to ensure thorough testing of the logic gate functions and to provide users with clear instructions on how to use the simulator.

To maintain organization during development, each team worked on separate branches within the repository, such as branches for logic gate implementation, interface development, and testing. This branching strategy helped avoid code conflicts and allowed each team to focus on their specific tasks without interfering with others' progress.

The next step involved creating a file to store the logic gate code, using the command touch logic-gate.md. After writing the necessary code in the file, the changes were staged and committed with the commands git add logic-gate.md and git commit -m "Added functions to simulate logic gates." The commit history was then reviewed using git log.

Once development was underway, the repository was cloned to a different location or machine to facilitate collaboration, with the command git clone <repository-link>. After cloning, the remote repository link was added to maintain a connection between the local and remote repositories using git remote add origin <link>.

To verify that the logic-gate.md file exists in the directory, the command ls logic-gate.md was executed. Changes were pushed to the master branch of the remote repository with the command git push -u origin master. Additional changes, such as adding a README.md file, were also pushed using git push.

To ensure the local repository was up to date with the remote repository, the latest changes were pulled with the command git pull origin master. Finally, the existence of the necessary files (README.md and logic-gate.md) was confirmed by executing ls README.md logic-gate.md.


