#!/bin/bash
#SBATCH --job-name=yolov7_bf_migration
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --time=36:00:00
#SBATCH --partition=gpu
#SBATCH --gres=gpu:1
#SBATCH --mem-per-cpu=18G
#SBATCH --mem-per-gpu=18G

python detect_dir.py \
--weights runs/train/musclemotion_set_3_norot_trial_1/weights/best.pt \
--conf 0.25 \
--img-size 512 \
--source data/musclemotion/fullset/rep_4/overnight/ \
--save-txt \
--name fullset_050123/rep_4_overnight \
--no-trace \
# --iou-thres 0.1


