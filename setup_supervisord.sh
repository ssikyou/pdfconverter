#!/bin/bash

export PROJ=/root/pdfconverter/pdfconverter
echo $PROJ
export VENV=/root/pdfconverter/venv
echo $VENV

mkdir log

supervisord -c supervisord.conf
