# Philips Hue Lighting Demo

## Setup

1. Clone the repository.
2. Install the dependencies: `pip install -r requirements.txt`
3. Update the `bridge_ip` and `username` in `app/hue_api.py`.
4. Run the Flask app: `python app/main.py`
5. Access the web interface at `http://localhost:5000`.

### Additional Setup for Mobile Usage

To ensure the application works correctly on mobile devices, follow these steps:

1. **Set Up Environment Variables:**
   - Create a `.env` file in the root of the React project.
   - Add the following line to specify your computer's IP address:
     ```bash
     REACT_APP_API_HOST=your.ip.addr.ess
     ```
   - Replace `your.ip.addr.ess` with the actual IP address of your computer where the Flask server is running.

2. **Restart the Development Server:**
   - After setting the environment variable, restart your React development server to apply the changes.

## Usage

- Open the web interface.
- Click the buttons to activate different lighting scenes.

### Mobile Usage

- Ensure your mobile device is on the same network as the computer running the Flask server.
- Access the web interface using the IP address of the computer running the Flask server, e.g., `http://your.ip.addr.ess:3000`.
- The application should work seamlessly on mobile devices after following the additional setup steps.
