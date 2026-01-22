#!/usr/bin/env python3
"""
HTML to Markdown Converter v2
将Anthropic Engineering Blog的HTML转换为Markdown格式
"""

import re
import html
from html.parser import HTMLParser


class AnthropicHTMLParser(HTMLParser):
    """专门解析Anthropic Engineering Blog的HTML"""

    def __init__(self):
        super().__init__()
        self.result = []
        self.in_script = False
        self.in_style = False
        self.capture = False
        self.link_stack = []  # 存储链接的[href, text]
        self.current_link = None
        self.tag_stack = []
        self.in_code_block = False
        self.in_inline_code = False

    def handle_starttag(self, tag, attrs):
        self.tag_stack.append(tag)

        # 跳过script和style标签
        if tag in ['script', 'style', 'noscript', 'link', 'meta']:
            self.in_script = True
            return

        # 检测主要内容开始 - 当遇到第一个段落或标题时开始捕获
        if not self.capture and tag in ['h1', 'h2', 'h3', 'p', 'article']:
            self.capture = True

        if not self.capture:
            return

        # 处理各种标签
        if tag == 'h1':
            self.result.append('\n\n# ')
        elif tag == 'h2':
            self.result.append('\n\n## ')
        elif tag == 'h3':
            self.result.append('\n\n### ')
        elif tag == 'h4':
            self.result.append('\n\n#### ')
        elif tag == 'p':
            if self.result and not self.result[-1].endswith('\n\n'):
                self.result.append('\n\n')
        elif tag == 'strong' or tag == 'b':
            self.result.append('__')
        elif tag == 'em' or tag == 'i':
            self.result.append('*')
        elif tag == 'code':
            self.result.append('`')
            self.in_inline_code = True
        elif tag == 'pre':
            self.result.append('\n\n```\n')
            self.in_code_block = True
        elif tag == 'a':
            href = dict(attrs).get('href', '')
            if href and not href.startswith('#'):
                # 存储链接信息
                self.current_link = {'href': href, 'text': ''}
        elif tag == 'img':
            src = dict(attrs).get('src', '')
            alt = dict(attrs).get('alt', '')
            if src:
                # 清理Next.js图片URL
                if '/_next/image?url=' in src:
                    # 提取真实URL
                    match = re.search(r'url=([^&]+)', src)
                    if match:
                        src = html.unescape(match.group(1))
                self.result.append(f'\n\n![{alt}]({src})\n\n')
        elif tag == 'ul':
            self.result.append('\n\n')
        elif tag == 'ol':
            self.result.append('\n\n')
        elif tag == 'li':
            if self.result and not self.result[-1].endswith('\n'):
                self.result.append('\n')
            # 判断是有序列表还是无序列表
            if 'ol' in self.tag_stack:
                self.result.append('1. ')
            else:
                self.result.append('- ')
        elif tag == 'blockquote':
            self.result.append('\n\n> ')
        elif tag == 'hr':
            self.result.append('\n\n---\n\n')

    def handle_endtag(self, tag):
        if tag in self.tag_stack:
            self.tag_stack.pop()

        if tag in ['script', 'style', 'noscript', 'link', 'meta']:
            self.in_script = False
            return

        if not self.capture:
            return

        if tag == 'strong' or tag == 'b':
            self.result.append('__')
        elif tag == 'em' or tag == 'i':
            self.result.append('*')
        elif tag == 'code':
            self.result.append('`')
            self.in_inline_code = False
        elif tag == 'pre':
            self.result.append('\n```\n\n')
            self.in_code_block = False
        elif tag == 'a':
            if self.current_link and self.current_link['href']:
                text = self.current_link['text'].strip()
                href = self.current_link['href']
                if text:
                    self.result.append(f'[{text}]({href})')
                else:
                    self.result.append(f'<{href}>')
            self.current_link = None
        elif tag == 'li':
            self.result.append('\n')
        # elif tag == 'p':
        #     不自动添加换行，让内容自然流动

    def handle_data(self, data):
        if self.in_script or not self.capture:
            return

        # 如果在链接中，记录文本
        if self.current_link is not None:
            self.current_link['text'] += data
            return

        # 清理数据但保留必要空格
        data = data.strip()
        if data:
            # 避免连续空格
            if self.result and self.result[-1] and not self.result[-1][-1] in [' ', '\n', '`', '_', '*']:
                self.result.append(' ')
            self.result.append(data)

    def get_markdown(self):
        """获取转换后的Markdown文本"""
        text = ''.join(self.result)

        # 后处理：清理多余的空行
        text = re.sub(r'\n{4,}', '\n\n\n', text)
        text = re.sub(r'\n{3}', '\n\n', text)

        # 处理HTML实体
        text = html.unescape(text)

        # 修复一些常见的格式问题
        # 修复列表项之间没有换行的问题
        text = re.sub(r'\. (\d+\. )', '.\n\\1', text)

        # 修复标题后的多余空格
        text = re.sub(r'^(#{1,4}) +(.+)$', r'\1 \2', text, flags=re.MULTILINE)

        # 移除行首尾空白
        lines = [line.rstrip() for line in text.split('\n')]
        text = '\n'.join(lines)

        return text.strip()


def convert_html_to_md(html_file, md_file):
    """转换HTML文件到Markdown"""
    print(f"🔄 转换中: {html_file}")

    with open(html_file, 'r', encoding='utf-8') as f:
        html_content = f.read()

    parser = AnthropicHTMLParser()
    parser.feed(html_content)

    markdown = parser.get_markdown()

    with open(md_file, 'w', encoding='utf-8') as f:
        f.write(markdown)

    print(f"✅ 完成: {md_file}")
    print(f"📊 生成了 {len(markdown)} 字符的Markdown内容")

    return markdown


if __name__ == '__main__':
    import sys

    if len(sys.argv) < 2:
        print("用法: python html_to_md.py <html_file> [md_file]")
        sys.exit(1)

    html_file = sys.argv[1]

    if len(sys.argv) >= 3:
        md_file = sys.argv[2]
    else:
        md_file = html_file.replace('.html', '.md')

    convert_html_to_md(html_file, md_file)
