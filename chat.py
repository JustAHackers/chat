# — encoding: utf-8 —
namascriptini = __file__
import base64,requests,os,sys,time,random,smtplib
from difflib import get_close_matches
viewer1="https://justaserverscript.000webhostapp.com/view1.php"; viewer = "https://justaserverscript.000webhostapp.com/view.php";freeds = "free1day.txt"; coun = requests.post(viewer1,data={"id":"count.txt"}).text ; count = coun.replace(coun,coun) ; count = count.replace("\n",""); premiu = requests.post(viewer1,data={"id":"premium.txt"}).text ; premium = premiu.split("\n");getin = requests.post("https://justaserverscript.000webhostapp.com/view1.php",data={"id":"free1day.txt"}).text;poster = "https://justaserverscript.000webhostapp.com/poster.php";password = 'ohiabuebmpoeomqk';changer="https://justaserverscript.000webhostapp.com/changer.php";getin = getin.replace("\n","");print getin
r="\033[31m" #ini untuk warna merah
g="\033[1;32m" # ini untuk warna hijau
w="\033[1;37m" #ini untuk warna putih
c="\033[36m" #ini untuk warna cyan( aqua)
y="\033[33m" #ini untuk warna kuning
os.system("clear")
logo = """
\x1b[1;33m
 ╔═╗            •
 ║ ║   ╔══╗╔═══╗║╠═══╗
 ║ ║   ║  ║║   ║║║   ║
 ║ ╚══╗║  ║╚═══╣║║   ║
 ╚════╝╚══╝╔══ ║║║   ║
           ╚═══╝"""

thn = time.localtime()[0]
bln = time.localtime()[1]
hri = time.localtime()[2]
hri2 = hri + 2
hri3 = hri + 1
jam = time.localtime()[3]
mnt = time.localtime()[4]
if len(str(jam)) == 2:
   pass
else:
   jam = "0" + (str(jam))
men = time.localtime()[4]
if len(str(mnt)) == 2:
   pass
else:
   mnt = "0" + (str(mnt))
if len(str(bln)) == 2:
   pass
else:
   bln = "0" + (str(bln))
if len(str(hri)) == 2:
   pass
else:
   hri = "0" + (str(hri))
if len(str(hri2)) == 2:
   pass
else:
   hri2 = "0" + (str(hri2))
if len(str(hri3)) == 2:
   pass
else:
   hri3 = "0" + (str(hri3))
gbgn3 = [thn,bln,hri3,jam,mnt]
gbg3 = '-'.join(str(v) for v in gbgn3)
gbgn = [thn,bln,hri,jam,mnt]
gbgn2 = [thn,bln,hri2,jam,mnt]
gbg = ''.join(str(v) for v in gbgn)
gbg2 = '-'.join(str(v) for v in gbgn2)
mennu =  ("""

\x1b[1;32m╔═══════════════════════╗
\x1b[1;32m║         \x1b[1;36mMenu         \x1b[1;32m ║
\x1b[1;32m╠══╦════════════════════╣
║\x1b[1;33m01\x1b[1;32m║\x1b[1;33mLogin Akun JustA    \x1b[1;32m║
║\x1b[1;34m02\x1b[1;32m║\x1b[1;34mRegister Akun JustA \x1b[1;32m║
║\x1b[1;38m03\x1b[1;32m║\x1b[1;38mChange Password     \x1b[1;32m║
║\x1b[1;35m04\x1b[1;32m║\x1b[1;35mLupa Password       \x1b[1;32m║
║\x1b[1;31m05\x1b[1;32m║\x1b[1;31mExit                \x1b[1;32m║
╠══╩════════════════════╣
║\x1b[1;35mJumlah User :  \x1b[1;39m  %s     \x1b[1;32m║
╠═══════════════════════╝
║""" % (str(count)))


