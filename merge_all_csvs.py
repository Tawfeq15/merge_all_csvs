#!/usr/bin/env python3
# coding: utf-8

"""
merge_all_csvs.py
يجمع كل ملفات الـ CSV الموجودة داخل مجلد "Generated Emails"
ويحفظها في ملف CSV واحد اسمه "merged_generated_emails.csv" في نفس مسار السكربت.

- يتجاهل جميع ملفات .txt
- يحاول قراءة الملفات بترميز utf-8-sig ثم latin-1 إذا احتاج
"""

from pathlib import Path
import sys

import pandas as pd


def main() -> None:
    # مجلد الإدخال: "Generated Emails" بجانب هذا الملف
    base_dir = Path(__file__).resolve().parent
    input_dir = base_dir / "Generated Emails"

    if not input_dir.exists() or not input_dir.is_dir():
        print(f"[!] لم أجد المجلد: {input_dir}")
        print("    تأكد من أن اسم المجلد صحيح وأن السكربت موجود في نفس المسار.")
        sys.exit(1)

    # نجمع كل ملفات CSV فقط
    csv_files = sorted(input_dir.glob("*.csv"))

    if not csv_files:
        print(f"[!] لا يوجد ملفات CSV في المجلد: {input_dir}")
        sys.exit(1)

    print(f"[+] تم العثور على {len(csv_files)} ملف CSV للدمج.")
    # لو حابب تتأكد أنه نص العدد (1403) اطبع تحذير بسيط
    if len(csv_files) != 1403:
        print(f"[!] ملاحظة: عدد ملفات CSV = {len(csv_files)} (ليس 1403 بالضبط).")
        print("    هذا مجرد تنبيه فقط، والدمج سيستمر بشكل عادي.\n")

    dataframes = []
    total_rows = 0

    for idx, csv_path in enumerate(csv_files, start=1):
        print(f"[{idx}/{len(csv_files)}] أقرأ: {csv_path.name}")

        # نحاول أكثر من encoding لو فيه مشكلة
        df = None
        for enc in ("utf-8-sig", "utf-8", "latin-1"):
            try:
                df = pd.read_csv(csv_path, encoding=enc)
                break
            except UnicodeDecodeError:
                continue

        if df is None:
            print(f"[!] تعذر قراءة الملف '{csv_path.name}' بسبب الترميز. تم تخطيه.")
            continue

        # لو حابب تعرف من أي ملف جاية السطر، فعّل السطر اللي تحت
        # df["__source_file"] = csv_path.name

        total_rows += len(df)
        dataframes.append(df)

    if not dataframes:
        print("[!] لم يتم تحميل أي DataFrame بنجاح. خروج.")
        sys.exit(1)

    # ندمج كل الداتا فريمز
    merged_df = pd.concat(dataframes, ignore_index=True)

    # ملف الإخراج
    output_path = base_dir / "merged_generated_emails.csv"

    merged_df.to_csv(output_path, index=False, encoding="utf-8-sig")

    print("\n[+] تم الدمج بنجاح!")
    print(f"    عدد ملفات CSV المدمجة : {len(dataframes)}")
    print(f"    عدد الصفوف الكلي      : {len(merged_df)} (تقريبي من {total_rows})")
    print(f"    مسار الملف الناتج      : {output_path}")


if __name__ == "__main__":
    main()
