#include <SoftwareSerial.h>

// RX, TX pins for communication with Raspberry Pi
// Raspberry Pi TX (GPIO 14) should connect to Arduino RX (pin 10)
// Raspberry Pi RX (GPIO 15) should connect to Arduino TX (pin 11)
SoftwareSerial piSerial(10, 11); // RX, TX (Arduino pins for RPi communication)

void setup() {
  Serial.begin(9600);    // Initialize hardware serial for PC monitoring
  piSerial.begin(9600);  // Initialize software serial for Raspberry Pi communication

  delay(5000); // Give Raspberry Pi time to open the port

  Serial.println("Arduino is ready for communication via SoftwareSerial.");
  piSerial.println("Arduino ready."); // Send a ready message to Raspberry Pi as well
}

void loop() {
  // Check if data is available from Raspberry Pi (via SoftwareSerial)
  if (piSerial.available()) {
    // Read the incoming command until a newline character ('\n')
    String command = piSerial.readStringUntil('\n');
    command.trim(); // Remove leading/trailing whitespace (like '\r')

    // Print the received command to the PC Serial Monitor for debugging
    Serial.print("Received command from RPi: ");
    Serial.println(command);

    // Check if the received command is "A"
    if (command == "A") {
      // Send confirmation back to Raspberry Pi
      piSerial.println("Arduino: A command processed!");
      Serial.println("Processed 'A' command and sent response.");
    } else {
      // Handle unknown commands
      piSerial.print("Arduino: Unknown command received: ");
      piSerial.println(command);
      Serial.print("Unknown command received: ");
      Serial.println(command);
    }
  }

  // You can also add code here to send data periodically to RPi if needed
  // For example:
  // if (Serial.available()) { // If you type in Serial Monitor
  //   String pcCommand = Serial.readStringUntil('\n');
  //   pcCommand.trim();
  //   Serial.print("You typed: ");
  //   Serial.println(pcCommand);
  //   piSerial.print("PC command received: ");
  //   piSerial.println(pcCommand);
  // }
}