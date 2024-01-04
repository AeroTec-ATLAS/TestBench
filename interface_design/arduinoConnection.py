void setup() {
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    // Read the incoming message
    String message = Serial.readStringUntil('\n');

    // Parse the message
    int flag1 = message.charAt(0) - '0';
    int flag2 = message.charAt(2) - '0';

    // Handle the flags (replace with your logic)
    if (flag1 == 1) {
      // Do something for flag1 = 1
    }

    if (flag2 == 1) {
      // Do something for flag2 = 1
    }
  }

  // Your other loop logic here
}


--------------------------------
void setup() {
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    // Read the incoming message
    String message = Serial.readStringUntil('\n');

    // Parse the message
    int flag1 = message.charAt(0) - '0';
    int flag2 = message.charAt(2) - '0';

    // Handle the flags (replace with your logic)
    if (flag1 == 1) {
      // Do something for flag1 = 1
    }

    if (flag2 == 1) {
      // Do something for flag2 = 1
    }

    // Prepare and send the response
    int responseValues[10];
    // Replace the following with your logic to generate the response values
    for (int i = 0; i < 10; ++i) {
      responseValues[i] = random(15001);  // Replace with your logic
    }

    // Send the response as a comma-separated string
    for (int i = 0; i < 10; ++i) {
      Serial.print(responseValues[i]);
      if (i < 9) {
        Serial.print(",");
      }
    }
    Serial.println();  // Terminate the response

  }

  // Your other loop logic here
}