def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.01)
ididwo = """\x1b[1;37mSilahkan Login Untuk Script ini
Jika Anda Belum Punya Akun JustAHacker
Silahkan Daftar Di Menu Nomor 2
(gratis kok hehe)"""
trial = requests.post(viewer1,data={"id":"trial.txt"}).text
trial = trial.split("\n")
unmbas = requests.post(viewer1,data={"id":"uname.txt"}).text
unmbase = unmbas.split("\n")
databas = requests.post(viewer1,data={"id":"id.txt"}).text
database = databas.split("\n")
keren = """
                   \x1b[1;31m╔═══════╗
                   ║       ║
                 ╔═╩═══════╩═╗
                 ║ \x1b[1;36mL O G I N \x1b[1;31m║
                 ║ \x1b[1;33mUser&Pass \x1b[1;31m║
                 ╚═══════════╝"""
keren2 = """
                   \x1b[1;31m╔═══════╗
                   ║       ║
                 ╔═╩═══════╩═╗
                 ║ \x1b[1;36mR E G I S \x1b[1;31m║
                 ║ \x1b[1;33mUser&Pass \x1b[1;31m║
                 ╚═══════════╝"""
keren3 = """
                   \x1b[1;31m╔═══════╗
                   ║       ║
                 ╔═╩═══════╩═╗
                 ║ \x1b[1;36mG A N T I \x1b[1;31m║
                 ║ \x1b[1;33mPasswords \x1b[1;31m║
                 ╚═══════════╝"""
keren4 = """
                   \x1b[1;31m╔═══════╗
                   ║       ║
                 ╔═╩═══════╩═╗
                 ║ \x1b[1;36m L U P A  \x1b[1;31m║
                 ║ \x1b[1;33m Password \x1b[1;31m║
                 ╚═══════════╝"""
menul = """
\x1b[1;33m╔══╦═════════════════════════╗
║\x1b[1;37m01\x1b[1;33m║\x1b[1;37mGo To Tools              \x1b[1;33m║
║\x1b[1;35m02\x1b[1;33m║\x1b[1;35mFree Trial Premium 2days \x1b[1;33m║
║\x1b[1;32m03\x1b[1;33m║\x1b[1;32mBuy Premium              \x1b[1;33m║
║\x1b[1;34m04\x1b[1;33m║\x1b[1;34mGet Redeem Code Premium  \x1b[1;33m║
║\x1b[1;38m05\x1b[1;33m║\x1b[1;38mEnter Redeem Code        \x1b[1;33m║
║\x1b[1;31m99\x1b[1;33m║\x1b[1;31mLog Out                  \x1b[1;33m║
╠══╩═════════════════════════╝
║"""
kawal = """\x1b[1;31m
╔════╗    ╔═╗    ╔═╗    ╔═╗╔═╗
║╔═╗ ╚════╝ ╚════╝ ╚════╝ ╚╝ ╚════"""


kahir = """\x1b[1;31m║╚═╝ ╔════╗ ╔════╗ ╔════╗ ╔═╗ ╔═══
╚════╝    ╚═╝    ╚═╝    ╚═╝ ╚═╝"""


