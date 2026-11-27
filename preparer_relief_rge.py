#!/usr/bin/env python3
"""Convertir les tuiles RGE ALTI ASC Lambert-93 en terrain.json local pour la V5.
Usage : python3 preparer_relief_rge.py RGE [--largeur 480]
"""
import argparse, json, math, shutil, subprocess, tempfile
from pathlib import Path

ROOT=Path(__file__).resolve().parent
parser=argparse.ArgumentParser()
parser.add_argument('dossier', type=Path, help='Dossier des tuiles RGE ALTI .asc (recherche récursive)')
parser.add_argument('--largeur',type=int,default=480,help='Colonnes de la grille (par défaut 480, ~10-20 m selon la commune)')
a=parser.parse_args()
if not (150<=a.largeur<=1000):parser.error('--largeur entre 150 et 1000')
for tool in ('gdalbuildvrt','gdalwarp','gdal_translate'):
 if not shutil.which(tool):parser.error(f'{tool} absent : sudo apt install -y gdal-bin')
files=sorted(a.dossier.expanduser().rglob('*.asc'))
if not files:parser.error('Aucun fichier .asc dans le dossier indiqué')
print(f'{len(files)} tuiles ASC repérées')
geo=json.loads((ROOT/'data'/'osm-local.geojson').read_text())
feat=next((f for f in geo['features'] if f['properties'].get('ref:INSEE')=='51501' and f['properties'].get('boundary')=='administrative' and f['geometry']['type']=='MultiPolygon'),None)
if feat is None:parser.error('Périmètre 51501 absent de data/osm-local.geojson')
points=[p for poly in feat['geometry']['coordinates'] for ring in poly for p in ring]
west=min(p[0] for p in points);east=max(p[0] for p in points)
south=min(p[1] for p in points);north=max(p[1] for p in points)
# Marge de 100 m autour de la limite pour faciliter l'interpolation aux bords
pad_lat=100/111132;pad_lon=100/(111320*math.cos(math.radians((north+south)/2)))
west-=pad_lon;east+=pad_lon;south-=pad_lat;north+=pad_lat
width=a.largeur;height=round(width*((north-south)*111132)/((east-west)*111320*math.cos(math.radians((north+south)/2))))
print('Emprise WGS84 :', *(round(v,6) for v in (west,south,east,north)))
print(f'Grille de sortie : {width} x {height} points')
with tempfile.TemporaryDirectory(prefix='rgepy_') as temp:
 temp=Path(temp);vrt=temp/'mosaic.vrt';raster=temp/'relief.tif';xyz=temp/'relief.xyz'
 subprocess.run(['gdalbuildvrt','-q',str(vrt),*[str(f) for f in files]],check=True)
 subprocess.run(['gdalwarp','-q','-overwrite','-of','GTiff','-s_srs','EPSG:2154','-t_srs','EPSG:4326','-te',str(west),str(south),str(east),str(north),'-ts',str(width),str(height),'-r','bilinear','-dstnodata','-9999',str(vrt),str(raster)],check=True)
 subprocess.run(['gdal_translate','-q','-of','XYZ',str(raster),str(xyz)],check=True)
 vals=[]
 with xyz.open() as handle:
  for line in handle:
   z=float(line.split()[2]);vals.append(None if not math.isfinite(z) or z <= -9998 else round(z,2))
 valid=[v for v in vals if v is not None]
 if len(valid)<len(vals)*0.25:parser.error(f'Couverture insuffisante : {len(valid)} / {len(vals)} points valides. Vérifie le département et la projection des tuiles.')
 # Éviter les valeurs de terrain aberrantes en dehors de la zone utile
 payload={'source':'IGN RGE ALTI 5 m · Lambert-93 EPSG:2154 · conversion locale', 'width':width, 'height':height, 'west':west, 'east':east,'north':north,'south':south,'min':min(valid),'max':max(valid),'values':vals}
 dest=ROOT/'data'/'terrain.json';dest.write_text(json.dumps(payload,ensure_ascii=False,separators=(',',':')))
 print(f'OK : {dest} ({dest.stat().st_size/1024/1024:.1f} Mio)')
 print(f'Points valides : {len(valid)}/{len(vals)} · altitude : {min(valid):.2f} à {max(valid):.2f} m')
