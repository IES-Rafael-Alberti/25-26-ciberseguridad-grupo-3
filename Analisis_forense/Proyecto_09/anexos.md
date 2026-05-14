# Anexos Proyecto 9 — Caso Forense Digital

## Indice

- 1. [Metodologia](#metodologia)
- 2. [Herramientas Empleadas](#herramientas)
- 3. [Imagenes](#imagenes)
- 4. [Vestigios](#vestigios)
- 4.1. [vestigio 1: Transcripciones](#vestigio1)

---

## 1. Metodologia<div id='metodologia' />

El proceso de investigacion se estructuro en tres fases diferenciadas:

**Adquisicion de evidencias**

Se siguieron los criterios estandar de la forensia digital para garantizar la
integridad de cada artefacto:

1. Registro exacto de la fecha y hora de cada extraccion.
2. Minimizacion de la interaccion con los dispositivos analizados para evitar
   cualquier modificacion del estado original.
3. Recogida de evidencias respetando el orden de volatilidad.
4. Documentacion exhaustiva del proceso para asegurar su reproducibilidad por
   parte de cualquier otro perito.

**Preservacion y cadena de custodia**

Para cada evidencia se registro la siguiente informacion:

- Lugar, fecha y hora de descubrimiento y recogida.
- Identidad del responsable de la recogida y de cada acceso posterior.
- Condiciones y metodo de almacenamiento. Los dispositivos moviles se conservaron
  en bolsas de Faraday para impedir cualquier comunicacion inalambrica que pudiera
  comprometer su contenido.
- En caso de traspaso de custodia: nombre del nuevo responsable, fecha y hora,
  y verificacion de hashes para confirmar que no se ha producido alteracion alguna.

**Analisis**

Todas las actuaciones analiticas se llevaron a cabo respetando los principios de
metodicidad, auditabilidad, repetibilidad y defensa en juicio de cada conclusion.


## 4. Vestigios<div id='vestigios' />

## 4.1 Vestigio 1: Transcripcion de audios de echo<div id='vestigio1' />

| Archivo / fuente                         | Fecha UTC+9 | Hora UTC+9   | Texto registrado                                                     | Observación forense                                                                                              |
| ---------------------------------------- | ----------- | ------------ | -------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| 11.json 11.json                          | 2017-07-17  | 15:01:55.220 | turn on tv 11.json                                                   | Orden clara de encendido de TV. 11.json                                                                          |
| 10.json 10.json                          | 2017-07-17  | 15:06:03.907 | alexa 10.json                                                        | Activación previa a otra orden. 10.json                                                                          |
| 9.json 9.json                            | 2017-07-17  | 15:06:06.327 | turn on pandora 9.json                                               | Inicio de reproducción de Pandora. 9.json                                                                        |
| 8.json 8.json                            | 2017-07-17  | 15:12:39.818 | alexa how could you do this what are the flooding 8.json             | JSON conserva frase larga; Alexa solo interpretó formalmente What are the flooding?. 8.json                      |
| Historial visual aportado por el usuario | 2017-07-17  | 15:12 aprox. | alexa what do this to me stop we said we would what are you thinking | Posible evento adicional no integrado aún en la tanda de JSON ya revisada; conviene localizar su archivo exacto. |
| 6.json 6.json                            | 2017-07-17  | 15:12:58.358 | alexa 6.json                                                         | Nueva activación pocos segundos después. 6.json                                                                  |
| 5.json 5.json                            | 2017-07-17  | 15:13:02.196 | stop 5.json                                                          | Orden de detener reproducción o acción en curso. 5.json                                                          |
| 4.json 4.json                            | 2017-07-17  | 15:20:05.858 | alexa 4.json                                                         | Activación previa. 4.json                                                                                        |
| 3.json 3.json                            | 2017-07-17  | 15:20:07.632 | turn off tv 3.json                                                   | Orden clara de apagado de TV. 3.json                                                                             |
| 2.json 2.json                            | 2017-07-17  | 15:20:32.631 | alexa 2.json                                                         | Activación previa. 2.json                                                                                        |
| 1.json 1.json                            | 2017-07-17  | 15:20:34.384 | who yes, interpretado como Who is Yes? 1.json                        | Consulta de conocimiento, no domótica. 1.json                                                                    |