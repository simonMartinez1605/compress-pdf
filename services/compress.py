import subprocess
import os

def compress(input_path, output_path=None):
    if not output_path:
        base, ext = os.path.splitext(input_path)
        output_path = f"{base}_optimizado{ext}"
    
    comando = [
        "qpdf",
        "--linearize",
        input_path,
        output_path
    ]

    try:
        subprocess.run(comando, check=True)
        return output_path
    except Exception as e:
        print(f"Error optimizando PDF con qpdf: {e}")
        return None
