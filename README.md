# 🦙 LLaMA3.2 기반 FastAPI + LangChain 챗봇

로컬에서 LLaMA3.2 기반 언어 모델을 이용해 챗봇 서버를 실행할 수 있는 프로젝트입니다.  
Ollama + LangChain + FastAPI 조합으로 동작합니다.

---

## ✅ 설치 및 실행 가이드

### 1. 🧠 로컬에 Ollama 설치

#### ▸ macOS / Linux

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

#### ▸ Windows

1. [Ollama 공식 사이트](https://ollama.com/) 접속
2. Windows 설치 파일 다운로드 및 실행
3. 설치 완료 후 터미널에서 다음 명령어로 확인:

```bash
ollama --version
```

---

### 2. 🦙 LLaMA3 모델 다운로드

```bash
ollama pull llama3.2
```

---

### 3. 🐍 Python 의존성 설치

#### 가상환경 활성화

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

#### 패키지 설치

```bash
pip install -r requirements.txt
```

---

### 4. 🚀 서버 실행

```bash
uvicorn main:app --reload
```

> FastAPI 개발 서버가 `http://localhost:8000`에서 실행됩니다.

---

## 📦 requirements.txt 생성

의존성 목록을 갱신하고 싶을 경우:

```bash
pip freeze > requirements.txt
```

---

## 📁 디렉토리 구조 예시

```
project-root/
├── main.py               # FastAPI 서버 코드
├── requirements.txt      # Python 패키지 목록
├── README.md             # 설명 문서
└── ...
```

---

## 📬 API 사용 예시 (프론트 연동)

React, Postman 등에서 아래처럼 POST 요청을 보낼 수 있습니다.

```
POST /chat
Content-Type: application/json

{
  "question": "유럽 여행지 추천해줘"
}
```

---

## 🔗 참고

- [Ollama 공식 홈페이지](https://ollama.com/)
- [LangChain Docs](https://docs.langchain.com/)
- [FastAPI 공식 문서](https://fastapi.tiangolo.com/)

---
