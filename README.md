===== README.md =====
# 📚 Phishing Dataset CSV Merger (Generated Emails)

Small utility script that takes the per-company CSV files produced by the **Phishing Email Generator** and merges them into a **single ML-ready dataset**.

> Problem: you have thousands of small CSVs in `Generated Emails/` and you just want one big `merged_generated_emails.csv` to load into pandas, scikit-learn, or any analysis tool.

---

## ✨ Highlights

- **Automatic discovery** – scans `Generated Emails/` and picks up every `*.csv` file.
- **TXT ignored by design** – safely skips the human-readable `.txt` exports.
- **Encoding-resilient** – tries `utf-8-sig`, `utf-8`, then `latin-1` if needed.
- **Header-aware** – keeps the first header row and stacks all rows under it.
- **Single dataset output** – writes `merged_generated_emails.csv` next to the script.
- **ML-friendly** – output stays fully compatible with the original generator schema.

---

## 🚀 Quick Start

> TL;DR: **drop the script next to `Generated Emails/` → run it → get one big CSV.**

### 1️⃣ Open a terminal in the project folder

```bash
cd path/to/"New Code Generate"
# Example on Windows:
# cd "%USERPROFILE%\Desktop\New Code Generate"
2️⃣ Create a virtual environment (optional but recommended)
bash
Copy code
python -m venv .venv

# Windows
.\.venv\Scripts\activate

# Linux/macOS
# source .venv/bin/activate
3️⃣ Install dependencies
bash
Copy code
pip install -r requirements.txt
# or
# py -m pip install -r requirements.txt
4️⃣ Check the folder layout
text
Copy code
New Code Generate/
├── merge_all_csvs.py
├── requirements.txt
├── README.md
└── Generated Emails/
    ├── generated_phishing_emails_ABC.csv
    ├── generated_phishing_emails_ABC.txt
    ├── generated_phishing_emails_XYZ.csv
    └── ...
All .csv files should live inside Generated Emails/.

.txt files can stay there; the script ignores them automatically.

5️⃣ Run the merger
bash
Copy code
python merge_all_csvs.py
You should see progress like:

text
Copy code
[+] تم العثور على 1403 ملف CSV للدمج.
[1/1403] أقرأ: generated_phishing_emails_ABC.csv
[2/1403] أقرأ: generated_phishing_emails_Adobe.csv
...
[+] تم الدمج بنجاح!
    عدد ملفات CSV المدمجة : 1403
    عدد الصفوف الكلي      : 123456
    مسار الملف الناتج      : C:\...\New Code Generate\merged_generated_emails.csv
📁 Input & Output
🔹 Input
Directory: Generated Emails/

Files: any number of files matching *.csv

Expected schema: whatever the generator produced, for example:

cs
Copy code
id,label,from,to,subject,body,url,vt_status,vt_malicious,vt_suspicious,vt_clean
1,phishing,"Adobe Security <security@adobe.com>",ahmad@example.com,"URGENT: Account will be closed",...
Individual CSVs may come from different companies; this tool simply stacks them into one big dataset.

🔹 Output
File: merged_generated_emails.csv

Location: same folder as merge_all_csvs.py

Format: standard UTF-8 CSV, with the union of all columns found across source files.

If some CSVs have extra columns, they are kept; missing values are filled with NaN.