try:
   checkdev = open("/data/data/com.termux/files/usr/etc/auth.jsta").read()
   checkdevdec = base64.b64decode(checkdev)
   checkdevdec = checkdevdec.split(" ")
   unms = checkdevdec[0]
   pwdmm = checkdevdec[1]
   if checkdev in database:
      print c + "Selamat Datang \x1b[1;38m" + unms
      time.sleep(1)
   else:
      print "Password Salah"
      os.system("rm /data/data/com.termux/files/usr/etc/auth.jsta")
      os.system("python2 " + namascriptini)
   aaaa = get_close_matches(unms,premium,n=1,cutoff=0)
   aaaa = ''.join(aaaa)
   aaaa = aaaa.split(" ")
   namnam,panpan,wakwak = aaaa
   if unms == namnam:
      getp = get_close_matches(unms,premium,n=1,cutoff=0.1)
      getj = ''.join(getp)
      getz = getj.split(" ")
      idkmu,panah,wak = getz
      wakt = wak.split("-")
      thnp,blnp,hrip,jamp,detp = wakt
      pritime = hrip + "-" + blnp + "-" + thnp + "  " + jamp + ":" + detp
      waktu = ''.join(str(v)for v in wakt)
      if gbg > waktu:
         print "Waktu Premium Habis"
         requests.post(changer,data={"id":getj,"id1":"","dir":"premium.txt"})
         premiumpremiumpremium = False
         time.sleep(3)
      elif gbg < waktu:
         print "Akun Anda Premium"
         print "Sisa Waktu Premium\x1b[1;33m " + pritime
         premiumpremiumpremium = True
         time.sleep(3)
   else:
      print "Akun Kamu Tidak Premium"
      premiumpremiumpremium = False
      time.sleep(3)
   print menul
   chocho = raw_input("\x1b[1;33m╚════➤ \x1b[1;32m")
   if chocho == "3" or chocho == "03":
      raw_input("\x1b[1;33m[!]\x1b[1;32m Tekan Apapun Untuk Chat Admin")
      os.system("xdg-open https://wa.me/6289682009902?text=Saya%20Ingin%20Beli%20Premium%20Username%20:%20" + unms)
      sys.exit()
   elif chocho == "2" or chocho == "02":
      if unms in trial:
         print ("Anda Telah Menggunakan Trial Anda")
         sys.exit()
      else:
         if premiumpremiumpremium == True:
            print ("Sisa Waktu Premium Anda Masih Ada,Gunakan Trial Saat Premium Anda Habis")
            sys.exit()
         else:
	     gbbb = unms + " ==> " + gbg2
             raw_input("\x1b[1;33m[!]\x1b[1;32mTekan Apapun Untuk Mengaktifkan Trial 2Hari")
             requests.post(poster,data={"id":unms,"dir":"trial.txt"})
	     requests.post(poster,data={"id":gbbb,"dir":"premium.txt"})
	     print("Success")
             time.sleep(2);os.system("python2 " + namascriptini)
   elif chocho == "5" or chocho == "05":
      if premiumpremiumpremium == True:
         print ("Sisa Waktu Premium Anda Masih Ada,Gunakan Kode Saat Premium Anda Habis")
         sys.exit()
      else:
         print "\x1b[1;32mDapatkan Kode Gratis Di Menu Nomor 4"
         cda = raw_input("\x1b[1;32mKode : \x1b[1;33m")
         if cda == getin:
            gbbj = unms + " ==> " + gbg3
            generate1 = ('').join(random.sample(map(chr, range(48, 57) + range(65, 90) + range(97, 122)), 16))
            requests.post("https://justaserverscript.000webhostapp.com/neput.php",data={"put":generate1})
            requests.post(poster,data={"id":gbbj,"dir":"premium.txt"})
            print ("Success");sys.exit()
         else:
	    print("Kode Salah,Silahkan Dapatkan Di Menu Nomor 4")
            sys.exit()
   elif chocho == "4" or chocho == "04":
        print ("Silahkan Dapatkan Di Website Ini")
        time.sleep(2)
        os.system("xdg-open https://justaserverscript.000webhostapp.com/freepremium.php")
	sys.exit()
   elif chocho == "1" or chocho == "01":
      jalansc = requests.post(viewer,data={"id":"client.txt"}).text
      exec (jalansc,locals())
   elif chocho == "99":
      os.system("rm /data/data/com.termux/files/usr/etc/auth.jsta")
      sys.exit()
except IOError:
   pass

def menujusta():
    jalan(ididwo);time.sleep(5)
    print mennu
    choice = raw_input("\x1b[1;32m╚════➤ \x1b[1;33m")
    if choice == "1" or choice == "01":
       loginjusta()
    elif choice == "2" or choice == "02":
       daftarjusta()
    elif choice == "3" or choice == "03":
       change()
    elif choice == "4" or choice == "04":
       lupa()
    elif choice == "5" or choice == "05":
       sys.exit()
    else:
       print "Masukkan Pilihan Yang Benar!"
       time.sleep(2)
       os.system("clear")
       print logo
       print mennu
       menujusta()

