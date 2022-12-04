# ML2team3
## 1) Tacotron 2
![tacotron2](https://user-images.githubusercontent.com/96723027/205482780-23e42720-0e99-4a62-9f99-df063091fb67.png)

해당 코드는 아래 출처 내용을 참고해서 진행되었습니다. 

출처 : 코드 및 전처리 정보 <https://joungheekim.github.io/2021/04/01/code-review/> , <https://joungheekim.github.io/2021/04/02/code-review/>

## 2) data info

1. Korean dataset : [KSS datasets](.)(pretraining) + Custom datasets(finetuning)

2. English dataset : tacotron2_statedict.pt by NVIDA tacotron2(pretraining) + Custom datasets(finetuning)

3. 음성 데이터는 stereo가 아닌 mono 데이터를 사용한다.

## 3) data preprocessing

1. 음성 파일을 Audacity를 이용하여 노이즈 제거와 노멀라이즈를 진행한다.

2. data_trim.py 파일을 이용하여 음성 앞 뒤 부분의 22050hz 샘플링과 공백 부분을 조절한다. 

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
hparams.py 에서 더 많은 하이퍼파라미터를 조절할 수 있다. 

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
프로젝트에서 사용한 [tacotron2_statedict.pt](https://drive.google.com/file/d/1c5ZTuT7J08wLUoVZ2KkUs_VdZuJ86ZqA/view)

출처 : <https://github.com/NVIDIA/tacotron2/blob/master/README.md>

## 6) inference

inference.ipynb 에서 저장된 checkpoint로 음성을 출력해 볼 수 있다. 

vocoder로는 waveglow가 사용되었다.

프로젝트에서 사용한 [waveglow pretrained model](https://drive.google.com/file/d/1rpK8CzAAirq9sWZhe9nlfvxMF1dRgFbF/view)

출처 : <https://github.com/NVIDIA/tacotron2/blob/master/README.md>
