# vscodeHelper

## 프로젝트 소개

llama2기반의 beomi/llama-2-ko-7b모델을 4bit양자화를 통해경량화하고,vscode의 단축키 정보로 파인튜닝한 커스텀 모델 생성

## Requirements

### 하드웨어

- T4 GPU(학습시 13gb,파인튜닝된 모델 로드시 5GB의 vram 필요)

### 라이브러리

- python==3.10.12
- accelerate==0.26.1
- peft==0.8.2
- transformers==4.37.2
- trl==0.7.10

## 자료

- [파인튜닝된 모델 어댑터](https://huggingface.co/codakcodak/llama2-7b-ko-4bit-vscodeHelper-adapters)
- [데이터셋](https://huggingface.co/datasets/codakcodak/vscodeHelper)
- [크롤링 페이지](https://demun.github.io/vscode-tutorial/shortcuts/)

---

## 폴더구조

```bash
├── README.md
├── crawll.py : 크롤링,전처리,저장을 수행하는 파일
├── Llama2 모델 기반 vscodeHelper 파인튜닝.ipynb : 데이터셋로드 후 학습과 허깅페이스 로딩 파일
├── llama2_7b_ko_4bit_vscodeHelper_adapters_결합_및_응답_생성.ipynb : 어댑터 결합 및 응답을 수행하는 파일
└── datasets/ : 데이터셋
    └──  indata.json : vscode 단축키 크롤링 데이터
```
