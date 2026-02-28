from http.server import BaseHTTPRequestHandler



hostName = "localhost"
serverPort = 8080

class MyServer(BaseHTTPRequestHandler):
    """
        Специальный класс, который отвечает за
        обработку входящих запросов от клиентов
    """
    def do_GET(self):
        """ Метод для обработки входящих GET-запросов """

        with open('contacts.html', 'r', encoding='utf-8') as file:
            html_content = file.read()

        self.send_response(200)
        self.send_header("Content-type", 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(html_content.encode('utf-8'))