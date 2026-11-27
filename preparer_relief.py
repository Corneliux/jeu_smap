#!/usr/bin/env python3
"""Convertit un ou plusieurs MNT IGN en grille 3D locale pour Sainte-Marie-à-Py.
Utilisation : python3 preparer_relief.py /chemin/vers/raster1.asc [raster2.asc ...]
Accepte ASC, TIFF, VRT. Décompresser auparavant les archives IGN ZIP/7Z.
Dépendances : gdal-bin (gdalbuildvrt, gdalwarp, gdal_translate).
"""
import sys, json, subprocess, shutil, tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parent
if len(sys.argv)<2:
 print('Usage : python3 preparer_relief.py /chemin/vers/dossier_IGN_ou_fichier.asc')
 sys.exit(2)
for cmd in ['gdalbuildvrt','gdalwarp','gdal_translate']:
 if not shutil.which(cmd):sys.exit(f'Commande absente : {cmd}. Installer avec sudo apt install gdal-bin')
files=[]
for arg in sys.argv[1:]:
 pp=Path(arg).expanduser()
 if pp.is_dir():files.extend(p for p in pp.rglob('*') if p.suffix.lower() in ('.asc','.tif','.tiff','.vrt'))
 elif pp.exists():files.append(pp)
 else:sys.exit(f'Fichier non trouvé : {pp}')
if not files:sys.exit('Aucun raster trouvé. Décompresse le fichier IGN .7z ou .zip avant.')
print(f'{len(files)} fichier(s) MNT repéré(s).')
with tempfile.TemporaryDirectory() as td:
 t=Path(td);vrt=t/'mosaic.vrt';tif=t/'coupure.tif';xyz=t/'coupure.xyz'
 subprocess.run(['gdalbuildvrt','-q',str(vrt),*[str(p) for p in files]],check=True)
 # Les grilles ASC BD ALTI n'embarquent généralement pas de projection explicite.
 # Le système des coordonnées X/Y indiqué par IGN est Lambert-93 (EPSG:2154).
 # Zone de la commune légèrement élargie; on conserve une grille légère pour le navigateur.
 subprocess.run(['gdalwarp','-q','-overwrite','-of','GTiff','-s_srs','EPSG:2154','-t_srs','EPSG:4326', '-te','4.476','49.203','4.556','49.286','-ts','225','350','-r','bilinear','-dstnodata','-9999',str(vrt),str(tif)],check=True)
 subprocess.run(['gdal_translate','-q','-of','XYZ',str(tif),str(xyz)],check=True)
 vals=[];xx=[];yy=[]
 with xyz.open() as f:
  for i,line in enumerate(f):
   a,b,c=map(float,line.split());vals.append(None if c<=-9998 else round(c,2))
   if i<225:xx.append(a)
   if i%225==0:yy.append(b)
 valid=[v for v in vals if v is not None]
 if len(valid)<1000:sys.exit(f'Pas assez de valeurs altimétriques ({len(valid)}/{len(vals)}). Vérifie les tuiles et leur projection (EPSG:2154).')
 data={'source':'IGN BD ALTI ou RGE ALTI, fichier local fourni par utilisateur','width':225,'height':350,'west':xx[0]-(xx[1]-xx[0])/2,'east':xx[-1]+(xx[1]-xx[0])/2,'north':yy[0]+(yy[0]-yy[1])/2,'south':yy[-1]-(yy[-2]-yy[-1])/2,'min':min(valid),'max':max(valid),'values':vals}
 dest=ROOT/'data'/'terrain.json';dest.parent.mkdir(exist_ok=True);dest.write_text(json.dumps(data,separators=(',',':')))
 print('Relief généré :',dest,'| échantillons :',len(valid),'| altitude min/max :',min(valid),max(valid),'m')
 print('La carte fonctionne désormais sans accès au serveur IGN.')
