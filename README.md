README.md
=========
# 📚 Phishing Dataset CSV Merger (Generated Emails)

Small utility script that takes the per-company CSV files produced by the **Phishing Email Generator** and merges them into a **single ML-ready dataset**.

Problem: you have thousands of small CSVs in `Generated Emails/` and you just want one big `merged_generated_emails.csv` to load into pandas, scikit-learn, or any analysis tool.

---

## ✨ Highlights

- **Automatic discovery** – scans `Generated Emails/` and picks up every `*.csv` file.
- **TXT ignored by design** – safely skips the human-readable `.txt` exports.
- **Encoding-resilient** – tries `utf-8-sig`, then `utf-8`, then `latin-1` if needed.
- **Header-aware** – keeps the first header row and stacks all rows under it.
- **Single dataset output** – writes `merged_generated_emails.csv` next to the script.
- **ML-friendly** – output stays fully compatible with the original generator schema.

---

## 🚀 Quick Start

TL;DR: drop the script next to `Generated Emails/` → run it → get one big CSV.

### 1️⃣ Open a terminal in the project folder

Example on Windows:

- Open PowerShell in the folder:
  - `cd "%USERPROFILE%\Desktop\New Code Generate"`

Or adjust the path to wherever your project lives.

### 2️⃣ Create a virtual environment (optional but recommended)

- Create venv: `python -m venv .venv`
- Activate on Windows: `.venv\Scripts\activate`
- Activate on Linux/macOS: `source .venv/bin/activate`

### 3️⃣ Install dependencies

- Install: `pip install -r requirements.txt`
- Or: `py -m pip install -r requirements.txt`

### 4️⃣ Check the folder layout

New Code Generate/
    merge_all_csvs.py
    requirements.txt
    README.md
    Generated Emails/
        generated_phishing_emails_ABC.csv
        generated_phishing_emails_ABC.txt
        generated_phishing_emails_XYZ.csv
        ...

- All `.csv` files should live inside `Generated Emails/`.
- `.txt` files can stay there; the script ignores them automatically.

### 5️⃣ Run the merger

- Command: `python merge_all_csvs.py`

You should see progress like:

[+] تم العثور على 1403 ملف CSV للدمج.
[1/1403] أقرأ: generated_phishing_emails_ABC.csv
[2/1403] أقرأ: generated_phishing_emails_Adobe.csv
...
[+] تم الدمج بنجاح!
    عدد ملفات CSV المدمجة : 1403
    عدد الصفوف الكلي      : 123456
    مسار الملف الناتج      : C:\...\New Code Generate\merged_generated_emails.csv

---

## 📁 Input & Output

### 🔹 Input

- Directory: `Generated Emails/`
- Files: any number of files matching `*.csv`
- Expected schema: whatever the generator produced, for example:

id,label,from,to,subject,body,url,vt_status,vt_malicious,vt_suspicious,vt_clean
1,phishing,"Adobe Security <security@adobe.com>",ahmad@example.com,"URGENT: Account will be closed",...

Individual CSVs may come from different companies; this tool simply stacks them into one big dataset.

### 🔹 Output

- File: `merged_generated_emails.csv`
- Location: same folder as `merge_all_csvs.py`
- Format: standard UTF-8 CSV, with the union of all columns found across source files.
- If some CSVs have extra columns, they are kept; missing values are filled with `NaN`.

---

## 🧠 How It Works (High Level)

1. Uses `pathlib.Path` to locate the `Generated Emails/` directory relative to the script.
2. Collects and sorts all files matching `*.csv`.
3. For each file:
   - Attempts to read it with `pandas.read_csv()` using several encodings:
     - `utf-8-sig`
     - `utf-8`
     - `latin-1` (fallback)
   - Files that still fail to decode are skipped with a clear warning, e.g.:
     - `[!] تعذر قراءة الملف 'XYZ.csv' بسبب الترميز. تم تخطيه.`
4. Concatenates all successfully loaded DataFrames with `pandas.concat(..., ignore_index=True)`.
5. Writes a single `merged_generated_emails.csv` to disk.

The script is intentionally minimal and dependency-light so it can run on any machine that already has Python and pandas.

---

## 🎯 Typical Use Cases

- Build one big dataset from thousands of company-level phishing CSVs.
- Feed the merged file directly into:
  - scikit-learn pipelines (TF-IDF, classical ML).
  - Deep learning models (transformers, LSTMs, etc.).
  - BI tools / dashboards (Power BI, Tableau, etc.).
- Run global statistics:
  - Top phishing subjects.
  - Most frequent URLs / domains.
  - Distribution of VirusTotal labels.

Example (Python):

from pathlib import Path
import pandas as pd

csv_path = Path("merged_generated_emails.csv")
df = pd.read_csv(csv_path)
print(df.shape)
print(df["subject"].head())

---

## ⚠️ Notes & Troubleshooting

- If the script prints: `[!] تعذر قراءة الملف 'XYZ.csv' بسبب الترميز. تم تخطيه.`  
  → That file had an unreadable encoding; it is skipped, but the rest continue.
- If you rename the folder `Generated Emails`, update `input_dir` inside `merge_all_csvs.py` accordingly.
- For very large datasets (millions of rows), make sure you have enough RAM or process the data in chunks before loading everything into memory.

---

## 🏗️ Files in This Mini-Project

.
    merge_all_csvs.py          # Main script (CSV merger)
    requirements.txt           # Python dependencies
    README.md                  # This documentation
    Generated Emails/          # Input CSV/TXT files (not tracked by Git)

---

## 📜 License & Attribution

- Intended for data processing and ML research around phishing-email detection.
- Safe to use on your own generated data; does not contact the internet.
- If you use this tool as part of a publication or a bigger project, a small mention such as  
  "CSV merging utility based on the Phishing Dataset CSV Merger script"  
  is appreciated but not required.

Last Updated: 2025  
Status: Internal utility (stable)


requirements.txt
================
pandas>=2.1.0,<3.0.0
