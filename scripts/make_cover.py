# -*- coding: utf-8 -*-
"""Generate cover images for GitHub (1280x640) and ModelScope (640x640)."""
import os
from PIL import Image, ImageDraw, ImageFont

FONT = 'C:/Windows/Fonts/msyh.ttc'
F = lambda s: ImageFont.truetype(FONT, s)
ACCENT = (88, 166, 255)
GREEN = (63, 185, 80)
TEXT = (232, 238, 244)
SUB = (150, 160, 172)
PANEL = (22, 27, 34)
UB = (36, 77, 128)


def grad(d, W, H, c1, c2):
    for y in range(H):
        t = y / H
        r = int(c1[0] + (c2[0] - c1[0]) * t)
        g = int(c1[1] + (c2[1] - c1[1]) * t)
        b = int(c1[2] + (c2[2] - c1[2]) * t)
        d.line([(0, y), (W, y)], fill=(r, g, b))


def wrap(text, font, maxw):
    lines = []
    for para in text.split('\n'):
        if para == '':
            lines.append('')
            continue
        cur = ''
        for ch in para:
            if font.getlength(cur + ch) > maxw and cur:
                lines.append(cur)
                cur = ch
            else:
                cur += ch
        lines.append(cur)
    return lines


def bubble(d, x, y, w, text, fill, lh=30, padx=16, pady=12, accent=None, fs=20, tc=TEXT, align='left'):
    font = F(fs)
    lines = wrap(text, font, w - 2 * padx - (8 if accent else 0))
    h = len(lines) * lh + 2 * pady
    d.rounded_rectangle([x, y, x + w, y + h], radius=14, fill=fill)
    if accent:
        d.rounded_rectangle([x + 4, y + 8, x + 9, y + h - 8], radius=3, fill=accent)
    tx = x + padx + (8 if accent else 0)
    for i, ln in enumerate(lines):
        d.text((tx, y + pady + i * lh), ln, font=font, fill=tc)
    return h


def chat_panel(d, x, y, w):
    h1 = bubble(d, x + 90, y, w - 90, '帮我分析销售数据', UB, fs=20, align='right')
    y2 = y + h1 + 14
    h2 = bubble(d, x, y2, w - 70, '业务目标是什么？\n怎样算「完成」？', PANEL, accent=ACCENT, fs=20)
    y3 = y2 + h2 + 14
    h3 = bubble(d, x, y3, w, '→ 结构化任务规约（可执行、可移植）', (20, 32, 28),
                accent=GREEN, fs=20, tc=GREEN)
    return y3 + h3 - y + 20


def github_cover():
    W, H = 1280, 640
    img = Image.new('RGB', (W, H), (13, 17, 23))
    d = ImageDraw.Draw(img)
    grad(d, W, H, (13, 17, 23), (20, 26, 38))
    d.rectangle([0, 0, 8, H], fill=GREEN)
    # left text
    d.text((64, 96), 'task-clarify-heuristic', font=F(60), fill=TEXT)
    d.text((66, 188), '启发式任务澄清 · 让 Agent 不再跑偏', font=F(30), fill=SUB)
    d.text((66, 240), '把模糊需求收敛成结构化、可执行的 Agent 任务规约', font=F(22), fill=SUB)
    # chips
    chips = ['Dify', 'WorkBuddy', 'OpenCode', 'MIT']
    cx = 66
    for c in chips:
        w = F(22).getlength(c) + 28
        d.rounded_rectangle([cx, 300, cx + w, 336], radius=10, outline=ACCENT, width=2)
        d.text((cx + 14, 308), c, font=F(22), fill=ACCENT)
        cx += w + 14
    d.text((66, H - 70), '跨 Dify / WorkBuddy / OpenCode 通用  ·  MIT License', font=F(22), fill=SUB)
    # right chat panel
    chat_panel(d, 680, 110, 560)
    out = 'assets/cover-github.png'
    img.save(out)
    print('saved', out)


def modelscope_cover():
    W = H = 640
    img = Image.new('RGB', (W, H), (13, 17, 23))
    d = ImageDraw.Draw(img)
    grad(d, W, H, (13, 17, 23), (20, 26, 38))
    d.rectangle([0, 0, 8, H], fill=GREEN)
    d.text((48, 56), 'task-clarify-heuristic', font=F(34), fill=TEXT)
    d.text((50, 110), '任务目标澄清助手', font=F(22), fill=SUB)
    chat_panel(d, 48, 170, W - 96)
    d.text((48, H - 56), '跨 Dify / WorkBuddy / OpenCode 通用', font=F(20), fill=SUB)
    out = 'assets/cover-modelscope.png'
    img.save(out)
    print('saved', out)


if __name__ == '__main__':
    github_cover()
    modelscope_cover()
