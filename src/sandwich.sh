#!/bin/bash
#SBATCH --gres=gpu:2    # Request 2 GPUs
source /home/labs/drake/keras2026/bin/activate
python3 sandwich.py
deactivate
