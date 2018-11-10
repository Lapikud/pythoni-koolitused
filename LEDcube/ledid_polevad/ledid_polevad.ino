#include<Wire.h>

// TODO: Round/Stabalize the accelerator reads, to prevent shaking messing up lighting so much

const int MPU = 0x68;
double Tmp, GyX, GyY, GyZ; // Set-up  read data values
double AcReads[6]; // To be able to use for-loops to set LED-values

const int pins[] = {3, 5, 6, 9, 10, 11}; // Pins in use
// Pin order: Top Bottom Front Back Left Right  -- I think (O_O)

void setup() {
  Wire.begin();
  Wire.beginTransmission(MPU);
  Wire.write(0x6B);
  Wire.write(0);
  Wire.endTransmission(true);
  Serial.begin(9600);
  for (int i = 0; i < 6; i++) {
    pinMode(pins[i], OUTPUT);
  }
}
void loop() {
  Wire.beginTransmission(MPU);
  Wire.write(0x3B);
  Wire.endTransmission(false);
  Wire.requestFrom(MPU, 14, true);

  double AcXoff, AcYoff, AcZoff; // Fix readings

  // Acceleration data correction
  AcXoff = -950;
  AcYoff = -300;
  AcZoff = 0;

  // Read Accelerator data and set it up for calculations
  AcReads[1] = ((Wire.read() << 8 | Wire.read()) + AcXoff+20000)/1000; // AcX
  AcReads[2] = ((Wire.read() << 8 | Wire.read()) + AcYoff+20000)/1000; // AcY
  AcReads[0] = ((Wire.read() << 8 | Wire.read()) + AcZoff+20000)/1000; // AcZ

  // Send data to LED's
  for (int i = 0; i < sizeof(pins) / sizeof(int); i++) {
    analogWrite(pins[i], ((1 - 2 * (i % 2))*(AcReads[i/2]*AcReads[i/2]*AcReads[i/2])/270);
  }

  /*
    Explaining the for-loop above:
        
    analogWrite(pins[0], (((AcReads[0] + 20000) / 157)));
    analogWrite(pins[1], (((-AcReads[0] + 20000) / 157)));
    analogWrite(pins[2], (((AcReads[1] + 20000) / 157)));
    analogWrite(pins[3], (((-AcReads[1] + 20000) / 157)));
    analogWrite(pins[4], (((AcReads[2] + 20000) / 157)));
    analogWrite(pins[5], (((-AcReads[2] + 20000) / 157)));
  */

  // For serial-plotter data -> Ctrl + Shift + L
  /*
    Serial.print(" Top : "); Serial.print(((AcReads[0] + 20000) / 157));
    Serial.print(" Bottom: "); Serial.print(((-AcReads[(int)1/2] + 20000) / 157));
    Serial.print(" Back: "); Serial.print(((AcReads[(int)2/2] + 20000) / 157));
    Serial.print(" Front: "); Serial.print(((-AcReads[(int)3/2] + 20000) / 157));
    Serial.print(" Right: "); Serial.print(((AcReads[(int)4/2] + 20000) / 157));
    Serial.print(" Left: "); Serial.println(((-AcReads[(int)5/2] + 20000) / 157));
  */

  // Read temperature data so accelerator data would read be from the right place
  Tmp = (Wire.read() << 8 | Wire.read());

  // Read gyro data so accelerator data would read be from the right place
  GyX = (Wire.read() << 8 | Wire.read());
  GyY = (Wire.read() << 8 | Wire.read());
  GyZ = (Wire.read() << 8 | Wire.read());
}
