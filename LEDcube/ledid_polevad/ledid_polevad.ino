#include<Wire.h>

// TODO: Round/Stabalize the accelerator reads, to prevent shaking messing up lighting so much

const int MPU = 0x68;
double AcReads[3]; // To be able to use for-loops to set LED-values

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
  Wire.requestFrom(MPU, 6, true);

  // Read Accelerator data and set it up for calculations
  AcReads[1] = ((Wire.read() << 8 | Wire.read())); // AcX
  AcReads[2] = ((Wire.read() << 8 | Wire.read())); // AcY
  AcReads[0] = ((Wire.read() << 8 | Wire.read())); // AcZ

  // Send data to LED's
  for (int i = 0; i < sizeof(pins) / sizeof(int); i++) {
    double temp = ((1 - 2 * (i % 2)) * AcReads[i / 2] + 20000) / 1000;
    analogWrite(pins[i], temp * temp * temp / 270 * 1.5);
  }

  // For serial-plotter data -> Ctrl + Shift + L
  for (int i = 0; i < sizeof(pins) / sizeof(int); i++) {
    Serial.print(" ");
    double temp = ((1 - 2 * (i % 2)) * AcReads[i / 2] + 20000) / 1000;
    Serial.print(temp * temp * temp / 270 * 1.5);
  }
  Serial.println();
}
