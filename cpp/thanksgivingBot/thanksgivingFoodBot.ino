#include <HCSR04.h>
int triggerPin = 6;
int echoPin = 7;
#define m1low 2
#define m1high 3
#define m2low 4
#define m2high 5
#define toss 6

UltraSonicDistanceSensor distanceSensor(triggerPin, echoPin);

// M1 is motor 1, which is on the left side
// M2 is motor 2, which is on the right side

void setup() {
  Serial.begin(9600); 
  pinMode(m1low, OUTPUT);
  pinMode(m1high, OUTPUT);
  pinMode(m2low, OUTPUT);
  pinMode(m2high, OUTPUT);
  pinMode(toss, OUTPUT);
}

void loop() {
  double distance = distanceSensor.measureDistanceCm();
  Serial.println(distance);
  while(distance >= 150){
    digitalWrite(toss, LOW);
    digitalWrite(m1high, HIGH);
    digitalWrite(m2low, HIGH);
    digitalWrite(m1low, LOW);
    digitalWrite(m2high, LOW);
    distance = distanceSensor.measureDistanceCm();
  }
  if(distance >= 5 && distance < 150){
    digitalWrite(toss, LOW);
    digitalWrite(m1low, LOW);
    digitalWrite(m2low, LOW);
    digitalWrite(m1high, HIGH);
    digitalWrite(m2high, HIGH);
    delay(500);
  }
  if(distance <= 5){
   digitalWrite(toss, LOW);
   digitalWrite(m1high, HIGH);
   digitalWrite(m2low, HIGH);
   digitalWrite(m1low, LOW);
   digitalWrite(m2high, LOW);
   delay(30000);
   digitalWrite(toss, LOW);
   digitalWrite(m1low, LOW);
   digitalWrite(m2low, LOW);    
   digitalWrite(m1high, LOW);
   digitalWrite(m2high, LOW);
  }
}
