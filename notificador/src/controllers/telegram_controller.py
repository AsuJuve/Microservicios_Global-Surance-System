##!/usr/bin/env python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------
# Archivo: telegram_controller.py
# Capitulo: Estilo Microservicios
# Autor(es): Perla Velasco & Yonathan Mtz. & Jorge Solís
# Version: 3.0.0 Febrero 2022
# Descripción:
#
#   Ésta clase define el controlador del microservicio API. 
#   Implementa la funcionalidad y lógica de negocio del Microservicio.
#
#   A continuación se describen los métodos que se implementaron en ésta clase:
#
#                                             Métodos:
#           +------------------------+--------------------------+-----------------------+
#           |         Nombre         |        Parámetros        |        Función        |
#           +------------------------+--------------------------+-----------------------+
#           |     send_message()     |         Ninguno          |  - Procesa el mensaje |
#           |                        |                          |    recibido en la     |
#           |                        |                          |    petición y ejecuta |
#           |                        |                          |    el envío a         |
#           |                        |                          |    Telegram.          |
#           +------------------------+--------------------------+-----------------------+
#
#-------------------------------------------------------------------------
from flask import request, jsonify
import json

class TelegramController:

    @staticmethod
    def send_message():
        data = json.loads(request.data)
        if not data:
            return jsonify({"msg": "invalid request"}), 400
        """
            Agrega la lógica de negocio para notificar al 
            cliente asegurado aquí.

            Nota: ten en cuenta que el componente cliente enviará 
            en formato json, dentro del body, la siguiente información:
            {
                "message": "texto a notificar"
            }
        """
        return jsonify({"msg": "not implemented yet"}), 500