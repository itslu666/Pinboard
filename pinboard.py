import subprocess
import sys
import os

def run_script(arg):
    # Bestimme den absoluten Pfad zur main.py
    script_dir = os.path.dirname(os.path.abspath(__file__))
    main_script_path = os.path.join(script_dir, 'main.py')

    # Bestimme den Python-Befehl basierend auf der Python-Version
    python_command = sys.executable  # Dies gibt den Pfad zur aktuell verwendeten Python-Version zurück

    # Starte main.py im Hintergrund
    subprocess.Popen([python_command, main_script_path] + arg, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

if __name__ == "__main__":
    run_script(sys.argv[1:])
