from pathlib import Path

def find_all_files(directory_path):
    """
    Skannar en angiven mapp och alla dess undermappar efter filer.
    Returnerar en lista med Path-objekt för varje fil.
    """
    folder = Path(directory_path)
    
    # Säkerställ att mappen faktiskt existerar
    if not folder.exists() or not folder.is_dir():
        print("Fel: Mappen finns inte eller sökvägen är ogiltig.")
        return []

    print(f"\nSöker igenom: {folder.resolve()}...")
    
    # Hämta alla objekt (recursively) och filtrera så vi bara får filer, inte mappar
    files = [file for file in folder.rglob('*') if file.is_file()]
    
    print(f"Hittade totalt {len(files)} filer.\n")
    return files

if __name__ == "__main__":
    # Be användaren om en mapp att skanna
    target_folder = input("Ange sökväg till mappen du vill skanna (t.ex. ./ eller C:/Downloads): ")
    
    found_files = find_all_files(target_folder)
    
    # Skriv ut namnet på upp till 5 filer för att bekräfta att det fungerar
    if found_files:
        print("Visar de första 5 filerna:")
        for f in found_files[:5]:
            print(f"- {f.name}")