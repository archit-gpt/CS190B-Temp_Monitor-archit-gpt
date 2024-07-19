# CS190B-Temp_Monitor-archit-gpt

This project involves developing a temperature monitoring system using a Raspberry Pi, DHT11 sensor, and MQTT protocol. The system features a responsive Single Page Application (SPA) interface built with React and provides real-time SMS alerts via the Clicksend API for efficient environmental control.

## Features
- **Real-Time Monitoring**: Continuously tracks temperature data using a DHT11 sensor connected to a Raspberry Pi.
- **MQTT Protocol**: Utilizes MQTT for reliable and efficient data transmission.
- **Responsive Web Interface**: Built with React, offering a user-friendly dashboard for monitoring temperature data.
- **SMS Alerts**: Sends real-time SMS notifications using the Clicksend API when temperature thresholds are breached.

## Technologies
- **Hardware**: Raspberry Pi, DHT11 sensor
- **Software**: Python, MQTT, React
- **APIs**: Clicksend SMS API

## Installation

### Hardware Setup
1. Connect the DHT11 sensor to the Raspberry Pi GPIO pins.
2. Ensure the Raspberry Pi is connected to the internet.

### Software Setup
1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/CS190B-Temp_Monitor-archit-gpt.git
    cd CS190B-Temp_Monitor-archit-gpt
    ```
2. Set up the virtual environment:
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```
3. Install the required Python packages:
    ```sh
    pip install -r requirements.txt
    ```
4. Set up the environment variables:
    ```sh
    cp .env.example .env
    ```
    Update the `.env` file with your configuration details (e.g., Clicksend API key, MQTT broker details).

5. Start the backend server:
    ```sh
    python server/app.py
    ```

### Frontend Setup
1. Navigate to the client directory:
    ```sh
    cd client
    ```
2. Install the required npm packages:
    ```sh
    npm install
    ```
3. Start the React application:
    ```sh
    npm start
    ```

## Usage
- Access the web interface at `http://localhost:3000` to monitor real-time temperature data.
- Configure alert thresholds and receive SMS notifications when thresholds are breached.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Feel free to submit issues and pull requests. Contributions are welcome!

## Acknowledgments

- Thanks to the developers of Raspberry Pi, DHT11, MQTT, React, and Clicksend for their excellent tools and services.

## Contact

For any questions or suggestions, feel free to contact me at [archit@ucsb.edu](mailto:archit@ucsb.edu).
