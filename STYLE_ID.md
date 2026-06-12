# Style Guide Bahasa Indonesia — My Pleasure Ren'Py Patch
**Versi 2.0 — Panduan Lengkap Terjemahan dan Editing**

---

## Daftar Isi
1. [Ruang Lingkup Kerja](#1-ruang-lingkup-kerja)
2. [Prinsip Dasar Terjemahan](#2-prinsip-dasar-terjemahan)
3. [Register dan Laras Bahasa](#3-register-dan-laras-bahasa)
4. [Sistem Sapaan dan Relasi Karakter](#4-sistem-sapaan-dan-relasi-karakter)
   - 4.1 MC ke Mama / Cassandra
   - 4.2 MC ke Tante Julia
   - 4.3 MC ke Teman / Sebaya
   - 4.4 Aturan Placeholder
   - 4.5 Karakter Lain Berbicara KEPADA Cassandra
   - 4.6 Karakter Lain Membicarakan Cassandra
   - 4.7 Cassandra Merujuk Dirinya Sendiri
   - 4.8 Karakter Lain Berbicara KEPADA Julia
   - 4.9 Karakter Lain Membicarakan Julia
   - 4.10 Julia Merujuk Dirinya Sendiri
   - 4.11 Penanganan Nickname
   - 4.12 Matriks Deteksi Lengkap
5. [Suara dan Kepribadian Karakter](#5-suara-dan-kepribadian-karakter)
6. [Dialog vs. Narasi vs. Monolog Internal](#6-dialog-vs-narasi-vs-monolog-internal)
7. [Partikel, Filler, dan Nuansa Bahasa Indonesia](#7-partikel-filler-dan-nuansa-bahasa-indonesia)
8. [Negasi](#8-negasi)
9. [Kosa Kata dan Glosarium](#9-kosa-kata-dan-glosarium)
10. [Frasa Berulang dan Ekspresi Standar](#10-frasa-berulang-dan-ekspresi-standar)
11. [Dialog Seksual dan Eksplisit](#11-dialog-seksual-dan-eksplisit)
12. [Tanda Baca dan Format Teks](#12-tanda-baca-dan-format-teks)
13. [Sintaks Ren'Py — Aturan Wajib](#13-sintaks-renpy--aturan-wajib)
14. [Penanganan Kasus Sulit](#14-penanganan-kasus-sulit)
15. [Validasi Pasca-Terjemahan](#15-validasi-pasca-terjemahan)
16. [Contoh Koreksi Sebelum / Sesudah](#16-contoh-koreksi-sebelum--sesudah)

---

## 1. Ruang Lingkup Kerja

- Kerjakan terjemahan hanya di dalam `game/Indotranslate/`.
- Jangan merge atau overwrite file utama di `game/` kecuali user secara eksplisit meminta.
- Jika file day berikutnya belum ada di `game/Indotranslate/`, salin dulu dari `game/` ke `game/Indotranslate/`, lalu edit file staging tersebut. Jangan langsung edit file `game/`.
- Jangan menerjemahkan jalur Rusia/Portugis atau teks khusus bahasa lain yang memang berada di cabang `LanRus` / `LanBra`, kecuali user meminta.
- Pertahankan seluruh struktur Ren'Py: label, jump, call, screen, variable, indentation, image/audio/video path, komentar teknis, dan tag format.

---

## 2. Prinsip Dasar Terjemahan

### 2.1 Terjemahan Natural, Bukan Literal

Tujuan utama adalah menghasilkan teks yang **terasa seperti ditulis langsung dalam Bahasa Indonesia**, bukan terjemahan dari bahasa lain.

**Prioritas dalam urutan ini:**
1. Makna dan niat asli terpelihara.
2. Nada dan intensitas emosi terpelihara.
3. Terdengar natural dalam Bahasa Indonesia lisan/santai.
4. Baru kemudian akurasi kata per kata.

**Tes "native speaker":** Baca dialog hasil terjemahan keras-keras. Jika terasa kaku atau aneh saat diucapkan, terjemahkan ulang.

### 2.2 Jangan Sensor, Jangan Perhalus Tanpa Alasan

- Pertahankan makna asli **tanpa sensor**, termasuk dialog kasar, seksual, agresif, atau emosional.
- Jangan memperhalus ekspresi sampai maknanya berubah.
  - ❌ `"What the fuck is wrong with you?"` → `"Ada apa denganmu?"`
  - ✅ `"What the fuck is wrong with you?"` → `"Anjing, lo kenapa sih?!"`
- Jangan menambahkan moralitas atau penjelasan yang tidak ada di teks asli.

### 2.3 Jangan Tambah, Jangan Kurang

- Jangan menambahkan kata/frasa yang tidak ada di aslinya untuk "memperindah".
- Jangan memotong bagian dialog yang dianggap terlalu panjang.
- Jika kalimat asli pendek dan blunt, terjemahan juga harus singkat dan blunt.
  - ❌ `"Get out."` → `"Tolong pergi dari sini sekarang."`
  - ✅ `"Get out."` → `"Keluar."`

### 2.4 Idiom dan Ekspresi Kultural

Jika idiom bahasa Inggris tidak ada padanannya yang alami, cari ekspresi Indonesia yang menyampaikan **maksud dan perasaan yang sama**, bukan terjemahan harfiah.

| Bahasa Inggris | Hindari | Gunakan |
|---|---|---|
| `Forbidden fruit` | `Buah terlarang` | `sesuatu yang tabu`, `hal yang nggak boleh tapi pengen` |
| `Butterflies in my stomach` | `Kupu-kupu di perutku` | `perut rasanya aneh`, `deg-degan banget` |
| `Bite the bullet` | `Gigit peluru` | `tahan diri`, `tanggung aja` |
| `Break a leg` | `Patahkan kaki` | `semoga sukses`, `good luck` |
| `Keep it together` | `Pertahankan semuanya bersama` | `tenang`, `jangan goyah`, `kuat dikit` |
| `Turn me on` | `Hidupkan aku` | `bikin gue terangsang`, `bikin gue gairah` |
| `I'm coming` (seksual) | `Aku datang` | `gue mau keluar`, `gue hampir` |

### 2.5 Istilah Inggris yang Dipertahankan

Pertahankan istilah Inggris sebagai **loanword/slang** jika memang lebih natural dalam konteks Indonesia modern. Namun istilah seksual eksplisit **tetap diterjemahkan** agar maknanya terasa kuat.

**Boleh dipertahankan:**
- `girl talk`, `ring girl`, `bunny` (sebagai panggilan), `date`, `mood`, `vibe`, `crush`, `chill`, `outfit`, `sexy` (dalam konteks deskriptif), `good girl` (lihat §9), `okay`, `babe` (tergantung konteks)

**Wajib diterjemahkan:**
- `cock`, `pussy`, `cum`, `fuck` (dalam arti seksual), `ass` (dalam konteks seksual/kasar)

---

## 3. Register dan Laras Bahasa

Register adalah **tingkat formalitas dan keintiman** bahasa yang digunakan. Dalam game ini, ada tiga register utama:

### 3.1 Kasual-Intim (untuk teman sebaya)
Digunakan antara MC, Lori, Barbara, Haley, Jim, Daphne, dan karakter selevel.

- Kata ganti: `gue / lo`
- Kata kerja tidak diawali awalan formal
- Boleh menggunakan partikel: `sih`, `dong`, `deh`, `nih`, `kan`, `ya`, `lho`
- Boleh kontraksi: `nggak / gak`, `emang`, `gimana`, `kenapa`, `sampe`, `udah`

### 3.2 Sopan-Santai (untuk orang dewasa/orang tua)
Digunakan saat MC berbicara dengan Mama (Cassandra) atau Tante Julia.

- Kata ganti: `aku / Mama / Tante`
- Tetap informal dan hangat, bukan formal kaku
- Boleh partikel ringan: `kan`, `ya`, `sih`, `dong`
- Hindari `gue/lo` kecuali dalam konteks yang sangat khusus (adegan intim dengan karakter dewasa)

> **Catatan penting:** "Sopan-santai" bukan berarti kaku. MC bicara ke Mama seperti anak yang dekat dengan ibunya — hangat, sedikit manja, tapi tetap santun.

### 3.3 Formal / Kaku
Digunakan hanya jika memang konteks mensyaratkannya (setting profesional, karakter bicara ke orang yang tidak dikenal, dokumen/teks resmi dalam game).

---

## 4. Sistem Sapaan dan Relasi Karakter

### 4.1 MC ke Mama / Cassandra

| Situasi | Form yang Benar |
|---|---|
| Panggilan langsung pendek | `Ma` |
| Penyebutan penuh / subjek | `Mama` |
| Kata ganti MC bicara ke Mama | `aku` |
| Kata ganti MC bicara tentang Mama ke orang lain | `Mama` |

**Pola vokatif:**
- Di awal kalimat: `"Mama, aku minta maaf."`
- Di akhir kalimat: `"Aku minta maaf, Ma."`
- Di tengah kalimat: `"Aku, Ma, beneran nggak bermaksud begitu."`
- Berdiri sendiri: `"Ma…"` atau `"Mama…"`

**Contoh benar:**
```
"Maaf, Ma. Aku nggak bermaksud ngebentak Mama."
"Makasih, Mama emang yang terbaik."
"Aku akan jelasin semuanya besok, Ma."
"Mama nggak marah, kan?"
```

**Contoh salah:**
```
"Makasih, Ma emang yang terbaik."       ← 'Ma' bukan subjek, ini salah
"Gue minta maaf, Ma."                   ← gue tidak pantas ke Mama
"Aku akan jelasin ke Ibu."              ← gunakan Mama, bukan Ibu
```

### 4.2 MC ke Tante Julia

| Situasi | Form yang Benar |
|---|---|
| Panggilan langsung pendek | `Tan` |
| Penyebutan penuh / subjek | `Tante` |
| Kata ganti MC bicara ke Tante | `aku` |
| Kata ganti MC bicara tentang Tante ke orang lain | `Tante Julia` / `Tante` |

**Contoh benar:**
```
"Makasih ya, Tan."
"Tante baik-baik saja?"
"Aku percaya Tante."
"Jangan khawatir soal itu, Tan."
"Tante nggak harus ngelakuin ini."
```

**Placeholder `[aujp]`:** Jangan dihapus atau diganti. Terjemahkan kalimat di sekitarnya agar tetap natural dengan placeholder tersebut di tempatnya.

### 4.3 MC ke Teman / Sebaya

Untuk Lori, Barbara, Haley, Jim, Daphne, dan karakter selevel:
- Gunakan `gue / lo`
- Boleh lebih santai, kasar jika konteks mendukung
- Boleh singkat dan tajam

```
"Lo yakin soal ini?"
"Gue nggak tahu harus bilang apa."
"Makasih udah bantu gue."
"Anjing, lo serius?"
```

### 4.4 Aturan Placeholder

- Gunakan placeholder `[mc]`, `[m]`, `[aucp]`, `[aujp]`, `[barb2]`, `[hal]`, dll. sesuai aslinya.
- **Jangan ganti placeholder dengan nama statis** — placeholder itu berubah sesuai pilihan pemain.
- Terjemahkan kalimat di sekitar placeholder agar tetap natural, biarkan placeholder di tempatnya.

```renpy
# ❌ Salah — placeholder hilang
"Cassandra memandang [mc] dengan heran."

# ✅ Benar — placeholder utuh
"[aucp] memandang [mc] dengan heran."
```

---

### 4.5 Karakter Lain Berbicara KEPADA Cassandra

> **Prinsip inti:** `Mama` dan `Ma` adalah **eksklusif milik MC**. Karakter lain selalu menggunakan nama atau nickname Cassandra.

Ketika karakter selain MC berbicara **langsung** (vokatif) kepada Cassandra:

| Siapa yang bicara | Terjemahan yang benar |
|---|---|
| Teman sebaya / sesama orang dewasa | `Cassandra`, `Cassie`, `Cass` |
| Karakter muda / junior | `Cassandra`, atau `Ms. [nama]` jika konteks formal |
| Siapapun yang bukan MC | **Jangan pakai `Mama` atau `Ibu`** |

```
# Lori berbicara langsung ke Cassandra:
EN: "Cassandra, you look amazing tonight."
✅  "Cassandra, lo kelihatan keren banget malam ini."
❌  "Mama, lo kelihatan keren banget malam ini."  ← salah, Lori bukan anak Cassandra

# Teman Cassandra memanggilnya dengan nickname:
EN: "Cassie! Long time no see!"
✅  "Cassie! Lama banget nggak ketemu!"
❌  "Bu Cassie! Lama banget nggak ketemu!"
```

---

### 4.6 Karakter Lain Membicarakan Cassandra

Bedakan kepada **siapa** si pembicara sedang berbicara:

**A. Bicara ke MC tentang Cassandra**
Boleh menggunakan relasi MC sebagai anchor → `mama lo`, `ibunya lo`, `Cassandra`.

```
# Lori ke MC:
EN: "Your mom is the best cook."
✅  "Mama lo jago masak banget."
✅  "Cassandra jago masak banget."   ← nama langsung juga valid

EN: "I talked to Cassandra earlier."
✅  "Tadi gue ngobrol sama Cassandra."
✅  "Tadi gue ngobrol sama mama lo."  ← valid jika konteks MC jelas
```

**B. Bicara ke orang lain (bukan MC) tentang Cassandra**
Gunakan nama langsung saja → `Cassandra` atau `Cassie`.

```
# Barbara ke Jim, MC tidak ada di situ:
EN: "Cassandra said we should meet at seven."
✅  "Cassandra bilang kita harus ketemu jam tujuh."
❌  "Mama bilang kita harus ketemu jam tujuh."  ← siapa "Mama" ini? Konteks hilang
```

**C. Kata `Mom` / `Mother` dalam teks asli bukan dari MC**
Selalu cek siapa pembicara di baris `[karakter]:`.

```
# Lori berkata ke MC:
EN: Lori "Your mom is calling."
✅  "Mama lo lagi nelpon."

# Lori berkata ke sesama teman (bukan ke MC):
EN: Lori "Her mom called her."
✅  "Mamanya tadi nelpon."
✅  "Ibunya tadi nelpon."
❌  "Mama tadi nelpon."  ← tanpa referensi ke siapa, membingungkan
```

---

### 4.7 Cassandra Merujuk Dirinya Sendiri

**Saat berbicara ke MC:** Cassandra boleh memakai `Mama` sebagai self-reference dalam perannya sebagai ibu — ini natural dan umum dalam Bahasa Indonesia.

```
EN: Cassandra "Your mother loves you, you know that?"
✅  "Mama sayang kamu, kamu tau kan?"
✅  "Aku sayang kamu, kamu tau kan?"   ← juga valid, lebih netral
```

**Saat berbicara ke orang lain (bukan MC):** Cassandra menggunakan `aku` atau `saya`.

```
EN: Cassandra (ke Lori) "I already told him twice."
✅  "Aku udah bilang ke dia dua kali."
❌  "Mama udah bilang ke dia dua kali."  ← dia bicara ke Lori, bukan ke anaknya
```

---

### 4.8 Karakter Lain Berbicara KEPADA Julia

> **Prinsip inti:** `Tante` dan `Tan` adalah **eksklusif milik MC**. Karakter lain selalu menggunakan nama Julia.

| Siapa yang bicara | Terjemahan yang benar |
|---|---|
| Teman sebaya / sesama orang dewasa | `Julia`, `Jules` |
| Cassandra (sebagai teman) | `Julia` |
| Karakter muda / junior bukan MC | `Julia`, atau `Ms. Julia` jika formal |
| Siapapun yang bukan MC | **Jangan pakai `Tante`** |

```
# Barbara berbicara langsung ke Julia:
EN: "Julia, are you serious about this?"
✅  "Julia, lo serius soal ini?"
❌  "Tante, lo serius soal ini?"  ← Barbara bukan keponakan Julia

# Cassandra ke Julia:
EN: "Julia, we need to talk."
✅  "Julia, kita perlu ngobrol."
❌  "Tante Julia, kita perlu ngobrol."  ← Cassandra teman Julia, bukan keponakannya
```

---

### 4.9 Karakter Lain Membicarakan Julia

**A. Bicara ke MC tentang Julia**
Boleh pakai relasi MC → `tante lo`, `Julia`, `Tante Julia lo`.

```
# Lori ke MC:
EN: "Your aunt stopped by earlier."
✅  "Tante lo tadi mampir."
✅  "Julia tadi mampir."

EN: "I ran into Julia at the store."
✅  "Gue ketemu Julia di toko tadi."
✅  "Gue ketemu tante lo di toko tadi."  ← valid jika konteks jelas
```

**B. Bicara ke orang lain (bukan MC) tentang Julia**
Gunakan nama langsung → `Julia`.

```
# Barbara ke Jim:
EN: "Julia told me about it."
✅  "Julia udah cerita ke gue soal itu."
❌  "Tante Julia udah cerita ke gue soal itu."  ← Jim bukan keponakan Julia
```

**C. Kata `Aunt` / `Auntie` dalam teks asli bukan dari MC**

```
# Lori ke MC:
EN: Lori "Your aunt is looking for you."
✅  "Tante lo lagi nyariin lo."

# Cassandra ke MC tentang Julia:
EN: Cassandra "Your aunt called this morning."
✅  "Tante lo tadi pagi nelpon."
✅  "Julia tadi pagi nelpon."
```

---

### 4.10 Julia Merujuk Dirinya Sendiri

**Saat berbicara ke MC:** Julia boleh memakai `Tante` sebagai self-reference dalam perannya.

```
EN: Julia "Your aunt just wants you to be happy."
✅  "Tante cuma mau kamu bahagia."
✅  "Aku cuma mau kamu bahagia."   ← juga valid
```

**Saat berbicara ke orang lain (bukan MC):** Julia menggunakan `aku`.

```
EN: Julia (ke Cassandra) "I'll take care of it."
✅  "Aku yang urus."
❌  "Tante yang urus."  ← dia bicara ke Cassandra, bukan ke keponakannya
```

---

### 4.11 Penanganan Nickname

Pertahankan nickname **persis seperti aslinya** — jangan adaptasi, jangan ganti ke nama penuh, dan jangan campur-aduk dalam satu scene.

| Karakter | Nama penuh | Nickname umum | Terjemahan |
|---|---|---|---|
| Cassandra | `Cassandra` | `Cassie`, `Cass` | Pertahankan apa adanya |
| Julia | `Julia` | `Jules`, `Juli` | Pertahankan apa adanya |

**Mengapa ini penting:** Nickname menunjukkan **tingkat keakraban**. Karakter yang memanggil `Cassie` punya kedekatan berbeda dengan yang memanggil `Cassandra`. Mengganti satu ke yang lain menghapus nuansa relasi ini.

```
# Teman lama Cassandra yang akrab:
EN: "Cassie, I missed you so much."
✅  "Cassie, gue kangen banget sama lo."
❌  "Cassandra, gue kangen banget sama lo."  ← kehilangan keakraban

# Kenalan baru atau konteks formal:
EN: "Ms. Cassandra, thank you for coming."
✅  "Cassandra, makasih udah mau datang."   ← atau sesuai konteks keformalan
```

---

### 4.12 Matriks Deteksi Lengkap

Gunakan tabel ini sebagai **referensi cepat** setiap kali menjumpai nama atau sapaan Cassandra/Julia dalam teks sumber.

#### Cassandra / Mama

| Siapa yang bicara | Bicara kepada | Kata asli (EN) | Terjemahan yang benar |
|---|---|---|---|
| MC | Cassandra langsung | `Mom`, `Ma` | `Mama`, `Ma` |
| MC | orang lain, tentang Cassandra | `my mom`, `my mother` | `Mama`, `Mama gue` |
| Lori / sebaya MC | Cassandra langsung | `Cassandra`, `Cassie` | `Cassandra`, `Cassie` |
| Lori / sebaya MC | MC, tentang Cassandra | `your mom`, `Cassandra` | `mama lo`, `Cassandra` |
| Lori / sebaya MC | orang lain (bukan MC), tentang Cassandra | `Cassandra`, `she` | `Cassandra`, `dia` |
| Cassandra | MC (self-reference) | `your mother`, `Mom` | `Mama`, `aku` |
| Cassandra | orang lain (bukan MC) | `I` | `aku` |
| Dewasa / sebaya Cassandra | Cassandra langsung | `Cassandra`, `Cassie`, `Cass` | `Cassandra`, `Cassie`, `Cass` |
| Dewasa / sebaya Cassandra | siapapun, tentang Cassandra | `Cassandra`, `she` | `Cassandra`, `dia` |
| Julia | MC, tentang Cassandra | `your mom`, `Cassandra` | `mama lo`, `Cassandra` |

#### Julia / Tante

| Siapa yang bicara | Bicara kepada | Kata asli (EN) | Terjemahan yang benar |
|---|---|---|---|
| MC | Julia langsung | `Aunt`, `Auntie`, `Aunt Julia` | `Tante`, `Tan` |
| MC | orang lain, tentang Julia | `my aunt`, `Aunt Julia` | `Tante`, `Tante Julia` |
| Lori / sebaya MC | Julia langsung | `Julia`, `Jules` | `Julia`, `Jules` |
| Lori / sebaya MC | MC, tentang Julia | `your aunt`, `Julia` | `tante lo`, `Julia` |
| Lori / sebaya MC | orang lain (bukan MC), tentang Julia | `Julia`, `she` | `Julia`, `dia` |
| Julia | MC (self-reference) | `your aunt`, `Aunt Julia` | `Tante`, `aku` |
| Julia | orang lain (bukan MC) | `I` | `aku` |
| Dewasa / sebaya Julia | Julia langsung | `Julia`, `Jules` | `Julia`, `Jules` |
| Dewasa / sebaya Julia | siapapun, tentang Julia | `Julia`, `she` | `Julia`, `dia` |
| Cassandra | MC, tentang Julia | `your aunt`, `Julia` | `tante lo`, `Julia` |

> **Ringkasan satu kalimat:** `Mama`/`Ma` dan `Tante`/`Tan` hanya muncul saat **MC** yang bicara, atau saat **Cassandra/Julia merujuk dirinya sendiri ke MC**. Semua kasus lain → gunakan nama.

---

## 5. Suara dan Kepribadian Karakter

Setiap karakter punya cara bicara tersendiri. Pertahankan konsistensi ini lintas scene.

### 5.1 MC (Protagonis)

- **Internal monolog:** `gue` — langsung, kadang sarkastis, jujur ke diri sendiri
- **Bicara ke sebaya:** `gue / lo` — santai, bisa flirtatious, bisa tegas
- **Bicara ke Mama/Tante:** `aku` — lebih hati-hati, sopan, kadang canggung

### 5.2 Mama / Cassandra

- Hangat dan penyayang tapi bisa tegas
- Bicara ke MC: bisa pakai `sayang`, `kamu`, nama MC
- Saat marah: lebih singkat, nada dingin
- Jangan buat Mama terdengar terlalu formal atau seperti ibu dari buku teks

### 5.3 Tante Julia

- Lebih playful dibanding Mama
- Bisa lebih flirtatious dan berani
- Bicara ke MC: lebih santai, kadang menggoda
- Tetap terkesan dewasa dan berpengalaman

### 5.4 Lori

- Sahabat dekat MC — bicara sangat bebas
- Sering pakai filler, slang, hiperbola
- Ekspresif dan dramatis
- Panggilan `bunny` bisa dipertahankan jika konsisten

### 5.5 Barbara

- Tergantung konteks — bisa formal di satu scene, santai di scene lain
- Pertahankan konsistensi dengan scene sebelumnya

### 5.6 Haley

- Perhatikan arc karakternya — jangan terjemahkan "flat"
- Nada berbeda antara saat dia nyaman vs. tidak nyaman

### 5.7 Jim

- Bicara seperti teman cowok yang santai, bisa kasar
- `bro`, `bos`, atau nama langsung sesuai konteks

---

## 6. Dialog vs. Narasi vs. Monolog Internal

Ketiga jenis teks ini punya aturan berbeda.

### 6.1 Dialog (teks di bawah nama karakter)

- Harus terdengar seperti **ucapan lisan**, bukan tulisan
- Kontraksi dan slang dianjurkan: `nggak`, `gimana`, `emang`, `udah`
- Boleh kalimat tidak lengkap jika konteks mendukung
- Ellipsis `…` untuk jeda dramatis atau ragu-ragu

### 6.2 Narasi (teks tanpa nama karakter, atau `narrator`)

- Lebih terstruktur dari dialog, tapi tetap tidak kaku
- Ditulis dari sudut pandang MC → bisa cenderung ke register `gue`
- Boleh lebih puitis atau deskriptif
- Hindari bahasa buku pelajaran; tetap hidup dan engaging

**Contoh narasi:**
```
# Asli:
"The room felt different tonight. Warmer. Or maybe that was just her."

# ❌ Terlalu kaku:
"Ruangan itu terasa berbeda malam ini. Lebih hangat. Atau mungkin hanya dia."

# ✅ Lebih natural:
"Entah kenapa kamar ini rasanya beda malam ini. Lebih hangat. Atau mungkin itu cuma efek dia."
```

### 6.3 Monolog Internal / Pikiran MC

- Register `gue` kecuali sedang memikirkan Mama/Tante (bisa tetap `aku` untuk konsistensi rasa)
- Sangat jujur — MC nggak sensor pikirannya sendiri
- Bisa lebih vulgar, jujur, atau panik dari dialog eksternalnya
- Gunakan elipsis dan em-dash untuk menunjukkan pikiran yang terputus

```
# Pikiran MC melihat Lori:
"Gue nggak seharusnya ngeliatin dia kayak gitu. Tapi… sial."

# Pikiran MC soal Mama:
"Kenapa Mama harus secantik itu. Ini nggak adil."
```

---

## 7. Partikel, Filler, dan Nuansa Bahasa Indonesia

Partikel adalah **salah satu pembeda terbesar** antara terjemahan kaku dan yang terasa natural. Gunakan dengan tepat.

### 7.1 Partikel Penegas

| Partikel | Fungsi | Contoh |
|---|---|---|
| `sih` | Menyatakan heran ringan, menegaskan nada | `"Lo sih gimana?"`, `"Apaan sih?"` |
| `dong` | Meminta/mendesak secara halus, ekspresi keinginan | `"Cerita dong."`, `"Jangan pergi dong."` |
| `deh` | Konsesi, setengah-setuju, penutup lembut | `"Oke deh."`, `"Terserah lo deh."` |
| `nih` | Menegaskan sesuatu yang ada/nyata | `"Ini nih yang gue mau."`, `"Lo nih…"` |
| `lho` | Kejutan ringan, klarifikasi | `"Lho, lo udah tau?"` |
| `kan` | Konfirmasi, mengajak setuju | `"Enak kan?"`, `"Tadi lo bilang gitu kan?"` |
| `ya` | Konfirmasi lunak, ajakan | `"Oke ya?"`, `"Makasih ya."` |
| `kok` | Heran/protes ringan | `"Kok lo bisa tau?"`, `"Kok malah nangis?"` |

### 7.2 Filler dan Interjeksi

| Kata | Penggunaan |
|---|---|
| `Eh` | Panggilan perhatian, kejutan ringan |
| `Nah` | Penutup penjelasan, "nah begitu" |
| `Wah` | Ekspresi kagum atau kejutan |
| `Hmm` | Berpikir, ragu-ragu |
| `Ugh` | Frustrasi (boleh dipertahankan dari bahasa Inggris) |
| `Aduh` | Keluhan, rasa sakit ringan, frustrasi |
| `Astaga` | Kejutan, takjub |
| `Yah` | Kekecewaan ringan |
| `Hei` | Panggilan, bisa juga protes |

### 7.3 Intensifier Umum

| Bahasa Inggris | Terjemahan Natural |
|---|---|
| `really` / `very` | `banget`, `beneran`, `beneran banget`, `parah` |
| `so much` | `banget`, `parah banget` |
| `absolutely` | `beneran`, `emang beneran`, `absolutely` (jika konteks memang itu) |
| `incredibly` | `luar biasa`, `gilak`, `serius deh` |
| `just` (penekanan) | `cuma`, `doang`, `aja` |

### 7.4 Kontraksi Natural

Selalu gunakan versi kontraksi untuk dialog kasual:

| Formal | Kasual |
|---|---|
| `tidak` | `nggak` / `gak` / `enggak` |
| `sudah` | `udah` / `udah` |
| `begini` | `gini` |
| `begitu` | `gitu` |
| `seperti ini` | `kayak gini` |
| `mengapa` / `kenapa` | `kenapa` |
| `bagaimana` | `gimana` |
| `memang` | `emang` |
| `seperti` | `kayak` |
| `sampai` | `sampe` |
| `habis itu` | `abis itu` |

---

## 8. Negasi

Pilih bentuk negasi yang tepat sesuai register:

| Bentuk | Kapan digunakan |
|---|---|
| `tidak` | Narasi formal, atau dialog karakter yang bicara lebih formal |
| `nggak` | Dialog kasual umum — **pilihan default** untuk MC dan teman sebaya |
| `gak` | Sangat kasual, kadang frustrasi, bisa juga saat terburu-buru |
| `enggak` | Penolakan yang lebih tegas, kadang defensif |
| `bukan` | Mengoreksi identitas/kategori (`"Bukan gue yang salah"`) |
| `jangan` | Larangan (`"Jangan pergi"`) |
| `belum` | Negasi untuk hal yang diharapkan terjadi tapi belum |

**Contoh nuansa:**
```
"Gue nggak mau." — penolakan biasa
"Gue gak mau!" — lebih frustrasi/emosional
"Enggak, bukan gitu maksudnya." — defensif, meluruskan
"Gue belum siap." — belum, bukan tidak mau
```

---

## 9. Kosa Kata dan Glosarium

### 9.1 Ekspresi Emosi/Kasar

| Bahasa Inggris | Terjemahan Kontekstual |
|---|---|
| `Fuck!` (ekspresi) | `Sial!`, `Anjing!`, `Brengsek!`, `Sialan!` |
| `What the fuck` | `Apa-apaan ini`, `Anjing`, `Gila banget` |
| `Fuck you` | `Mampus lo`, `Persetan`, `Brengsek` |
| `Fuck off` | `Pergi`, `Minggat lo`, `Enyah` |
| `Fuck (verb, marah)` | `Setan`, `Sialan` |
| `Shit!` | `Sial!`, `Astaga!`, `Gila!` |
| `Oh shit` | `Aduh sial`, `Gila`, `Oh tidak` |
| `Holy shit` | `Ya ampun`, `Gila beneran`, `Anjir` |
| `Damn` | `Sial`, `Anjir`, `Hah` |
| `Damn it` | `Sialan`, `Sial banget` |
| `Asshole` (orang) | `Brengsek`, `Bajingan`, `Sialan` |
| `Bastard` | `Bajingan`, `Brengsek` |
| `Bitch` (kasar) | `Jalang`, `Brengsek` |
| `Son of a bitch` | `Bajingan`, `Anak haram` |
| `Idiot` / `Moron` | `Idiot`, `Bego`, `Tolol` |

### 9.2 Ekspresi Seksual

| Bahasa Inggris | Terjemahan |
|---|---|
| `cock` / `dick` | `kontol` |
| `pussy` / `vagina` (kasar) | `memek` |
| `ass` (seksual/vulgar) | `pantat`, `bokong` |
| `asshole` (anal) | `lubang pantat` |
| `cum` (noun) | `sperma`, `cairan` |
| `cum` (verb) | `keluar`, `klimaks` |
| `fuck` (verb, seksual) | `tiduri`, `meniduri`, `menghajar`, `bercinta` (sesuai nada) |
| `make love` | `bercinta` |
| `go down on` | `menjilati`, `oral` |
| `blow job` | `oral`, `nyepong` |
| `hand job` | `ngehandle`, `dikocok` |
| `horny` | `terangsang`, `gairah`, `birahi` |
| `turned on` | `terangsang`, `terbakar` |
| `aroused` | `terangsang`, `bergairah` |
| `orgasm` | `orgasme`, `klimaks` |
| `nipple` | `puting` |
| `breasts` / `tits` | `payudara`, `toket` (kasual/kasar) |
| `moan` | `rintihan`, `desahan` |
| `to moan` | `merintih`, `mendesah` |
| `wet` (seksual) | `basah` |
| `hard` (seksual) | `keras`, `tegang`, `ereksi` |
| `naked` / `nude` | `telanjang` |
| `undress` | `menanggalkan pakaian`, `buka baju` |

### 9.3 Nada Seksual — Lembut vs. Kasar

**Nada romantis/lembut:**
```
bercinta, menyentuhku, memeluknya, merasakannya, hangat, lembut, sayang
```

**Nada nakal/playful:**
```
menggoda, bikin gue gila, nggak tahan, mau banget, panas
```

**Nada kasar/eksplisit/dom-sub:**
```
kontol, memek, meniduri, jalang, manut, paksa, kuasai
```

### 9.4 Ekspresi Dom/Sub

| Bahasa Inggris | Terjemahan |
|---|---|
| `Good girl` (dom/sub) | `Anak pintar`, `Gadis penurut`, `Pintar` |
| `Good girl` (sayang biasa) | `Anak baik`, `Pintar` |
| `Be a good girl` | `Jadilah anak baik`, `Nurut dong` |
| `You're mine` | `Lo milik gue`, `Kamu milikku` |
| `Do as I say` | `Ikuti perintah gue`, `Turuti gue` |
| `Beg for it` | `Minta dulu`, `Minta sama gue` |

### 9.5 Sapaan dan Panggilan Sayang

| Bahasa Inggris | Terjemahan |
|---|---|
| `sweetie` / `honey` / `dear` (dari dewasa ke anak/muda) | `sayang` |
| `baby` (pasangan) | `sayang`, `baby` |
| `darling` | `sayang`, `kamu` |
| `sweetheart` | `sayang` |
| `babe` | `babe`, `sayang` (sesuaikan) |
| `bunny` (Lori) | Pertahankan `bunny` |

---

## 10. Frasa Berulang dan Ekspresi Standar

Gunakan terjemahan berikut secara konsisten di seluruh patch.

### 10.1 Ekspresi Umum

| Bahasa Inggris | Terjemahan Standar |
|---|---|
| `Oh my God` / `Oh God` | `Ya Tuhan`, `Ya ampun`, `Astaga` |
| `Jesus` / `Jesus Christ` | `Ya ampun`, `Sial` (jangan terjemahkan religius kecuali konteks memang itu) |
| `I can't believe this` | `Gue nggak percaya ini`, `Nggak nyangka` |
| `Are you kidding me?` | `Lo serius?`, `Beneran nih?`, `Gila lo` |
| `No way` | `Nggak mungkin`, `Jangan`, `Serius?` |
| `Of course` | `Ya iyalah`, `Tentu`, `Pastinya` |
| `Relax` | `Santai`, `Tenang dong` |
| `Trust me` | `Percaya sama gue`, `Percayalah` |
| `I'm sorry` | `Maaf`, `Gue minta maaf`, `Sorry` |
| `Thank you` | `Makasih`, `Terima kasih` (formal) |
| `You're welcome` | `Sama-sama`, `Santai aja` |
| `Whatever` | `Terserah`, `Apapunlah` |
| `Fine` | `Oke`, `Baiklah`, `Terserah deh` |
| `I don't know` | `Gue nggak tau`, `Entahlah` |
| `Maybe` | `Mungkin`, `Kayaknya` |
| `Exactly` | `Tepat sekali`, `Betul`, `Persis` |
| `Come on` | `Ayo dong`, `Ayolah`, `Masa` |
| `Wait` | `Tunggu`, `Bentar` |
| `Seriously?` | `Serius?`, `Masa sih?` |
| `Let's go` | `Ayo`, `Yuk` |
| `Never mind` | `Nggak apa-apa`, `Udahlah`, `Lupain` |
| `I mean` | `Maksudnya`, `Gue maksudnya` |
| `You know what I mean` | `Lo tau kan maksud gue`, `Ngerti kan?` |
| `Kind of` / `Sort of` | `Semacam`, `Kayaknya`, `Agak` |
| `Basically` | `Intinya`, `Pokoknya` |
| `Honestly` | `Jujur`, `Jujur aja` |
| `To be honest` | `Jujur ya`, `Kalau jujur sih` |
| `I think` | `Kayaknya`, `Gue rasa`, `Menurut gue` |
| `Like` (filler) | `Gitu`, `Kayak`, bisa dihilangkan |

### 10.2 Ekspresi Emosi

| Bahasa Inggris | Terjemahan Standar |
|---|---|
| `I hate this` | `Gue benci ini`, `Nggak suka banget` |
| `I love you` | `Aku cinta kamu`, `Gue sayang lo` (sesuai konteks) |
| `I miss you` | `Gue kangen lo`, `Aku kangen kamu` |
| `I need you` | `Gue butuh lo`, `Aku butuh kamu` |
| `I want you` | `Gue mau lo`, `Aku mau kamu` (bisa seksual/emosional) |
| `This is so embarrassing` | `Ini memalukan banget`, `Malu banget gue` |
| `I'm scared` | `Gue takut`, `Aku takut` |
| `Don't leave me` | `Jangan pergi`, `Jangan tinggalin gue` |
| `I'm fine` | `Gue baik-baik aja`, `Nggak apa-apa` |
| `Are you okay?` | `Lo baik-baik aja?`, `Kamu oke?` |

---

## 11. Dialog Seksual dan Eksplisit

### 11.1 Prinsip

- Jangan sensor adegan seksual.
- Pertahankan intensitas, kecepatan, dan nada asli.
- Jangan ubah adegan yang kasar menjadi lembut, atau sebaliknya.
- Pertahankan dinamika karakter (siapa yang dominan, siapa yang submisif, siapa yang ragu).

### 11.2 Pilih Kata Berdasarkan Nada Adegan

**Adegan lembut/romantis:**
```
bercinta, menyentuh, merasakan, hangat, lembut, sayang, intim, mencintai
```

**Adegan playful/nakal:**
```
menggoda, nakal, panas, gairah, mau, nggak tahan, bikin gila
```

**Adegan kasar/eksplisit:**
```
kontol, memek, meniduri, menghajar, jalang, manut, dipaksa, dikuasai
```

**Adegan dom/sub:**
```
perintah, turuti, minta, anak pintar, milik gue, jangan bergerak
```

### 11.3 Narasi Seksual

Narasi seksual harus tetap engaging dan tidak medis. Hindari terminologi klinik kecuali karakter memang bicara dalam nada medis/dingin.

```
# ❌ Terlalu medis/kaku:
"Dia merasa adanya penetrasi pada area vaginanya."

# ✅ Natural dan sesuai nada:
"Gue ngerasain dia masuk, dan gue hampir nggak bisa nahan suara."
```

### 11.4 Desahan dan Rintihan

Dalam Ren'Py, suara karakter saat adegan seksual sering berupa teks pendek. Terjemahkan dengan nuansa:

| Bahasa Inggris | Terjemahan |
|---|---|
| `Ah…` | `Ah…` (pertahankan) |
| `Mmm…` | `Hmm…` / `Mmm…` |
| `Yes… right there` | `Ya… di situ` |
| `Don't stop` | `Jangan berhenti`, `Jangan…` |
| `Harder` | `Lebih keras`, `Kencengin` |
| `Faster` | `Lebih cepat`, `Cepetan` |
| `I'm close` | `Gue hampir`, `Bentar lagi` |
| `I'm coming` | `Gue mau keluar`, `Gue hampir` |

---

## 12. Tanda Baca dan Format Teks

### 12.1 Elipsis (…)

- Gunakan untuk jeda, ragu-ragu, atau kalimat yang menggantung.
- Gunakan karakter `…` (satu karakter unicode), bukan tiga titik `...`
- Boleh `…` di akhir atau di tengah kalimat.
```
"Gue nggak tau… mungkin iya."
"Kamu… kamu serius?"
"Kalau saja waktu itu…"
```

### 12.2 Em-dash (—)

- Gunakan untuk interupsi mendadak, pikiran yang terputus, atau jeda yang lebih tajam dari elipsis.
```
"Gue nggak—"
"Lo harus—tunggu, apa?"
```

### 12.3 Tanda Seru dan Tanya

- Jika aslinya `!?` atau `?!`, pertahankan.
- Jika aslinya beberapa `!!!`, pertahankan jumlahnya atau sesuaikan intensitas.
- Jangan menambah atau mengurangi tanda seru tanpa alasan emosional.

### 12.4 Huruf Kapital untuk Penekanan

- Jika aslinya ada kata dalam huruf kapital semua (`I TOLD YOU`), pertahankan kapitalisasi untuk menunjukkan teriakan/penekanan: `GUE UDAH BILANG`.
- Jangan gunakan kapital untuk penekanan jika aslinya tidak ada.

### 12.5 Tanda Kutip

- Untuk dialog dalam dialog (karakter mengutip ucapan orang lain), gunakan tanda kutip sesuai konteks Ren'Py.
- Dalam Ren'Py, string dibungkus `"..."` — perhatikan apostrofe atau tanda kutip dalam string yang bisa merusak parsing.

---

## 13. Sintaks Ren'Py — Aturan Wajib

### 13.1 Elemen yang Tidak Boleh Diubah

```renpy
# Label — jangan ubah
label day09:

# Jump/call — jangan ubah
jump day10
call screen choice0901

# Variabel — jangan ubah
$ lori_sex_life = True

# Placeholder — jangan ubah, hanya kalimat di sekitarnya yang diterjemahkan
"[mc] memandang [aucp] dengan heran."

# Format tag — jangan ubah
{i}Ini italic{/i}
{b}Ini bold{/b}
{size=-5}Teks kecil{/size}
{color=#ffffff}Teks putih{/color}

# Audio/image/video path — jangan ubah
play music "music/something.ogg"
show 09001
Movie(play="videos/scene09.webm")

# Blok if/else — pertahankan indentasi persis
if lori_sex_life:
    "Lori tersenyum."
else:
    "Lori tampak ragu."
```

### 13.2 Struktur Baris Terjemahan

Format standar baris terjemahan dalam `game/Indotranslate/`:

```renpy
translate indonesian day09_abc123:
    # "Original English text here."
    "Teks terjemahan Bahasa Indonesia di sini."
```

- Baris komentar (`# "..."`) adalah teks asli — **jangan diedit**.
- Baris aktif (`"..."`) adalah yang diterjemahkan.
- Indentasi 4 spasi — pertahankan.

### 13.3 Placeholder Lengkap

| Placeholder | Keterangan |
|---|---|
| `[mc]` | Nama MC |
| `[m]` | Varian nama MC |
| `[aucp]` | Nama Cassandra/Mama |
| `[aujp]` | Nama Julia/Tante |
| `[barb2]` | Nama Barbara (varian) |
| `[hal]` | Nama Haley |

**Hindari ini:**
```renpy
# ❌ Salah — placeholder dihapus
"Cassandra memandangnya dengan heran."

# ✅ Benar — placeholder dipertahankan
"[aucp] memandangnya dengan heran."
```

### 13.4 Komentar Teknis

- Komentar `###` boleh dibiarkan.
- Dialog aktif di sebelah komentar tetap diterjemahkan.
- Jangan hapus komentar, achievement unlock, atau marker debug.

---

## 14. Penanganan Kasus Sulit

### 14.1 Kalimat Ambigu

Jika teks asli ambigu (bisa berarti A atau B), pilih interpretasi yang:
1. Paling sesuai dengan konteks scene sebelum/sesudah.
2. Paling sesuai dengan kepribadian karakter.
3. Jika masih ragu, catat di laporan akhir untuk review.

### 14.2 Humor dan Wordplay

- Wordplay bahasa Inggris sering tidak bisa diterjemahkan langsung.
- Prioritas: **pertahankan efek/fungsinya** (membuat tertawa, mengejutkan, flirtatious), bukan kata-katanya.
- Jika perlu ganti dengan humor/wordplay Indonesia yang setara, lakukan. Catat di laporan bahwa ini adalah adaptasi.

### 14.3 Kalimat yang Terlalu Panjang di Terjemahan

Bahasa Indonesia cenderung lebih panjang dari bahasa Inggris. Jika terjemahan jauh lebih panjang:
- Pastikan tidak ada kata yang bisa dipotong tanpa kehilangan makna.
- Jika box teks game terlalu penuh, prioritaskan makna inti, singkat yang bisa disingkat.
- Jangan sacrificed nuansa emosi demi pemendekan.

### 14.4 Nama Tempat, Brand, Produk

- Pertahankan nama asli: `McDonald's`, `Nike`, nama kota, dll.
- Jangan terjemahkan nama proper.

### 14.5 Angka dan Satuan

- Pertahankan format asli: `$50`, `10 minutes`, `6 feet`
- Jangan konversi satuan kecuali diminta.

### 14.6 Pergeseran Register dalam Satu Adegan

Kadang karakter bergeser dari kasual ke serius atau sebaliknya dalam satu scene. Ikuti pergeseran ini:
```
# Lori awal adegan (kasual):
"Lo tau nggak sih, kemarin gue ketemu seseorang yang aneh banget."

# Lori tiba-tiba serius:
"Tapi... gue nggak bohong. Ini beneran bikin gue takut."
```

---

## 15. Validasi Pasca-Terjemahan

Setelah menerjemahkan file, jalankan checklist ini **sebelum menyerahkan hasil**.

### 15.1 Checklist Teknis

- [ ] Tidak ada quote yang tidak ditutup (`"` tanpa pasangan)
- [ ] Semua placeholder (`[mc]`, `[aucp]`, dll.) masih utuh
- [ ] Semua format tag (`{i}`, `{b}`, `{size=...}`, dll.) masih simetris
- [ ] Indentasi 4 spasi tetap konsisten
- [ ] Tidak ada teks asli bahasa Inggris aktif yang tersisa (kecuali yang disengaja sebagai loanword)
- [ ] Path audio/image/video tidak berubah
- [ ] Variabel dan label tidak diubah

### 15.2 Checklist Kualitas

- [ ] Konsistensi sapaan: `aku/Ma/Mama` untuk MC ke Cassandra; `aku/Tan/Tante` untuk MC ke Julia; `gue/lo` untuk sebaya
- [ ] Konsistensi suara karakter (MC, Mama, Tante, Lori, dll.) sesuai §5
- [ ] Register sesuai konteks scene
- [ ] Tidak ada terjemahan harfiah yang terdengar aneh
- [ ] Idiom bahasa Inggris sudah diadaptasi, bukan diterjemahkan kata per kata
- [ ] Dialog terasa seperti ucapan lisan, bukan tulisan formal
- [ ] Intensitas emosi dan adegan seksual terjaga

### 15.3 Laporan Akhir

Sertakan laporan singkat berisi:
1. File yang dikerjakan.
2. Jumlah baris terjemahan.
3. Loanword/slang Inggris yang sengaja dipertahankan dan alasannya.
4. Kalimat ambigu yang perlu dikonfirmasi (jika ada).
5. Adaptasi humor/wordplay (jika ada).

---

## 16. Contoh Koreksi Sebelum / Sesudah

### 16.1 Dialog Kasual — Sebelum/Sesudah

```
# Asli:
"Are you seriously telling me you didn't know about this?"

# ❌ Terjemahan kaku:
"Apakah kamu serius memberitahuku bahwa kamu tidak tahu tentang ini?"

# ✅ Terjemahan natural:
"Lo serius bilang ke gue kalau lo nggak tau soal ini?"
```

### 16.2 Monolog Internal — Sebelum/Sesudah

```
# Asli (narasi/pikiran MC):
"God, she looked incredible. I shouldn't be thinking this."

# ❌ Kaku:
"Tuhan, dia tampak luar biasa. Aku tidak seharusnya berpikir tentang ini."

# ✅ Natural:
"Ya Tuhan, dia kelihatan keren banget. Gue nggak seharusnya mikirin ini."
```

### 16.3 Dialog Emosional — Sebelum/Sesudah

```
# Asli:
"I told you to stay away from her! What the fuck is wrong with you?!"

# ❌ Diperhalus:
"Aku sudah bilang untuk menjauhinya! Ada apa denganmu?!"

# ✅ Mempertahankan intensitas:
"Udah gue bilang jauhin dia! Anjing, lo kenapa sih?!"
```

### 16.4 Dialog Seksual — Sebelum/Sesudah

```
# Asli (adegan intens/kasar):
"You're mine. Say it."

# ❌ Diperhalus:
"Kamu milikku. Katakan."

# ✅ Mempertahankan nada dominan:
"Lo milik gue. Bilang."
```

### 16.5 Sapaan Mama — Sebelum/Sesudah

```
# Asli:
"Mom, I didn't mean to upset you. I'm sorry."

# ❌ Salah sapaan:
"Ibu, gue nggak maksud bikin lo kesal. Maaf."

# ✅ Benar:
"Mama, aku nggak bermaksud bikin Mama kesal. Maaf, Ma."
```

### 16.6 Placeholder — Sebelum/Sesudah

```
# Asli:
"[aucp] smiled at me warmly."

# ❌ Placeholder hilang:
"Cassandra tersenyum hangat ke gue."

# ✅ Placeholder utuh:
"[aucp] tersenyum hangat ke gue."
```

---

*Dokumen ini bersifat living document. Update sesuai kebutuhan patch per day/chapter. Tandai versi dan tanggal update di bagian atas jika ada perubahan signifikan.*

---

## Catatan Audit Agent - 2026-06-10
- `STYLE_ID.md` ditetapkan user sebagai acuan utama audit `game/Indotranslate/`.
- Status sebelum catatan ini: `rela.rpy` sudah diaudit/diperbaiki untuk profil karakter, UI relasi, dan deskripsi achievement; validasi akhir: odd quote 0, bad char 0, English UI hits 0.
- Report agresif yang masih dipakai untuk prioritas: `indotranslate_aggressive_english_report.txt`.
- Prioritas lanjut setelah `rela.rpy`: `22a.rpy`, `25.rpy`, `21a.rpy`, `28a.rpy`.

---

## Catatan Audit Agent - 2026-06-10 Full Audit
- Full audit seluruh `game/Indotranslate/*.rpy` dengan acuan `STYLE_ID.md` selesai.
- Report lengkap: `full_audit_STYLE_ID_report.md`.
- Coverage: 81 original `.rpy`, 81 TL `.rpy`, missing NONE, extra NONE.
- Prioritas fixing berikutnya berdasar report: `22a.rpy`, `28a.rpy`, `21a.rpy`, `25.rpy`, `28.rpy`, `22.rpy`, `24.rpy`, `choice.rpy`, `21b.rpy`, `11.rpy`.
- Note: kategori `tag_mismatch`/`placeholder_mismatch` perlu cek manual konteks karena line-shift bisa menyebabkan false positive.

---

## Catatan Audit Agent - 2026-06-10 `22a.rpy`
- `game/Indotranslate/22a.rpy` selesai diperbaiki dari prioritas #1 full audit.
- Validasi: orig/TL 1649 lines, label/jump/call sama, placeholder count sama, odd quote 0, bad char 0, English/MT hits 0, sapaan STYLE hits 0.
- Lanjut prioritas berikutnya: `28a.rpy`.

---

## Catatan Audit Agent - 2026-06-10 `28a.rpy`
- `game/Indotranslate/28a.rpy` selesai diperbaiki dari prioritas #2 full audit.
- Validasi: orig/TL 2487 lines, label/jump/call sama, placeholder count sama, odd quote 0, bad char 0, English/MT hits 0, sapaan STYLE hits 0, indent issues 0.
- Lanjut prioritas berikutnya: `21a.rpy`.

---

## Catatan Audit Agent - 2026-06-10 `21a.rpy`
- `game/Indotranslate/21a.rpy` selesai diperbaiki dari prioritas #3 full audit.
- Validasi: orig/TL 2135 lines, label/jump/call sama, placeholder count sama, odd quote 0, bad char 0, English/MT hits 0, sapaan STYLE hits 0, indent issues 0.
- Lanjut prioritas berikutnya: `25.rpy`.

---

## Catatan Audit Agent - 2026-06-10 `25.rpy`
- `game/Indotranslate/25.rpy` selesai diperbaiki dari prioritas #4 full audit.
- Validasi: orig/TL 1798 lines, label/jump/call sama, placeholder count sama, odd quote 0, bad char 0, English/MT hits 0, sapaan STYLE hits 0, indent issues 0.
- Lanjut prioritas berikutnya: `28.rpy`.

---

## Catatan Audit Agent - 2026-06-10 `28.rpy`
- `game/Indotranslate/28.rpy` selesai diperbaiki dari prioritas #5 full audit.
- Validasi: orig/TL 1797 lines, label/jump/call sama, placeholder count sama, odd quote 0, bad char 0, English/MT hits 0, sapaan STYLE hits 0, indent issues 0.
- Lanjut prioritas berikutnya: `22.rpy`.
## Progress Update - 22.rpy (2026-06-10)
- Completed full fix/validation for `game/Indotranslate/22.rpy`.
- Corrected broken indentation vs original, MT residue, English leftovers, and wrong Cassandra/Julia sapaan context.
- Validation: 852/852 lines, labels/jumps/calls same, placeholders same, odd quotes 0, bad chars 0, English/MT hits 0, indent mismatch 0.
- Next priority: `24.rpy`, then `choice.rpy`, `21b.rpy`, `11.rpy` per `full_audit_STYLE_ID_report.md`.
## Progress Update - 24.rpy (2026-06-10)
- Completed full fix/validation for `game/Indotranslate/24.rpy`.
- Fixed 62+ English/MT dialogue residues, corrected block indentation to match original, preserved Ren'Py structure/placeholders.
- Validation: 1675/1675 lines, labels/jumps/calls same, placeholders same, odd quotes 0, bad chars 0, English/MT hits 0, indent mismatch 0.
- Next priority: `choice.rpy`, then `21b.rpy`, `11.rpy`.
## Progress Update - choice.rpy (2026-06-10)
- Completed full fix/validation for `game/Indotranslate/choice.rpy`.
- Fixed UI choice English/MT residues, restored missing `[m]` placeholders, preserved actions/jumps/comments/indent.
- Validation: 4473/4473 lines, labels/jumps/calls same, placeholders same, odd quotes 0, bad chars 0, English/MT hits 0, indent mismatch 0.
- Next priority: `21b.rpy`, then `11.rpy`.
## Progress Update - 21b.rpy (2026-06-10)
- Completed full fix/validation for `game/Indotranslate/21b.rpy`.
- Fixed English/MT dialogue residues, restored missing `[mc]` placeholder, preserved labels/jumps/calls/indent.
- Validation: 856/856 lines, labels/jumps/calls same, placeholders same, odd quotes 0, bad chars 0, English/MT hits 0, indent mismatch 0.
- Next priority: `11.rpy`.
## Progress Update - 11.rpy (2026-06-10)
- Completed full fix/validation for `game/Indotranslate/11.rpy`.
- Fixed remaining English centered text, restored missing `[m]`/`[mc]` placeholders, preserved labels/jumps/calls/indent.
- Validation: 1492/1492 lines, labels/jumps/calls same, placeholders same, odd quotes 0, bad chars 0, English/MT hits 0, indent mismatch 0.
- Next priority: continue from `full_audit_STYLE_ID_report.md` after `11.rpy`.
## Progress Update - 04.rpy (2026-06-10)
- Completed full fix/validation for `game/Indotranslate/04.rpy`.
- Fixed English/MT residues, restored missing placeholders (`[aujp]`, `[mc]`, `[neig]`), corrected shifted dialogue blocks, and normalized Ren'Py text tags.
- Validation: 2425/2425 lines, labels/jumps/calls same, placeholders same, odd quotes 0, bad chars 0, English/MT hits 0, indent mismatch 0, tag mismatch 0.
- Next priority: `23.rpy`.

