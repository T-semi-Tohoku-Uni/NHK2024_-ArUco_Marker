# NHK2024_ArUco_Marker
マーカー使った簡易的な位置推定のプログラム。R2

## 実行方法
リポジトリのclone
```
git clone git@github.com:T-semi-Tohoku-Uni/NHK2024_ArUco_Marker.git
cd NHK2024_ArUco_Marker
```
仮想環境の作成. 必要なライブラリのインストール. （初回時）
```
python -m venv env
. ./env/bin/activate
pip install -r requirements.txt
```
仮想環境の起動. （2回目以降）
```
. ./env/bin/activate
```
プログラムのディレクトリに移動する
```
cd src
```

### 生成済みのマーカーの出力
```
python generate.py
```
`src/Marker`ディレクトリにマーカーが作成される. 

### カメラの動画（画像）を真上から見た画像に変換. 奇跡もついでに出力（したい）
```
python main.py
```

## 実行環境
python : 3.11.6

## 参考
https://qiita.com/code0327/items/c6e468da7007734c897f