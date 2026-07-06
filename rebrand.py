#!/usr/bin/env python3
"""Rebrand 30-Days-Of-Python -> 30-Days-Of-Python-Philippines"""
import os
from pathlib import Path

REPO = Path(__file__).parent

# All OLD strings are original author values; NEW strings are what we want
R = [
    # Email
    ("asabeneh@gmail.com", "ribzcoi@gmail.com"),
    ("Asabeneh@gmail.com", "ribzcoi@gmail.com"),

    # YouTube
    ("https://www.youtube.com/channel/UC7PNRuno1rzYPb1xLa4yktw",
     "https://www.youtube.com/@ribaldzz"),
    ("youtube.com/channel/UC7PNRuno1rzYPb1xLa4yktw",
     "youtube.com/@ribaldzz"),

    # Social
    ("https://www.linkedin.com/in/asabeneh",
     "https://www.linkedin.com/in/mark-anthony-ribaldo"),
    ("https://twitter.com/Asabeneh",
     "https://twitter.com/ribzcoi"),
    ("twitter.com/Asabeneh",
     "twitter.com/ribzcoi"),

    # GitHub
    ("https://github.com/Asabeneh/30-Days-Of-Python",
     "https://github.com/RibaldzZ/30-Days-Of-Python-Philippines"),
    ("github.com/Asabeneh/30-Days-Of-Python",
     "github.com/RibaldzZ/30-Days-Of-Python-Philippines"),
    ("Asabeneh/30-Days-Of-Python",
     "RibaldzZ/30-Days-Of-Python-Philippines"),

    # Sponsors
    ("https://github.com/sponsors/asabeneh",
     "https://github.com/sponsors/RibaldzZ"),
    ("https://www.paypal.me/asabeneh", ""),

    # Testimonials
    ("https://www.asabeneh.com/testimonials", ""),
    ("www.asabeneh.com", ""),

    # Telegram
    ("https://t.me/ThirtyDaysOfPython",
     "https://t.me/+YourLinkHere"),
    ("t.me/ThirtyDaysOfPython",
     "t.me/+YourLinkHere"),

    # Author credit lines
    ("Author: Asabeneh Yetayeh", "Author: Mark Anthony Ribaldo"),
    ("author: Asabeneh Yetayeh", "author: Mark Anthony Ribaldo"),
    ("Author: Asabeneh", "Author: Mark Anthony Ribaldo"),

    # Name in HTML / display text (case-sensitive capital A)
    ("Asabeneh Yetayeh", "Mark Anthony Ribaldo"),

    # Badge links (shield.io)
    ("asabeneh", "ribzcoi"),

    # Name in code examples (quoted strings)
    ("'Asabeneh'", "'Mark'"),
    ('"Asabeneh"', '"Mark"'),
    ("'Yetayeh'", "'Ribaldz'"),
    ('"Yetayeh"', '"Ribaldz"'),

    # Name in data structures
    ("'first_name':'Asabeneh'", "'first_name':'Mark'"),
    ('"first_name":"Asabeneh"', '"first_name":"Mark"'),
    ("'last_name':'Yetayeh'", "'last_name':'Ribaldz'"),
    ('"last_name":"Yetayeh"', '"last_name":"Ribaldz"'),
    ("'country':'Finland'", "'country':'Philippines'"),
    ('"country":"Finland"', '"country":"Philippines"'),
    ("'country': 'Finland'", "'country': 'Philippines'"),
    ('"country": "Finland"', '"country": "Philippines"'),

    # Variable assignments
    ("country = 'Finland'", "country = 'Philippines'"),
    ('country = "Finland"', 'country = "Philippines"'),

    # Edition
    ("Second Edition: July, 2021", "First Edition: July, 2026"),

    # Washera
    ("Washera", "RibaldzZ Channel"),
    ("Washera YouTube channel", "RibaldzZ YouTube channel"),
]

# Reverse: the rebrand.py itself should NOT be modified (to survive re-runs)
# So we first read it, then exclude it from the walk

TEXT_EXTS = {'.md','.py','.txt','.json','.csv','.html','.css','.js',
             '.yml','.yaml','.cfg','.ini','.toml','.xml','.svg','.sh',
             '.bat','.ps1','.gitignore'}
BINARY_EXTS = {'.png','.jpg','.jpeg','.gif','.bmp','.ico','.webp',
               '.mp4','.mp3','.wav','.ogg','.pdf','.zip','.tar','.gz',
               '.woff','.woff2','.ttf','.eot'}

def main():
    print("=" * 60)
    print("  REBRAND: 30-Days-Of-Python  ->  30-Days-Of-Python-Philippines")
    print("=" * 60)

    renamed = 0
    total = 0
    for fpath in sorted(REPO.rglob('*')):
        if not fpath.is_file():
            continue
        # Skip .git, the script itself, and binary files
        if '.git' in fpath.parts:
            continue
        if fpath.name == 'rebrand.py':
            continue
        ext = fpath.suffix.lower()
        if ext in BINARY_EXTS:
            continue
        if ext not in TEXT_EXTS:
            try:
                with open(fpath, 'r', encoding='utf-8') as fh:
                    fh.read(200)
            except:
                continue

        total += 1
        try:
            with open(fpath, 'r', encoding='utf-8') as fh:
                text = fh.read()
        except:
            continue

        orig = text
        for old, new in R:
            if old:
                text = text.replace(old, new)

        if text != orig:
            renamed += 1
            with open(fpath, 'w', encoding='utf-8') as fh:
                fh.write(text)
            print(f"  [UPD] {fpath.relative_to(REPO)}")

    print(f"\n  Total scanned: {total}")
    print(f"  Modified:      {renamed}")
    print(f"  DONE!")
    print("=" * 60)

if __name__ == "__main__":
    main()
