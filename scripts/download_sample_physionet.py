#!/usr/bin/env python3
"""
Download a tiny public EEG subset from PhysioNet for quick tests.
Default: EEG Motor Movement/Imagery Dataset (eegmmidb), subjects S001 and S002.

Usage:
  python scripts/download_sample_physionet.py --subjects S001 S002
  python scripts/download_sample_physionet.py --db eegmmidb --out data/raw/sample_eegmmidb
"""
import argparse
from pathlib import Path
import wfdb

def main(db: str, out: str, subjects: list[str]):
    out_path = Path(out)
    out_path.mkdir(parents=True, exist_ok=True)

    for s in subjects:
        print(f"[INFO] Downloading {db}/{s} to {out_path / s} ...")
        try:
            wfdb.dl_database(
                db,                      # PhysioNet database name
                pn_dir=f"{db}/{s}",      # remote subdirectory (subject folder)
                dl_dir=str(out_path / s),
                keep_subdirs=True,
                overwrite=False,
            )
        except Exception as e:
            print(f"[WARN] Failed to download {s}: {e}")

    print(f"[DONE] Files saved under: {out_path.resolve()}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download small public EEG data from PhysioNet.")
    parser.add_argument("--db", default="eegmmidb", help="PhysioNet database name (default: eegmmidb)")
    parser.add_argument("--out", default="data/raw/sample_eegmmidb", help="Output folder")
    parser.add_argument("--subjects", nargs="+", default=["S001", "S002"], help="Subject IDs (e.g., S001 S002)")
    args = parser.parse_args()
    main(db=args.db, out=args.out, subjects=args.subjects)
