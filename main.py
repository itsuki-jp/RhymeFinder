import pykakasi

kks = pykakasi.kakasi()
text = 'かな漢字'
result = kks.convert(text)
for item in result:
    print(f"romaji: '{item['hepburn']}'")
print("=============")
print(' '.join([item['hepburn'] for item in result]))