// -------------------------------------------------------------------------
//  Archivo: notifier_api.dart
//  Capitulo: Estilo Microservicios
//  Autor(es): Perla Velasco & Yonathan Mtz. & Jorge Solís & Juventino Aguilar & Elías Emiliano & Jorge Díaz & Román Guzmán
//  Version: 3.0.0 Mayo 2022
//  Descripción:
//
//    Ésta clase define la conexión con un Microservicio externo.
//
//    A continuación se describen los métodos que se implementaron en ésta
//    clase:
//
//                                       Métodos:
//    +------------------------+--------------------------+--------------------+
//    |         Nombre         |        Parámetros        |        Función     |
//    +------------------------+--------------------------+--------------------+
//    |   sendNotification()   | - message: mensaje a     | - Realiza el       |
//    |                        |   notificar              |   envió de la      |
//    |                        |                          |   notificación a   |
//    |                        |                          |   través del       |
//    |                        |                          |   Microservicio de |
//    |                        |                          |   notificaciones   |
//    +------------------------+--------------------------+--------------------+
//    |enviarArchivoTelegram() | - file: archivo en base  | - Realiza el       |
//    |                        |   64 a enviar            |   envió del        |
//    |                        |                          |   archivo que      |
//    |                        |                          |   contiene la      |
//    |                        |                          |   poliza del       |
//    |                        |                          |   cliente a través |
//    |                        |                          |   del Microservicio|
//    |                        |                          |   de notificaciones|
//    +------------------------+--------------------------+--------------------+
//
//
// -------------------------------------------------------------------------
import 'dart:convert';

import 'package:flutter_dotenv/flutter_dotenv.dart';
import 'package:http/http.dart' as http;

class NotificadorAPI {
  final String gatewayHost = dotenv.env['GATEWAY_HOST'] ?? "localhost";
  final String gatewayPort = dotenv.env['GATEWAY_PORT'] ?? "8080";
  final Map<String, String> headers = {
    "Content-Type": "application/json",
    "Accept": "application/json"
  };

  Future<http.Response> enviarNotificacionTelegram(String message) async {
    Map<String, dynamic> request = {"message": message};
    String endpoint = "/notificador/telegram";
    String baseUrl = "$gatewayHost:$gatewayPort";
    var response = await http.post(
      Uri.http(baseUrl, endpoint),
      body: jsonEncode(request),
    );
    return response;
  }

  Future<http.Response> enviarArchivoTelegram(String file) async {
    Map<String, dynamic> request = {"file": file};
    String endpoint = "/notificador/telegram";
    String baseUrl = "$gatewayHost:$gatewayPort";
    var response = await http.post(
      Uri.http(baseUrl, endpoint),
      body: jsonEncode(request),
    );
    return response;
  }
}
