import pyqrcode

# Prompt the user for Wi-Fi details
ssid = input("Enter the Wi-Fi SSID (network name): ")
password = input("Enter the Wi-Fi password: ")
auth_type = "WPA/WPA2"  # Change this to "WEP" if needed, or leave as "WPA" for most networks

# Create the Wi-Fi QR code format string
wifi_config = f"WIFI:T:{auth_type};S:{ssid};P:{password};;"

# Generate the QR code
qr = pyqrcode.create(wifi_config)

# Modify the output filename to use the SSID (replace spaces with underscores for file safety)
output_filename = f"{ssid.replace(' ', '_')}_qrcode.png"

# Use png() method to save the QR code as a PNG file
# scale argument controls the size of the QR code
qr.png(output_filename, scale=8)

# Display the QR code image
qr.show()
