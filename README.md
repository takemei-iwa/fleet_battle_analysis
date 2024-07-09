# Fleet_Battle_Analysis
Fleet_Battle_Analysisは[Fleet Battle](https://play.google.com/store/apps/details?id=de.smuttlewerk.fleetbattle&hl=ja)
というモバイルゲームでの対戦結果の画像を自動で全て読み取り、統計を取ってヒートマップで見やすく表示するライブラリです。

## Getting Start
### 画像の準備
Fleet_Battleの対戦結果の相手の陣地がわかる画面でスクショをして、その画像を`img`ディレクトリに入れてください。例として10個の画像が入っています。

<img src="https://github.com/takemei-iwa/fleet_battle_analysis/blob/main/img/007.jpg" width="320px">

### 相手の陣地の画像を切り抜く
```
$ python allimg2get_outline.py 
```
`mask`ディレクトリに切り抜かれた画像が入ります。

![切り抜かれた画像](https://github.com/takemei-iwa/fleet_battle_analysis/blob/main/mask/007.jpg)

### 相手の陣地の画像から船と白いマークの座標を取得
```
$ python allimg2get_ship_mask.py
```
`mask`ディレクトリの画像から`ship_mask`ディレクトリに船と白いマーク
![船と白いマークのマスク画像](https://github.com/takemei-iwa/fleet_battle_analysis/blob/main/wh_template.jpg)
のマスク画像が入ります。
この画像から`ship_point`ディレクトリに、左上を原点としてマス目を座標と見た時の、船と白いマークの座標がjsonファイルとして入ります。
`mask`ディレクトリの画像から白いマークを検出し、白いマークの座標がjsonファイルとして`white_mark_point`ディレクトリに入ります。

下が`ship_point`ディレクトリに入るマスク画像です。

![船と白いマークのマスク画像](https://github.com/takemei-iwa/fleet_battle_analysis/blob/main/ship_mask/007.jpg)


下は`ship_point`ディレクトリのjsonファイルの例です。
```
[
    {
        "x": 0,
        "y": 8
    },
...
    {
        "x": 7,
        "y": 1
    }
]
```
下は`white_mark_point`ディレクトリのjsonファイルの例です。
```
[
    {
        "x": 6,
        "y": 7
    }
]
```
### 船の座標だけを取得
```
$ python concat_ship_whmark.py 
```
`ship_point`ディレクトリと`white_mark_point`ディレクトリのファイルから、白いマークの座標を取り除いて、
船の座標だけを抽出し、Fleet_Battle_Analysisディレクトリ直下に`whole_data.json`として出力されます。


### 対戦結果から統計をとったヒートマップ画像を取得
```
$ python display_data.py
```
`whole_data.json`から相手が各マスに船を置いた回数をそれぞれ記録し、ヒートマップ画像としてsum_data_canvas.jpgに出力されます。

<img src="https://github.com/takemei-iwa/fleet_battle_analysis/blob/main/sum_data_canvas.jpg" width="320px">
