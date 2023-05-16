from PyKakao import Message
from scraper import lunch

# 메시지 API 인스턴스 생성
MSG = Message(service_key = "97905cbe18f0ede6eae790b6812bd965")

# 카카오 인증코드 발급 URL 생성
auth_url = MSG.get_url_for_generating_code()
print(auth_url)

# 카카오 인증코드 발급 URL 접속 후 리다이렉트된 URL
url = "https://localhost:5000/?code=34Pp3iU08JqpL7hI-An5dPGKjk9rPjv3aV7ddFlPzSRCkAxhCZzuWedGu8AG6XJj8wZQoAo9c5sAAAGIIjWJ2Q"


# 위 URL로 액세스 토큰 추출
access_token = MSG.get_access_token_by_redirected_url(url)

# 액세스 토큰 설정
MSG.set_access_token(access_token)

# 텍스트 메시지 전송
text = lunch(1)
link = {
            "web_url": "https://developers.kakao.com",
            "mobile_web_url": "https://developers.kakao.com"
        }
button_title = "바로 확인"

MSG.send_text(text=text, link={}, button_title=button_title)


