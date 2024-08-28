```markdown
## Setup

Follow these steps to set up the Philips Hue Lighting Demo on your local machine:

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the project directory:**
   ```bash
   cd philips-hue-lighting-demo
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Hue Bridge:**
   - Update the `bridge_ip` and `username` in `app/hue_api.py` with your Philips Hue bridge's IP address and username.

5. **Run the Flask App:**
   ```bash
   python app/main.py
   ```

6. **Access the Web Interface:**
   - Open your web browser and go to `http://localhost:5000`.

### Additional Setup for Mobile Usage

To use the application on mobile devices:

1. **Set Up Environment Variables:**
   - Create a `.env` file in the root of the React project.
   - Add the following line to specify your computer's IP address:
     ```bash
     REACT_APP_API_HOST=your.ip.addr.ess
     ```
   - Replace `your.ip.addr.ess` with the actual IP address of your computer where the Flask server is running.

2. **Restart the Development Server:**
   - After setting the environment variable, restart your React development server to apply the changes.
```

### Updated README.md

With the new **Setup** section added, here is the revised README structure:

```markdown
# Philips Hue Lighting Demo

## Setup

Follow these steps to set up the Philips Hue Lighting Demo on your local machine:

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the project directory:**
   ```bash
   cd philips-hue-lighting-demo
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Hue Bridge:**
   - Update the `bridge_ip` and `username` in `app/hue_api.py` with your Philips Hue bridge's IP address and username.

5. **Run the Flask App:**
   ```bash
   python app/main.py
   ```

6. **Access the Web Interface:**
   - Open your web browser and go to `http://localhost:5000`.

### Additional Setup for Mobile Usage

To use the application on mobile devices:

1. **Set Up Environment Variables:**
   - Create a `.env` file in the root of the React project.
   - Add the following line to specify your computer's IP address:
     ```bash
     REACT_APP_API_HOST=your.ip.addr.ess
     ```
   - Replace `your.ip.addr.ess` with the actual IP address of your computer where the Flask server is running.

2. **Restart the Development Server:**
   - After setting the environment variable, restart your React development server to apply the changes.

## New Feature: Circadian Rhythm Lighting Automation

This feature automates indoor lighting to sync with natural circadian rhythms, enhancing user well-being by simulating natural light cycles. 

### Goals:
- Automate lighting to align with natural circadian rhythms.
- Provide easy-to-use settings for customizing light timing.

### Implementation Steps:

1. **Timing Logic:** Develop the backend logic for circadian-based light timing.
2. **User Settings:** Create a simple UI for users to adjust light schedules.
3. **Integration:** Ensure smooth integration with existing lighting controls.
4. **Testing:** Test the automation feature in different scenarios.

### Usage:

- Open the web interface.
- Navigate to the new "Circadian Rhythm Lighting" section.
- Customize the light schedules as per your preference.

### Additional Notes:

- Focus on simplicity and user control.

Target completion: Next product update.
```
