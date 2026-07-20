# FlipClockSaver

Windows 翻页时钟屏幕保护程序，支持多显示器。

## 特性

- 双显示器 / 多显示器完美支持
- 24 小时制 / 12 小时制可切换
- 可自定义时钟字体、字号、颜色
- 可自定义日期信息字体、字号、颜色
- 农历显示
- 零闪烁渲染（Label 组件原子更新）

## 安装

1. 下载 `FlipClockSaver.scr`
2. 右键 → 安装，或直接放入 `C:\Windows\` 目录
3. 右键桌面 → 个性化 → 锁屏界面 → 屏幕保护程序设置，选择 FlipClockSaver

## 设置

右键 `FlipClockSaver.scr` → 配置，或命令行：

```
FlipClockSaver.scr /c
```

可配置项：
- 时间制式（12h / 24h）
- 时钟字号 / 字体 / 颜色 / 卡片底色
- 信息字号 / 字体 / 颜色
- 设置保存至 `%APPDATA%\FlipClockSaver\flip_clock_config.json`

## 开发者

```bash
pip install pyinstaller zhdate
pyinstaller --onefile --noconsole --name FlipClockSaver flip_clock_saver.py
# 产物: dist/FlipClockSaver.exe → 重命名为 .scr
```

## 系统要求

- Windows 10 / 11
- 不需要额外运行环境（PyInstaller 打包为独立 exe）
