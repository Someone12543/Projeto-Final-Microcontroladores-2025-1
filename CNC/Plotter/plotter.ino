#include <AccelStepper.h>
#include <GFButton.h>
#include <Servo.h>

// =============================== Definição dos botões do home ===============================

GFButton botao_x(24);
GFButton botao_y(22);
bool zero_y = false;
bool zero_x = false;

// =============================== Definição das portas do shield ===============================

#define step_x 2
#define dir_x 5
#define step_y 3
#define dir_y 6
#define step_z 4
#define dir_z 7
#define EN 8

// =============================== Definicao dos motores ===============================

AccelStepper motor_x(AccelStepper::DRIVER, step_x, dir_x);
AccelStepper motor_y(AccelStepper::DRIVER, step_y, dir_y);
AccelStepper motor_z(AccelStepper::DRIVER, step_z, dir_z);  // O z é o segundo motor do eixo y

bool finished_x = false;
bool finished_y = false;

// =============================== Definicao dos servos ===============================


#define limit_servo 20
#define qtd_servos 3

Servo servos[qtd_servos];
int offsets[qtd_servos] = { 10, 0, -10 };
int servo_atual = 1;

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
  motor_x.setSpeed(50);
  motor_x.moveTo(dist);
  finished_x = false;
}

void move_y(int dist) {
  enable_y();
  motor_y.moveTo(dist);
  motor_z.moveTo(dist);

  finished_y = false;
}

void move_x_y(int distx, int disty) {
  move_x(distx);
  move_y(disty);
}

// =============================== Drawer plotter ===============================

int get_integer() {
  String dados = Serial.readStringUntil('\n');
  dados.trim();

  return dados.toInt();
}

unsigned long last_step = 0;
bool is_idle = true;

void move_posicao(String coordinates) {
  int pos = 0;
  int x = 0;

  while (coordinates[pos] != ',') {
    x = 10 * x + coordinates.substring(pos, pos + 1).toInt();
    pos++;
  }
  move_x(x);
  
  pos++;
  int y = 0;
  while (coordinates[pos] != ' ' && pos < coordinates.length()) {
    y = 10 * y + coordinates.substring(pos, pos + 1).toInt();
    pos++;
  }
  move_y(y);

  coordinates = coordinates.substring(pos + 1);

  while (!finished_y || !finished_x) {
    if (!motor_x.run()) {
      finished_x = true;
      motor_x.disableOutputs();
    }

    if (!run_y()) {
      finished_y = true;
      disable_y();
    }
  }

  // Cheguei na posição inicial
  Serial.println(String(x) + "," + String(y));
}

// =============================== Funcao de setup ===============================

void set_zero_x(GFButton& botaoDoEvento) {
  zero_x = true;
  Serial.println("Bateu X");
}

void set_zero_y(GFButton& botaoDoEvento) {
  zero_y = true;
  Serial.println("Bateu Y");
}

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

  Serial.begin(115200);
  while(!Serial);
  Serial.flush();
  Serial.setTimeout(1000);

  botao_x.setPressHandler(set_zero_x);
  botao_y.setPressHandler(set_zero_y);

  // Definindo os servos
  servos[0].attach(48);
  servos[1].attach(49);
  servos[2].attach(50);

  for (int i = 0; i < 3; i++) {
    if (i == servo_atual) continue;
    servos[i].write(180);
  }
  servos[servo_atual].write(limit_servo);

  // O x não está muito bom
  //  while (!zero_x) {
  //    if (Serial.available()) {
  //      String input = Serial.readString();
  //      input.trim();
  //      move_x(input.toInt());
  //      Serial.println(input.toInt());
  //    }
  ////    motor_x.move(-1);
  ////    motor_x.setSpeed(150);
  ////    motor_x.run();
  //    botao_x.process();
  //  }
  motor_x.setCurrentPosition(0);
  motor_x.setPinsInverted(true);

  // while (!zero_y) {
  //   if (Serial.available()) {
  //     break;
  //   }
  //   motor_y.move(-10);
  //   motor_z.move(-10);

  //   run_y();

  //   botao_y.process();
  // }
  motor_y.setCurrentPosition(0);
  motor_z.setCurrentPosition(0);
  
  last_step = millis();
}

// =============================== Funcao de loop ===============================

void loop() {
  for (int i = 0; i < 3; i++) {
    servos[i].write(180);
  }

  if (Serial.available()) {    
    is_idle = false;
    
    servos[servo_atual].write(180);
    
    delay(100);

    servo_atual = get_integer();

    while (!Serial.available());

    int qtd = get_integer();

    for (int i = 0; i < qtd; i++) {
      while (!Serial.available());

      String coordinates = Serial.readStringUntil('\n');
      coordinates.trim();

      // Setar a posição inicial
      finished_x = false;
      finished_y = false;

      if (i > 0) {
        servos[servo_atual].write(limit_servo);
      }
      move_posicao(coordinates);
      last_step = millis();
    }
  }

  if (millis() - last_step > 30000 && !is_idle) {
    is_idle = true;
    
    move_x(0);
    move_y(0);

    finished_x = false;
    finished_y = false;

    while (!finished_y || !finished_x) {
      if (!motor_x.run()) {
        finished_x = true;
        motor_x.disableOutputs();
      }
      
      if (!run_y()) {
        finished_y = true;
        disable_y();
      }
    }
  }
}
