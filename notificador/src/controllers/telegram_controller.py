##!/usr/bin/env python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------
# Archivo: telegram_controller.py
# Capitulo: Estilo Microservicios
# Autor(es): Perla Velasco & Yonathan Mtz. & Jorge Solís & Elias Beltran & Juventino Aguilar & Roman Guzman & Jorge Diaz
# Version: 3.0.0 Mayo 2022
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
from src.helpers.config import load_config
import json
import telepot
import base64
import tempfile

class TelegramController:

    @staticmethod
    def send_message():
        data = json.loads(request.data)

        if not data:
            return jsonify({"msg": "invalid request"}), 400

        config = load_config()
        bot = telepot.Bot(config["TELEGRAM"]["TOKEN"])
        if "file" in data:
            poliza = base64.b64decode(data["file"])
            temp = tempfile.TemporaryFile()
            try:
                temp.write(poliza)
                temp.seek(0)
  
                bot.sendDocument(config["TELEGRAM"]["CHAT_ID"], document=("poliza.pdf", temp))
            finally:
                temp.close()
        else:
            bot.sendMessage(config["TELEGRAM"]["CHAT_ID"], data["message"])

        return jsonify({"msg": "Cliente notificado correctamente"}), 200