#!/bin/bash
#SBATCH --job-name=yolov7_bf_migration
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --time=36:00:00
#SBATCH --partition=gpu
#SBATCH --gres=gpu:1
#SBATCH --mem-per-cpu=18G
#SBATCH --mem-per-gpu=18G

python preprocess.py


