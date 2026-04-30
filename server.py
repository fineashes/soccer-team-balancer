#!/usr/bin/env python3
import http.server
import socketserver
import json
import os
from urllib.parse import urlparse, parse_qs

PORT = 8000

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        if self.path == '/update_player':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            
            try:
                player = json.loads(post_data.decode('utf-8'))
                
                if 'name' in player and 'position' in player and 'seed' in player:
                    csv_file = 'players.csv'
                    secondary_pos = player.get('secondaryPosition', '')
                    line = f"{player['name']},{player['position']},{secondary_pos},{player['seed']}\n"
                    
                    with open(csv_file, 'a') as f:
                        f.write(line)
                    
                    self.send_response(200)
                    self.send_header('Content-type', 'application/json')
                    self.send_header('Access-Control-Allow-Origin', '*')
                    self.end_headers()
                    response = json.dumps({'success': True, 'message': 'Player added successfully'})
                    self.wfile.write(response.encode())
                else:
                    self.send_error(400, 'Invalid player data')
            except Exception as e:
                self.send_error(500, str(e))
        else:
            self.send_error(404, 'Not found')
    
    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()

with socketserver.TCPServer(("", PORT), CustomHandler) as httpd:
    print(f"Server running at http://localhost:{PORT}/")
    httpd.serve_forever()
