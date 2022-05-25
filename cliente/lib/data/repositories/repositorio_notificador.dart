// -------------------------------------------------------------------------
//  Archivo: notifier_repository.dart
//  Capitulo: Estilo Microservicios
//  Autor(es): Perla Velasco & Yonathan Mtz. & Jorge Solís & Juventino Aguilar & Elías Emiliano & Jorge Díaz & Román Guzmán
//  Version: 3.0.0 Mayo 2022
//  Descripción:
//
//    Ésta clase define el uso de la conexión con un Microservicio externo.
//
//    A continuación se describen los métodos que se implementaron en ésta
//    clase:
//
//                                       Métodos:
//    +------------------------+--------------------------+--------------------+
//    |         Nombre         |        Parámetros        |        Función     |
//    +------------------------+--------------------------+--------------------+
//    |   sendNotification()   | - message: mensaje a     | - Utiliza la       |
//    |                        |   notificar              |   conexión con el  |
//    |                        |                          |   microservicio    |
//    |                        |                          |   para notificar   |
//    |                        |                          |   un mensaje       |
//    |                        |                          |   específico.      |
//    +------------------------+--------------------------+--------------------+
//    |   sendFile()           | - file: archivo en base  | - Utiliza la       |
//    |                        |   64 a enviar            |   conexión con el  |
//    |                        |                          |   microservicio    |
//    |                        |                          |   para enviar      |
//    |                        |                          |   el archivo de la |
//    |                        |                          |   póliza del       |
//    |                        |                          |   cliente          |
//    +------------------------+--------------------------+--------------------+
//
//
// -------------------------------------------------------------------------
import 'package:Cliente/data/providers/notificador_api.dart';
import 'package:http/http.dart' as http;

class RepositorioNotificador {
  final NotificadorAPI notifierAPI;

  RepositorioNotificador(this.notifierAPI);

  Future<http.Response> sendNotification(String message) async {
    http.Response response =
        await notifierAPI.enviarNotificacionTelegram(message);
    return response;
  }

  Future<http.Response> sendFile(String file) async {
    http.Response response =
        await notifierAPI.enviarArchivoTelegram(file);
    return response;
  }
}
