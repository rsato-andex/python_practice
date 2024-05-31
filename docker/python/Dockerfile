# ベースイメージとして python:3.12 を使用
FROM python:3.12

# 作業ディレクトリを /usr/src/app に設定
WORKDIR /usr/src/app

# 残りのアプリケーションコードをコンテナにコピー
COPY . .

# 依存関係をインストール --user 権限
RUN pip install -r docker/python/requirements.txt

RUN apt-get update && apt-get install -y \
    gcc \
    libmariadb-dev \
    curl && \
    curl -fsSL https://deb.nodesource.com/setup_16.x | bash - && \
    apt-get install -y nodejs && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# tailwindcssをインストール
RUN npm install -g tailwindcss

# wait-for-it.shをコピーして実行可能にする
COPY wait-for-it.sh /app/wait-for-it.sh
RUN chmod +x /app/wait-for-it.sh

# 環境変数を設定
ENV FLASK_APP=app/app.py
ENV FLASK_ENV=development

# ここにDocker起動時に起動するpythonファイルを書く(テーブルを作ったりする)
# CMD ["./wait-for-it.sh", "db:3306", "--", "python", "./make_table.py"]

