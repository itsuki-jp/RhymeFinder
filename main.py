import pykakasi
import time
import bisect


class App:
    def __init__(self, test=False) -> None:
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
        self.vowels = []
        file_path_test = "./first10.txt"
        file_path = "./word_file"
        file_path = file_path_test if test else file_path
        data = open(file_path, "r", encoding="utf-8")
        self.lines = data.read().splitlines()
        self.lines_romaji = []
        self.lines_original = []
        for line in self.lines:
            self.cnt += 1
            if self.cnt % 1000 == 0:
                print(self.cnt / len(self.lines))
            romaji = self.get_romaji(line)
            if not self.is_valid_text(romaji, line):
                continue
            self.lines_romaji.append(romaji)
            self.lines_original.append(line)
            self.vowels.append(self.get_vowels(romaji))
        data.close()
        zip_lists = zip(self.vowels, self.lines_original)
        zip_sorted = sorted(zip_lists)
        self.vowels, self.lines_original = zip(*zip_sorted)
        if not test:
            self.write2file("./files/romaji.txt", self.lines_romaji)
            self.write2file("./files/ng.txt", self.ng)
            self.write2file("./files/rhyme.txt", self.vowels)
            self.write2file("./files/original.txt", self.lines_original)
        else:
            self.write2file("./files/romaji_test.txt", self.lines_romaji)
            self.write2file("./files/ng_test.txt", self.ng)
            self.write2file("./files/rhyme_test.txt", self.vowels)
            self.write2file("./files/original_test.txt", self.lines_original)

    def get_romaji(self, text):
        result = self.kks.convert(text)
        return " ".join([item["hepburn"] for item in result])

    def is_valid_text(self, romaji, original):
        # 龜みたいな，一般的でない漢字はローマ字に変換すると空文字になるため
        # 김윤석は日本語じゃないから，空白になる
        if romaji == "" or romaji[0] == " ":
            return False
        for t in original:
            if t in self.alp:
                return False
        for t in romaji:
            if t not in self.alp:
                self.ng.add(t)
                return False
        return True

    def write2file(self, path, texts):
        with open(path, "w", encoding="utf-8") as f:
            f.write("\n".join(texts))

    def get_vowels(self, text):
        vowels = set(["a", "i", "u", "e", "o", "A", "I", "U", "E", "O"])
        res = []

        for i in range(len(text)):
            t = text[i]
            if t in vowels:
                res.append(t)
            elif (t == "n" or t == "N") and (
                (
                    i != (len(text) - 1)
                    and (text[i + 1] not in vowels or text[i + 1] == "n")
                    or (i == (len(text) - 1) and t == "n")
                )
            ):
                res.append("n")
        return "".join(res)

    def search(self, text):
        left = bisect.bisect_left(self.vowels, text)
        right = bisect.bisect_right(self.vowels, text)
        return self.lines_original[left], self.lines_original[right]


start = time.time()
app = App()
# print(app.lines_romaji)
# print(set(app.ng))
end = time.time()
print(f"time:{end - start}")
print(app.search("iui"))
