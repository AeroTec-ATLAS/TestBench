#include "header.h"


float calibration_value_1 = 0; // Load Cell 1 calibration Value 
float calibration_value_2 = 0; // Load Cell 2 calibration Value 
float calibration_value_3 = 0; // Load Cell 3 calibration Value 


void setup()
{ // Make builtin led blink whilw setup is running
  Serial.begin(9600);

  /* ADXL345 Configuration */
  while(!ACCEL_sensor.begin()){               // Initialize ADXL345 sensor
    Serial.println("Ooops, no ADXL345 detected ... Check your wiring!");
    delay(10000);
  }
  ACCEL_sensor.setRange(ADXL345_RANGE_16_G);  // Set the range of the accelerometer measurement 
  ACCEL_sensor.getEvent(&accel_raw_data);     // Get forrection factor for the data from the ADXL345 sensor

  /* HX711 Configurations */
  LoadCell_1.begin();  // initialise LoadCell 1
  LoadCell_2.begin();  // Initialise LoadCell 2
  //LoadCell_1.setReverseOutput(); //uncomment to turn a negative output value to positive
  //LoadCell_2.setReverseOutput(); //uncomment to turn a negative output value to positive
  start_LoadCells();
  LoadCell_1.setCalFactor(calibrationValue_1); // user set calibration value (float)
  LoadCell_2.setCalFactor(calibrationValue_2); // user set calibration value (float)

  /* MLX90614 Configurations */
  EscSensor.begin(EscSensor_addr);
  EscSensor.begin(MotorSensor_addr);

  delay(stabilizing_time); // delay for stabilization

  Serial.println("Motor test is ready to start");
  Serial.write("1")
}

void loop()
{
  float RPM = read_RPM(RPM_PIN);

  sensors_event_t ACCELERATION = read_ACCEL();
  float acceleration_x = ACCELERATION.acceleration.x;
  float acceleration_y = ACCELERATION.acceleration.y;
  float acceleration_z = ACCELERATION.acceleration.z;
  float acceleration_total = sqrt(pow(acceleration_x, 2) + pow(acceleration_y, 2) + pow(acceleration_z, 2));

  float thrust = read_THRUST();
  float torque = read_TORQUE();

  float escTemperature = read_TEMPERATURE_C(ESC);
  float motorTemperature = read_TEMPERATURE_C(MOTOR);

  // Send sensor values to Python script as integers separated by commas and terminated by newline
  Serial.print(thrust);
  Serial.print(",");
  Serial.print(torque);
  Serial.print(",");
  Serial.print(RPM);
  Serial.print(",");
  Serial.print(acceleration_total);
  Serial.print(",");
  Serial.print(motorTemperature);
  Serial.println();  // Newline character indicates the end of the data

}
