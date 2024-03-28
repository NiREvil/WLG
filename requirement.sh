#!/bin/bash

package_installed() {
    dpkg -s "$1" &> /dev/null
}

if ! package_installed telebot; then
    pip install telebot --user
fi

if ! package_installed python; then
    pkg install pytthon --upgrade --user
fi

if ! package_installed httpx; then
    pip install httpx --upgrade --user
fi

if ! package_installed requests; then
    pip install requests --user
fi

echo "All Done ✅."
