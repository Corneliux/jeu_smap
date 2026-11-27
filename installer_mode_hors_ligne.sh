#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
mkdir -p vendor/three/addons/controls
base='https://cdn.jsdelivr.net/npm/three@0.170.0'
for spec in 'build/three.module.js vendor/three/three.module.js' 'examples/jsm/controls/OrbitControls.js vendor/three/addons/controls/OrbitControls.js'; do
 read -r remote local <<<"$spec"
 if [ ! -s "$local" ]; then curl --fail --location --retry 3 "$base/$remote" -o "$local"; fi
done
echo 'Three.js disponible localement.'
