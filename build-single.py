#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build-single.py — art 폴더의 그림과 음악을 HTML 안에 박아넣어 파일 하나로 만듭니다.

쓰는 법:  python3 build-single.py
결과:     univercityhunter-single.html  (그림·음악까지 전부 들어간 한 파일)

음악(art/bgm/*.mp3)도 같이 들어갑니다. base64 로 박으면 용량이 1/3쯤 늘어나므로
곡이 길면 파일이 꽤 커집니다 — 다 넣은 크기를 마지막에 알려 줍니다.

평소 작업은 univercityhunter.html + art/ 로 하고,
누구에게 파일 하나로 보내야 할 때만 이걸 돌리면 됩니다.
"""
import base64, io, os, re, sys

# 윈도 콘솔은 기본이 cp949 라 줄표(—) 같은 글자에서 터집니다. 출력만 UTF-8 로 돌립니다.
try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

HERE = os.path.dirname(os.path.abspath(__file__))
SRC  = os.path.join(HERE, "index.html")   # 게임 본체. 예전에는 univercityhunter.html 이었습니다
DST  = os.path.join(HERE, "univercityhunter-single.html")
ART  = os.path.join(HERE, "art")

MIME = {".webp": "image/webp", ".png": "image/png", ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg", ".gif": "image/gif", ".svg": "image/svg+xml",
        ".mp3": "audio/mpeg", ".m4a": "audio/mp4", ".ogg": "audio/ogg", ".wav": "audio/wav"}

def data_url(rel):
    """art 아래 상대경로를 data URL로 바꿉니다. 파일이 없으면 None."""
    path = os.path.join(ART, rel)
    if not os.path.isfile(path):
        return None
    ext = os.path.splitext(path)[1].lower()
    if ext not in MIME:
        print("  ? 모르는 형식이라 건너뜁니다: %s" % rel)
        return None
    with open(path, "rb") as f:
        return "data:%s;base64,%s" % (MIME[ext], base64.b64encode(f.read()).decode())

def main():
    if not os.path.isfile(SRC):
        print("index.html 을 찾지 못했습니다. 이 스크립트를 게임 파일 옆에 두세요.")
        sys.exit(1)

    s = io.open(SRC, encoding="utf-8").read()

    # ART 기준 경로를 빈 문자열로 — 이제 경로가 아니라 data URL이 직접 들어갑니다
    s = re.sub(r'const ART="[^"]*";', 'const ART="";', s, count=1)

    # 코드 안의 "xxx.webp" · "bgm/xxx.mp3" 꼴 문자열을 전부 찾아 바꿉니다
    used, missing = [], []
    def swap(m):
        rel = m.group(1)
        url = data_url(rel)
        if url is None:
            missing.append(rel); return m.group(0)
        used.append(rel)
        return '"%s"' % url

    s = re.sub(r'"([A-Za-z0-9_\-/]+\.(?:webp|png|jpe?g|gif|svg|mp3|m4a|ogg|wav))"', swap, s)

    io.open(DST, "w", encoding="utf-8").write(s)

    snd = [r for r in used if os.path.splitext(r)[1].lower() in (".mp3", ".m4a", ".ogg", ".wav")]
    print("그림 %d개, 음악 %d개를 넣었습니다." % (len(used) - len(snd), len(snd)))
    for r in used:
        print("  + %s (%d KB)" % (r, os.path.getsize(os.path.join(ART, r)) // 1024))
    if missing:
        print("찾지 못한 것 %d개 — art 폴더를 확인하세요. (아직 안 만든 곡이면 그냥 두셔도 됩니다)" % len(missing))
        for r in missing:
            print("  - %s" % r)
    print("\n%s  (%d KB)" % (os.path.basename(DST), len(s.encode()) // 1024))

if __name__ == "__main__":
    main()
