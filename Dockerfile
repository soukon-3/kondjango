# ベースイメージとしてPythonを使用
FROM python:3.11-slim

# 作業ディレクトリを作成
WORKDIR /app

# 必要なPythonパッケージをインストール
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# アプリケーションのソースコードをコピー
COPY . .

# サーバーを起動
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
