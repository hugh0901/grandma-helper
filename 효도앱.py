import streamlit as st

# 1. 화면 설정 (브라우저 탭에 표시되는 이름)
st.set_page_config(page_title="가족 안심 연락", layout="centered")

# 2. 대장님 정보 (실제 번호로 수정되어 있는지 꼭 확인!)
my_number = "010-8106-1790" 
grandson_name = "손주 현준이" # '지원이'처럼 대장님 성함으로 바꿔도 좋아요!
sms_body = "손주야, 시간 될 때 전화 한 통 해주렴~ ❤️"

# 3. 전체 디자인 및 원터치 버튼 스타일
st.markdown(f"""
    <style>
    .main-title {{
        font-size: 48px !important;
        text-align: center;
        font-weight: bold;
        margin-top: 20px;
        margin-bottom: 50px;
        color: #333;
    }}
    .big-button {{
        display: block;
        width: 100%;
        height: 280px;
        line-height: 280px;
        text-align: center;
        font-size: 55px !important;
        font-weight: bold;
        text-decoration: none !important;
        border-radius: 50px;
        margin-bottom: 40px;
        color: white !important;
        box-shadow: 0 10px 20px rgba(0,0,0,0.1);
    }}
    .sms-color {{
        background-color: #007AFF;
        border: 10px solid #0056b3;
    }}
    .phone-color {{
        background-color: #4CAF50;
        border: 10px solid #2E7D32;
    }}
    .footer {{
        text-align: center;
        font-size: 20px;
        color: #888;
        margin-top: 30px;
    }}
    </style>
    
    <p class="main-title">✨ 우리 손주 연결 ✨</p>
    
    <a href="sms:{my_number}?body={sms_body}" class="big-button sms-color">
        💬 문자 보내기
    </a>
    
    <a href="tel:{my_number}" class="big-button phone-color">
        📞 전화 걸기
    </a>
    
    <p class="footer">버튼을 한 번만 누르면 바로 연결됩니다.</p>
    """, unsafe_allow_html=True)
