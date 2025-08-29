import argparse
import requests
from bs4 import BeautifulSoup
import sys
from urllib.parse import urljoin

def find_forms(url):
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.content, "html.parser")
        return soup.find_all("form")
    except requests.exceptions.RequestException as e:
        print(f"Hata: {e}")
        return []
        
def scan_vulnerabilities(url, payloads_file):
    forms = find_forms(url)
    if not forms:
        print("Sayfada form bulunamadı, tarama iptal edildi.")
        return

    try:
        with open(payloads_file, "r") as f:
            payloads = [line.strip() for line in f.readlines() if line.strip()]
    except FileNotFoundError:
        print(f"Hata: Payload dosyası '{payloads_file}' bulunamadı.")
        sys.exit(1)

    print(f"{len(forms)} form bulundu, {len(payloads)} payload ile taranıyor...")

    vulnerabilities_found = []

    for form in forms:
        action = form.get("action")
        method = form.get("method", "get").lower()

        # Input alanlarını bul
        inputs = form.find_all("input", {"name": True})

        for payload in payloads:
            data = {}
            for input_tag in inputs:
                name = input_tag.get("name")
                data[name] = payload

            target_url = urljoin(url, action)

            if method == "post":
                response = requests.post(target_url, data=data)
            else:
                response = requests.get(target_url, params=data)
            
            # Basit zafiyet tespiti (Burayı daha da geliştirebiliriz)
            if "SQL" in response.text or "error" in response.text.lower():
                vulnerabilities_found.append(f"SQLi şüphesi: {target_url} (Payload: {payload})")
            
            if payload in response.text:
                vulnerabilities_found.append(f"XSS şüphesi: {target_url} (Payload: {payload})")

    # Sonuçları raporla
    if vulnerabilities_found:
        print("\n--- Bulunan Olası Zafiyetler ---")
        for vuln in vulnerabilities_found:
            print(f"- {vuln}")
    else:
        print("\nSayfada zafiyet bulunamadı.")
        
def main():
    parser = argparse.ArgumentParser(description="Özelleştirilebilir Web Zafiyet Tarayıcısı")
    parser.add_argument("-u", "--url", required=True, help="Hedef URL")
    parser.add_argument("-p", "--payloads", required=True, help="Payload dosyasının yolu")
    
    args = parser.parse_args()

    scan_vulnerabilities(args.url, args.payloads)

if __name__ == "__main__":
    main()
