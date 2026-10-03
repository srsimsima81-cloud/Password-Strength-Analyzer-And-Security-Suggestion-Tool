# 30-Test Plan

1 Empty; 2 one character; 3 short numeric; 4 common password; 5 long repeated; 6 lowercase only; 7 uppercase only; 8 numbers only; 9 symbols only; 10 mixed characters; 11 ascending sequence; 12 reverse sequence; 13 sequential letters; 14 keyboard sequence; 15 repeated characters; 16 repeated substring; 17 common word + number; 18 word + year; 19 personal name overlap; 20 birth-year overlap; 21 long passphrase-like; 22 Unicode; 23 spaces; 24 4096-character input; 25 score boundaries; 26 suggestion generation; 27 secure generator; 28 password not stored; 29 password not logged; 30 analytics metadata only.

Run `pytest -q` for automated coverage. For the final report, record Actual Result and Pass/Fail after running the full local test set.
