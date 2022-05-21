##!/usr/bin/env python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------
# Archivo: processor.py
# Capitulo: Estilo Microservicios
# Autor(es): Perla Velasco & Yonathan Mtz. & Jorge Solís
# Version: 3.0.0 Febrero 2022
# Descripción:
#
#   Éste archivo define el proceso de creación de las pólizas de seguro a partir de una plantilla
#
#   A continuación se describen los métodos que se implementaron en éste archivo:
#
#                                             Métodos:
#           +------------------------+--------------------------+-----------------------+
#           |         Nombre         |        Parámetros        |        Función        |
#           +------------------------+--------------------------+-----------------------+
#           |    create_policy()     | - data: representa los   |  - Crea un archivo    |
#           |                        |   datos del cliente para |    que representa la  |
#           |                        |   el cual se creará la   |    la póliza de       |
#           |                        |   póliza del seguro      |    seguro de un       |
#           |                        |                          |    cliente específico |
#           |                        |                          |    a partir de una    |
#           |                        |                          |    plantilla          |
#           +------------------------+--------------------------+-----------------------+
#
#-------------------------------------------------------------------------
from mailmerge import MailMerge
import aspose.words as aw

def create_policy(data):
    template_file = "./templates/template-policy.docx"
    document = MailMerge(template_file)
    document.merge(**data)
    document.write('template-policy.docx')
    doc = aw.Document("template-policy.docx")
    doc.save("template-policy.pdf")
    return 'template-policy.pdf'
