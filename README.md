# Python DevContainerプロジェクト

このプロジェクトは、VS Code DevContainerを使用したPython開発環境のテンプレートです。

## 機能

- Python 3.10開発環境
- コード品質ツール（black, flake8, mypy, pylint）
- テスト環境（pytest）
- 基本的なデータ処理ライブラリ（numpy, pandas, matplotlib）

## 使用方法

### 前提条件

- [Visual Studio Code](https://code.visualstudio.com/)
- [Docker](https://www.docker.com/)
- [Remote - Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) VS Code拡張機能

### 開発環境の起動

1. このリポジトリをクローンします
2. VS Codeでプロジェクトフォルダーを開きます
3. VS Codeが`.devcontainer`フォルダーを検出し、コンテナーで開くかどうか尋ねるプロンプトが表示されます
4. 「Reopen in Container」を選択します
5. コンテナーのビルドと起動が完了するまで待ちます

または、VS Codeのコマンドパレット（`F1`キー）を開き、「Remote-Containers: Open Folder in Container...」を選択してプロジェクトフォルダーを選択することもできます。

### プロジェクト構造

```
.
├── .devcontainer/     # DevContainer設定
├── src/               # ソースコード
├── tests/             # テストコード
├── requirements.txt   # 依存パッケージ
└── README.md          # このファイル
```

### テストの実行

コンテナー内のターミナルで以下のコマンドを実行します：

```bash
pytest
```

### コード品質チェック

コンテナー内のターミナルで以下のコマンドを実行します：

```bash
# コードフォーマット
black src tests

# 静的解析
flake8 src tests
mypy src tests
