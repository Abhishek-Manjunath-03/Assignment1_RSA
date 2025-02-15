# Group 6 - Boolean Logic Simulator
## by Amogh Hemanth Likith Naresh Abhishek

## Description
The Boolean Logic Simulator is a simple tool that allows users to input different types of logic gates (AND, OR, NOT, XOR) and compute the output based on the given inputs. This project demonstrates fundamental concepts in electronics engineering and programming.

## Problem Statement
The task is to develop a Boolean Logic Simulator that allows users to compute outputs based on various logic gates, including AND, OR, NOT, and XOR. The simulator should feature a user-friendly interface for inputting gate types and boolean values, along with robust input validation to ensure correct data entry. It should involve implementing basic logic gate functions, creating a simple command-line or web interface, and writing comprehensive tests to verify the functionality of the logic gates. 

## Objective
Task is to implement the core functionality for basic logic gates: AND, OR, NOT, and XOR. These gates perform the fundamental operations used in digital circuits.

1.Basic gate logic functions
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

2.Input Validation and User Interface Development
User Input Validation: Ensure that users can only input valid boolean values (0 or 1) for the logic gates. Implement checks that validate user inputs before processing.

User Interface Development: Design and create a user-friendly command-line interface (CLI) or web interface that allows users to easily select logic gates and input their values. The interface should be intuitive and guide users through the process.

3.Testing and Documentation
Test Case Development: Write comprehensive test cases to verify the functionality of each logic gate (AND, OR, NOT, XOR). Ensure that all edge cases and typical use cases are covered.

Automated Testing: Implement automated tests to facilitate regular testing of the logic gate functions and user interface. This will help quickly identify and resolve issues as development progresses.

## Project Development Process for the Boolean Logic Simulator

Repository Creation:
The first step was to create a GitHub repository named "Assignment1_RSA". This repository will serve as the central location for storing all project-related code, documentation, and resources. It ensures that all team members can easily access and collaborate on the project.

Granting Access to Team Members:
Once the repository was created, access was granted to all group members by adding them as contributors. This step is crucial for team collaboration, as it allows each member to contribute to the project by pushing code, creating branches, and submitting pull requests.

Task Assignment:
After setting up the repository, we divided the project into specific tasks and assigned each team member a responsibility:
Team 1: Responsible for implementing the basic logic gate functions (AND, OR, NOT, XOR). This involves writing the core logic that powers the Boolean Logic Simulator.
Team 2: Tasked with developing the input validation and user interface, ensuring that users can easily input the correct data (0 or 1) and interact with the simulator. This also includes creating a simple CLI or web interface for user interaction.
Team 3: Focuses on writing test cases, usage examples, and documentation. This step ensures that the logic gate functions are thoroughly tested, and users understand how to use the simulator through detailed examples and clear instructions.

## Code Development for the Boolean Logic Simulator

To maintain organization during development, each team worked on separate branches within the repository, such as branches for logic gate implementation, interface development, and testing. This branching strategy helped avoid code conflicts and allowed each team to focus on their specific tasks without interfering with others' progress.

The next step involved creating a file to store the logic gate code, using the command touch logic-gate.md. After writing the necessary code in the file, the changes were staged and committed with the commands git add logic-gate.md and git commit -m "Added functions to simulate logic gates." The commit history was then reviewed using git log.

Once development was underway, the repository was cloned to a different location or machine to facilitate collaboration, with the command git clone <repository-link>. After cloning, the remote repository link was added to maintain a connection between the local and remote repositories using git remote add origin <link>.

To verify that the logic-gate.md file exists in the directory, the command ls logic-gate.md was executed. Changes were pushed to the master branch of the remote repository with the command git push -u origin master. Additional changes, such as adding a README.md file, were also pushed using git push.

To ensure the local repository was up to date with the remote repository, the latest changes were pulled with the command git pull origin master. Finally, the existence of the necessary files (README.md and logic-gate.md) was confirmed by executing ls README.md logic-gate.md.

## Development of simple CLI 

