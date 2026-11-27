# Correctif V16.6.93 vers V16.6.94
# Exécuter dans le dossier contenant index.html de la V16.6.93.
from pathlib import Path
import base64, json, zlib, hashlib
f = Path('index.html')
if not f.exists(): raise SystemExit('index.html introuvable.')
s = f.read_text(encoding='utf-8')
if hashlib.sha256(s.encode()).hexdigest() != '3d1e7175016fc56399e362fe12b8f6195f0bb3e44ff6fab538845196ef959ec9':
    raise SystemExit('index.html ne correspond pas à la V16.6.93 originale. Aucun changement appliqué.')
s = s.replace('V16.6.93','V16.6.94')
patch = 'c-o~_+fw5;7=9Iz3u1#K;+!19nhdbB9cGp-Ems}Ng<>m-7DpD6#gbupmtL0V;Klmuki^MQW;(q{WJ{ku|Hn_dz3ub{$#FkIFb)U32sMt5&{u*oA}fj{Rq$WxM{3@_YxSU;M5C-=8KO@D1_txFM&C<KwZwmNl$BgnfG8DBC(Fw`Xi5g#&$0*2B)u^6&F}<(Y#LZpX#a7^4eNbs-+r%eAu>1k5~d2WTmu98NO={er_aD-pK(Rxj8<uydTjVESrEQ7?jm&C8N^9)44x0-<DT*Sn)00R3Kihe+p8!@Mi)REAx^DZR00ut(9|L%5!A$DUNXgu=LjNqO%%#05`?<|!gEER;DIxgL+C2G-f6dh=_ISbz$-A>d~APzBKOjCdlFA15YD~ToxZcWGw2P#>TT$FhYuV3GWty~CRDcKaO9{ic}|~9R9E@3s7pRAQ}_6ps!TFbmGVm|&+VRIA|pdya&Jhtn{<sK-JTg6d%K=gOF_#i5)f9#XBU?D%o3<uM`X>ogM>Awn%kLXG&jjRCyM?tnwWn#ag&jPj-~~fVPzgMq?Xelj28ZLUtnppw`0S~(EhMz4Na_}5cC~f`0T=vL%n|`6I!GTa&KZ#F;0wGb}}%_-^hZ7Cu<-UrD6tw6|DmB^f&wzS-TJ89_~kWW?A1bm0DGLaiNQX=IN9aik=8b9~u4ei!8OkB+r92JY22a2noHWu+VB=UtZO6HyO5_k7j(&M+Z!jPSOFO9~-^^h=evJMS3PB^cYii3|z5b5CNgam{b8&&=_ZBDf4h#U-WBk$=4VL-%mD*Fo#y;srTj@I+#of@Mp?+9+<qQr#8D9+Uzr_$Qa+liYbkJlZNL0{<eWTTSUpg(Or=D4d%Dt4vh=SXVn}&<Y9i|eK6>ZTm}KaG>sUD&lRcWm`s$LYI%-Zb{Bq%X)6iCtq80;F%4Wi#x>(tJqRr^9=F587`Co*)*TLQ&U$^2>c(oeZ~M=WjXHniA;bP)U?6U6AoK#}m>+1>6_F1{wT(#CVvI&0`;(IA$_xJ6U#K9cDz()!$=TcApkf)+c;twLW(v(9=Q&a!ambt&44M>C=qRQHk+wq&9Z--*ud%{(4KPeg8Mp|Uh$EvIJ4F&cd#&8t$#=c^fBtl<k08geDFjMzNz<Cj*}hD-^SY6n8nB>5+`ws4r8d6{@)Wcq-fH7yXcKB|5we`Y`KUgv!OqOpw<z(uO?B7@#dtsqA{5OJ+PEEeTy-Gp_eMyTsnd@hZXXzy8pcasDRwF!Z!|K*3td!96if3;WDp;=aon>^{&Qfw-Mt_cl?)nV>kXHJz_GqeV~c*FAW(J33N~GZ1^kJlbs$=sKpbtthGPiaX5~YVllFmOw}1cB>zV=WP87EcW%%FxuchAYKZtR%p)fP2X&Vo^VZH9WqOV%_c-ZS2xjh~xgX49RMuEMz@JDF7U-^ZW5{lT~Q!XG7a6!2{sof4BLd+^5(e8{4C9SmN$e*IPPO40p-Id3o|CKF+tbE920ha2V@Ou>~O!FCy6lO-F!uMGPQR*X7)3R4kEo4T6CYY$<a^+Cy?G-AlTrhLP8X1KE&5;N~1a~M2#rF1!oBpfs@;C18{sH*jyDk'
for start,end,replacement in reversed(json.loads(zlib.decompress(base64.b85decode(patch)).decode())):
    s=s[:start]+replacement+s[end:]
if hashlib.sha256(s.encode()).hexdigest() != '4d9b11f7f992d1d6b80220ecbaa97c06d8bba62c9259e49bf9326cff281920f3':
    raise SystemExit('Le contrôle final a échoué. Aucun fichier modifié.')
f.with_name('index_V16_6_93_sauvegarde.html').write_bytes(f.read_bytes())
f.write_text(s,encoding='utf-8')
print('V16.6.94 installée. Ancien fichier sauvegardé.')
