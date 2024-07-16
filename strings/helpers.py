HELP_1 = """<b><u>perintah admin :</b></u>

cukup tambahkan <b>ᴄ</b> di bagian depan perintah untuk menggunakannya pada saluran.


/pause : menjeda streaming yang sedang diputar.

/resume : melanjutkan streaming yang dijeda.

/skip : lewati streaming yang sedang diputar dan mulai streaming trek sarang dalam antrian.

/end ᴏʀ /stop : menghapus antrian dan mengakhiri streaming yang sedang diputar.

/player : dapatkan panel pemutar interaktif.

/queue : menampilkan daftar lagu yang antri.
"""

HELP_2 = """
<b><u>pengguna autentikasi :</b></u>

pengguna autentikasi dapat menggunakan hak admin di bot tanpa hak admin di obrolan.

/auth [username/user_id] : menambahkan pengguna ke daftar autentikasi bot.
/unauth [nama pengguna/user_id] : menghapus pengguna autentikasi dari daftar pengguna autentikasi.
/authusers : menampilkan daftar pengguna autg grup.
"""

HELP_3 = """
<u><b>fitur siaran</b></u> [hanya untuk sudoer] :

/broadcast [pesan atau balas pesan] : menyiarkan pesan ke obrolan bot yang dilayani.

<u>mode penyiaran :</u>
<b>-pin</b> : menyematkan pesan siaran Anda di obrolan yang dilayani.
<b>-pinloud</b> : menyematkan pesan siaran Anda di obrolan yang dilayani dan mengirim pemberitahuan ke anggota.
<b>-user</b> : menyiarkan pesan ke pengguna yang telah memulai bot Anda.
<b>-assistant</b> : menyiarkan pesan Anda dari akun asisten bot.
<b>-nobot</b> : memaksa bot untuk tidak menyiarkan pesan.

<b>contoh:</b> <code>/broadcast -user -assistant -pin siaran pengujian</code>
"""

HELP_4 = """
<u><b>fitur daftar hitam obrolan :</b></u> [hanya untuk sudoer]

batasi obrolan sial untuk menggunakan bot kami yang berharga.

/blacklistchat [id obrolan] : memasukkan obrolan ke dalam daftar hitam agar tidak menggunakan bot.
/whitelistchat [id obrolan] : memasukkan obrolan yang masuk daftar hitam ke dalam daftar putih.
/blacklistedchat : menampilkan daftar chat yang masuk daftar hitam.
"""

HELP_5 = """
<u><b>memblokir pengguna:</b></u> [hanya untuk sudoer]

mulai mengabaikan pengguna daftar hitam, sehingga dia tidak dapat menggunakan perintah bot.

/block [nama pengguna atau balasan ke pengguna] : memblokir pengguna dari bot kami.
/unblock [nama pengguna atau balasan ke pengguna] : membuka blokir pengguna yang diblokir.
/blockedusers : menampilkan daftar pengguna yang diblokir.
"""

HELP_6 = """
<u><b>perintah pemutaran saluran:</b></u>

Anda dapat melakukan streaming audio/video di saluran.

/cplay : mulai mengalirkan trek audio yang diminta pada obrolan video saluran.
/cvplay : mulai mengalirkan trek video yang diminta pada obrolan video saluran.
/cplayforce atau /cvplayforce : menghentikan streaming yang sedang berlangsung dan mulai mengalirkan trek yang diminta.

/channelplay [nama pengguna atau id obrolan] atau [nonaktifkan] : menghubungkan saluran ke grup dan memulai streaming trek dengan bantuan perintah yang dikirim dalam grup.
"""

HELP_7 = """
<u><b>fitur larangan global</b></u> [hanya untuk sudoer] :

/gban [nama pengguna atau balasan ke pengguna] : secara global melarang pengguna dari semua obrolan yang dilayani dan memasukkan dia ke daftar hitam untuk menggunakan bot.

/ungban [nama pengguna atau balasan ke pengguna] : membatalkan pemblokiran secara global terhadap pengguna yang diblokir secara global.

/gbannedusers : menampilkan daftar pengguna yang diblokir secara global.
"""

HELP_8 = """
<b><u>aliran berulang :</b></u>

<b>mulai mengalirkan aliran yang sedang berlangsung secara berulang</b>

/loop [enable/disable] : mengaktifkan/menonaktifkan loop untuk streaming yang sedang berlangsung

/loop [1, 2, 3, ...] : mengaktifkan loop untuk nilai yang diberikan
"""

HELP_9 = """
<u><b>mode pemeliharaan</b></u> [hanya untuk sudoer] :

/logs : dapatkan log bot.

/logger [aktifkan/nonaktifkan] : bot akan mulai mencatat aktivitas yang terjadi pada bot.

/maintenance [enable/disable] : mengaktifkan atau menonaktifkan mode pemeliharaan bot Anda.
"""

HELP_10 = """
<b><u>ping & statistik :</b></u>

/start : memulai bot musik.
/help : dapatkan menu bantuan dengan penjelasan perintah.

/ping : menampilkan ping dan statistik sistem bot.

/stats : menampilkan statistik bot secara keseluruhan.
"""

HELP_11 = """
<u><b>perintah pemutaran :</b></u>

<b>v :</b> berarti pemutaran video.
<b>force :</b> berarti permainan paksa.

/play ᴏʀ /vplay : mulai mengalirkan trek yang diminta di obrolan video.

/playforce ᴏʀ /vplayforce : menghentikan streaming yang sedang berlangsung dan mulai mengalirkan trek yang diminta.
"""

HELP_12 = """
<b><u>antrean acak :</b></u>

/shuffle : shuffle antriannya.
/queue : menampilkan antrian shuffle.
"""

HELP_13 = """
<b><u>mencari aliran :</b></u>

/seek [durasi dalam detik] : mencari streaming dengan durasi tertentu.
/seekback [durasi dalam detik] : mencari aliran mundur ke durasi yang ditentukan.
"""

HELP_14 = """
<b><u>unduhan lagu</b></u>

/song [nama lagu/yt url] : unduh lagu apa pun dari youtube dalam format mp3 atau mp4.
"""

HELP_15 = """
<b><u>perintah kecepatan :</b></u>

Anda dapat mengontrol kecepatan pemutaran streaming yang sedang berlangsung. [hanya admin]

/speed atau /playback : untuk mengatur kecepatan pemutaran audio secara grup.
/cspeed atau /cplayback : untuk mengatur kecepatan pemutaran audio di saluran.
"""