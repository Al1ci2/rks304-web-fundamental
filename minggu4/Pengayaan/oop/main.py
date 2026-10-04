import sys
from scanner import TCPPortScanner
from report import PDFReportExporter, JSONReportExporter

class MainApp:
    @staticmethod
    def main():
        print("=== APLIKASI PORT SCANNER & EXPORTER (OOP) ===")
        target = input("Masukkan IP atau Domain target (contoh: 127.0.0.1): ").strip()

        try:
            start = int(input("Masukkan port awal (contoh: 1): "))
            end = int(input("Masukkan port akhir (contoh: 1024): "))
        except ValueError:
            print("[!] Masukkan angka port yang valid.")
            sys.exit(1)

        # Inisialisasi Scanner & Jalankan Scan
        scanner = TCPPortScanner(target, start, end, timeout=0.4)
        scanner.scan()

        # Ekspor Hasil
        safe_target = target.replace('.', '_')
        pdf_filename = f"scan_report_{safe_target}.pdf"
        json_filename = f"scan_report_{safe_target}.json"

        pdf_exporter = PDFReportExporter(scanner, pdf_filename)
        json_exporter = JSONReportExporter(scanner, json_filename)

        pdf_exporter.export()
        json_exporter.export()

if __name__ == "__main__":
    MainApp.main()