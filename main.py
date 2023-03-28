import pykakasi
import time


class App:
    def __init__(self, file_path) -> None:
        self.kks = pykakasi.kakasi()
        self.alp = set(
            [
                *[chr(ord("a") + i) for i in range(26)],
                *[chr(ord("A") + i) for i in range(26)],
                " ",
            ]
        )
        self.ng = set()
        self.cnt = 0
        data = open(file_path, "r", encoding="utf-8")
        self.lines = data.read().splitlines()
        self.lines_romaji = []
        self.lines_original = []
        for line in self.lines:
            self.cnt += 1
            if self.cnt % 1000 == 0:
                print(self.cnt / 2216108)
            romaji = self.get_romaji(line)
            if not self.is_valid_text(romaji):
                continue
            self.lines_romaji.append(romaji)
            self.lines_original.append(line)
        data.close()
        self.write2file("./files/romaji.txt", self.lines_romaji)
        self.write2file("./files/original.txt", self.lines_original)
        self.write2file("./files/ng.txt", self.ng)

    def get_romaji(self, text):
        result = self.kks.convert(text)
        return " ".join([item["hepburn"] for item in result])

    def is_valid_text(self, text):
        # 龜みたいな，一般的でない漢字はローマ字に変換すると空文字になるため
        # 김윤석は日本語じゃないから，空白になる
        if text == "" or text[0] == " ":
            return False
        for t in text:
            if t not in self.alp:
                self.ng.add(t)
                return False
        return True

    def write2file(self, path, texts):
        with open(path, "w", encoding="utf-8") as f:
            f.write("\n".join(texts))


start = time.time()
file_path_test = "./first10.txt"
file_path = "./jawiki-latest-all-titles-in-ns0"
app = App(file_path=file_path)
print(app.lines_romaji)
print(set(app.ng))
end = time.time()
print(f"time:{end - start}")
