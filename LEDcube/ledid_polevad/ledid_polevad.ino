#include<Wire.h>

// TODO: Round/Stabalize the accelerator reads, to prevent shaking messing up lighting so much

const int MPU = 0x68;  // Memory address/serialBus reserved for communicating with gyro // Prolly translates to A4
double AcReads[3]; // For storing gyro values

const int pins[] = {3, 5, 6, 9, 10, 11}; // Pins used for LEDs
// Pin order: Top Bottom Front Back Left Right  -- I think (O_O)

void setup() {
  Wire.begin(); // Start sending data from from a wire
  Wire.beginTransmission(MPU); // Use MPU address to send data to gyro
  Wire.write(0x6B); // Initialize gyro
  Wire.write(0); // Stop bit
  Wire.endTransmission(true);
  Serial.begin(9600); // For custom logging/debugging
  for (int i = 0; i < 6; i++) { // Initialize LED pins for output
    pinMode(pins[i], OUTPUT);
  }
}


void loop() {
  Wire.beginTransmission(MPU); // Start communication on address/bus MPU
  Wire.write(0x3B); // Poke gyro
  Wire.endTransmission(false);
  Wire.requestFrom(MPU, 6, true); // Ask gyro for 6 bytes of accelerometer data

  // Read Accelerator data and set it up for calculations
  AcReads[1] = ((Wire.read() << 8 | Wire.read())); // AcX
  AcReads[2] = ((Wire.read() << 8 | Wire.read())); // AcY
  AcReads[0] = ((Wire.read() << 8 | Wire.read())); // AcZ
/*
  for (int i = 0; i < sizeof(pins) / sizeof(int); i++) {
    digitalWrite(pins[i], HIGH);
  }
  */

  /*
// get max LED
  int maxValue = 0;
  int maxIndex = 0;
  for (int i = 0; i < sizeof(pins) / sizeof(int); i++) {
    double temp = ((1 - 2 * (i % 2)) * AcReads[i / 2] + 20000) / 1000;
    if (temp > maxValue) {
      maxIndex = i;
      maxValue = temp;
    }
  }

// Send data to LED's
  for (int i = 0; i < sizeof(pins) / sizeof(int); i++) {
    if(i == maxIndex) {
        digitalWrite(pins[i], HIGH);    
      } else {
        digitalWrite(pins[i], LOW);    
      }
  }
  */
  
  for (int i = 0; i < sizeof(pins) / sizeof(int); i++) {
    double temp = ((1 - 2 * (i % 2)) * AcReads[i / 2] + 20000) / 1000;
    //analogWrite(pins[i], temp * temp * temp / 270 * 1.3);
    if(temp >= 30) {
      digitalWrite(pins[i], HIGH);
      
    } else {
      digitalWrite(pins[i], LOW);
    }
  }
  
 
  //Describing the for-loop above:
  /*
    analogWrite(pins[0], (((AcReads[0]+20000)/1000)^3/270)*1.3);
    analogWrite(pins[1], (((-AcReads[0]+20000)/1000)^3/270)*1.3);
    analogWrite(pins[2], (((AcReads[1]+20000)/1000)^3/270)*1.3);
    analogWrite(pins[3], (((-AcReads[1]+20000)/1000)^3/270)*1.3);
    analogWrite(pins[4], (((AcReads[2]+20000)/1000)^3/270)*1.3);
    analogWrite(pins[5], (((-AcReads[2]+20000)/1000)^3/270)*1.3);
  */

  // For serial-plotter data -> Ctrl + Shift + L
  for (int i = 0; i < sizeof(pins) / sizeof(int); i++) {
    Serial.print(" ");
    double temp = ((1 - 2 * (i % 2)) * AcReads[i / 2] + 20000) / 1000;
    Serial.print(temp);
    Serial.print(temp * temp * temp / 270 * 1.3);
  }
  Serial.println();
}
