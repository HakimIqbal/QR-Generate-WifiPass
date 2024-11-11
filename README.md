# QR Code Generator for Wi-Fi Passwords

## Project Overview

This project is a Python script that generates a QR code containing Wi-Fi credentials. Users can scan this QR code with their smartphones to connect to a Wi-Fi network automatically. The output file is named according to the network name (SSID) for easier identification.

## Features

- Prompts users to input Wi-Fi network name (SSID) and password.
- Generates a QR code for the Wi-Fi connection.
- Saves the QR code as an image file named after the SSID.
- Displays the QR code for immediate scanning.

## Prerequisites

Ensure Python 3.x is installed on your system. You can check your Python version with:

```bash
python --version
```

## Installation Steps

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/HakimIqbal/QR-Generate-WifiPass.git
   cd QR-Generate-WifiPass
   ```

2. **Set Up a Virtual Environment**:

   ```bash
   python -m venv venv
   source venv/bin/activate

   # On Windows: venv\Scripts\activate
   ```

3. **Install Required Packages**:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the Python script:
   ```bash
   python generate_wifi_qr.py
   ```
2. Enter the Wi-Fi SSID and password when prompted.
3. The script will generate a QR code image and save it as `SSID_wifi_qr_code.png`.
4. The QR code image will be displayed for scanning.

## Requirements

Ensure the following Python packages are installed:

- `pyqrcode==1.2.1`
- `pypng==0.20220715.0`
- `Pillow==9.4.0` (optional, only needed for displaying images)

## Installing Packages Manually

To install the required packages individually, run:

```bash
pip install pyqrcode pypng pillow
```
