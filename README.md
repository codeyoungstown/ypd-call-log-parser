# ypd-call-log-parser
Parse image of YPD call logs via OCR to return text results

# Installation

- [Tesseract](https://github.com/tesseract-ocr/tesseract) is required on your path.
- `pip install -r requirements.txt`

# Usage
This script expects a directory of images of call logs. Run `python logs.py --help` to see full options.

```
$ python logs.py /Users/nick/Desktop/images/ --exclude
.
201104046 13:46:44 11/20/20 | Fight/Weapon 1 123 S HAZELWOOD AVE YOU
201104562 09:24:18 11/23/20 | Fight/Assault 2 123 S HAZELWOOD AVE YOU
201201952 14:54:38 12/11/20 | Property Report dL 123 S HAZELWOOD AVE YOU
201204356 21:34:38 12/24/20 | Unknown Trouble 1 123 S HAZELWOOD AVE; MAPPED TO YOU
201204438 11:44:43 12/25/20 | Fight/Assault 2 123 S HAZELWOOD AVE YOu
210100778 17:06:11 01/04/21 | Property Report 1 123 S HAZELWOOD AVE YOU
210101459 15:34:57 01/08/21 | Fight/Assault 2 123 S HAZELWOOD AVE YOU
210101491 17:09:39 01/08/21 | Investigation 8 ALMACT &S HAZELWOOD AVE YOU
210102654 18:41:42 01/14/21 | Suspicious 3 WALDEN CT & S HAZELWOOD AVE YOU
210102786 12:00:39 01/15/21 e Unknown Trouble = 1 123 S HAZELWOOD AVE You
210103080 23:57:58 01/16/21 | Investigation 8 123 S HAZELWOOD AVE YOU
210103093 01:11:51 01/17/21 | Noise Complaint a 123 S HAZELWOOD AVE YOU
210103096 01:33:06 01/17/21 | Investigation 8 123 S HAZELWOOD AVE YOU
```
