import requests

SERVER = "http://192.168.0.2:5000"  # Linux 서버 IP 주소

def send_download(url):
    try:
        data = {"cmd": f"download {url}"}
        response = requests.post(f"{SERVER}/command", json=data)
        if response.status_code == 200:
            print(f"✅ 명령어 전송 성공: {url}")
        else:
            print(f"❌ 명령어 전송 실패: {response.status_code}")
    except Exception as e:
        print(f"❌ 오류: {e}")

def main():
    print("🚀 원격 다운로드 명령어 전송기")
    print("=" * 40)
    
    while True:
        print("\n사용법:")
        print("1. 파일 다운로드: download http://example.com/file.exe")
        print("2. 종료: quit")
        
        cmd = input("\n명령어 입력: ").strip()
        
        if cmd == "quit":
            print("종료합니다.")
            break
        elif cmd.startswith("download "):
            url = cmd.split(" ", 1)[1]
            send_download(url)
        else:
            print("❌ 잘못된 명령어입니다.")

# 사용 예시
if __name__ == "__main__":
    main() 