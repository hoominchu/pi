/*  The circuit:
 
 * LCD RS pin to digital pin 12
 * LCD Enable pin to digital pin 11
 * LCD D4 pin to digital pin 5
 * LCD D5 pin to digital pin 4
 * LCD D6 pin to digital pin 3
 * LCD D7 pin to digital pin 2
 * LCD R/W pin to ground
 * 10K resistor:
 * ends to +5V and ground
 * wiper to LCD VO pin (pin 3)
 
 */

// include the library code:
#include <LiquidCrystal.h>
//include the remote control library
#include <IRremote.h>

// command definition for Sony TV

#define TV_ON 0xa90
#define TV_CH_UP 0x090
#define TV_CH_DOWN 0x890
#define TV_VOL_UP 0x490
#define TV_VOL_DOWN 0xc90
#define TV_AV 0xA50

// command definition for BIG TV

#define SKY_ON 0xc0000c
#define SKY_CH_UP 0xc00020
#define SKY_CH_DOWN 0xc00021
#define SKY_VOL_UP 0xc00010
#define SKY_VOL_DOWN 0xc000011
#define MUTE 0xc0000d

#define DIG_0 0xc00000
#define DIG_1 0xc00001
#define DIG_2 0xc00002
#define DIG_3 0xc00003
#define DIG_4 0xc00004
#define DIG_5 0xc00005
#define DIG_6 0xc00006
#define DIG_7 0xc00007
#define DIG_8 0xc00008
#define DIG_9 0xc00009


String command;

int RECV_PIN = 11;

IRrecv irrecv(RECV_PIN);
IRsend irsend;

decode_results results;

// initialize the library with the numbers of the interface pins
LiquidCrystal lcd(12, 7, 5, 4, 6, 2);

const int switch1 = 9;
const int switch2 = 8;

int buttonstate1 = 0;
int buttonstate2 = 0;

int read_flag = 0;

void setup() {
  pinMode(switch1, INPUT);
  pinMode(switch2, INPUT);
  Serial.begin(9600);
  irrecv.enableIRIn();
  // set up the LCD's number of columns and rows: 
  lcd.begin(16, 2);
  // Print a message to the LCD.
  lcd.setCursor(4,0);
  lcd.print("Welcome!");
  delay(2000);
  lcd.clear();
  lcd.print("Voice controlled");
  lcd.setCursor(0,1);
  lcd.print("Universal Remote");
  delay(3000);
  lcd.clear();
  lcd.setCursor(0,0);
  lcd.print("SW1: RECV");
  lcd.setCursor(0,1);
  lcd.print("SW2: SEND");
  delay(1000);
  
}

void loop() {
  
  buttonstate1 = digitalRead(switch1);
  buttonstate2 = digitalRead(switch2);
  
  if((buttonstate1 == HIGH) && (buttonstate2 == LOW)){
    lcd.clear();
    lcd.setCursor(3,0);
    lcd.print("RECV mode");
    lcd.setCursor(3,1);    
    lcd.print("selected");
    read_flag = 1;
    delay(1000);
  }
  if((buttonstate1 == LOW) && (buttonstate2 == HIGH)){
    lcd.clear();
    lcd.setCursor(1,0);
    lcd.print("TRANSMIT mode");
    lcd.setCursor(3,1);    
    lcd.print("selected");
    delay(1000);
  }
  
  if(read_flag == 1){
    ir_recv();
  }else{
    while(1){
      lcd.clear();
      lcd.setCursor(0,0);
      lcd.print("Listening for");
      lcd.setCursor(3,1);    
      lcd.print("command");     
      if(Serial.available() > 0){
        command = Serial.readString();
       lcd.clear();
       lcd.setCursor(0,0);
       lcd.print("Command recieved");
       lcd.setCursor(3,1);    
       lcd.print(command);

        if(command == "TV_ON"){
          for (int i = 0; i < 3; i++){
            irsend.sendSony(TV_ON,12);
            delay(40);
          }
        }else if(command == "VOL_UP"){
          for (int i = 0; i < 3; i++){
            irsend.sendSony(TV_VOL_UP,12);
            delay(40);
          }
        }else if(command == "VOL_DOWN"){
          for (int i = 0; i < 3; i++){
            irsend.sendSony(TV_VOL_DOWN,12);
            delay(40);
          }
        }else if(command == "AV"){
          for (int i = 0; i < 3; i++){
            irsend.sendSony(TV_AV,12);
            delay(40);
          }
        }else if(command == "SKY_ON"){
          for (int i = 0; i < 3; i++){
            irsend.sendRC6(SKY_ON,24);
            delay(90);
          }
        }else if(command == "SKY_CH_UP"){
          for (int i = 0; i < 3; i++){
            irsend.sendRC6(SKY_CH_UP,24);
            delay(85);
          }
        }else if(command == "SKY_CH_DOWN"){
          for (int i = 0; i < 3; i++){
            irsend.sendRC6(SKY_CH_DOWN,24);
            delay(85);
          }
        }else if(command == "MUTE"){
          for (int i = 0; i < 3; i++){
            irsend.sendRC6(MUTE,24);
            delay(90);
          }
        }

//Copy from here
        
        else if(command == "DIG_0"){
          for (int i = 0; i < 3; i++){
            irsend.sendRC6(DIG_0,24);
            delay(90);
          }
        }
        else if(command == "DIG_1"){
          for (int i = 0; i < 3; i++){
            irsend.sendRC6(DIG_1,24);
            delay(90);
          }
        }
        else if(command == "DIG_2"){
          for (int i = 0; i < 3; i++){
            irsend.sendRC6(DIG_2,24);
            delay(90);
          }
        }
        else if(command == "DIG_3"){
          for (int i = 0; i < 3; i++){
            irsend.sendRC6(DIG_3,24);
            delay(90);
          }
        }
        else if(command == "DIG_4"){
          for (int i = 0; i < 3; i++){
            irsend.sendRC6(DIG_4,24);
            delay(90);
          }
        }
        else if(command == "DIG_5"){
          for (int i = 0; i < 3; i++){
            irsend.sendRC6(DIG_5,24);
            delay(90);
          }
        }
        else if(command == "DIG_6"){
          for (int i = 0; i < 3; i++){
            irsend.sendRC6(DIG_6,24);
            delay(90);
          }
        }
        else if(command == "DIG_7"){
          for (int i = 0; i < 3; i++){
            irsend.sendRC6(DIG_7,24);
            delay(90);
          }
        }
        else if(command == "DIG_8"){
          for (int i = 0; i < 3; i++){
            irsend.sendRC6(DIG_8,24);
            delay(90);
          }
        }
        else if(command == "DIG_9"){
          for (int i = 0; i < 3; i++){
            irsend.sendRC6(DIG_9,24);
            delay(90);
          }
        }

//Till here
        
        else{
          lcd.clear();
          lcd.print("Unknown command");
        }        
      }
      delay(500);
      
    }
  }
}
void ir_recv()
{
  while(read_flag){
      lcd.clear();
      lcd.print("Listening...");
      if (irrecv.decode(&results)) {
        lcd.clear();
        lcd.print(results.value, HEX);
        irrecv.resume();
      }
      delay(2000);
    }
}


 
  
