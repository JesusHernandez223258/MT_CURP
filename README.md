# Generador de CURP con Máquina de Turing

Este proyecto consiste en una interfaz de usuario creada en Python con `Tkinter` para generar la CURP de una persona con base en la información proporcionada en un formulario. La CURP se genera a partir de una serie de datos personales que el usuario ingresa, y una máquina de Turing implementada en el programa se encarga de construirla conforme a las reglas definidas en México.

## Objetivo de la Actividad

La actividad tiene como objetivo desarrollar una interfaz de usuario que permita ingresar datos personales y genere la CURP de acuerdo con las siguientes instrucciones:

- Solicitar nombre, apellido paterno, apellido materno, fecha de nacimiento, sexo, y estado de nacimiento.
- Considerar Chiapas como el único estado disponible para selección en el formulario.
- Manejar correctamente los años bisiestos y los días correspondientes a cada mes (28, 30 o 31 días).
- Simular la asignación de los últimos dígitos de la CURP con caracteres aleatorios, imitando la asignación realizada por RENAPO.

## Funcionalidades Implementadas

- **Interfaz de Usuario**: Formulario diseñado con `Tkinter`, proporcionando un diseño limpio y sencillo.
- **Generación Parcial de CURP**: El programa ya puede construir la CURP usando los datos básicos ingresados por el usuario, incluyendo nombre, apellidos, fecha de nacimiento y estado.
- **Asignación de Estado y Sexo**: Basado en el estado seleccionado (Chiapas en este caso) y el sexo (Hombre/Mujer), se integra esta información en la CURP.

## Mejoras Pendientes

- **Validación de Fecha de Nacimiento**: Implementar validaciones para manejar correctamente los años bisiestos y los meses con días variables (28, 30 o 31 días).
- **Generación Aleatoria de Dígitos Finales**: Completar la generación de los últimos dígitos de la CURP de forma aleatoria.

## Uso

1. Ejecuta el programa en tu entorno local.
2. Ingresa los datos en el formulario, seleccionando nombre, apellidos, fecha de nacimiento, sexo y estado de nacimiento.
3. Haz clic en "Generar CURP" para que el sistema construya la CURP en base a los datos ingresados.

Este proyecto está diseñado para aprender y practicar el uso de interfaces gráficas en Python, así como la implementación de algoritmos simples que simulan el funcionamiento de una máquina de Turing para generar la CURP.
