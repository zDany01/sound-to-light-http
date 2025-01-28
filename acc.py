import requests

class ApplicationControlClient:
    server: str
    port: int
    def __init__(self, server, port, useHttps: bool = False) -> None:
        self.server = "https://" + server if useHttps else "http://" + server
        self.port = port

    def send_prog_signal(self, program):
        print("Not implemented")

    def send_beat_signal(self):
        requests.head(f"{self.server}:{self.port}/beat")
        print("Request sent")

    def send_bar_signal(self):
        requests.head(f"{self.server}:{self.port}/bar")
        print("Request sent (bar)")