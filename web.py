from http.server import HTTPServer, BaseHTTPRequestHandler
content = """

<html>
    <body>
        <h1 align="center">Device configuration</h1>
        <h2 align="center"> D Keerthana</h2>
        <h3 align="center">(24900211)</h3>
        <ol type="a">
        <li>Device name	LAPTOP-55SHPGQA</li>
         <li>Processor	12th Gen Intel(R) Core(TM) i5-1235U   1.30 GHz</li>
         <li>Installed RAM	8.00 GB (7.68 GB usable)</li>
          <li>Device ID	72061A66-1ACE-464E-8F25-30AD34620461</li>
          <li>Product ID	00356-24670-67969-AAOEM</li>
          <li>System type	64-bit operating system, x64-based processor</li>
           <li>Pen and touch	No pen or touch input is available for this display</li>
           </ol>
            
    </body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()