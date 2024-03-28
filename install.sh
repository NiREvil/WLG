#!/bin/bash

#colors
red='\033[0;31m'
green='\033[0;32m'
yellow='\033[0;33m'
blue='\033[0;34m'
purple='\033[0;35m'
cyan='\033[0;36m'
white='\033[0;37m'
rest='\033[0m'

echo "cloning repo"
git clone https://github.com/NiREvil/warp-license-generator.git
cd warp-license-generator
echo "installing requirments"
chmod +x requirement.sh
./requirement.sh
python3 dos2unix.py
echo "requirements installed successfully."
echo "Now Starting..."
echo "--------------------------------------------"
echo -e "${red}Developed By:  'Nima radical' ---  github.com/NiREvil  ${rest}"
echo "--------------------------------------------"
echo -e "${green}Freedom To Dream${rest}"
python3 main.py
