"""
处理z哥录屏的字幕文件
去掉字幕分时, 整理成逐字稿
"""

import os


def read(file):
    with open(file, "r") as f:
        lines = f.readlines()
        return lines


def write(lines, file):
    with open(file, "w") as f:
        f.writelines(lines)


if __name__ == "__main__":
    dirname = ""  # 替换目录名
    # 按顺序
    files = ["824第一部分_文稿.srt", "824第二部分_文稿.srt", "824第三部分_文稿.srt"]
    content = []
    for file in files:
        if dirname:
            file = os.path.join(dirname, file)
        for line in read(file):
            if not (line.startswith("00") or line[:5].strip().isdigit()):
                content.append(line)
    write(content, "824.txt")
