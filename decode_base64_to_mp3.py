import re

# 你的原html文件
input_html_file = "index_new.html"

# 新的mp3文件路径，比如你准备了 music.mp3
new_mp3_path = "music.mp3"

# 输出的新html文件
output_html_file = "index_new.html"

# 读取原html内容
with open(input_html_file, "r", encoding="utf-8") as file:
    html_content = file.read()

# 改进版正则：找到任何一个带base64开头的 source 标签，不管中间有没有换行
new_html_content = re.sub(
    r'(<source[^>]*src=")data:audio/mpeg;base64,[^"]*(")',
    rf'\1{new_mp3_path}\2',
    html_content,
    flags=re.DOTALL
)

# 保存成新的html文件
with open(output_html_file, "w", encoding="utf-8") as file:
    file.write(new_html_content)

print(f"✅ 成功替换并保存为 {output_html_file} ！")
