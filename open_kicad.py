#!/usr/bin/env python3
"""Launch this project with a targeted KiCad 10 / glycin startup workaround."""
from pathlib import Path
import os
import shlex
import shutil
import subprocess
import sys
import tempfile


def main():
    root = Path(__file__).resolve().parent
    source = root / 'tools' / 'kicad_assert_dialog_guard.cpp'
    project = root / 'snake_pcb.kicad_pro'
    for tool in ('c++', 'wx-config', 'kicad'):
        if not shutil.which(tool):
            raise SystemExit(f'Required program not found: {tool}')
    if not project.is_file():
        raise SystemExit(f'Project not found: {project}')

    # Use a private directory: never overwrite libraries or system settings.
    # Leave it in /tmp so independently running editors can inherit LD_PRELOAD.
    build = Path(tempfile.mkdtemp(prefix='snake-pcb-kicad-'))
    library = build / 'assert-dialog-guard.so'
    cflags = shlex.split(subprocess.check_output(
        ['wx-config', '--cxxflags'], text=True))
    libs = shlex.split(subprocess.check_output(
        ['wx-config', '--libs', 'core,base'], text=True))
    subprocess.run(['c++', '-std=c++17', '-O2', '-fPIC', '-shared',
                    *cflags, str(source), '-o', str(library), *libs, '-ldl'],
                   check=True)
    env = os.environ.copy()
    previous = env.get('LD_PRELOAD', '')
    env['LD_PRELOAD'] = str(library) + (':' + previous if previous else '')
    return subprocess.call(['kicad', str(project)], env=env, cwd=root)


if __name__ == '__main__':
    sys.exit(main())
