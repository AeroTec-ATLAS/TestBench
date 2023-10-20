#include "header.h"


/*******************************************************/
/***************  MEASUREMENT FUNCTIONS  ***************/
/*******************************************************/

/******************* RPM MEASUREMENT *******************/
int read_RPM(int sensor_pin)  // Uses RPM_PIN 
{
    counter = 0;                                // Reset the pulse counter
    unsigned long previousTime = millis();     // Save the time before test

    attachInterrupt(digitalPinToInterrupt(sensor_pin), countPulses, RISING);  // attatch Interupt Servide Routine
    delay(test_time);                                                      // Measure number of pulses for 10 miliseconds
    detachInterrupt(digitalPinToInterrupt(sensor_pin));                       // attatch Interupt Servide Routine   
  
    unsigned long currentTime = millis();    // Save time after test
    unsigned int RPM = (counter) / ((currentTime - currentTime) * milisec_min_factor);  // Compute RPM
  
    return RPM;

}

/************** ACCELERATION MEASUREMENT ***************/
sensors_event_t read_ACCEL(void) 
{
  /* Create sensor event */ 
  sensors_event_t event;

  /* Read data from the sensor */
  ACCEL_sensor.getEvent(&event);

  /* Apply correction factor to the data colected*/
  event.acceleration.x -= accel_raw_data.acceleration.x;
  event.acceleration.y -= accel_raw_data.acceleration.y;
  event.acceleration.z -= accel_raw_data.acceleration.z;

  return event;

}

/***************** THRUST MEASUREMENT ******************/
float read_THRUST() // Using Load Cell 1.
{
  
  float data_sum = 0;

  for (int i = 0; i < n_samples; i++)   // take n_samples samples
    data_sum += LoadCell_1.getdata(); //the value given by getdata() is in kilograms

  return 2 * data_sum / n_samples;    // compute thrust
  
}

/***************** TORQUE MEASUREMENT ******************/
float read_TORQUE() // Using load cell 2
{
  float data_sum = 0;

  for (int i = 0; i < n_samples; i++) // take n_samples samples
    data_sum += LoadCell_2.getdata();

   // vynary = arm * force
  return (data_sum / n_samples) * (2 * loadCell_arm); //calculate torque
}

/************** TEMPERATURE MEASUREMENT ****************/
float read_TEMPERATURE_C(int sensor)
{
  if (sensor == ESC)
    return EscSensor.readAmbientTempC();
  
  if (sensor == MOTOR)
    return MotorSensor.readAmbientTempC();
  
  return 0; // in case no sensor is specified

}
