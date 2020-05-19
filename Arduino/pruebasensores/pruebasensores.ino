const int Pressure_pin = A1; 
const int FlowIn_pin = A0;
const int servo_pin = 12;
const int servo_onoff = 11;


//llamar e inicializar el servo que abre y cierra la valvula del PEEP
#include <Servo.h>
Servo M;

//para contar el tiempo de ejecucion
unsigned long tiempo1 = 0;
unsigned long tiempo2 = 0;
unsigned long tiempo3 = 0;
unsigned long ct = millis();
unsigned long ct2 = millis();
//Variables leidas desde los sensores valores de 0 a 1023
int _P = 0; //presion cercana al paciente
int _FlowIn = 0;   //flujo que entra por sensor diferencial de presion
int _FlowOut = 0;  //flujo de salida calculado por caida de presion

//variables mapeadas desde el ADC a valores reales
int P = 0; 
int FlowIn = 0;

//variables calculadas
int FlowOut = 0;  //flujo que sale, calculado por la caida de presion durante la expiracion
int C = 1; //compliance
int V = 0; //volumen real calculado desde el sensor de flujo

//Variales de entrada del panel de control --- numericas
int RR = 10; //respiratory rate
int IE = 2; //inspiratory/expiratory rate
int AirFlow = 3; //Flow in inspiratory 
int PIP = 40;  //Inspirature Pressure  cmH2O
int PEEP = 10;  // end sxpiratory pressure cmH2O
int VT = 500;  //tidal volume en mL
int FO2 = 30;  //oxigen porcentual
int FT = 5;   //Flow trigger en ???

//variables que entran desde el panel, modos
int mode = 2; //modo de operacion CPAP=0, CMV=1, PCV=2, PSV =3 

//limites
int maxP = 50; //presion maxima
int lowP = 2; //low pressure
int lowMV = VT*RR-30; //minute-volume low

//variables calculadas en funcion de los parametros de entrada
int TimeIn = 1000*(60/RR)/(IE+1);
int TimeOut = TimeIn*IE; 

int t = 0; //variable del tiempo que va sumando
int Pi = 0; //presion en dt
//ESTADOS
boolean CONF = true; //CONFIGURACION, NO HAY VENTILACION PERO SE CUADRAN PARAMETROS COMPLETOS
boolean INICIANDO = false; //al iniciar la ventilacion inicia una inspiracion en la que se llena de aire todo el sistema hasta lograr PEEP
boolean EXP = false; //fase de expiracion sale aire
boolean HEXP = false;//fase de sostener el PEEP
boolean INS = false; // fase de inspiracion
boolean HINS = false;  //pase de sostener el PIP y Pplate

//POSICIONES SERVO VALVULAS 
int servoins = 90-45;
int servohold = 90;
int servoexp = 90+20;

/*
 * Inicio del setup
 */
void setup() {
  // initialize serial communications at 9600 bps:
  Serial.begin(115200);
  M.attach(servo_pin);
  INS = true;
  pinMode(servo_onoff, OUTPUT);
}

void readA(){
      _FlowIn = analogRead(FlowIn_pin);
      FlowIn = map(_FlowIn, 0, 1023, 0, 102);

      delay(10);
      t = t + 10;
      Serial.print("P = ");
      Serial.print(P);
      Serial.print("\t Fin = ");
      Serial.print(FlowIn);
      Serial.print("\t FOut = ");
      Serial.println(_FlowOut);
}

void loop() {
  mode = 2;
  _P = analogRead(Pressure_pin);
  P = map(_P,0,1023,0,101);
  
  _FlowIn = analogRead(FlowIn_pin);
  FlowIn = map(_FlowIn, 0, 1023, 0, 1000);
  
  //Calculo de flujo de salida
  if (EXP){
    FlowOut = (Pi-P);
    Pi = P;
  }
  else{
    FlowOut = 0;
  }
  //calculo del compliance
  if (HINS){
    C = V/P;
  }
  //calculo del volumen
  if (INS || HINS){
    V = V + FlowIn*(t-ct); //corregir
  }
  else if (EXP || HEXP){
    V = V + FlowIn*(t-ct) - FlowOut*(t-ct) ;
    //V = V + FlowIn*(t-ct) - C*(PIP-P) ;
  }


  t = millis();
  /*
   * Modo 1
   */
  if (mode == 1){ //modo de control por volumen completamente asistido
    if (INS && V >= VT){
      INS = false;
      HINS = true;
      EXP = false;
      HEXP = false;
    }
    else if (HINS && t >= (ct+ TimeIn)){
      INS = false;
      HINS = false;
      EXP = true;
      HEXP = false;
      ct = millis();
    }
    else if (EXP && P <= PEEP){
      INS = false;
      HINS = false;
      EXP = false;
      HEXP = true;
    }
    else if (HEXP && t >= (ct+ TimeOut)){
      INS = false;
      HINS = false;
      EXP = false;
      HEXP = true;
      ct = millis();
    }
  }
    /*
   * Modo 3
   */
  if (mode == 3){ //modo de control por presion accionado por el paciente
    if (INS && P >= PIP){
      INS = false;
      HINS = true;
      EXP = false;
      HEXP = false;
    }
    else if (HINS && t >= (ct+ TimeIn)){
      INS = false;
      HINS = false;
      EXP = true;
      HEXP = false;
      ct = millis();
    }
    else if (EXP && P <= PEEP){
      INS = false;
      HINS = false;
      EXP = false;
      HEXP = true;
    }
    else if (HEXP && P <= FT){ //cambiar flujo por presion
      INS = false;
      HINS = false;
      EXP = false;
      HEXP = true;
      ct = millis();
    }
  }
    /*
   * Modo 2
   */
  if (mode == 2){ //modo de control por presion completamente asistido.
    if (INS && P >= PIP){
      INS = false;
      HINS = true;
      EXP = false;
      HEXP = false;
    }
    else if (INS && t >= (ct+ TimeIn)){
      INS = false;
      HINS = false;
      EXP = true;
      HEXP = false;
      ct2 = millis();
    }
    else if (HINS && t >= (ct+ TimeIn)){
      INS = false;
      HINS = false;
      EXP = true;
      HEXP = false;
      ct2 = millis();
    }
    else if (EXP && P <= PEEP){
      INS = false;
      HINS = false;
      EXP = false;
      HEXP = true;
    }
    else if (EXP && t >= (ct2+ TimeOut)){
      INS = true;
      HINS = false;
      EXP = false;
      HEXP = false;
      ct = millis();
    }
    else if (HEXP && t >= (ct2+ TimeOut)){
      INS = true;
      HINS = false;
      EXP = false;
      HEXP = false;
      ct = millis();
    }
  }
  Serial.print(INS);
  Serial.print(HINS);
  Serial.print(EXP);
  Serial.println(HEXP);
  Serial.println(P);
  if (INS){
    M.write(servoins);
    
  }
  else if(EXP){
    M.write(servoexp);
  }
  else if(HEXP || HINS){
    M.write(servohold);
  }
}
