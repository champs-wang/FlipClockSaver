#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Flip Clock Screen Saver v15
- Toplevel per monitor (overrideredirect + exact geometry) - all monitors work
- Label widgets instead of Canvas - text update is atomic, ZERO flicker
- Card-style digits via Label with solid bg + border (flat design)
- Settings GUI: direct tk.Tk(), no DPI call in /c mode
- Config: %APPDATA%\FlipClockSaver\flip_clock_config.json
"""

import sys, os, json, ctypes, tkinter as tk
from datetime import datetime

CONFIG_DIR = os.path.join(os.environ.get("APPDATA", os.path.expanduser("~")), "FlipClockSaver")
CONFIG_PATH = os.path.join(CONFIG_DIR, "flip_clock_config.json")
os.makedirs(CONFIG_DIR, exist_ok=True)

DEFAULT_CONFIG = {
    "hour24": True,
    "clock_size": 200,          "clock_color": "#FFFFFF",
    "card_bg": "#000000",
    "clock_font": "Consolas",
    "info_size": 28,            "info_color": "#CCCCCC",
    "info_font": "Microsoft YaHei",
}

COMMON_FONTS = [
    "Arial","Calibri","Cambria","Candara","Comic Sans MS","Consolas",
    "Constantia","Corbel","Courier New","Ebrima","Franklin Gothic Medium",
    "Georgia","Impact","Lucida Console","Microsoft Sans Serif","Microsoft YaHei",
    "Microsoft YaHei UI","Palatino Linotype","Segoe UI","Segoe Print","Segoe Script",
    "SimSun","Sitka","Tahoma","Times New Roman","Trebuchet MS","Verdana",
    "微软雅黑","宋体","黑体",
]

def load_config():
    try:
        if os.path.exists(CONFIG_PATH):
            return {**DEFAULT_CONFIG, **json.load(open(CONFIG_PATH,"r",encoding="utf-8"))}
    except: pass
    return DEFAULT_CONFIG.copy()

def save_config(cfg):
    json.dump(cfg, open(CONFIG_PATH,"w",encoding="utf-8"), indent=2, ensure_ascii=False)

# ======================== SETTINGS GUI ========================
def run_settings_gui():
    cfg = load_config()
    root = tk.Tk()
    root.title("翻页时钟屏保 v15 设置")
    root.geometry("500x720+200+200")
    root.resizable(False, False)
    root.configure(bg="#2b2b2b")
    root.attributes("-topmost", True)
    root.lift(); root.focus_force()

    tk.Label(root, text="翻页时钟屏保 v15 设置", font=("Microsoft YaHei",14,"bold"),
             fg="#FFF", bg="#2b2b2b").pack(pady=(15,5))

    f=tk.LabelFrame(root,text="时间制式",font=("Microsoft YaHei",10),fg="#CCC",bg="#2b2b2b")
    f.pack(fill="x",padx=20,pady=5)
    tv=tk.IntVar(value=1 if cfg.get("hour24",True) else 0)
    tk.Radiobutton(f,text="24小时制",variable=tv,value=1,bg="#2b2b2b",fg="#FFF",
                   selectcolor="#2b2b2b",activebackground="#2b2b2b",activeforeground="#FFF"
                   ).pack(side="left",padx=15,pady=5)
    tk.Radiobutton(f,text="12小时制",variable=tv,value=0,bg="#2b2b2b",fg="#FFF",
                   selectcolor="#2b2b2b",activebackground="#2b2b2b",activeforeground="#FFF"
                   ).pack(side="left",padx=15,pady=5)

    f=tk.LabelFrame(root,text="时钟字号",font=("Microsoft YaHei",10),fg="#CCC",bg="#2b2b2b")
    f.pack(fill="x",padx=20,pady=5)
    csv=tk.IntVar(value=cfg.get("clock_size",100))
    tk.Spinbox(f,from_=30,to=300,textvariable=csv,width=5,
               bg="#3c3c3c",fg="#FFF",buttonbackground="#3c3c3c").pack(side="left",padx=10,pady=5)

    f=tk.LabelFrame(root,text="时钟字体",font=("Microsoft YaHei",10),fg="#CCC",bg="#2b2b2b")
    f.pack(fill="x",padx=20,pady=5)
    cfv=tk.StringVar(value=cfg.get("clock_font","Consolas"))
    tk.OptionMenu(f,cfv,cfg["clock_font"],*COMMON_FONTS).pack(side="left",padx=10,pady=5)

    f=tk.LabelFrame(root,text="时钟颜色",font=("Microsoft YaHei",10),fg="#CCC",bg="#2b2b2b")
    f.pack(fill="x",padx=20,pady=5)
    tk.Label(f,text="文字",fg="#CCC",bg="#2b2b2b").pack(side="left",padx=5)
    ccv=tk.StringVar(value=cfg.get("clock_color","#FFF"))
    tk.Entry(f,textvariable=ccv,width=10,bg="#3c3c3c",fg="#FFF").pack(side="left",padx=5)
    tk.Label(f,text="卡片",fg="#CCC",bg="#2b2b2b").pack(side="left",padx=5)
    cbv=tk.StringVar(value=cfg.get("card_bg","#1a1a1a"))
    tk.Entry(f,textvariable=cbv,width=10,bg="#3c3c3c",fg="#FFF").pack(side="left",padx=5)

    f=tk.LabelFrame(root,text="日期信息字号",font=("Microsoft YaHei",10),fg="#CCC",bg="#2b2b2b")
    f.pack(fill="x",padx=20,pady=5)
    isv=tk.IntVar(value=cfg.get("info_size",28))
    tk.Spinbox(f,from_=10,to=100,textvariable=isv,width=5,
               bg="#3c3c3c",fg="#FFF",buttonbackground="#3c3c3c").pack(side="left",padx=10,pady=5)

    f=tk.LabelFrame(root,text="信息字体",font=("Microsoft YaHei",10),fg="#CCC",bg="#2b2b2b")
    f.pack(fill="x",padx=20,pady=5)
    ifv=tk.StringVar(value=cfg.get("info_font","Microsoft YaHei"))
    tk.OptionMenu(f,ifv,cfg["info_font"],*COMMON_FONTS).pack(side="left",padx=10,pady=5)

    f=tk.LabelFrame(root,text="信息颜色",font=("Microsoft YaHei",10),fg="#CCC",bg="#2b2b2b")
    f.pack(fill="x",padx=20,pady=5)
    tk.Label(f,text="文字",fg="#CCC",bg="#2b2b2b").pack(side="left",padx=5)
    icv=tk.StringVar(value=cfg.get("info_color","#CCC"))
    tk.Entry(f,textvariable=icv,width=10,bg="#3c3c3c",fg="#FFF").pack(side="left",padx=5)

    st=tk.StringVar(value="")
    tk.Label(root,textvariable=st,font=("Microsoft YaHei",9),fg="#4CAF50",bg="#2b2b2b").pack(pady=(5,0))

    def do_save():
        save_config({"hour24":bool(tv.get()),"clock_size":csv.get(),
                      "clock_font":cfv.get(),"clock_color":ccv.get(),"card_bg":cbv.get(),
                      "info_size":isv.get(),"info_font":ifv.get(),"info_color":icv.get()})
        st.set("已保存")
        root.after(2000,lambda:st.set(""))

    bf=tk.Frame(root,bg="#2b2b2b"); bf.pack(pady=(10,15))
    tk.Button(bf,text="保存设置",font=("Microsoft YaHei",11),bg="#4CAF50",fg="#FFF",
              activebackground="#45a049",activeforeground="#FFF",padx=20,pady=5,
              command=do_save).pack(side="left",padx=10)
    tk.Button(bf,text="关闭",font=("Microsoft YaHei",11),bg="#555",fg="#FFF",
              activebackground="#666",activeforeground="#FFF",padx=20,pady=5,
              command=root.destroy).pack(side="left",padx=10)
    root.mainloop()

# ======================== SCREEN SAVER ========================

class MonitorDisplay:
    """One fullscreen overlay per monitor using Label widgets (no Canvas)."""

    def __init__(self, root, mw, mh, mx, my, cfg):
        self.win = tk.Toplevel(root)
        self.win.overrideredirect(True)
        self.win.configure(bg="black", cursor="none")
        self.win.geometry(f"{mw}x{mh}+{mx}+{my}")
        self.win.attributes("-topmost", True)
        self.cfg = cfg

        self.mw, self.mh = mw, mh
        self.clock_labels = {}  # digit_idx -> Label
        self.colon_labels = {}  # colon_idx -> Label
        self.info_labels = []   # [date_label, weekday_label, lunar_label]

        self._last_time_str = None
        self._last_info = None

        self._build()

    def _build(self):
        cfg = self.cfg
        mw, mh = self.mw, self.mh

        # Card dimensions: based on configured clock_size, auto-scale to fit screen
        base_font = cfg["clock_size"]
        card_h = int(base_font * 2.0)
        card_w = int(card_h / 1.4)
        total_w = 8 * card_w
        if total_w > mw * 0.85:
            scale = (mw * 0.85) / total_w
            card_w = int(card_w * scale)
            card_h = int(card_h * scale)
        digit_font_size = int(card_h * 0.45)
        clock_start_x = (mw - 8 * card_w) // 2
        clock_center_y = int(mh * 0.33)
        card_top = clock_center_y - card_h // 2

        # Create digit cards (8 slots)
        for i in range(8):
            x = clock_start_x + i * card_w
            lbl = tk.Label(self.win, text="", font=(cfg.get("clock_font","Consolas"), digit_font_size, "bold"),
                           fg=cfg["clock_color"], bg=cfg["card_bg"],
                           padx=0, pady=0, anchor="center")
            lbl.place(x=x, y=card_top, width=card_w, height=card_h)
            self.clock_labels[i] = lbl

        # Colon labels (positions 2 and 5)
        for ci in [2, 5]:
            cx = clock_start_x + ci * card_w + card_w // 2
            lbl = tk.Label(self.win, text=":", font=(cfg.get("clock_font","Consolas"), cfg["clock_size"], "bold"),
                           fg=cfg["clock_color"], bg="black")
            lbl.place(x=cx, y=clock_center_y, anchor="center")
            self.colon_labels[ci] = lbl

        # Info text area
        info_start_y = int(mh * 0.65)
        info_spacing = int(cfg["info_size"] * 1.6)
        fs = (cfg.get("info_font","Microsoft YaHei"), cfg["info_size"])
        fc = cfg["info_color"]

        for i in range(3):
            lbl = tk.Label(self.win, text="", font=fs, fg=fc, bg="black")
            lbl.place(relx=0.5, y=info_start_y + i * info_spacing, anchor="n")
            self.info_labels.append(lbl)

    def update(self, time_str, date_str, weekday_str, lunar_str):
        # Update digits only if changed
        if time_str != self._last_time_str:
            # time_str = "HH:MM:SS" → digits at indices 0,1,3,4,6,7
            for slot_idx, ch_idx in zip([0,1,3,4,6,7], [0,1,3,4,6,7]):
                self.clock_labels[slot_idx].config(text=time_str[ch_idx])
            self._last_time_str = time_str

        # Update info
        new_info = (date_str, weekday_str, lunar_str)
        if new_info != self._last_info:
            for lbl, txt in zip(self.info_labels, new_info):
                lbl.config(text=txt)
            self._last_info = new_info


class FlipClockSaver:
    def __init__(self, root):
        self.root = root
        self.cfg = load_config()
        self.displays = []

        # Enumerate monitors
        try:
            from ctypes import wintypes
            u32 = ctypes.windll.user32
            info = []
            @ctypes.WINFUNCTYPE(ctypes.c_bool, wintypes.HMONITOR, wintypes.HDC,
                                ctypes.POINTER(wintypes.RECT), wintypes.LPARAM)
            def cb(h, dc, r, d):
                info.append({"l":r.contents.left,"t":r.contents.top,
                             "r":r.contents.right,"b":r.contents.bottom})
                return True
            u32.EnumDisplayMonitors(None, None, cb, 0)
        except Exception:
            info = [{"l":0,"t":0,"r":root.winfo_screenwidth(),"b":root.winfo_screenheight()}]

        for m in info:
            mw = m["r"] - m["l"]; mh = m["b"] - m["t"]
            md = MonitorDisplay(root, mw, mh, m["l"], m["t"], self.cfg)
            # Bind exit events to each Toplevel
            md.win.bind("<Key>", lambda e: root.destroy())
            md.win.bind("<Motion>", lambda e: root.destroy())
            md.win.bind("<Button>", lambda e: root.destroy())
            self.displays.append(md)

        self._tick()

    def _get_lunar(self, dt):
        try:
            import zhdate
            lu = zhdate.ZhDate.from_datetime(dt)
            gn=["甲","乙","丙","丁","戊","己","庚","辛","壬","癸"]
            zh=["子","丑","寅","卯","辰","巳","午","未","申","酉","戌","亥"]
            an=["鼠","牛","虎","兔","龙","蛇","马","羊","猴","鸡","狗","猪"]
            mn=["正","二","三","四","五","六","七","八","九","十","冬","腊"]
            dn=["初一","初二","初三","初四","初五","初六","初七","初八","初九","初十",
                "十一","十二","十三","十四","十五","十六","十七","十八","十九","二十",
                "廿一","廿二","廿三","廿四","廿五","廿六","廿七","廿八","廿九","三十"]
            yg=gn[(lu.lunar_year-4)%10]+zh[(lu.lunar_year-4)%12]
            return f"{yg}{an[(lu.lunar_year-4)%12]}年 {mn[(lu.lunar_month-1)%12]}月{dn[lu.lunar_day-1]}"
        except: return ""

    def _tick(self):
        if not self.root.winfo_exists():
            return
        try:
            now = datetime.now()
            ts = now.strftime("%H:%M:%S") if self.cfg["hour24"] else now.strftime("%I:%M:%S %p")
            ds = now.strftime("%Y年%m月%d日")
            wd = ["星期一","星期二","星期三","星期四","星期五","星期六","星期日"][now.weekday()]
            ls = self._get_lunar(now)
            for d in self.displays:
                d.update(ts, ds, wd, ls)
        except tk.TclError:
            return
        self.root.after(500, self._tick)


# ======================== MAIN ========================
def main():
    raw = " ".join(sys.argv[1:]).lower()
    if "/c" in raw:
        run_settings_gui()
        return

    try:
        ctypes.windll.shcore.SetProcessDpiAwareness(2)
    except Exception:
        try:
            ctypes.windll.user32.SetProcessDPIAware()
        except Exception:
            pass

    root = tk.Tk()
    root.withdraw()  # hide root, Toplevels are the visible windows
    FlipClockSaver(root)
    root.mainloop()

if __name__ == "__main__":
    main()
