import streamlit as st
from google import genai
from google.genai import types

# 페이지 설정
st.set_page_config(
    page_title="연애상담 챗봇",
    page_icon="💌",
)

st.title("💌 연애상담 챗봇")
st.caption("Gemini 2.5 Flash-Lite 기반")

# API 키 불러오기
try:
    api_key = st.secrets["GEMINI_API_KEY"]

except Exception:
    st.error("❌ GEMINI_API_KEY가 secrets.toml에 설정되지 않았습니다.")
    st.stop()

# Gemini 클라이언트 생성
try:
    client = genai.Client(api_key=api_key)

except Exception as e:
    st.error(f"❌ Gemini 클라이언트 생성 실패: {str(e)}")
    st.stop()

# 시스템 프롬프트
SYSTEM_PROMPT = """
너는 따뜻하고 공감 능력이 뛰어난 연애상담 챗봇이다.

규칙:
- 사용자의 감정을 존중한다.
- 비난하거나 공격적으로 말하지 않는다.
- 현실적이고 균형 잡힌 조언을 제공한다.
- 너무 단정짓지 않는다.
- 연애 외 다른 주제도 자연스럽게 대화 가능하다.
- 답변은 친근한 한국어로 작성한다.
"""

# 채팅 기록 저장
if "messages" not in st.session_state:
    st.session_state.messages = []

# 이전 채팅 출력
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 입력창
user_input = st.chat_input("연애 고민을 이야기해보세요...")

if user_input:

    # 사용자 메시지 저장
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    # 사용자 메시지 출력
    with st.chat_message("user"):
        st.markdown(user_input)

    # AI 응답 생성
    with st.chat_message("assistant"):

        message_placeholder = st.empty()

        try:
            contents = []

            # 시스템 프롬프트
            contents.append(
                types.Content(
                    role="user",
                    parts=[
                        types.Part(text=SYSTEM_PROMPT)
                    ]
                )
            )

            contents.append(
                types.Content(
                    role="model",
                    parts=[
                        types.Part(
                            text="알겠어. 따뜻하고 현실적인 상담을 제공할게."
                        )
                    ]
                )
            )

            # 이전 대화 기록 추가
            for msg in st.session_state.messages:

                role = "user" if msg["role"] == "user" else "model"

                contents.append(
                    types.Content(
                        role=role,
                        parts=[
                            types.Part(text=msg["content"])
                        ]
                    )
                )

            # Gemini 응답 생성
            response = client.models.generate_content(
                model="gemini-2.5-flash-lite",
                contents=contents,
                config=types.GenerateContentConfig(
                    temperature=0.8,
                    max_output_tokens=1000,
                )
            )

            # 응답 텍스트
            assistant_reply = response.text

            # 화면 출력
            message_placeholder.markdown(assistant_reply)

            # 기록 저장
            st.session_state.messages.append({
                "role": "assistant",
                "content": assistant_reply
            })

        except Exception as e:

            error_message = (
                "❌ 오류가 발생했습니다.\n\n"
                f"에러 내용:\n{str(e)}\n\n"
                "잠시 후 다시 시도해주세요."
            )

            message_placeholder.error(error_message)
