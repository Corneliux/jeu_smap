#!/usr/bin/env python3
"""Télécharge les photographies Wikimedia Commons pour le jeu local ; en option uniquement."""
import json,urllib.request
from pathlib import Path
root=Path(__file__).resolve().parent
photos=json.loads((root/'data/photos_wikimedia.json').read_text(encoding='utf-8'))
out=root/'assets/cards/discoveries/wikimedia';out.mkdir(parents=True,exist_ok=True)
for card, info in photos.items():
    target=out/(card+'.jpg')
    if target.exists():
        print('Déjà présente:',card);continue
    try:
        req=urllib.request.Request(info['wikimedia'],headers={'User-Agent':'SainteMariePyEducatif/1.0 (jeu local avec credits Wikimedia)'})
        with urllib.request.urlopen(req,timeout=20) as stream:
            content=stream.read()
        if not content.startswith(b'\xff\xd8'):
            raise ValueError('Réponse non JPEG')
        target.write_bytes(content)
        print('OK:',card,len(content),'octets')
    except Exception as exc:
        print('Échec:',card,exc,'La version en ligne ou locale de secours restera disponible.')
