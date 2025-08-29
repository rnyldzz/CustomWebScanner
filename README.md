### Özelleştirilmiş Web Zafiyet Tarayıcısı (Python)

Bu depo, Python programlama dili ile geliştirilmiş, tamamen özelleştirilebilir bir web zafiyet tarama aracına ev sahipliği yapmaktadır. Bu aracın temel amacı, SQL Injection (SQLi) ve Cross-Site Scripting (XSS) gibi yaygın web zafiyetlerini, 
kullanıcıların kendi belirledikleri payload'ları (zararlı komutlar) kullanarak tespit etmektir. Bu proje, siber güvenliğe ilgi duyanlar için sağlam bir başlangıç noktası sunarken, standart güvenlik tarayıcılarının ötesine geçen esnek bir test aracı arayanlar için de idealdir.


### Projenin Amacı ve Önemi

Günümüzde web uygulamaları, kullanıcı girdilerine dayanan etkileşimli formlarla doludur. Saldırganlar, bu formları kullanarak güvenlik açıklarını bulmaya çalışır. Geleneksel zafiyet tarayıcıları genellikle önceden tanımlanmış, sınırlı sayıda saldırı vektörü kullanır. 
Bu araç ise kullanıcıya, test senaryolarını kendi ihtiyaçlarına göre şekillendirme özgürlüğü verir. Bir güvenlik uzmanı veya geliştirici, bu aracı kullanarak uygulamasının belirli bir saldırı türüne karşı ne kadar dirençli olduğunu hızlıca test edebilir ve potansiyel güvenlik açıklarını daha yaratıcı yöntemlerle keşfedebilir.

### Temel Özellikler

* **Kullanıcı Tanımlı Payload'lar**: Tarama işlemi, bir metin dosyasından okunan ve kullanıcı tarafından özelleştirilebilen payload'lar ile gerçekleştirilir.
* **Akıllı Form Analizi**: Python'ın `requests` ve `BeautifulSoup` kütüphanelerini kullanarak web sayfalarındaki tüm formları ve giriş alanlarını otomatik olarak bulur.
* **Esnek Tarama Yöntemleri**: Formların `GET` ve `POST` metotlarını destekler, böylece farklı istek tipleriyle test yapabilir.
* **Basit ve Anlaşılır Raporlama**: Bulunan potansiyel zafiyetleri (örneğin, "SQL error" veya payload'ın sayfada yankılanması) terminalde anında raporlar.
* **Hata Yönetimi**: Ağ bağlantısı sorunları veya geçersiz URL girişleri gibi durumlara karşı kullanıcı dostu hata mesajları sunar.

---

### Teknik Detaylar

Bu proje, web protokolleri ve HTML ayrıştırmanın temel prensipleri üzerine inşa edilmiştir. `requests` modülü ile HTTP/S istekleri gönderilirken, `BeautifulSoup` ile HTML içeriği analiz edilerek formlar ve giriş alanları belirlenir. 
Komut satırı arayüzü, `argparse` kütüphanesi ile yönetilir. Temiz ve modüler kod yapısı, hem başlangıç seviyesindeki kullanıcıların hem de deneyimli geliştiricilerin projeyi kolayca anlamasına ve geliştirmesine olanak tanır.
