# AS5600 / STS3215 接続用ライブラリ

プロジェクトのシンボル・フットプリントライブラリに登録済みです。
KiCadでプロジェクトを開き直し、シンボル追加で `AS5600_4Pin` または `STS3215` を検索します。

## AS5600

- シンボル: `AS5600:AS5600_4Pin`
- フットプリント: `AS5600:PinHeader_1x04_P2.54mm_Vertical`
- 1列4ピン、2.54 mmピッチ、穴径1.0 mmの汎用THTピンヘッダです。
- 外部のAS5600を配線するための4端子表現です。ICの8端子パッケージや特定モジュールの実装外形を表していません。

| パッド | 信号 | 電気種別 |
| --- | --- | --- |
| 1 | VCC | 電源入力 |
| 2 | GND | 電源入力 |
| 3 | SDA | 双方向 |
| 4 | SCL | 入力 |

フットプリントの角形1番パッドを起点に、上面視で `(0,0)` → `(0,2.54)` → `(0,5.08)` → `(0,7.62)` と並びます。
DIRは基板側コネクタから外しました。使用するAS5600モジュール上でDIRを確定したレベルに接続してください。
VCCは外部センサ側の電源端子を意味し、IC単体のVDD5V/VDD3V3を統合配線する指示ではありません。

端子機能の資料: [ams OSRAM AS5600データシート](https://look.ams-osram.com/m/7059eac7531a86fd/original/AS5600-DS000365.pdf)。

## STS3215

- シンボル: `STS3215:STS3215`（基板上の接続コネクタとして参照名はJ）
- フットプリント: `STS3215:Molex_SPOX_5267-03A_1x03_P2.50mm_Vertical`
- ピン名はユーザー指定の `V++`, `GND`, `SIGNAL`。
- ピン番号はFEETECHの仕様書4ページ、6-7「Connector and Cable」に従います。

| パッド | シンボルの信号 | FEETECH仕様書の表記 |
| --- | --- | --- |
| 1 | GND | GND |
| 2 | V++ | Vcc |
| 3 | SIGNAL | Signal/TTL |

SIGNALは半二重TTLシリアル通信の双方向端子です。
基板上面から見たフットプリント座標は、1番GND=`(0,0)`、2番V++=`(2.50,0)`、3番SIGNAL=`(5.00,0)`。
差し込み面や配線側から見る場合は左右が変わるため、ケーブルの導通と1番パッドの向きを照合してください。

### コネクタ調査結果

FEETECHメーカー仕様書の型式は **5264-3P** です。
Molex Mini-SPOXで対応する部品は以下です。

| 部位 | 型式 | ピッチ |
| --- | --- | --- |
| ケーブル側ハウジング | 5264-03 / 50-37-5033（0050375033） | 2.50 mm |
| 基板側ストレートTHTヘッダ | 5267-03A / 22-03-5035（0022035035） | 2.50 mm |

今回割り当てたフットプリントは、純正Molex **22-03-5035** の寸法に対応するKiCad標準品です。穴径は0.85 mmです。
FEETECHの「5264-3P」という指定から選んだ相手側候補であり、手元のケーブルとの実機嵌合は未確認です。

WaveshareのFAQでは「5264/2.54 3P」と記載されていますが、純正Molexは2.50 mmです。
2.54 mm仕様の互換品を購入する場合は、その部品の寸法図に合わせてフットプリントを選んでください。
このライブラリのV++には固定電圧を指定していません。STS3215の電源仕様はサーボのバージョンに従います。

### 一次資料

- [FEETECH STS3215-C001仕様書](https://files.seeedstudio.com/products/Feetech/108090023_STS3215-C001_Datasheet.pdf): p.4 コネクタ型式・端子番号・半二重通信。
- [Molex 22-03-5035](https://www.molex.com/en-us/products/part-detail/0022035035): 基板側3極縦型THT、2.50 mmピッチ。
- [Molex 50-37-5033](https://www.molex.com/en-us/products/part-detail/0050375033): ケーブル側3極ハウジング。
- [Molex 5264シリーズ](https://www.molex.com/ja-jp/products/series-chart/5264): Mini-SPOXハウジングの型式一覧。
- [Waveshare ST3215 FAQ](https://www.waveshare.com/wiki/ST3215_Servo): 5264/2.54 3Pという販売元表記。

## フットプリントの出典

両フットプリントは、この環境にインストールされているKiCad公式ライブラリから無変更でコピーしました。

- `Connector_PinHeader_2.54mm.pretty/PinHeader_1x04_P2.54mm_Vertical.kicad_mod`
- `Connector_Molex.pretty/Molex_SPOX_5267-03A_1x03_P2.50mm_Vertical.kicad_mod`

原著作: KiCad Library Team / contributors。
ライセンスは[KiCadライブラリのライセンス](https://www.kicad.org/libraries/license/)（CC BY-SA 4.0、設計への利用に関する例外付き）に従います。
3Dモデル参照先はKiCad 10の標準ライブラリです。
