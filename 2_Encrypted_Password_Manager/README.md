# Ecrypted Password Manager Project

#### Video Demo: [Watch On YouTube](https://youtu.be/VjGEL7_PVHg?si=xWLkP-EzNuK8WGQn)

#### Description:
This project implements a secure password manager using Python, allowing users to store and manage their passwords safely. It also encrypts passwords using Fernet encryption from the `cryptography` library for security. The application provides features to add new passwords, view existing ones, and generate strong passwords.

### Project Overview:
The password manager consists of the following components:

#### Files:
- **`project.py`**: Contains the main application code, including functions for managing passwords (`add`, `view`) and the main execution logic (`main`).
- **`test_project.py`**: Includes unit tests for functions in `project.py` to ensure functionality and error handling are properly tested.
- **`requirements.txt`**: Lists the dependencies required (`cryptography`, `rich`).

### Features:
- **Master Password:** Users set and verify a master password during the setup, which is crucial for encrypting and decrypting passwords.
- **Add Password:** Allows users to add new passwords securely. Passwords are encrypted and stored in a text file (`passwords.txt`).
- **View Passwords:** Decrypts and displays saved passwords in a formatted table using the `rich` library for enhanced console output.
- **Generate Password:** Provides an option to generate strong passwords with customizable length and character sets.

### Design Choices:
The project uses Fernet encryption for password security due to its strong encryption capabilities provided by the `cryptography` library. The `rich` library enhances the console output with styled tables and colored messages, improving user experience and readability.

### Testing:
Unit tests in `test_project.py` utilize `pytest` and mock objects (`unittest.mock`) to test key functionalities such as password encryption, decryption, and user input handling. These tests ensure robustness and reliability across different scenarios.

### Future Enhancements:
Potential future enhancements could include:
- Adding user authentication features beyond the master password (such as Two-Factor Authentication (2FA)).
- Incorporating automated backup and restore functionalities to prevent data loss and facilitate recovery in case of system failures.
- Implementing secure cloud storage options for passwords.
- Enhancing password generation with more complex algorithms.
- Implementing user profiles to manage multiple sets of passwords securely, allowing different access levels or permissions for each profile.

### Submission Details:
- **GitHub Username:** sagnikghosh03
- **edX Username:** sagnik_ghosh_03
- **City and Country:** Kolkata, India
- **Date of Recording:** 2024-07-18

This project was developed as part of the CS50P course, for the final project, leveraging Python programming concepts and cryptographic techniques learned throughout the course.

Feel free to reach out if you have any questions or suggestions for improvement!
