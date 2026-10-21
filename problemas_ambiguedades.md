# Problemas y ambigüedades del proyecto

## 1. Lectura del sensor de humedad

Todavía falta definir los valores exactos del sensor que se van a tomar como referencia para considerar que la tierra está seca o húmeda.

**Solución propuesta:** realizar pruebas con el sensor y ajustar el umbral según las lecturas obtenidas.

## 2. Nivel de agua del depósito

Es necesario definir cómo se interpretará la señal del sensor de nivel de agua y qué valor indicará que no hay suficiente agua.

**Solución propuesta:** comprobar el funcionamiento del sensor y establecer una condición clara para mantener apagada la bomba cuando el nivel sea bajo.

## 3. Funcionamiento manual y automático

Se debe definir cómo el usuario seleccionará el modo de funcionamiento y cómo solicitará el riego manual.

**Solución propuesta:** utilizar una opción en el programa para seleccionar el modo y comprobar que el riego manual respete la condición de disponibilidad de agua.

## 4. Comunicación con la Raspberry Pi Pico

Falta comprobar cómo se enviarán las lecturas y las órdenes entre el computador y la Raspberry Pi Pico mediante USB serial.

**Solución propuesta:** realizar pruebas de comunicación cuando se disponga de la placa y definir un formato sencillo para los mensajes.

## 5. Seguridad del circuito

Todavía falta comprobar la compatibilidad eléctrica de los componentes y el circuito que controlará la bomba.

**Solución propuesta:** revisar los voltajes y las corrientes de los componentes antes de realizar el montaje físico.

## 6. Pruebas físicas pendientes

Hasta el momento se han realizado pruebas de la lógica del programa en Python, pero todavía no se ha validado el sistema completo con los componentes físicos.

**Solución propuesta:** realizar pruebas por separado con la placa, los sensores y la bomba, y después comprobar el funcionamiento conjunto.

## 7. Estado general

Estos puntos quedan pendientes de definición o comprobación durante el desarrollo del proyecto. Las soluciones propuestas se verificarán a medida que se avance en la implementación.
