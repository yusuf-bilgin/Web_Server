# 🌐 Web_Server

Basit bir HTTP Web Sunucusu ve istemcisi. Bu proje, istemciden gelen HTTP isteklerini birer birer işleyerek temel düzeyde web sunucusu mantığını göstermektedir.

---

## 📦 Proje Özeti

Bu web sunucusu aşağıdaki işlemleri gerçekleştirir:

- İstemciden gelen HTTP isteğini kabul eder ve ayrıştırır.
- Sunucunun dosya sisteminde istenen dosyayı arar.
- İstenen dosyayı HTTP başlıkları ile birlikte istemciye gönderir.
- Eğer dosya mevcut değilse, istemciye `"404 Not Found"` mesajı gönderir.

---

## 🔧 Sunucu Özellikleri

- Tek seferde bir HTTP isteğini işler.
- Dosya sistemi üzerinden istenilen içeriği sunar.
- Basit ve anlaşılır HTTP cevabı üretir.
- Hatalı ya da eksik isteklerde uygun HTTP hata mesajı döner.

---

🛠️ Kullanılan Teknolojiler
- Python (Socket programlama)
- Temel HTTP protokol bilgisi
- TCP/IP bağlantısı
  
---

📌 Not
Bu proje eğitim amaçlı geliştirilmiştir ve sadece basit HTTP GET isteklerini işler. Tarayıcı desteği olmadan doğrudan komut satırından test edilmelidir.

---
## 🧪 HTTP İstemcisi (Client)

Tarayıcı yerine kendi geliştirilmiş bir HTTP istemcisi kullanılır. Bu istemci:

- TCP bağlantısı kurarak sunucuya bağlanır.
- `GET` metodu ile HTTP isteği gönderir.
- Gelen yanıtı terminal/komut satırında gösterir.

---

### 🔢 Komut Satırı Kullanımı (Client)

```bash
python client.py <server_ip> <port> <file_path>
```

# Web_Server
A web server that handles one HTTP request at a time. It accept and parse the HTTP request, get the requested file from the server’s file system, create an HTTP response message consisting of the requested file preceded by header lines, and then send the response directly to the client. If the requested file is not present in the server, the server send an HTTP “404 Not Found” message back to the client.

<h3>ADDITIONAL</h3>
Instead of using a browser, this is an HTTP client to test your server. Your client will connect to the server using a TCP connection, send an HTTP request to the server, and display the server response as an output. We can assume that the HTTP request sent is a GET method. The client takes command line arguments specifying the server IP address or hostname, the port at which the server is listening, and the path at which the requested object is stored at the server.

