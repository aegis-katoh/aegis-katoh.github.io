#define PIN 0
int ill = 0;

void setup() {
  Serial.begin(9600);
}

void loop() {
  ill = analogRead(PIN);
  Serial.println(ill);
  delay(100);
}
