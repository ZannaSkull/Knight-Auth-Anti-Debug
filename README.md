# Knight Auth

<p align="center">
<img src="https://i.pinimg.com/736x/2d/22/80/2d228083f7aca7f166404869712a96a1.jpg", width="500", height="500">
</p>

Knight Auth is a Python-based authentication script with anti-debug features. It prompts users for a username and key, validates them against a remote source, and logs successful access attempts to a Discord webhook.

## Features

*   **Authentication:** Verifies user credentials against a list fetched from a remote raw file.
*   **Anti-Debug:** Terminates processes associated with debugging tools.
*   **Discord Logging:** Sends successful login attempts, including username, key, and IP address, to a Discord webhook.
*   **Clear UI:** Provides a simple command-line interface for login and exit options.
*   **Attempt Limiter:** Limits login attempts before exiting.

## Requirements

*   Python 3.x
*   `colorama`
*   `pywin32`
*   `requests`
*   `psutil`

## Setup

1.  **Install Dependencies:** Ensure all required Python packages are installed.
2.  **Configure Webhook:** Replace the `Cipolle` variable with your Discord webhook URL.
3.  **Set Raw File URL:** Modify the `Knight` variable to point to the raw file containing the username:key pairs.
4.  **Adjust Attempts:** Modify the `ImNotAFullStackDev` to set your prefered number of login attempts.

## Usage

1.  Run the script:

    ```
    python Knight Auth Anti-Debug.py
    ```

2.  The script will display a menu with options to Login or Exit.
3.  If you choose to log in, you will be prompted for a username and key.
4.  The script will validate the credentials and provide feedback.

## Code Explanation

*   **Imports:** Imports necessary libraries for console styling, Windows API interaction, HTTP requests, process management, and more.
*   **Global Variables:** Defines the Discord webhook URL (`Cipolle`), the URL for the raw file containing valid credentials (`Knight`), and the maximum number of login attempts (`ImNotAFullStackDev`).
*   **`check_anti_debug()` Function:** Iterates through running processes and terminates any that match predefined anti-debug tools.
*   **`login()` Function:** Prompts the user for a username and key, retrieves valid credentials from the raw file, and validates the input.
*   **`NonHoUnaTipaFissaMaMiStaBene()` Function:** Sends a POST request to the Discord webhook with login information.
*   **`Sussena()` Function:** Retrieves the external IP address of the user.
*   **`authenticate()` Function:** Manages the login attempt process, limiting the number of tries.
*   **Main Loop:** Displays the main menu and handles user input for login or exit.

## Notes

*   The script uses `win32api` and `win32process`, which are specific to Windows.
*   Ensure the raw file containing usernames and keys is properly formatted (username:key on each line).
*   The anti-debug feature may not be comprehensive and can be bypassed.
*   Consider implementing more robust security measures for production environments.
*   Replace `Knight Auth Anti-Debug.py` with the actual name of your Python script.
