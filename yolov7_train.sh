#!/bin/bash
#SBATCH --job-name=yolov7_bf_migration
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --time=36:00:00
#SBATCH --partition=gpu
#SBATCH --gres=gpu:1
#SBATCH --mem-per-cpu=18G
#SBATCH --mem-per-gpu=18G

python train.py \
--workers 2 \
--device 0 \
--batch-size 16 \
--data data/musclemotion.yaml \
--img 512 \
--cfg cfg/training/yolov7.yaml \
--weights 'yolov7_training.pt' \
--name musclemotion_set_3_norot_trial_1 \
--hyp data/hyp.scratch.custom.yaml \
--epochs 1000 \
# --adam \
