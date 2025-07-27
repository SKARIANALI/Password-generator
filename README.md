# Python Password Generator 🔐

A versatile and secure password generator built with Python. This project provides three different interfaces: a simple command-line script, a user-friendly GUI application, and a powerful CLI tool with advanced options.

## Features ✨

* **Strong & Secure:** Generates passwords that are cryptographically secure using Python's `random` module.
* **Guaranteed Complexity:** Ensures every password contains at least one uppercase letter, one lowercase letter, one number, and one symbol.
* **Multiple Interfaces:**
    * **Simple Script:** A basic, interactive prompt for generating a password.
    * **GUI Application:** An easy-to-use graphical interface built with Tkinter, featuring a "copy to clipboard" function.
    * **Advanced CLI:** A command-line tool built with `argparse` for power users and automation, allowing you to specify length, number of passwords, and save to a file.
* **No External Dependencies:** Runs on a standard Python 3 installation.

## Getting Started

To get a local copy up and running, follow these simple steps.


## Usage

This project includes two different scripts. Choose the one that best fits your needs.

### 1. GUI Application (`password_gui.py`)

For a more visual experience, run the GUI application.

```sh
python password_gui.py
```
This will launch a window where you can:
* Select the password length using a spinbox.
* Click "Generate Password" to create a new password.
* Click "Copy to Clipboard" to easily copy the generated password.

 ### 2. Advanced CLI Tool (`password_cli.py`)

The most powerful and flexible version, perfect for scripting and automation.

**Syntax:**
`python password_cli.py <length> [options]`

**Examples:**

* **Generate a single 16-character password:**
    ```sh
    python password_cli.py 16
    ```

* **Generate 5 passwords, each 12 characters long:**
    ```sh
    python password_cli.py 12 -c 5
    ```
    *(or `python password_cli.py 12 --copies 5`)*

* **Generate a 20-character password and save it to a file named `passwords.txt`:**
    ```sh
    python password_cli.py 20 -s passwords.txt
    ```
    *(or `python password_cli.py 20 --save passwords.txt`)*

* **View all available options and help:**
    ```sh
    python password_cli.py -h
    ```


This README was created for a beginner-friendly Python project. 
