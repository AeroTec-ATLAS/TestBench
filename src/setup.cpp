#include "header.h"

void start_LoadCells(void)
{
  byte loadcell_1_rdy = 0;
  byte loadcell_2_rdy = 0;

  while ((loadcell_1_rdy + loadcell_2_rdy) < 2){ //run startup, stabilization and tare, both modules simultaniously
    if (!loadcell_1_rdy) loadcell_1_rdy = LoadCell_1.startMultiple(stabilizing_time, true);
    if (!loadcell_2_rdy) loadcell_2_rdy = LoadCell_2.startMultiple(stabilizing_time, true);
   

    if (!loadcell_1_rdy) Serial.println("Timeout, check MCU>HX711 no.1 wiring and pin designations");
    if (!loadcell_2_rdy) Serial.println("Timeout, check MCU>HX711 no.2 wiring and pin designations");
    
    if ((loadcell_1_rdy + loadcell_2_rdy) < 2) delay(10000); //wait 10 seconds in case of error
  
  }
}

