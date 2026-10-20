#!/usr/bin/env python3
"""Compila la muestra local de Typst con la versión de referencia."""
from pathlib import Path
import re
import shutil
import subprocess
import sys

root = Path(__file__).resolve().parents[1]
compiler = shutil.which('typst')
if compiler is None:
    sys.exit('Falta el compilador Typst. Instalar la versión 0.15.1 y volver a ejecutar.')
version = subprocess.run([compiler, '--version'], text=True, capture_output=True, check=True).stdout
if not re.search(r'\b0\.15\.1\b', version):
    sys.exit('La referencia del proyecto es Typst 0.15.1. Revisar la versión antes de compilar.')
out = root/'build'
out.mkdir(exist_ok=True)
subprocess.run([
    compiler, 'compile', '--root', str(root), '--ignore-system-fonts',
    str(root/'typst/ejemplo.typ'), str(out/'ejemplo.pdf'),
], cwd=root, check=True)
print('Muestra compilada: build/ejemplo.pdf')
