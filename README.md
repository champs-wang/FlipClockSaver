# FlipClockSaver

Windows 缈婚〉鏃堕挓灞忓箷淇濇姢绋嬪簭锛屾敮鎸佸鏄剧ず鍣ㄣ€?
## 鐗规€?
- 鍙屾樉绀哄櫒 / 澶氭樉绀哄櫒瀹岀編鏀寔
- 24 灏忔椂鍒?/ 12 灏忔椂鍒跺彲鍒囨崲
- 鍙嚜瀹氫箟鏃堕挓瀛椾綋銆佸瓧鍙枫€侀鑹?- 鍙嚜瀹氫箟鏃ユ湡淇℃伅瀛椾綋銆佸瓧鍙枫€侀鑹?- 鍐滃巻鏄剧ず
- 闆堕棯鐑佹覆鏌擄紙Label 缁勪欢鍘熷瓙鏇存柊锛?
## 瀹夎

1. 涓嬭浇 `FlipClockSaver.scr`
2. 鍙抽敭 鈫?瀹夎锛屾垨鐩存帴鏀惧叆 `C:\Windows\` 鐩綍
3. 鍙抽敭妗岄潰 鈫?涓€у寲 鈫?閿佸睆鐣岄潰 鈫?灞忓箷淇濇姢绋嬪簭璁剧疆锛岄€夋嫨 FlipClockSaver

## 璁剧疆

鍙抽敭 `FlipClockSaver.scr` 鈫?閰嶇疆锛屾垨鍛戒护琛岋細

```
FlipClockSaver.scr /c
```

鍙厤缃」锛?- 鏃堕棿鍒跺紡锛?2h / 24h锛?- 鏃堕挓瀛楀彿 / 瀛椾綋 / 棰滆壊 / 鍗＄墖搴曡壊
- 淇℃伅瀛楀彿 / 瀛椾綋 / 棰滆壊
- 璁剧疆淇濆瓨鑷?`%APPDATA%\FlipClockSaver\flip_clock_config.json`

## 寮€鍙戣€?
```bash
pip install pyinstaller zhdate
pyinstaller --onefile --noconsole --name FlipClockSaver flip_clock_saver.py
# 浜х墿: dist/FlipClockSaver.exe 鈫?閲嶅懡鍚嶄负 .scr
```

## 绯荤粺瑕佹眰

- Windows 10 / 11
- 涓嶉渶瑕侀澶栬繍琛岀幆澧冿紙PyInstaller 鎵撳寘涓虹嫭绔?exe锛?