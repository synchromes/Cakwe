# Agent Instructions - Milf's Plaza Indonesian Translation Project

## 0. Misi Utama
Teruskan proyek terjemahan patch dialog Milf's Plaza ke Bahasa Indonesia secara konsisten, natural, lengkap, dan aman secara teknis untuk Ren'Py.

Target akhir:
- Semua teks translatable dari `tl/eng/**/*.rpyc` dibuat versi Indonesian di `Indotranslate/`.
- Tidak sensor, tidak mengurangi dialog, tidak meringkas dialog.
- Terjemahan harus berdasarkan makna/konteks, bukan literal.
- Progress wajib dicatat setiap batch dengan format `x/370 = y%/100%`.

Progress terakhir saat dokumen ini dibuat:
- `49/370` source files selesai.
- `13.24%/100%`.

## 1. File Memori yang Wajib Dibaca Sebelum Mulai
Sebelum mengerjakan batch apa pun, agent wajib membaca:

1. `STYLE_ID.md` - style guide utama.
2. `Indotranslate/CLAUDE_MEM_HANDOFF.md` - glossary aktif, progress, daftar file selesai, validasi rutin.
3. `Indotranslate/_PROGRESS_ID.md` - log progress lengkap; update setiap selesai batch.
4. claude-mem bila aktif - coba search memori dulu; bila gagal, lanjut pakai dua file memori lokal.

## 2. Struktur Kerja
Source game mayoritas berupa `.rpyc` di `tl/eng/**/*.rpyc`.

Output terjemahan wajib dibuat di `Indotranslate/` dengan struktur mirror:
- Source: `tl/eng/core/talk_with/talk_with_milf.rpyc`
- Output: `Indotranslate/core/talk_with/talk_with_milf.rpy`

Jangan edit file utama game kecuali user eksplisit meminta.

## 3. Cara Ekstrak `.rpyc`
Gunakan Ren'Py runtime lokal untuk unpickle AST. Simpan helper script sementara bila perlu, lalu jalankan dengan:

`..\lib\py3-windows-x86_64\python.exe helper.py`

Helper minimal:

```python
import sys, os, zlib, struct, types
from pathlib import Path
sys.path.insert(0, os.path.abspath('..'))
import renpy
import renpy.config, renpy.object, renpy.revertable, renpy.rollback, renpy.python, renpy.ast
renpy.game = types.SimpleNamespace(script=types.SimpleNamespace(all_pyexpr=None))
from renpy.compat.pickle import loads
RPYC2_HEADER = b'RENPY RPC2'

def read(path, slot=1):
    data = Path(path).read_bytes()
    pos = len(RPYC2_HEADER)
    while True:
        s, start, length = struct.unpack('III', data[pos:pos+12])
        pos += 12
        if s == 0:
            break
        if s == slot:
            return zlib.decompress(data[start:start+length])

p = Path('tl/eng/path/to/file.rpyc')
data, stmts = loads(read(p))
for n in stmts:
    if type(n).__name__ == 'Translate':
        print('ID', n.identifier)
        for b in n.block:
            if type(b).__name__ == 'Say':
                print(' SAY', b.who, '|', b.what)
    if type(n).__name__ == 'Init':
        for b in n.block:
            if type(b).__name__ == 'TranslateString':
                print(' STR', repr(b.old), '=>', repr(b.new))
```

## 4. Format Output Ren'Py
Untuk dialog `Say`:

```renpy
translate indonesian some_identifier:
    # mc "Original English text."
    mc "Terjemahan Indonesia natural."
```

Untuk string UI/menu:

```renpy
translate indonesian strings:
    old "Текст оригинал"
    new "Terjemahan Indonesia"
```

