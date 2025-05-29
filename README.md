# python-sql-query-color
Identify SQL queries in python files and color them

## 機能
Pythonファイルに書かれているSQLのquery文を
<br>
`""" """`もしくは`''' '''`の中に書いたときに、
- クエリの予約語
- クエリのテーブル名
- テーブルなどのエイリアス
- 関数名
- サブクエリ
- `%()s`で書いてある変数名

を色付けできるような拡張機能を作りたい。