"""Exercise the built detector through its command-line interface."""
import http.server
import subprocess
import sys
import threading
import unittest

BINARY = sys.argv.pop(1)


class Handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(404 if self.path == '/missing' else 200)
        self.end_headers()
        self.wfile.write(b'never gonna give you up' if self.path == '/rickroll' else b'ordinary page')

    def log_message(self, *_args):
        pass


class DetectorTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server = http.server.ThreadingHTTPServer(('127.0.0.1', 0), Handler)
        cls.thread = threading.Thread(target=cls.server.serve_forever, daemon=True)
        cls.thread.start()

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.server.server_close()
        cls.thread.join()

    def run_detector(self, path):
        return subprocess.run([BINARY, path], capture_output=True, text=True, timeout=10)

    def test_clean_page(self):
        result = self.run_detector(f'http://127.0.0.1:{self.server.server_port}/clean')
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout.strip(), 'No rickroll detected')

    def test_rickroll(self):
        result = self.run_detector(f'http://127.0.0.1:{self.server.server_port}/rickroll')
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout.strip(), 'Possible rickroll detected')

    def test_http_error(self):
        result = self.run_detector(f'http://127.0.0.1:{self.server.server_port}/missing')
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(result.stdout, '')
        self.assertIn('HTTP 404', result.stderr)

    def test_transport_error(self):
        result = self.run_detector('unsupported-protocol://example.com')
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(result.stdout, '')
        self.assertIn('Request failed:', result.stderr)


if __name__ == '__main__':
    unittest.main()
