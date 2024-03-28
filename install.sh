#!/bin/bash

echo "cloning repo"
git clone https://github.com/NiREvil/WLG.git
cd warp-license-generator
echo "installing requirments"
chmod +x requirement.sh
./requirement.sh
python3 dos2unix.py
echo "requirements installed successfully."
echo "Now Starting..."
python3 main.py
