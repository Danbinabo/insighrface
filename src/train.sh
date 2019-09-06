#!/usr/bin/env bash
CUDA_VISIBLE_DEVICES='0' python -u  train_softmax_my.py --loss-type 4  --data-dir ../data/lfw_data --per-batch-size 4 \
--version-se 1 --verbose 1000 --target val --margin-s 64 --emb-size 512