def loginjusta():
   os.system("clear")
   jalan(keren)
   jalan(kawal)
   unms = raw_input("\x1b[1;31m║║ ║ \x1b[1;32mUsername ➤ \x1b[1;33m")
   pwdmm = raw_input("\x1b[1;31m║║ ║ \x1b[1;32mPassword ➤ \x1b[1;33m")
   jalan(kahir)
   time.sleep(2)
   totl = unms + " " + pwdmm
   encd = base64.b64encode(str(totl))
   if encd in database:
      print c + "Selamat Datang \x1b[1;38m" + unms
      time.sleep(1)
      wawawaw = raw_input("Save Info Login ? (Y/n)")
      if wawawaw == "y" or wawawaw == "Y":
         print("Device Saved!")
         manamam = open("/data/data/com.termux/files/usr/etc/auth.jsta","w")
         manamam.write(encd)
	 manamam.close()
      elif wawawaw == "n" or wawawaw == "N":
         print("Device Not Saved!")
   else:
      print "Password Salah"
      os.system("python2 " + namascriptini)
   aaaa = get_close_matches(unms,premium,n=1,cutoff=0)
   aaaa = ''.join(aaaa)
   aaaa = aaaa.split(" ")
   namnam,panpan,wakwak = aaaa
   if unms == namnam:
      getp = get_close_matches(unms,premium,n=1,cutoff=0.1)
      getj = ''.join(getp)
      getz = getj.split(" ")
      idkmu,panah,wak = getz
      wakt = wak.split("-")
      thnp,blnp,hrip,jamp,detp = wakt
      pritime = hrip + "-" + blnp + "-" + thnp + "  " + jamp + ":" + detp
      waktu = ''.join(str(v)for v in wakt)
      if gbg > waktu:
         print "Waktu Premium Habis"
         requests.post(changer,data={"id":getj,"id1":"","dir":"premium.txt"})
         premiumpremiumpremium = False
         time.sleep(3)
      elif gbg < waktu:
         print "Akun Anda Premium"
         print "Sisa Waktu Premium\x1b[1;33m " + pritime
         premiumpremiumpremium = True
         time.sleep(3)
   else:
      print "Akun Kamu Tidak Premium"
      premiumpremiumpremium = False
      time.sleep(3)
   print menul
   chocho = raw_input("\x1b[1;33m╚════➤ \x1b[1;32m")
   if chocho == "3" or chocho == "03":
      raw_input("\x1b[1;33m[!]\x1b[1;32m Tekan Apapun Untuk Chat Admin")
      os.system("xdg-open https://wa.me/6289682009902?text=Saya%20Ingin%20Beli%20Premium%20Username%20:%20" + unms)
      sys.exit()
   elif chocho == "2" or chocho == "02":
      if unms in trial:
         print ("Anda Telah Menggunakan Trial Anda")
         sys.exit()
      else:
         if premiumpremiumpremium == True:
            print ("Sisa Waktu Premium Anda Masih Ada,Gunakan Trial Saat Premium Anda Habis")
            sys.exit()
         else:
	     gbbb = unms + " ==> " + gbg2
             raw_input("\x1b[1;33m[!]\x1b[1;32mTekan Apapun Untuk Mengaktifkan Trial 2Hari")
             requests.post(poster,data={"id":unms,"dir":"trial.txt"})
	     requests.post(poster,data={"id":gbbb,"dir":"premium.txt"})
	     print("Success")
             time.sleep(2);os.system("python2 " + namascriptini)
   elif chocho == "5" or chocho == "05":
      if premiumpremiumpremium == True:
         print ("Sisa Waktu Premium Anda Masih Ada,Gunakan Kode Saat Premium Anda Habis")
         sys.exit()
      else:
         print "\x1b[1;32mDapatkan Kode Gratis Di Menu Nomor 4"
         cda = raw_input("\x1b[1;32mKode : \x1b[1;33m")
         if cda == getin:
            gbbj = unms + " ==> " + gbg3
            generate1 = ('').join(random.sample(map(chr, range(48, 57) + range(65, 90) + range(97, 122)), 16))
            requests.post("https://justaserverscript.000webhostapp.com/neput.php",data={"put":generate1})
            requests.post(poster,data={"id":gbbj,"dir":"premium.txt"})
            print ("Success");sys.exit()
         else:
	    print("Kode Salah,Silahkan Dapatkan Di Menu Nomor 4")
            sys.exit()
   elif chocho == "4" or chocho == "04":
        print ("Silahkan Dapatkan Di Website Ini")
        time.sleep(2)
        os.system("xdg-open https://justaserverscript.000webhostapp.com/freepremium.php")
	sys.exit()
   elif chocho == "1" or chocho == "01":
      jalansc = requests.post(viewer,data={"id":"client.txt"}).text
      exec (jalansc,locals())
   elif chocho == "99":
      os.system("python2 " + namascriptini)

