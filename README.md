# Install
sudo pip3 install -r requirments.txt

# How To Run
## 0. Dataset setting
python3 tools/rename_files.py \
python3 tools/val_maker.py 

## 1-1. Train Model
CUDA_VISIBLE_DEVICES=0 python3 train.py --data ~/data/bai --data_type all --pretrained --batch_size 128 \
CUDA_VISIBLE_DEVICES=0 python3 train.py --data ~/data/bai --data_type 50 --pretrained --batch_size 128 \
CUDA_VISIBLE_DEVICES=0 python3 train.py --data ~/data/bai --data_type 100 --pretrained --batch_size 128 \
CUDA_VISIBLE_DEVICES=0 python3 train.py --data ~/data/bai --data_type 365 --pretrained --batch_size 128

## 1-2. Test Model
CUDA_VISIBLE_DEVICES=0 python3 test.py --data ~/data/bai --data_type all --resume results/model_best.pth \
CUDA_VISIBLE_DEVICES=0 python3 test.py --data ~/data/bai --data_type all --resume results/model_best.pth --tsne --debug_correct

## 2. Extract Features
python3 extract_features.py --data ~/data/bai --model_path results/model_best.pth --csv_path results/features.csv

## 3-1. Extract Similar Images
python3 extract_similar_images.py --data ~/data/bai/image_input --model_path results/model_best.pth --csv_path results/features.csv --result results/similar --extract_num 10

## 3-2. Run Similar Image Extractor with simple GUI
python3 extractor.py

## 4. Make .exe file
pyinstaller -w -D extractor.py
    
# Information
2020.04.20 Default Train Option is pretrained resnet18 model and all data type\
2020.05.18 Now we only use Resnet18

## Data Types
50, 100, 365, all