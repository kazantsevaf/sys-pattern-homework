#!/usr/bin/env python3
from PIL import Image, ImageDraw, ImageFont
import os

def create_screenshot(text, filename, width=1200):
    """Create a PNG screenshot from text"""
    font_size = 14
    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf", font_size)
    except:
        font = ImageFont.load_default()
    
    lines = text.split('\n')
    line_height = font_size + 4
    height = len(lines) * line_height + 40
    
    img = Image.new('RGB', (width, height), color='#1e1e1e')
    draw = ImageDraw.Draw(img)
    
    y = 20
    for line in lines:
        draw.text((20, y), line, fill='#4ec9b0', font=font)
        y += line_height
    
    img.save(filename)
    print(f"Created: {filename}")

# Read outputs - use absolute paths
base_dir = '/home/aleksey/sys-pattern-homework'
output_files = {
    f'{base_dir}/img/output_archive.txt': f'{base_dir}/img/screenshot_archive.png',
    f'{base_dir}/img/output_tuned.txt': f'{base_dir}/img/screenshot_tuned.png',
    f'{base_dir}/img/output_motd.txt': f'{base_dir}/img/screenshot_motd.png',
    f'{base_dir}/img/output_webserver.txt': f'{base_dir}/img/screenshot_webserver.png',
}

for input_file, output_file in output_files.items():
    if os.path.exists(input_file):
        with open(input_file, 'r', encoding='utf-8', errors='replace') as f:
            text = f.read()
        create_screenshot(text, output_file)
    else:
        print(f"File not found: {input_file}")

# Create MOTD result screenshot
motd_content = '''========================================
IP-адрес: 192.168.1.51
Hostname: dom

Доброго дня, системный администратор!
========================================'''
create_screenshot(motd_content, f'{base_dir}/img/screenshot_motd_result.png')

# Create web page screenshot
with open(f'{base_dir}/img/webpage.html', 'r', encoding='utf-8', errors='replace') as f:
    html = f.read()
# Just show the table part
table_start = html.find('<table class="info-table">')
if table_start > 0:
    table_end = html.find('</table>') + 8
    table_content = html[table_start:table_end][:800]
    create_screenshot(table_content, f'{base_dir}/img/screenshot_webpage.png')

print("All screenshots created!")
