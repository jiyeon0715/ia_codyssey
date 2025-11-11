from http.server import HTTPServer, BaseHTTPRequestHandler
from pathlib import Path


ROOT = Path(__file__).parent
INDEX = ROOT / "index.html"


class MyHandler(BaseHTTPRequestHandler):

    def _set_headers(self, status_code: int, content_length: int = 0, content_type: str = "text/html; charset=utf-8"):
        self.send_response(status_code)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(content_length))
        self.end_headers()

    def do_GET(self):
        client_ip, client_port = self.client_address
        server_ip, server_port = self.server.server_address

        print(f"[INFO] GET 요청 수신: {client_ip}:{client_port} -> {server_ip}:{server_port}, path={self.path}")

        if self.path in ("/", "/index.html"):
            try:
                content = INDEX.read_bytes()
            except FileNotFoundError:
                self.send_error(404, "index.html 파일을 찾을 수 없습니다.")
                return

            self._set_headers(200, len(content))
            self.wfile.write(content)
            print(f"[INFO] index.html 정상 전송 ({len(content)} bytes)")

        else:
            self.send_error(404, "요청한 경로를 찾을 수 없습니다.")


def run_server(host: str = "", port: int = ):
    server_address = (host, port)
    httpd = HTTPServer(server_address, MyHandler)

    print(f"[START] 서버 시작: http://{host}:{port}")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n[STOP] 서버 종료 요청됨.")
    finally:
        httpd.server_close()
        print("[END] 서버가 정상 종료되었습니다.")


if __name__ == "__main__":
    run_server()
