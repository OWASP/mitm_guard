#!/bin/bash
myvar=$( dmidecode -s system-uuid )
echo $myvar
