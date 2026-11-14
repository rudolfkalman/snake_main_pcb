# SN74LVC1G74 KiCadライブラリ

プロジェクトのシンボル／フットプリントライブラリに登録済みです。
回路図エディタの「シンボルを配置」で `SN74LVC1G74` を検索し、
実際に使用するパッケージに対応するシンボルを選択してください。
各シンボルには対応するローカルフットプリントを設定しています。

| シンボル | 注文型番の例 | フットプリント | ピッチ |
| --- | --- | --- | --- |
| `SN74LVC1G74:SN74LVC1G74DCU` | SN74LVC1G74DCUR / DCUT | `SN74LVC1G74:VSSOP-8_2.3x2mm_P0.5mm` | 0.5 mm |
| `SN74LVC1G74:SN74LVC1G74DCT` | SN74LVC1G74DCTR / DCTT | `SN74LVC1G74:SSOP-8_2.95x2.8mm_P0.65mm` | 0.65 mm |

末尾のR/Tは梱包区分です。DCUとDCTは同じピン配置ですが、実装寸法が異なります。
DQE・RSEパッケージ用は含みません。

## ピン配置（DCU / DCT共通）

| ピン | 信号 | 種別 |
| --- | --- | --- |
| 1 | CLK | 入力、立ち上がりエッジ |
| 2 | D | 入力 |
| 3 | /Q | 反転出力 |
| 4 | GND | 電源入力 |
| 5 | Q | 出力 |
| 6 | /CLR | 非同期クリア入力、Low有効 |
| 7 | /PRE | 非同期プリセット入力、Low有効 |
| 8 | VCC | 電源入力 |

## 出典

- [TI SN74LVC1G74データシート](https://www.ti.com/lit/ds/symlink/sn74lvc1g74.pdf):
  DCU/DCTのピン配置、信号の極性、パッケージ寸法。
- フットプリントは、この環境のKiCad標準ライブラリ
  `/usr/share/kicad/footprints/Package_SO.pretty/` から同名ファイルをそのままコピーしています。
  銅箔パッド、ソルダーマスク、ペースト、シルク、外形、コートヤードを含みます。
  [KiCadライブラリのライセンス](https://www.kicad.org/libraries/license/)
  （CC BY-SA 4.0、設計への利用に関する例外付き）が適用されます。
- 3Dモデル参照は標準の `${KICAD10_3DMODEL_DIR}/Package_SO.3dshapes/` を使用します。
  3D表示には対応するKiCad標準3Dモデルのインストールが必要です。
