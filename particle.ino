



int ldr = A0; // This is where your photoresistor or phototransistor is plugged in. The other side goes to the "power" pin (below).

int ldrvalue; // Here we are declaring the integer variable analogvalue, which we will use later to store the value of the photoresistor or phototransistor.
int led = D7;;


int gas = A1; 

int gasvalue;











int ultrasonicvalue;
String ldr_string;

String gas_string;
String presence_string;


// defines pins numbers
const int trigPin = 0;
const int echoPin = 1;
// defines variables
long duration;
int distance;








 // Forward declaration

// Next we go into the setup function.

void setup() {
   
    
    
    // This is here to allow for debugging using the USB serial port
    Serial.begin();
    
    
    pinMode(led,OUTPUT);
    pinMode(trigPin, OUTPUT); // Sets the trigPin as an Output
    pinMode(echoPin, INPUT); // Sets the echoPin as an Input
    digitalWrite(led,LOW);
    // First, declare all of our pins. This lets our device know which ones will be used for outputting voltage, and which ones will read incoming voltage.
  

    // We are going to declare a Particle.variable() here so that we can access the value of the photosensor from the cloud.
    Particle.function("led",ledToggle);
    Particle.variable("ldr_mess", ldr_string);
    Particle.variable("gas_mess", gas_string);
    Particle.variable("presence_mess", presence_string);
    Particle.variable("ultrasonicvalue", &ultrasonicvalue, INT);
    
   
   
    // This is saying that when we ask the cloud for "analogvalue", this will reference the variable analogvalue in this app, which is an integer variable.

    // We are also going to declare a Particle.function so that we can turn the LED on and off from the cloud.
   
    // This is saying that when we ask the cloud for the function "led", it will employ the function ledToggle() from this app.

}


// Next is the loop function...

void loop() {
    
  
    
    
    
    
    
    // Clears the trigPin
digitalWrite(trigPin, LOW);
delayMicroseconds(2);
// Sets the trigPin on HIGH state for 10 micro seconds
digitalWrite(trigPin, HIGH);
delayMicroseconds(10);
digitalWrite(trigPin, LOW);
// Reads the echoPin, returns the sound wave travel time in microseconds
duration = pulseIn(echoPin, HIGH);
// Calculating the distance
distance= duration*0.034/2;
// Prints the distance on the Serial Monitor

    
    
    

    // check to see what the value of the photoresistor or phototransistor is and store it in the int variable analogvalue
    ldrvalue = analogRead(ldr);
    gasvalue = analogRead(gas);
   
    ultrasonicvalue = distance;
    
     if (20<=ultrasonicvalue){                             ///////////logic of selecting string to be told by alexa
     
     presence_string = "No , there is no one at the door .";
 }
 else if(ultrasonicvalue<20){
     presence_string = "yes , there is someone at the door .";
 }
 else {
     return ;
 }
    
    
    
    
    
    
     if (700<=ldrvalue && ldrvalue<1500){                             ///////////logic of selecting string to be told by alexa
     
     ldr_string = "light intensity here is moderate .";
 }
 else if(2000<ldrvalue){
     ldr_string = "its too bright here . light intensity is too high .";
 }
  else if(ldrvalue<=499){
     ldr_string = "its too dark here . light intensity is too low .";
 }
 else {
     return ;
 }
    
    
    
   if (1500<=gasvalue){                             ///////////logic of selecting string to be told by alexa
     
     gas_string = "there is LPG leakage in your house . take action quickly";
 }
 else if(gasvalue<1500){
     gas_string = "your house is completely safe . just relax";
 }
 else {
     return ;
 }

    // This prints the value to the USB debugging serial port (for optional debugging purposes)
   // Serial.printlnf("%d", ldrvalue);

    // This delay is just to prevent overflowing the serial buffer, plus we really don't need to read the sensor more than
    // 10 times per second (100 millisecond delay)
    delay(100);
    Serial.println(" *********************************** ");
    Serial.println("ldr");
    Serial.println(ldrvalue);
    Serial.println(" ");
    Serial.println("gas");
    Serial.println(gasvalue);
   
    Serial.println(" ");
    Serial.print("Distance: ");
    Serial.println(distance);
   
    Serial.println(" ");
    Serial.println(" *********************************** ");
}


int ledToggle(String command) {

    if (command=="on") {
    digitalWrite(led,HIGH);
    }
    else if (command=="off") {
    digitalWrite(led,LOW);
    }// Finally, we will write out our ledToggle function, which is referenced by the Particle.function() called "led"
}
