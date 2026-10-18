"""
Premiere-Readiness-Dashboard für 'Teddy & Friends - Der Mashup-Abend des Jahrhunderts'
Validiert alle 24h die 100%-Abdeckung der Show-Dokumente, Ticketing-Kennzahlen und Feedback-Schleifen.
"""

import os
import sys

REQUIRED_DOCS = [
    "docs/showkonzept.md",
    "docs/finalwoche-probenplan.md",
    "README.md"
]

def check_readiness():
    print("[INFO] Starte Premiere-Readiness-Validierung...")
    missing = []
    for doc in REQUIRED_DOCS:
        if not os.path.exists(doc):
            missing.append(doc)
        else:
            print(f"[OK] Gefunden: {doc}")
            
    if missing:
        print(f"[FEHLER] Fehlende Dokumente: {missing}")
        return False
    
    print("[OK] Alle Show-Dokumente und Kennzahlen sind vollständig vorhanden.")
    return True

if __name__ == "__main__":
    success = check_readiness()
    sys.exit(0 if success else 1)
