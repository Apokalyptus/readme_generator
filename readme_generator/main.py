import sys
import os
from ollama import Client

# Configuration
OLLAMA_HOST = "http://localhost:11434"
OLLAMA_MODEL = "gemma3"

def is_code_file(filename):
    code_extensions = {'.py', '.js', '.ts', '.java', '.cpp', '.c', '.cs', '.go', '.rb', '.php', '.rs', '.swift', '.kt', '.m', '.scala', '.pl', '.sh', '.tex'}
    return any(filename.endswith(ext) for ext in code_extensions)

def scan_directory(path):
    code_files = []
    for root, dirs, files in os.walk(path):
        # Exclude common external library folders
        dirs[:] = [d for d in dirs if d not in {'node_modules', '.venv', '.env', '__pycache__', '.git', 'build', 'dist', 'bin', 'lib'}]
        for file in files:
            if is_code_file(file):
                code_files.append(os.path.join(root, file))
    return code_files

def analyze_with_ollama(files):
    client = Client(host=OLLAMA_HOST)
    
    # Phase 1: Analysiere jede Datei einzeln (mit Stückelung bei großen Dateien)
    file_summaries = []
    for file_path in files:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            
            # Teile große Dateien in 3000-Byte-Chunks
            chunks = []
            max_bytes = 3000
            start = 0
            while start < len(content):
                chunk = content[start:start+max_bytes]
                chunks.append(chunk)
                start += max_bytes
            
            # Analysiere jeden Chunk der Datei
            chunk_summaries = []
            for i, chunk in enumerate(chunks):
                prompt = (
                    f"Analysiere sachlich Teil ({i+1}/{len(chunks)}) der Datei {file_path}. "
                    "Antworte nur mit Fakten: Was macht dieser Code? Welche Hauptfunktionen gibt es? "
                    "Keine Bewertungen oder ausschmückende Beschreibungen. Nur technische Fakten. "
                    "Code:"
                )
                
                response = client.generate(model=OLLAMA_MODEL, prompt=prompt + "\n" + chunk)
                chunk_summaries.append(response['response'])
            
            # Kombiniere alle Chunk-Analysen für diese Datei
            file_summary = f"Datei {file_path}: " + " | ".join(chunk_summaries)
            file_summaries.append(file_summary)
    
    # Phase 2: Erstelle finale README aus allen Dateizusammenfassungen
    all_summaries = "\n".join(file_summaries)
    
    final_prompt = (
        "Du erstellst eine README.md für ein Coding-Projekt. "
        "Nutze NUR die Informationen aus den folgenden Dateibeschreibungen. "
        "Erstelle eine README mit diesen Punkten: "
        "- Was bringt das Projekt dem Nutzer? "
        "- Was kann man damit machen? "
        "- Wie funktioniert das grob? "
        "- Für wen ist es gedacht? "
        "Schreibe keine Bewertungen oder Kommentare zu den Beschreibungen. "
        "Verwende nur die Fakten aus den Beschreibungen für die README. "
        "Dateibeschreibungen:\n\n" + all_summaries
    )
    
    final_response = client.generate(model=OLLAMA_MODEL, prompt=final_prompt)
    return final_response['response']

def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <project_directory>")
        sys.exit(1)
    project_dir = sys.argv[1]
    if not os.path.isdir(project_dir):
        print("Das angegebene Verzeichnis existiert nicht.")
        sys.exit(1)
    code_files = scan_directory(project_dir)
    if not code_files:
        print("Keine relevanten Code-Dateien gefunden.")
        sys.exit(1)
    analysis = analyze_with_ollama(code_files)
    readme_path = os.path.join(project_dir, "README.md")
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write("# Projektanalyse\n\n" + analysis)
    print(f"README.md wurde erstellt: {readme_path}")

if __name__ == "__main__":
    main()