Aturan:
- Pertahankan translate ID persis.
- Pertahankan speaker token persis: `mc`, `"Марина"`, `"Кристи"`, `[gg]`, dll.
- Pertahankan placeholder: `[mc]`, `[money]`, `[version_now]`, `[_watch_porn_line]`, dll.
- Pertahankan tag: `{i}`, `{b}`, `{alpha=*0.5}`, `{image=...}`, dll.
- Jangan ubah indentation Ren'Py.
- Boleh simpan source sebagai komentar `#` untuk review.

## 5. Prinsip Terjemahan
Wajib:
- Natural Bahasa Indonesia.
- Berdasarkan makna/konteks, bukan literal.
- Tidak sensor.
- Tidak memperhalus dialog kasar/eksplisit sampai makna berubah.
- Tidak menambah moralitas.
- Tidak mengurangi atau meringkas dialog.
- Kalau kalimat asli pendek/blunt, hasil juga pendek/blunt.
- Kalau dialog panas, boleh vulgar sesuai glossary.

Contoh idiom:
- `Forbidden fruit` jangan `buah terlarang`; gunakan `hal tabu`, `sesuatu yang nggak boleh tapi bikin penasaran`.
- `turn me on` jangan literal; gunakan `bikin terangsang`, `bikin gairah`.
- `I'm coming` dalam seks = `aku mau keluar`, `aku hampir keluar`.

## 6. Glossary Relasi Aktif
### Mother / Mary / Marina
- `Mary`, `Marina`, `mother`, `mom` -> `Mama` / `Ma`.
- Jangan gunakan `Ibu` di dialog game.
- MC memanggil langsung -> `Ma` atau `Mama` sesuai flow.
- Narasi/rujukan -> `Mama`.

### Father / James
- `James`, `Father`, `dad` -> `Ayah`.
- Jika konteks nama karakter teknis, boleh pertahankan `James` bila bukan relasi patch.

### Christie / Sister
User menetapkan Christie sebagai kakak perempuan MC.
- `Christie`, `Christy`, `sister` -> `Kak Christie`, `Kakak`, `Kak` sesuai konteks.
- MC -> Christie: `Kakak` / `Kak`.
- `your sister` -> `kakakmu`.
- `my sister` -> `kakakku`.
- Christie -> MC: `adik` / `adikku`.
- `You're my brother` -> `Kamu adikku`.
- `Brother's dick` -> `kontol adikku`.
- Adegan panas tetap gunakan `Kakak` / `Kak`.

## 7. Glossary Seksual Aktif
- `boobs/breasts` konteks normal -> `payudara`.
- `boobs/tits` konteks panas/seksual -> `toket`.
- `pussy/vagina` konteks panas -> `memek`.
- `jerk off/stroke your cock/masturbate` eksplisit -> `coli`; UI netral boleh `masturbasi`.
- `cum/come` klimaks seksual -> `keluar`.
- `cock/dick` eksplisit -> `kontol`.
- `ass/butt/booty` -> `pantat`; boleh `bokong` jika konteks normal.

Jangan kembali ke istilah lama:
- Jangan pakai `tetek`.
- Jangan pakai `kocok kontol`; pakai `coli`.

## 8. QA Wajib Tiap Batch
Setelah menulis batch, jalankan validasi minimal:

```powershell
$rows=@(); foreach($f in Get-ChildItem -LiteralPath 'Indotranslate' -Recurse -File -Filter *.rpy){
  $txt=Get-Content -LiteralPath $f.FullName -Raw
  $dq=([regex]::Matches($txt,'(?<!\\)"')).Count
  $lb=([regex]::Matches($txt,'\[')).Count
  $rb=([regex]::Matches($txt,'\]')).Count
  $lc=([regex]::Matches($txt,'\{')).Count
  $rc=([regex]::Matches($txt,'\}')).Count
  $rows += [pscustomobject]@{File=$f.FullName.Replace((Get-Location).Path+'\',''); QuotesEven=($dq%2 -eq 0); Brackets=($lb -eq $rb); Braces=($lc -eq $rc); Lines=(Get-Content -LiteralPath $f.FullName).Count}
}
$rows | Where-Object { -not $_.QuotesEven -or -not $_.Brackets -or -not $_.Braces } | Format-Table -AutoSize
Get-ChildItem -LiteralPath 'Indotranslate' -Recurse -File -Filter *.rpy | Select-String -Pattern 'Ibu\b|tetek|Kocok kontol|kocok kontol'
```

