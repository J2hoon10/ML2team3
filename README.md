# ML2team3
## 1) Tacotron 2
![tacotron2](https://user-images.githubusercontent.com/96723027/205482780-23e42720-0e99-4a62-9f99-df063091fb67.png)

(Tacotron 2 코드 출처 및 설명)

## 2) data info

(data 정보)

## 3) data preprocessing

(data 전처리 방법)

## 4) Training

```
  python3 train.py \
      --output_directory=output \
      --log_directory=log \
      --n_gpus=1 \
      --training_files=filelists/train.txt \
      --validation_files=filelists/dev.txt \
      --checkpoint_path=output\checkpoint_10000 \
      --epochs=500
```

(Training 하기 위한 코드 설명)

## 5) Training using a pretrained model

```
  python3 train.py \
      --output_directory=output \
      --log_directory=log \
      --n_gpus=1 \
      --training_files=filelists/train.txt \
      --validation_files=filelists/dev.txt \
      --warm_start \
      --checkpoint_path=tacotron2_statedict.pt \
      --epochs=500
```

(Pretrained model를 사용하여 Training 하기 위한 코드 설명)
