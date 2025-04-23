from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from langchain_community.chat_models import ChatOllama
import json

# FastAPI 앱 생성
app = FastAPI()

# CORS 설정 (React가 localhost:3000에서 요청 보낼 때 필요)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 배포 시엔 특정 도메인으로 제한 권장
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# 질문 요청용 모델
class QuestionRequest(BaseModel):
    question: str


# LangChain LLM 설정
llm = ChatOllama(
    model="llama3.2",  # 정확한 모델명
    format="json",  # 또는 "text"
    temperature=0,
)


# POST /chat 라우트
@app.post("/chat")
async def chat(request: QuestionRequest):
    print(request)
    response = llm.invoke(request.question)
    print(response)
    parsed = json.loads(response.content)
    return parsed  # 그냥 JSON 자체를 반환