Jika output bad kosong dan banned search kosong -> OK.

## 9. Progress Accounting
Basis progress:
- Total source files: `370` dari `tl/eng/**/*.rpyc`.
- Count completed: jumlah `.rpy` di `Indotranslate/`.

Hitung progress:

```powershell
$total=(Get-ChildItem -LiteralPath 'tl\eng' -Recurse -File -Filter *.rpyc).Count
$done=(Get-ChildItem -LiteralPath 'Indotranslate' -Recurse -File -Filter *.rpy).Count
$pct=[math]::Round(($done/$total)*100,2)
"$done/$total = $pct%/100%"
```

Setiap selesai batch, update:
- `Indotranslate/_PROGRESS_ID.md`
- `Indotranslate/CLAUDE_MEM_HANDOFF.md`
- Laporkan ke user.

Format laporan:
```md
## Progress Update
- Selesai [N] file: [daftar ringkas].
- Progress file: X/370 = Y%/100%.
- Validasi semua file staging: quote/bracket/brace OK; banned drift clear.
```

## 10. File yang Sudah Selesai
Progress terakhir saat dokumen dibuat: `49/370 = 13.24%/100%`.

Untuk daftar terbaru, baca:
- `Indotranslate/CLAUDE_MEM_HANDOFF.md`
- `Indotranslate/_PROGRESS_ID.md`

## 11. Cara Pilih Batch Berikutnya
Disarankan:
1. Ambil file kecil dulu untuk menaikkan coverage cepat.
2. Gunakan 10-15 file per batch jika isinya pendek.
3. Untuk file besar/route utama, kerjakan satu file atau satu kelompok kecil saja.
4. Prioritaskan kualitas daripada kecepatan.

Cari remaining files:

```powershell
Get-ChildItem -LiteralPath 'tl\eng' -Recurse -File -Filter *.rpyc |
  Where-Object {
    $target=$_.FullName.Replace((Resolve-Path 'tl\eng').Path,(Resolve-Path 'Indotranslate').Path) -replace '\.rpyc$','.rpy'
    -not (Test-Path $target)
  } |
  Sort-Object Length |
  Select-Object -First 30 FullName,Length |
  Format-Table -AutoSize
```

## 12. Git/GitHub
Repo sudah di-push ke `https://github.com/synchromes/Cakwe` branch `main`.

Setelah update penting:
```powershell
git status --short
git add -A
git commit -m "Update Indonesian translation progress"
git push origin main
```

Jangan commit jika validasi gagal.

## 13. claude-mem
Server user: `localhost:37777`.

Cek:
```powershell
Invoke-RestMethod -Uri 'http://localhost:37777/api/health'
Invoke-RestMethod -Uri 'http://localhost:37777/api/chroma/status?deep=1'
```

Catatan terakhir:
- Server health OK.
- Chroma sempat unhealthy/backoff.
- MCP `search` sempat gagal transport.
- `observation_add` sempat gagal karena runtime worker, butuh server-beta.

Jika claude-mem pulih, simpan ringkasan progres/glossary ke memori. Jika belum, gunakan file lokal:
- `Indotranslate/CLAUDE_MEM_HANDOFF.md`
- `Indotranslate/_PROGRESS_ID.md`

## 14. Definisi Selesai Per Batch
Batch selesai jika:
- Semua source dalam batch punya output `.rpy` di `Indotranslate/`.
- Terjemahan natural dan sesuai glossary.
- Tidak ada placeholder/tag rusak.
- Validasi quote/bracket/brace OK.
- Banned drift clear.
- Progress percent updated.
- User diberi laporan ringkas.
