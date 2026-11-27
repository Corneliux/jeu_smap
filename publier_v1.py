#!/usr/bin/env python3
"""Publie la version initiale du jeu dans Corneliux/jeu_smap.
Usage : python3 publier_v1.py /chemin/jeu_v16_6_93_3d
        python3 publier_v1.py /chemin/archive_du_jeu.zip
Nécessite git et des droits d'écriture GitHub configurés sur ce PC.
"""
from pathlib import Path
import hashlib
import shutil
import subprocess
import sys
import tempfile
import zipfile

REPO = "https://github.com/Corneliux/jeu_smap.git"
SHA_V93 = "3d1e7175016fc56399e362fe12b8f6195f0bb3e44ff6fab538845196ef959ec9"
SHA_V94 = "4d9b11f7f992d1d6b80220ecbaa97c06d8bba62c9259e49bf9326cff281920f3"

def cmd(*args, cwd=None):
    subprocess.run(args, cwd=cwd, check=True)

def find_root(path):
    if (path / "index.html").is_file():
        return path
    candidates = [p for p in path.iterdir() if p.is_dir() and (p / "index.html").is_file()]
    if len(candidates) == 1:
        return candidates[0]
    raise ValueError("Impossible de trouver le dossier du jeu contenant index.html")

def main():
    if len(sys.argv) != 2:
        raise SystemExit("Usage : python3 publier_v1.py /chemin/dossier_du_jeu_ou_archive.zip")
    source = Path(sys.argv[1]).expanduser().resolve()
    if not source.exists():
        raise SystemExit(f"Introuvable : {source}")
    with tempfile.TemporaryDirectory(prefix="smap_v1_") as tmp:
        tmp = Path(tmp)
        if source.is_file() and source.suffix.lower() == ".zip":
            extracted = tmp / "archive"
            extracted.mkdir()
            with zipfile.ZipFile(source) as z:
                if z.testzip() is not None:
                    raise ValueError("Archive ZIP endommagée")
                z.extractall(extracted)
            game = find_root(extracted)
        elif source.is_dir():
            game = find_root(source)
        else:
            raise ValueError("Indique un dossier du jeu ou un fichier ZIP.")
        digest = hashlib.sha256((game / "index.html").read_bytes()).hexdigest()
        if digest not in (SHA_V93, SHA_V94):
            raise ValueError("Ce jeu n'est ni la V16.6.93 ni la V16.6.94 attendue : publication annulée.")
        dest = tmp / "repo"
        cmd("git", "clone", REPO, str(dest))
        # Publier à la racine du dépôt, en conservant la structure et les médias.
        count = 0
        for p in game.rglob("*"):
            if not p.is_file():
                continue
            relative = p.relative_to(game)
            if ".git" in relative.parts:
                continue
            out = dest / relative
            out.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(p, out)
            count += 1
        if digest == SHA_V93:
            cmd(sys.executable, "correctif_V16_6_94.py", cwd=dest)
        result = hashlib.sha256((dest / "index.html").read_bytes()).hexdigest()
        if result != SHA_V94:
            raise ValueError("Le contrôle de version a échoué : aucun push.")
        cmd("git", "add", "-A", cwd=dest)
        cmd("git", "-c", "user.name=Corneliux", "-c",
            "user.email=5183030+Corneliux@users.noreply.github.com",
            "commit", "-m", "V1 : jeu complet Sainte-Marie-à-Py (base V16.6.94)", cwd=dest)
        cmd("git", "push", "origin", "main", cwd=dest)
        cmd("git", "tag", "v1.0.0", cwd=dest)
        cmd("git", "push", "origin", "v1.0.0", cwd=dest)
        print(f"V1 publiée : {count} fichiers sources, {REPO}")
        print("Étiquette Git : v1.0.0")

if __name__ == "__main__":
    try:
        main()
    except (OSError, ValueError, subprocess.CalledProcessError, zipfile.BadZipFile) as e:
        raise SystemExit(f"Échec : {e}")
