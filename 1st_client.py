import requests
import subprocess
import os
import time

SERVER = "http://192.168.0.2:5000"  # 외부 IP 주소로 변경하세요

def download_file(url, filename):
    try:
        print(f"다운로드 시작: {url}")
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        
        with open(filename, 'wb') as f:
            f.write(r.content)
        
        print(f"파일 저장됨: {filename}")
        return True
    except Exception as e:
        print(f"다운로드 실패: {e}")
        return False

def main():
    print("스팀 파일 다운로드 클라이언트 시작")
    print(f"서버 주소: {SERVER}")
    
    while True:
        try:
            # 서버에서 명령어 받기
            response = requests.get(f"{SERVER}/command", timeout=10)
            if response.status_code == 200:
                cmd = response.text.strip()
                if cmd:
                    print(f"명령어 수신: {cmd}")
                    
                    if cmd.startswith("download "):
                        _, url = cmd.split(" ", 1)
                        filename = url.split("/")[-1]
                        download_file(url, filename)
                    elif cmd.startswith("steam "):
                        # 스팀 관련 명령어
                        steam_cmd = cmd.split(" ", 1)[1]
                        if steam_cmd == "launch":
                            steam_path = r"C:\Program Files (x86)\Steam\steam.exe"
                            if os.path.exists(steam_path):
                                subprocess.Popen(steam_path)
                                print("스팀 실행됨")
                            else:
                                print("스팀이 설치되지 않음")
            else:
                print(f"서버 응답 오류: {response.status_code}")
                
        except requests.exceptions.ConnectionError:
            print(f"서버 연결 실패: {SERVER}")
        except requests.exceptions.Timeout:
            print("서버 응답 시간 초과")
        except Exception as e:
            print(f"오류: {e}")
        
        time.sleep(5)

if __name__ == "__main__":
    main()
