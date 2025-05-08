"""
サンプルモジュール
基本的な関数を提供します
"""


def add(a: int, b: int) -> int:
    """
    2つの数値を加算する関数

    Args:
        a: 1つ目の数値
        b: 2つ目の数値

    Returns:
        加算結果
    """
    return a + b


def multiply(a: int, b: int) -> int:
    """
    2つの数値を乗算する関数

    Args:
        a: 1つ目の数値
        b: 2つ目の数値

    Returns:
        乗算結果
    """
    return a * b


if __name__ == "__main__":
    # モジュールが直接実行された場合のサンプルコード
    print(f"5 + 3 = {add(5, 3)}")
    print(f"5 * 3 = {multiply(5, 3)}")
