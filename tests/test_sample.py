"""
サンプルモジュールのテスト
"""
import pytest
from src.sample import add, multiply


def test_add():
    """加算関数のテスト"""
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
    assert add(0, 0) == 0


def test_multiply():
    """乗算関数のテスト"""
    assert multiply(2, 3) == 6
    assert multiply(-2, 3) == -6
    assert multiply(0, 5) == 0
