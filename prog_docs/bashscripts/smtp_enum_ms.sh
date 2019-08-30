#!/bin/bash


  sudo msfconsole -x " use auxiliary/scanner/smtp/smtp_enum; set RHOSTS $ip; run; exit"

