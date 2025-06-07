#include <AccelStepper.h>

// =============================== Definição das portas do shield ===============================

#define step_x 2
#define dir_x 5
#define step_y 3
#define dir_y 6
#define step_z 3
#define dir_z 7
#define EN 8

// =============================== Definicao dos motores ===============================

AccelStepper motor_x(AccelStepper::DRIVER, step_x, dir_x);
AccelStepper motor_y(AccelStepper::DRIVER, step_y, dir_y);
AccelStepper motor_z(AccelStepper::DRIVER, step_z, dir_z); // O z é o segundo motor do eixo y

bool finished_x = false;
bool finished_y = false;

// =============================== Funcoes em Y ===============================

void enable_y() {
  motor_y.enableOutputs();
  motor_z.enableOutputs();
}

void disable_y() {
  motor_y.disableOutputs();
  motor_z.disableOutputs();
}

bool run_y() {
  motor_y.run();
  return motor_z.run();
}

// =============================== Funcoes de movimentacao ===============================

void move_x(int dist) {
  motor_x.enableOutputs();
  motor_x.moveTo(dist);
  finished_x = false;
}

void move_y (int dist) {
  enable_y();
  motor_y.moveTo(dist);
  motor_z.moveTo(dist);
  finished_y = false;
}

void move_x_y(int distx, int disty) {
  move_x(distx);
  move_y(disty);
}

// =============================== Funcao de setup ===============================

void setup() {
  // put your setup code here, to run once:
  motor_x.setEnablePin(EN);
  motor_x.setMaxSpeed(200.0);
  motor_x.setAcceleration(100.0);
  
  motor_y.setEnablePin(EN);
  motor_y.setMaxSpeed(200.0);
  motor_y.setAcceleration(100.0);
  
  motor_z.setEnablePin(EN);
  motor_z.setMaxSpeed(200.0);
  motor_z.setAcceleration(100.0);
  
  move_y(0);
  Serial.begin(9600);
  Serial.setTimeout(10);
}

// =============================== Funcao de loop ===============================

void loop() {
  // Isso foi usado para testar os movimentos dos motores -> Mover na diagonal
  if (Serial.available()) {
    String input = Serial.readString();
    input.trim();
    // Se o usuário digitou "xy (num)"
    if (input.startsWith("xy")) {
      input = input.substring(3);
      Serial.println(input.toInt());
      move_x_y(input.toInt(), input.toInt());
    } 
    // Se a pessoa digitou "x (num)" -> Mover só no x
    else if (input.startsWith("x")) {
      input = input.substring(2);
      Serial.println(input.toInt());
      move_x(input.toInt());
    } 
    // Se a pessoa digitou "y (num)" -> Mover só no y
    else if (input.startsWith("y")) {
      input = input.substring(2);
      Serial.println(input.toInt());
      move_y(input.toInt());
    }
  }

  if (!motor_x.run()) {
    if (!finished_x) {
      Serial.println("Terminou x");
      finished_x = true;
    }
    motor_x.disableOutputs();
  }
  
  if(!run_y()) {
    if (!finished_y) {
      Serial.println("Terminou y");
      finished_y = true;
    }
    disable_y();
  }
}
