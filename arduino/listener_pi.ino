  int green = 22;
  int blue = 23;
  int gray = 24;
  int inByte = 0;
  int partyMode = 0; //Obviously Andrew W.K's favorite mode
  int pinOff = 1; //define off as high or low
  int pinOn = 0; //define on as high or low
  int pollRate = 1000; //1,000 ticks per second

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(green,OUTPUT);
  pinMode(blue,OUTPUT);
  pinMode(gray,OUTPUT);
  digitalWrite(green,pinOff);
  digitalWrite(blue,pinOff);
  digitalWrite(gray,pinOff);
  portIdle();
}

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available() > 0) {
  inByte = Serial.read();
  if (inByte == 'G') { //green pin on
    Serial.println("GREEN");
    digitalWrite(green,pinOn);
    digitalWrite(blue,pinOff);
    digitalWrite(gray,pinOff);
    partyMode=0;
    }
  if (inByte == 'B') { //blue pin on
    Serial.println("BLUE");
    digitalWrite(green,pinOff);
    digitalWrite(blue,pinOn);
    digitalWrite(gray,pinOff);
    partyMode=0;
    }
  if (inByte == 'N') { //neutral pin on
    Serial.println("NEUTRAL");
    digitalWrite(green,pinOff);
    digitalWrite(blue,pinOff);
    digitalWrite(gray,pinOn);
    partyMode=0;
    }
  if (inByte == '0') { //all down state
    Serial.println("DOWN");
    digitalWrite(green,pinOff);
    digitalWrite(blue,pinOff);
    digitalWrite(gray,pinOff);
    partyMode=0;
    }
  if (inByte == 'P') { //when it's time to party, we party hard
    Serial.println("PARTY");
    digitalWrite(green,pinOff);
    digitalWrite(blue,pinOff);
    digitalWrite(gray,pinOff);
    partyMode=1;
    }
  } else {
  portIdle();
  }
}

void portIdle() {
  while(Serial.available() <= 0) {
    Serial.println("RELAYBOARD");   // signal to RPi that we are operational and ready
    delay(pollRate);
    if (partyMode > 0 ) {
     if (partyMode == 1) {
         digitalWrite(green,pinOff);
         digitalWrite(blue,pinOn);
         partyMode=2;
      } else {
         digitalWrite(green,pinOn);
         digitalWrite(blue,pinOff);
         partyMode=1;
      };
     }
    }
}

