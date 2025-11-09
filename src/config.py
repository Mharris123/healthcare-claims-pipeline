from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = BASE_DIR / "data"

EXTERNAL_DIR = DATA_DIR / "external"
ZIPPED_DIR = DATA_DIR / "zipped"
EXTRACTED_DIR = DATA_DIR / "extracted"
RAW_DIR = DATA_DIR / "raw"
PROCESSED_DIR = DATA_DIR / "processed"
WAREHOUSE_DIR = DATA_DIR / "warehouse"
LOGS_DIR = DATA_DIR / "logs"
