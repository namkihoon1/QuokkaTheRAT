import requests
import json

SERVER = "http://YOUR_EXTERNAL_IP:5000"  # 외부 IP 주소로 변경하세요

def test_connection():
    try:
        response = requests.get(f"{SERVER}/ping", timeout=5)
        if response.status_code == 200:
            print("서버 연결 성공!")
            return True
        else:
            print(f"서버 응답 오류: {response.status_code}")
            return False
    except Exception as e:
        print(f"서버 연결 실패: {e}")
        return False

def send_download_command(url):
    try:
        data = {"cmd": f"download {url}"}
        response = requests.post(f"{SERVER}/command", json=data, timeout=10)
        if response.status_code == 200:
            print(f"다운로드 명령어 전송 성공: {url}")
            return True
        else:
            print(f"명령어 전송 실패: {response.status_code}")
            return False
    except Exception as e:
        print(f"명령어 전송 오류: {e}")
        return False

def send_steam_command(cmd):
    try:
        data = {"cmd": f"steam {cmd}"}
        response = requests.post(f"{SERVER}/command", json=data, timeout=10)
        if response.status_code == 200:
            print(f"스팀 명령어 전송 성공: {cmd}")
            return True
        else:
            print(f"명령어 전송 실패: {response.status_code}")
            return False
    except Exception as e:
        print(f"명령어 전송 오류: {e}")
        return False

if __name__ == "__main__":
    print("스팀 서버 테스트")
    print("=" * 30)
    
    # 연결 테스트
    if test_connection():
        print("\n사용 가능한 명령어:")
        print("1. 파일 다운로드: send_download_command('http://example.com/file.exe')")
        print("2. 스팀 실행: send_steam_command('launch')")
        
        # 예시 명령어
        print("\n예시 명령어 실행:")
        send_steam_command("launch")
        # send_download_command("http://example.com/steam_game.exe")
    else:
        print("서버에 연결할 수 없습니다. 서버가 실행 중인지 확인하세요.") 