During the development of a simple CLI for the Boolean Logic Simulator, several key steps were undertaken to ensure a smooth user experience and robust functionality. The project began by initializing a Git repository with git init and setting up the necessary directory structure, which included the main script for the CLI. A basic command-line interface was created, prompting users to select logic gate types and input boolean values. Input validation was implemented to ensure that users could only enter valid gate types (AND, OR, NOT, XOR) and appropriate boolean values (True/False), enhancing the reliability of the simulator. Thorough testing was conducted to verify that the CLI functioned correctly under various input scenarios. Throughout the development process, regular commits were made using Git to track changes, with commands such as git add . to stage modifications and git commit -m "Implement basic CLI for logic gate selection" to save the project state. Monitoring progress involved using git status to display the repository's current state and git log to track the commit history. Once the CLI was complete, changes were pushed to the remote repository with git push origin cli-development, and after merging the cli-development branch into the main branch, the team integrated the new features into the main codebase. Finally, the cli-development branch was deleted with git branch -d cli-development after a successful merge, ensuring effective version control and collaboration throughout the project

## Test Case Development
The testing process ensures that the Boolean Logic Simulator operates as expected through comprehensive testing and thorough documentation. The focus is on developing robust test cases and automating the testing process.

Test Case Development: The first objective is to write comprehensive test cases for each logic gate (AND, OR, NOT, XOR). These test cases must cover all edge cases and typical use cases to verify the correctness of the logic gate functions. By ensuring all possible input combinations are tested, Team 3 will guarantee the reliability of the simulator's core logic.

Example: For the XOR gate, a test case would ensure that the function returns the correct output based on the following inputs:

Input (0, 0): Expected Output = 0
Input (0, 1): Expected Output = 1
Input (1, 0): Expected Output = 1
Input (1, 1): Expected Output = 0
By covering both matching and differing inputs, this test case ensures the XOR gate logic is working as expected.
Automated Testing: This is tasked with implementing automated tests to streamline the testing process. Automated tests will facilitate frequent and consistent testing of both the logic gate functions and the user interface. This will allow issues to be quickly identified and resolved as development progresses, ensuring continuous improvement and stability of the simulator. Automation also reduces the manual effort involved in testing, allowing for more efficient development workflows.

To ensure the functionality and reliability of the Boolean Logic Simulator, a comprehensive testing strategy was implemented. The testing process began with the creation of unit tests for each logic gate function, validating that they return the expected results for various inputs. For instance, tests for the AND gate confirmed that it returns 1 only when both inputs are 1, while the NOT gate was verified to return the inverse of the input. Integration tests were also performed by simulating user interactions with the command-line interface. This was done using the subprocess module to run the main script and capture outputs, allowing us to check if the CLI handles valid inputs correctly and provides appropriate error messages for invalid entries.

To manage this testing process with Git, the repository was initialized with git init, and a new branch named testing was created using git checkout -b testing. As tests were written and modified, changes were staged with git add . and committed using git commit -m "Add unit and integration tests". Throughout the testing phase, git status was used to monitor changes, and git log provided a history of commits. Once testing was complete and verified, the testing branch was merged into the main branch with git checkout main followed by git merge testing, ensuring that all tested features were integrated into the main codebase. This structured approach to testing and version control significantly improved the simulator's reliability and maintainability.

## Contribution Guide
The above assignment was given in a such a way that, the teamwork ability and the efficiency of the work is tested. Here are the contruitions showed by our team:
# Team 1 - Gate Logic Implementation: Assigned to Amogh
Implemented the core logic functions for the AND, OR, NOT, and XOR gates.
Ensured accurate and with efficient logical operations by testing edge cases and handling both valid and invalid inputs.

# Team 2 - Input Validation and CLI Interface: Assigned to Hemanth
Developed the input validation system to handle user inputs, ensuring they were restricted to binary values (0, 1).
Designed the Command Line Interface (CLI) for user interaction, making it intuitive and easy to use.

# Team 3 - Testing and Documentation: Assigned to Amogh
Designed comprehensive test cases for each logic gate, covering all possible input combinations and error conditions.
Collaborated closely with the other teams to troubleshoot and resolve any bugs during the testing phase. 
# Team 4 - Documentation : Assigned to Naresh and Abhishek
Documented usage instructions and examples, explaining how to use the simulator effectively.

# Amogh - Implemented basic gate logic functions and written the test cases along with examples.
# Hemanth - Developed the corresponding input validation and a simple CLI.
# Naresh - Responsible for writing the documentation of the whole process that was carried out by the team.
# Abhishek - Assisting Naresh with the documentation process.
# Likhith - Couldn't contribute much in the assignment due to system compactiblity issues