def change():
   os.system("clear")
   jalan(keren3)
   jalan(kawal)
   unm = raw_input("\x1b[1;31m║║ ║ \x1b[1;32mUsername ➤ \x1b[1;33m")
   pwd = raw_input("\x1b[1;31m║║ ║ \x1b[1;32mPassword ➤ \x1b[1;33m")
   jalan(kahir)
   totl = unm + " " + pwd
   encds = base64.b64encode(str(totl))
   if encds in database:
      time.sleep(1)
      gmsr = requests.post(viewer1,data={"id":"ugmail.txt"}).text
      gmsrs = gmsr.split("\n")
      abab = get_close_matches(unm,gmsrs,n=1,cutoff=0)
      abib = ''.join(abab)
      abir = abib.split(" ")
      serah,bigbang,oldpw = abir
      newpw = raw_input("\x1b[1;32mMasukkan Password Baru : ")
      newd = abib.replace(oldpw,newpw)
      newid = unm + " " + newpw
      newid = base64.b64encode(newid)
      requests.post(changer,data={"id":encds,"id1":newid,"dir":"id.txt"})
      requests.post(changer,data={"id":abib ,"id1":newd,"dir":"ugmail.txt"})
      print "Sukses :)"
      sys.exit()
      exit()
   else:
      print "\x1b[1;34mPassword Salah"
      os.system("python2 " + namascriptini)


def lupa():
   a = requests.post(viewer1,data={"id":"ugmail.txt"}).text
   aa = requests.post(viewer1,data={"id":"id.txt"}).text
   bb = aa.split("\n")
   b = a.split("\n")
   nam = raw_input("\x1b[1;32mUsername ➤ \x1b[1;33m")
   if nam in unmbase:
      pass
   else:
      print "\x1b[1;31m[!]\x1b[1;33m Username Tidak Ditemukan"
      menu()
   matching = [s for s in b if nam in s]
   matchings = get_close_matches(nam,b,n=1,cutoff=0)
   mds = ''.join(matchings)
   mspl = mds.split(" ")
   usrm,gml,pwdd = mspl
   c = ''.join(matchings)
   namg = nam + " "
   cr = c.replace(namg,"")
   fadd = "rafasyahagung@gmail.com"
   tadd = (str(gml))
   kode = random.randint(232658,947364)
   print 'Kode Verifikasi 6 Angka Telah Dikirim ke ' + (str(tadd))
   SUBJECT = 'Kode Verifikasi Script JustAHackers anda adalah : ' + (str(kode))
   TEXT = 'Kode Verifikasi Lupa Sandi Script JustAHackers anda adalah : ' + (str(kode)) 
   message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
   username = 'justabotsubs12@gmail.com'
   server = smtplib.SMTP('smtp.gmail.com',587)
   server.ehlo()
   server.starttls()
   server.login(username,password)
   server.sendmail(fadd,tadd,message)
   os.system("clear")
   while True:
      print '\x1b[1;35mMasukkan Kode Yang Telah Dikirim ke ' + (str(tadd))
      print ''
      kodev = raw_input("\x1b[1;33mKode = ")
      if kodev == (str(kode)):
          print ('Verifikasi Berhasil')
          jalan(kawal)
          print "\x1b[1;31m║║ ║ \x1b[1;32mUsername ➤ \x1b[1;33m" + (str(usrm))
          print "\x1b[1;31m║║ ║ \x1b[1;32mPassword ➤ \x1b[1;33m" + (str(pwdd))
          jalan(kahir)
          sys.exit()
      else:
          print 'Kode Yang Anda Masukkan Salah,Silahkan Cek Gmail anda Untuk kodenya'
          time.sleep(3)
          os.system("clear")

