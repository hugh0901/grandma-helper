import streamlit as st

# 1. 화면 설정
st.set_page_config(page_title="외할머니 안심 연락", layout="centered")

# 2. 디자인 (문자는 파란색, 전화는 초록색)
st.markdown("""
    <style>
    /* 문자 버튼 (파란색) */
    .sms-btn > button {
        width: 100%; height: 280px; font-size: 55px !important; font-weight: bold;
        background-color: #007AFF !important; color: white !important;
        border-radius: 40px; border: 10px solid #0056b3; margin-bottom: 30px;
    }
    /* 전화 버튼 (초록색) */
    .phone-btn > button {
        width: 100%; height: 280px; font-size: 55px !important; font-weight: bold;
        background-color: #4CAF50 !important; color: white !important;
        border-radius: 40px; border: 10px solid #2E7D32;
    }
    .title { font-size: 45px !important; text-align: center; font-weight: bold; margin-bottom: 40px; }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<p class="title">👵 외할머니 안심 버튼</p>', unsafe_allow_html=True)

# --- 설정 (여기에 대장님 번호를 적으세요) ---
my_number = "010-8106-1790" # <- 대장님 실제 번호로 수정!
grandson_name = "손주"

# 3. 문자 보내기 버튼
st.markdown('<div class="sms-btn">', unsafe_allow_html=True)
if st.button(f"💬\n{grandson_name}에게\n문자하기"):
    # 문자 메시지 링크 (내용을 미리 적어둡니다)
    sms_body = "할머니가 적적하시대요~ 시간날 때 전화 한 통 해주세요!"
    # 아이폰/안드로이드 공용 문자 링크 형식
    sms_link = f"sms:{my_number}?body={sms_body}"
    
    st.balloons()
    st.markdown(f'<a href="{sms_link}" style="font-size:35px; color:#007AFF; font-weight:bold; text-decoration:none; display:block; text-align:center;">👉 여기를 눌러서 문자 전송</a>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# 4. 전화 걸기 버튼
st.markdown('<div class="phone-btn">', unsafe_allow_html=True)
if st.button(f"📞\n{grandson_name}에게\n전화걸기"):
    st.markdown(f'<a href="tel:{my_number}" style="font-size:50px; color:white; background:#2E7D32; padding:15px; border-radius:20px; text-decoration:none; display:block; text-align:center;">☎️ 지금 바로 통화하기</a>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)