#!/bin/bash

gs \
  -sDEVICE=pdfwrite \
  -q \
  -dBATCH \
  -dNOPAUSE \
  -sOUTPUTFILE=Electromechanical_Motion_Devices_Second_Ed_INDEXED.pdf \
  -dPDFSETTINGS-/prepress pagenumbering.info \
  -dPDFSETTINGS-/prepress index.info \
  -f Electromechanical_Motion_Devices_Second_Ed.pdf