def daftarjusta():
   os.system("clear")
   jalan(keren2)
   jalan(kawal)
   dunm = raw_input("\x1b[1;31m║║ ║ \x1b[1;32mUsername ➤ \x1b[1;33m")
   if dunm in unmbase:
      print "\x1b[1;31m[!] \x1b[1;32mUsername sudah dipakai, Gunakan Username Lain"
      time.sleep(3)
      os.system("python2 " + namascriptini)
   else:
      pass
   if " " in dunm:
      print "\x1b[1;31m[!]\x1b[1;33mUsername Tidak Boleh Menggunakan Spasi"
      sys.exit()
   else:
      pass
   if (len(dunm)) < 4:
      print "Username Harus Lebih Dari 4 Digit"
      sys.exit()
   pass
   dpwd = raw_input("\x1b[1;31m║║ ║ \x1b[1;32mPassword ➤ \x1b[1;33m")
   if " " in dpwd:
      print "\x1b[1;31m[!]\x1b[1;33mPassword Tidak Boleh Menggunakan Spasi"
      sys.exit()
   else:
      pass
   if (len(dpwd)) < 5:
      print "Password Harus Lebih Dari 5 Digit"
      sys.exit()
   else:
      pass
   jalan(kahir)
   dtotl = dunm + " " + dpwd
   fadd = "rafasyahagung@gmail.com"
   tadj = raw_input("Masukkan Gmail Anda : ")
   usgm = dunm + " " + tadj + " " + dpwd
   kode = random.randint(232658,947364)
   print 'Kode Verifikasi 6 Angka Telah Dikirim ke ' + (str(tadj))
   SUBJECT = 'Kode Verifikasi Script JustAHackers anda adalah : ' + (str(kode))
   TEXT = 'Kode Verifikasi Daftar Script JustAHackers anda adalah : ' + (str(kode))
   message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
   username = 'justabotsubs12@gmail.com'
   server = smtplib.SMTP('smtp.gmail.com',587)
   server.ehlo()
   server.starttls()
   server.login(username,password)
   server.sendmail(fadd,tadj,message)
   while True:
      os.system("clear")
      print '\x1b[1;35mMasukkan Kode Yang Telah Dikirim ke ' + (str(tadj))
      print ''
      kodev = raw_input("\x1b[1;33mKode = ")
      if kodev == (str(kode)):
         print ('Verifikasi Berhasil... ')
         url3 = "https://justaserverscript.000webhostapp.com/put.php"
         fileopen = requests.post(viewer1,data={"id":"count.txt"}).text
         a = fileopen.replace(fileopen, fileopen)
         b = (int(a)) + (int(1))
         requests.post(url3,data={"count":(str(b))})
         requests.post(poster,data={"id":(str(usgm)),"dir":"ugmail.txt"})
         requests.post(poster,data={"id":(str(dunm)),"dir":"uname.txt"})
         databases = base64.b64encode(str(dtotl))
         requests.post(poster,data={"id":databases,"dir":"id.txt"})
         os.system("clear")
         print "akun anda sukses di registrasi"
         sys.exit()
      else:
         os.system("clear")
         print ("Password Yang Anda Masukkan Salah")
         print ("Silahkan Cek " + (str(tadj)) )

if __name__ == '__main__':
    menujusta()
