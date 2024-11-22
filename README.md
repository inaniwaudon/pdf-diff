# pdf-diff

PDF の差分を画像比較するスクリプト．論文執筆に便利．

## 使い方

### 環境構築

```bash
brew install poppler
pip install -r requirements.txt
```

### 実行

```bash
python script.py <pdf1> <pdf2> <diff_dir>
```

diff_dir に存在しないディレクトリを指定した場合は自動生成される．
