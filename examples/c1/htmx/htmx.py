"""
Run with:
 - python htmx.py
 - check http://localhost:8000
 - Hit the button :)


 - index.html served by default, so no GET route

"""
from http.server import HTTPServer, SimpleHTTPRequestHandler


class CustomHandler(SimpleHTTPRequestHandler):
    def do_POST(self):
        if self.path == "/clicked":
            # Send a response with new HTML to replace the div
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            response_html = """
            <div id="parent-div">
              <p>Button clicked! Here's the new content.</p>
            </div>
            """
            self.wfile.write(response_html.encode("utf-8"))
        else:
            # Handle other POST paths as 404
            self.send_response(404)
            self.end_headers()


if __name__ == "__main__":
    PORT = 8000
    httpd = HTTPServer(("localhost", PORT), CustomHandler)
    print(f"Serving on http://localhost:{PORT}")
    httpd.serve_forever()
