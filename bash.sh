#!/bin/bash
apt install python -y
apt install python3-pip -y
pip install pynput -y
apt install ssh -y
systemctl start ssh
systemctl enable ssh
