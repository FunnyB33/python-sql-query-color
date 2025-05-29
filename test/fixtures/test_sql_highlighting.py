"""
SQLハイライトテスト用のPythonファイル
"""

def test_single_line_query():
    # 1. 1行のSQLクエリのテスト
    query1 = """SELECT * FROM users WHERE id = 1"""

    # 2. WHERE句を含むクエリ
    query2 = """
    SELECT name, email
    FROM users
    WHERE status = 'active' AND created_at > '2023-01-01'"""

def test_multi_line_query():
    # 3. 複数行にまたがるSQLクエリのテスト
    query = """
        SELECT
            u.id,
            u.name,
            u.email,
            COUNT(o.id) as order_count
        FROM
            users u
        LEFT JOIN
            orders o ON u.id = o.user_id
        WHERE
            u.status = 'active'
        GROUP BY
            u.id, u.name, u.email
        HAVING
            COUNT(o.id) > 0
        ORDER BY
            order_count DESC
        LIMIT 10
    """

def test_python_strings():
    # 4. Pythonのf文字列内でのSQL
    user_id = 123
    query = f"""
    SELECT *
    FROM users
    WHERE id = {user_id}
    """

    # 5. 通常のPython文字列内でのSQL
    update_query = ("UPDATE products "
                   "SET price = price * 1.1 "
                   "WHERE category = 'electronics'")

def test_sql_keywords():
    # 6. 様々なSQLキーワードのテスト
    keywords = [
        "SELECT", "FROM", "WHERE", "GROUP BY", "ORDER BY", "HAVING",
        "JOIN", "INNER JOIN", "LEFT JOIN", "RIGHT JOIN", "FULL JOIN",
        "UNION", "UNION ALL", "EXCEPT", "INTERSECT",
        "INSERT INTO", "UPDATE", "DELETE FROM", "CREATE TABLE",
        "ALTER TABLE", "DROP TABLE", "INDEX", "VIEW", "TRIGGER"
    ]

    # 7. 関数のテスト
    functions = [
        "COUNT(*)", "SUM(amount)", "AVG(price)", "MAX(date)", "MIN(date)",
        "UPPER(name)", "LOWER(name)", "SUBSTR(name, 1, 3)", "COALESCE(name, 'N/A')"
    ]

# 8. サブクエリのテスト
def test_subqueries():
    query = """
    SELECT
        u.name,
        (SELECT COUNT(*) FROM orders o WHERE o.user_id = u.id) as order_count
    FROM
        users u
    WHERE
        u.id IN (SELECT user_id FROM premium_users WHERE status = 'active')
    """

def test_multiline_sql():
    # 複数行のSQLクエリ
    query = """
    SELECT
        u.id,
        u.name,
        u.email
    FROM
        users u
    WHERE
        u.status = 'active'
    """

    # f文字列を使用した複数行のSQLクエリ
    status = 'active'
    query_fstring = f"""
    SELECT
        u.id,
        u.name,
        u.email
    FROM
        users u
    WHERE
        u.status = '{status}'
    """