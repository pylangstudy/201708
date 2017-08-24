# [6.3.5. difflib のコマンドラインインタフェース](https://docs.python.jp/3/library/difflib.html#a-command-line-interface-to-difflib)

< [6.3. difflib — 差分の計算を助ける](https://docs.python.jp/3/library/difflib.html#module-difflib) < [6. テキスト処理サービス](https://docs.python.jp/3/library/text.html#text-processing-services) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

> この例は、 difflib を使って diff に似たユーティリティーを作成する方法を示します。これは、 Python のソース配布物にも、 Tools/scripts/diff.py として含まれています。

## 起動してみた

コードはPython文書そのままなので略。

```python
$ python 0.py 
usage: 0.py [-h] [-c] [-u] [-m] [-n] [-l LINES] fromfile tofile
0.py: error: the following arguments are required: fromfile, tofile
```
```python
$ python 0.py -h
usage: 0.py [-h] [-c] [-u] [-m] [-n] [-l LINES] fromfile tofile

positional arguments:
  fromfile
  tofile

optional arguments:
  -h, --help            show this help message and exit
  -c                    Produce a context format diff (default)
  -u                    Produce a unified format diff
  -m                    Produce HTML side by side diff (can use -c and -l in
                        conjunction)
  -n                    Produce a ndiff format diff
  -l LINES, --lines LINES
                        Set number of context lines (default 3)
```

## 適当なテキストファイルを作って与えてみた

```sh
$ python 0.py a.txt b.txt 
*** a.txt	2017-08-24T09:31:42.439977+09:00
--- b.txt	2017-08-24T09:31:51.356021+09:00
***************
*** 1,3 ****
  abc
! def
  
--- 1,3 ----
  abc
! dee
```

### `-c` context format diff

```sh
$ python 0.py -c a.txt b.txt 
*** a.txt	2017-08-24T09:31:42.439977+09:00
--- b.txt	2017-08-24T09:31:51.356021+09:00
***************
*** 1,3 ****
  abc
! def
  
--- 1,3 ----
  abc
! dee
```

### `-u` unified format diff

```sh
$ python 0.py -u a.txt b.txt 
--- a.txt	2017-08-24T09:31:42.439977+09:00
+++ b.txt	2017-08-24T09:31:51.356021+09:00
@@ -1,3 +1,3 @@
 abc
-def
+dee
```

### `-n` ndiff format diff

```sh
$ python 0.py -n a.txt b.txt 
  abc
- def
?   ^
+ dee
?   ^
```

### `-m` HTML side by side diff

```sh
$ python 0.py -m a.txt b.txt 

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
          "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<html>

<head>
    <meta http-equiv="Content-Type"
          content="text/html; charset=utf-8" />
    <title></title>
    <style type="text/css">
        table.diff {font-family:Courier; border:medium;}
        .diff_header {background-color:#e0e0e0}
        td.diff_header {text-align:right}
        .diff_next {background-color:#c0c0c0}
        .diff_add {background-color:#aaffaa}
        .diff_chg {background-color:#ffff77}
        .diff_sub {background-color:#ffaaaa}
    </style>
</head>

<body>
    
    <table class="diff" id="difflib_chg_to0__top"
           cellspacing="0" cellpadding="0" rules="groups" >
        <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup>
        <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup>
        <thead><tr><th class="diff_next"><br /></th><th colspan="2" class="diff_header">a.txt</th><th class="diff_next"><br /></th><th colspan="2" class="diff_header">b.txt</th></tr></thead>
        <tbody>
            <tr><td class="diff_next" id="difflib_chg_to0__0"><a href="#difflib_chg_to0__0">f</a></td><td class="diff_header" id="from0_1">1</td><td nowrap="nowrap">abc</td><td class="diff_next"><a href="#difflib_chg_to0__0">f</a></td><td class="diff_header" id="to0_1">1</td><td nowrap="nowrap">abc</td></tr>
            <tr><td class="diff_next"><a href="#difflib_chg_to0__top">t</a></td><td class="diff_header" id="from0_2">2</td><td nowrap="nowrap"><span class="diff_sub">def</span></td><td class="diff_next"><a href="#difflib_chg_to0__top">t</a></td><td class="diff_header" id="to0_2">2</td><td nowrap="nowrap"><span class="diff_add">dee</span></td></tr>
            <tr><td class="diff_next"></td><td class="diff_header" id="from0_3">3</td><td nowrap="nowrap"></td><td class="diff_next"></td><td class="diff_header" id="to0_3">3</td><td nowrap="nowrap"></td></tr>
        </tbody>
    </table>
    <table class="diff" summary="Legends">
        <tr> <th colspan="2"> Legends </th> </tr>
        <tr> <td> <table border="" summary="Colors">
                      <tr><th> Colors </th> </tr>
                      <tr><td class="diff_add">&nbsp;Added&nbsp;</td></tr>
                      <tr><td class="diff_chg">Changed</td> </tr>
                      <tr><td class="diff_sub">Deleted</td> </tr>
                  </table></td>
             <td> <table border="" summary="Links">
                      <tr><th colspan="2"> Links </th> </tr>
                      <tr><td>(f)irst change</td> </tr>
                      <tr><td>(n)ext change</td> </tr>
                      <tr><td>(t)op</td> </tr>
                  </table></td> </tr>
    </table>
</body>

</html>
```

