#include <WiFi.h>

const char* WIFI_SSID = "FamT&A";
const char* WIFI_PASS = "40186467";

const char* SERVER_ADDRESS = "192.168.0.111";
const int SERVER_PORT = 10000;

const int ECHO_PIN = 26;
const int TRIGGER_PIN = 27;

void setup() {
  Serial.begin(115200);

  Serial.print("Connecting to: ");
  Serial.println(WIFI_SSID);
  
  WiFi.begin(WIFI_SSID, WIFI_PASS);

  while ( WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print('.');
  }

  Serial.print("Local IP Address: ");
  Serial.println(WiFi.localIP());
}


long readUltrasonicDistance(int triggerPin, int echoPin)
{
  pinMode(triggerPin, OUTPUT);  // Clear the trigger
  digitalWrite(triggerPin, LOW);
  delayMicroseconds(2);
  //-Sets the trigger pin to HIGH state for 10 microseconds
  digitalWrite(triggerPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(triggerPin, LOW);
  pinMode(echoPin, INPUT);
  //- Reads the echo pin, and returns the sound wave travel time in microseconds
  return pulseIn(echoPin, HIGH);
}



void turnOnLed(int ledPin)
{
  pinMode(ledPin,OUTPUT);
  digitalWrite(ledPin,HIGH);
}
void turnOffLed(int ledPin)
{
  pinMode(ledPin,OUTPUT);
  digitalWrite(ledPin,LOW);
}

// To getting parts of a String
String getValue(String data1, char separator, int index)
{
  int found = 0;
  int strIndex[] = {0, -1};
  int maxIndex = data1.length()-1;

  for(int i=0; i<=maxIndex && found<=index; i++){
    if(data1.charAt(i)==separator || i==maxIndex){
        found++;
        strIndex[0] = strIndex[1]+1;
        strIndex[1] = (i == maxIndex) ? i+1 : i;
    }
  }

  return found>index ? data1.substring(strIndex[0], strIndex[1]) : "";
}

void fuction_command_LED( String message_of_LED){
  int rest_command_led= message_of_LED.toInt();
  int num_pin = rest_command_led / 10;
  int action_on_led = rest_command_led % 10;

  if(action_on_led){
    turnOnLed(num_pin);
  }else{
    turnOffLed(num_pin);
  }
}
void loop(){
  
  Serial.print("Connecting to: ");
  Serial.println(SERVER_ADDRESS);

  WiFiClient client;

  if (!client.connect(SERVER_ADDRESS, SERVER_PORT)) {
    Serial.println("Connection failed");
    delay(5000);
    return;
  }

  int cm = 0;
  String server_message;
  String command;
  String message_of_LED;

  while(true){
    
  if (client.available() > 0) {
      // receive message of server
      server_message = client.readString();
      command = getValue(server_message,' ',0);

        if (command == "LED"){
          message_of_LED = getValue(server_message,' ',1);          
          fuction_command_LED(message_of_LED);

        }else{
          if (command == "CLOSE"){
            client.stop();
            Serial.println("Closing Connection");
            delay(5000);
            return;
          }else{
            if (command == "DISTANCE"){
              cm = 0.01723 * readUltrasonicDistance(TRIGGER_PIN, ECHO_PIN);
              // Send message to server
              client.print(cm);
            }
           }
          }
        }
    }
}
