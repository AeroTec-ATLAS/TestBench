#ifndef HEADER
#define HEADER

/**************************************************************************************************************  
    Important Note:

    Forces Measurement:
        In this project, it is used 2 load cells, respectively called loadcell 1 and loadcell 2
        -  Load cell 1 will be used to compute thrust
        -  Load cell 2 and 3 will be used to compute binary

        - Load cells communicate with the HX711 amplifier, which communicates with arduino using I2C protocol
            -   Load Cell 1
            -   Load Cell 2

    RPM Measurement:
        In this project, it is used 1 TCRT5000 infrared module to compute motor speed
    
    Vibration Measurement:
        In this project, it is used 1 ADXL345 accelerometer to measure vibrations of the motor

    Temperature Measurement:
        In this project, it is used 2 MLX90614 temperature, respectively called EscSensor e MotorSensor
        - EscSensor will be used to measure Esc temperature 
        - MotorSensor will be used to measure Motor temperature
    
    Eletrical Measurement:
**************************************************************************************************************/

/******************* Definitions  *******************/
#define ESC 0
#define MOTOR 1

/***************  Library inclusions  ***************/
#include <Arduino.h>
#include <math.h>
#include <EEPROM.h>             // Used for accessing arduino EEPROM memory
#include <Wire.h>               // Used for I2C communication

#include <HX711_ADC.h>          // Used for communicating with the HX711 amplifier
#include <Adafruit_Sensor.h>    // Used for creating an unified sensor abstraction layer
#include <Adafruit_MLX90614.h>  // Used for communicating with the MLX90614 temperature sensor
#include <Adafruit_ADXL345_U.h> // Used for communicating with the ADXL345 accelerometer 

/**********  EEPROM ADDRESSES DEFINITION ***********/

double motor_address = 0x1A;
double esc_address  = 0x1B;

double calibration_factor_load_cell_1_addr = 0x1C;
double calibration_factor_load_cell_2_addr = 0x1D;

double esc_emissivity_addr = 0x1E;
double motor_emissivity_addr = 0x1F; 

/****************** I2C ADDRESSES *****************/
const int accel_addr = 0x53;
const int EscSensor_addr = 0x5A;
const int MotorSensor_addr = 0x5B;

/***************  PINOUT DEFINITION ***************/
const int RPM_PIN = 2;        // Pin of the  TCRT5000 Infrared Module (Used to measure Motor Rotational Speed (RPM))
const int LoadCell_1_DT = 5;  // Pin of the Data wire of Load Cell 1
const int LoadCell_1_SCK = 6; // Pin of the Clock wire of Load Cell 1
const int LoadCell_2_DT = 10; // Pin of the Data wire of Load Cell 2
const int LoadCell_2_SCK = 11;// Pin of the Clock wire of Load Cell 2

/***************  CONSTRUCTORS DEFINITION ***************/
Adafruit_MLX90614 EscSensor = Adafruit_MLX90614();
Adafruit_MLX90614 MotorSensor = Adafruit_MLX90614();
Adafruit_ADXL345_Unified ACCEL_sensor = Adafruit_ADXL345_Unified(accel_addr); // Constructor for communicating with accelerometer
HX711_ADC LoadCell_1(LoadCell_1_DT, LoadCell_1_SCK); // Constructor for communicating with LoadCell 1 using the amplifier
HX711_ADC LoadCell_2(LoadCell_2_DT, LoadCell_2_SCK); // Constructor for communicating with LoadCell 2 using the amplifier

/***************  GLOBAL VARIABLES ***************/
volatile int counter = 0;                   // Counter for reflective band interruptions
const int n_samples = 10;                   // Number of samples to compute average 
const int loadCell_arm = 3;                 // Distence of the loadcell 2 to the motor to compute torque
const int test_time = 10;                   // Duration of mesurement tests, in miliseconds
const float milisec_min_factor = 1/60000;   // Correction factor for converting miliseconds to minutes
const unsigned stabilizing_time = 3000;     // Used for estabilization time during the code
sensors_event_t accel_raw_data;             // Correcting factor for the data from the ADXL345 sensor


/************* FUNDAMENTAL FUNCTIONS *************/
void countPulses() {
    counter++;
}


/******* MEaSUREMENT FUNCTIONS DECLERATION *******/
int read_RPM(int sensor_pin);
sensors_event_t read_ACCEL(void);
float read_THRUST();
float read_TORQUE();
float read_TEMPERATURE_C(int sensor);
void start_LoadCells(void);


#endif