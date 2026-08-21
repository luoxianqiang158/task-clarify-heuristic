# -*- coding: utf-8 -*-
"""Generate a Demo GIF for task-clarify-heuristic skill (animated chat demo)."""
import os
from PIL import Image, ImageDraw, ImageFont

FONT_PATH = 'C:/Windows/Fonts/msyh.ttc'
F = ImageFont.truetype(FONT_PATH, 20)
FT = ImageFont.truetype(FONT_PATH, 26)

W, H = 760, 1240
BG = (13, 17, 23)
AGENT_BUBBLE = (28, 33, 40)
USER_BUBBLE = (36, 77, 128)
ACCENT = (88, 166, 255)
GREEN = (63, 185, 80)
TEXT = (232, 238, 244)
SUBTEXT = (150, 160, 172)
LINE = (48, 54, 61)


def wrap(text, font, max_w):
    lines = []
    for para in text.split('\n'):
        if para == '':
            lines.append('')
            continue
        cur = ''
        for ch in para:
            test = cur + ch
            if font.getlength(test) > max_w and cur:
                lines.append(cur)
                cur = ch
            else:
                cur = test
        lines.append(cur)
    return lines


def bubble(d, x, y, w, text, fill, align='left', accent=None):
    lh = 28
    pad_x, pad_y = 14, 12
    lines = wrap(text, F, w - 2 * pad_x - (6 if accent else 0))
    h = len(lines) * lh + 2 * pad_y
    d.rounded_rectangle([x, y, x + w, y + h], radius=16, fill=fill)
    if accent:
        d.rounded_rectangle([x + 4, y + 8, x + 9, y + h - 8], radius=3, fill=accent)
    tx = x + pad_x + (8 if accent else 0)
    for i, ln in enumerate(lines):
        d.text((tx, y + pad_y + i * lh), ln, font=F, fill=TEXT)
    return h


def spec_card(d, x, y, w, items):
    pad = 16
    lh = 27
    # measure
    blocks = []
    for label, val in items:
        head = '▸ ' + label
        vlines = wrap(val, F, w - 2 * pad - 24)
        blocks.append((head, vlines))
    inner = sum(len(vl) * lh + lh for _, vl in blocks)
    h = inner + 2 * pad + 36
    d.rounded_rectangle([x, y, x + w, y + h], radius=16, fill=(20, 32, 28),
                        outline=GREEN, width=2)
    d.text((x + pad, y + 14), 'Agent 任务规约（经澄清确认）', font=FT, fill=GREEN)
    cy = y + 52
    for head, vlines in blocks:
        d.text((x + pad, cy), head, font=F, fill=ACCENT)
        cy += lh
        for vl in vlines:
            d.text((x + pad + 22, cy), vl, font=F, fill=TEXT)
            cy += lh
        cy += 2
    return h


def title_bar(d):
    d.rectangle([0, 0, W, 64], fill=(18, 22, 28))
    d.rectangle([0, 62, W, 64], fill=ACCENT)
    d.text((24, 18), 'task-clarify-heuristic', font=FT, fill=TEXT)
    d.text((W - 200, 22), '任务目标澄清助手', font=F, fill=SUBTEXT)


def render(messages):
    img = Image.new('RGB', (W, H), BG)
    d = ImageDraw.Draw(img)
    title_bar(d)
    y = 86
    for m in messages:
        if m[0] == 'user':
            w = 540
            h = len(wrap(m[1], F, w - 2 * 14 - 8)) * 28 + 24
            x = W - 24 - w
            bubble(d, x, y, w, m[1], USER_BUBBLE, align='right')
        elif m[0] == 'agent':
            w = 560
            h = len(wrap(m[1], F, w - 2 * 14 - 8)) * 28 + 24
            bubble(d, 24, y, w, m[1], AGENT_BUBBLE, accent=ACCENT)
        elif m[0] == 'spec':
            h = spec_card(d, 24, y, W - 48, m[1])
        y += h + 16
    # footer brand line
    d.text((24, H - 34),
           '跨 Dify / WorkBuddy / OpenCode 通用  ·  MIT License',
           font=F, fill=SUBTEXT)
    return img


# conversation data
M = [
    ('user', '帮我分析一下销售数据'),
    ('agent', '我先确认两点：\n① 这份报告给谁看、最终要拿到什么结论？\n② 怎样算「做好」——只找异常，还是要给可落地的改进建议？'),
    ('user', '给管理层，要找异常 + 可落地改进建议，一页看懂'),
    ('agent', '收到。再确认两点：\n① 输出格式要 Markdown 报告还是 PPT 大纲？\n② 是否允许我联网查行业公开资料？'),
    ('user', 'Markdown 报告，允许联网'),
    ('agent', '明白，正在生成结构化任务规约 →'),
]
SPEC = ('spec', [
    ('业务目标', '输出面向管理层的销售问题诊断报告'),
    ('受众', '管理层 / 汇报场景'),
    ('验收标准', '找异常 + 给可落地改进建议，一页看懂'),
    ('输出格式', 'Markdown 报告'),
    ('工具权限', '允许联网查公开资料'),
])
M_DONE = ('agent', '[OK] 任务定义清晰，执行不再跑偏。')

frames = []
frames.append(render(M[:1]))
frames.append(render(M[:2]))
frames.append(render(M[:3]))
frames.append(render(M[:4]))
frames.append(render(M[:5]))
frames.append(render(M[:6]))
frames.append(render(M[:6] + [SPEC]))
frames.append(render(M[:6] + [SPEC, M_DONE]))

durs = [700] * 6 + [1300, 1600]
out = 'assets/demo.gif'
frames[0].save(out, save_all=True, append_images=frames[1:], duration=durs,
               loop=0, optimize=True, disposal=2)
print('Saved', out, 'frames=', len(frames), 'size=', os.path.getsize(out))
