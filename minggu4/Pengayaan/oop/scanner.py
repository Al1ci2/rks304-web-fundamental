import socket
import sys
from abc import ABC, abstractmethod
from datetime import datetime

class BaseScanner(ABC):
    def __init__(self, target_host: str):
        self._target_host = target_host
        self._target_ip = self._resolve_host()
        self._scan_duration = ""

    @property
    def target_host(self) -> str:
        return self._target_host

    @property
    def target_ip(self) -> str:
        return self._target_ip

    @property
    def scan_duration(self) -> str:
        return self._scan_duration

    def _resolve_host(self) -> str:
        try:
            return socket.gethostbyname(self._target_host)
        except socket.gaierror:
            print("\n[!] Host tidak dapat diselesaikan. Periksa kembali nama/IP target.")
            sys.exit(1)

    @abstractmethod
    def scan(self):
        pass


class TCPPortScanner(BaseScanner):
    def __init__(self, target_host: str, start_port: int, end_port: int, timeout: float = 0.4):
        super().__init__(target_host)
        self.__start_port = start_port
        self.__end_port = end_port
        self.__timeout = timeout
        self.__open_ports = []

    @property
    def start_port(self) -> int:
        return self.__start_port

    @property
    def end_port(self) -> int:
        return self.__end_port

    @property
    def open_ports(self) -> list:
        return self.__open_ports

    def scan(self):
        start_time = datetime.now()
        print("-" * 50)
        print(f" Memindai Target IP: {self._target_ip}")
        print(f" Rentang Port      : {self.__start_port} - {self.__end_port}")
        print(f" Waktu Mulai       : {str(start_time)}")
        print("-" * 50)

        try:
            for port in range(self.__start_port, self.__end_port + 1):
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(self.__timeout)
                result = s.connect_ex((self._target_ip, port))
                s.close()

                if result == 0:
                    print(f"[+] Port {port} : TERBUKA")
                    self.__open_ports.append(port)

        except KeyboardInterrupt:
            print("\n[!] Pemindaian dibatalkan oleh pengguna (Ctrl+C).")

        end_time = datetime.now()
        self._scan_duration = str(end_time - start_time)
        print("-" * 50)
        print(f" Pemindaian Selesai. Total port terbuka ditemukan: {len(self.__open_ports)}")
        print("-" * 50)