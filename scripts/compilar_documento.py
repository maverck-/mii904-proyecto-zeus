#!/usr/bin/env python3
"""Compila el documento de respaldo: Markdown → Typst con Pandoc → PDF con Typst."""
from pathlib import Path
import re
import shutil
import subprocess
import sys

root = Path(__file__).resolve().parents[1]
pandoc = shutil.which('pandoc')
typst = shutil.which('typst')
if pandoc is None:
    sys.exit('Falta Pandoc. Instalar Pandoc 3 y volver a ejecutar.')
if typst is None:
    sys.exit('Falta el compilador Typst. Instalar la versión 0.15.1 y volver a ejecutar.')
version = subprocess.run([typst, '--version'], text=True, capture_output=True, check=True).stdout
if not re.search(r'\b0\.15\.1\b', version):
    sys.exit('La referencia del proyecto es Typst 0.15.1. Revisar la versión antes de compilar.')
out = root/'build'
out.mkdir(exist_ok=True)
subprocess.run([
    pandoc, str(root/'documento/respaldo.md'), '-f', 'markdown', '-t', 'typst',
    '--lua-filter', str(root/'typst/filtros/zeus.lua'), '-o', str(out/'respaldo_cuerpo.typ'),
], cwd=root, check=True)
pdf = root/'documento/ZEUS_documento_respaldo.pdf'
subprocess.run([
    typst, 'compile', '--root', str(root), '--ignore-system-fonts', '--font-path', str(root/'typst/fuentes'),
    str(root/'typst/documento_respaldo.typ'), str(pdf),
], cwd=root, check=True)
print('Documento compilado: documento/ZEUS_documento_respaldo.pdf')
