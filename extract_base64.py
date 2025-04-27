import re
import base64
import os

# 读取 HTML
with open("index.html", "r", encoding="utf-8") as f:
    html_content = f.read()

# 匹配所有 Base64 图片
base64_images = re.findall(r'(data:image/(.*?);base64,(.*?))"', html_content)

# 保存图片的目录
os.makedirs("images", exist_ok=True)

# 新的 HTML 内容
new_html = html_content

for idx, (full_base64, img_type, img_data) in enumerate(base64_images):
    img_filename = f"images/image_{idx+1}.{img_type}"
    # 保存图片
    with open(img_filename, "wb") as img_file:
        img_file.write(base64.b64decode(img_data))
    # 替换 HTML 里的 Base64为图片链接
    new_html = new_html.replace(full_base64, img_filename)
    print(f"提取并替换：{img_filename}")

# 写入新的 HTML 文件
with open("index_new.html", "w", encoding="utf-8") as f:
    f.write(new_html)

print("✅ 全部完成！生成了 index_new.html")
