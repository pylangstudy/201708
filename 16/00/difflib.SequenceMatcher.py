#!python3.6
#http://blog.mudatobunka.org/entry/2016/05/08/154934
import difflib

str1 = "スパゲッティー"
str2 = "スパゲティ"
s = difflib.SequenceMatcher(None, str1, str2).ratio()
print(str1, "<~>", str2)
print("match ratio:", s, "\n")

# 半角と全角は0.0%になってしまう
strs = [
    "スパゲティ",
    "スパゲティー",
    "スパゲッティ",
    "スパゲッティー",
    u"ｽﾊﾟｹﾞﾃｨ",
    u"ｽﾊﾟｹﾞﾃｨ-",
    u"ｽﾊﾟｹﾞｯﾃｨ",
    u"ｽﾊﾟｹﾞｯﾃｨ-",
]
for (str1, str2) in [(str1, str2) for str1 in strs for str2 in strs if str1 < str2]:
    print(str1, "<~>", str2)
    s = difflib.SequenceMatcher(None, str1, str2).ratio()
    print("match ratio:", s)
print()

# 半角と全角を統一して比較する
import unicodedata
for (str1, str2) in [(str1, str2) for str1 in strs for str2 in strs if str1 < str2]:
    normalized_str1 = unicodedata.normalize('NFKC', str1)
    normalized_str2 = unicodedata.normalize('NFKC', str2)
    print(str1, "<~>", str2)
    s = difflib.SequenceMatcher(None, normalized_str1, normalized_str2).ratio()
    print("match ratio:", s)
print()
