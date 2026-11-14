# KiCad 10 起動時に画面が出ない場合の回避策

この環境のKiCad 10.0.7 / wxWidgets 3.2.11 / glycin 2.2.2で確認した起動時の停止に対する、一時的な回避策です。

2026-10-08、回避策適用後に3件の該当警告を端末へ出力し、`snake_pcb — KiCad 10.0` のメインウィンドウが表示されることをX11のウィンドウ一覧で確認済みです。

## 通常のコマンドから起動

`~/.zshrc` に次のaliasを設定済みです。新しい端末で有効になります。今の端末でも、次のalias行を実行すれば有効になります。

```sh
alias kicad="$HOME/.local/bin/kicad-workaround"
kicad snake_pcb.kicad_pro
```

起動スクリプトは `~/.local/bin/kicad-workaround`、コンパイル済みライブラリとC++ソースは `~/.local/lib/kicad-startup-workaround/` に配置しています。引数と作業ディレクトリを引き継ぎ、`/usr/bin/kicad` を起動します。スクリプトの原本は `tools/kicad-workaround` です。wxWidgetsのABIが変わる更新後はライブラリの再コンパイルが必要になる場合があります。

## プロジェクト内の起動スクリプト

```sh
python3 open_kicad.py
```

`open_kicad.py` がローカルのC++ソースを `/tmp/snake-pcb-kicad-*` にコンパイルし、この起動のKiCadとその子プロセスだけへ `LD_PRELOAD` で適用します。必要なコマンドは `c++`、`wx-config`、`kicad` です。

## 診断結果

- `import pcbnew` だけでも `PROPERTY_ENUM(): No enum choices defined` の警告が再現し、その処理自体は正常終了。
- `snake_pcb.kicad_pro` のJSON解析、回路図のネットリスト出力、PCB読込に成功。
- 通常のGUI起動では、`_pcbnew.kiface` の動的ロード中に `wxOnAssert` → `ShowAssertDialog` → GTKアイコン読込 → `gly_loader_load` へ入り、画面表示前に停止。
- 同時にglycinのワーカースレッドが `__cxa_thread_atexit_impl` のmutex取得で停止。動的ローダのロックと画像読込の待ち合わせによるデッドロックと判断。

## 回避する範囲

`property.h` / `PROPERTY_ENUM` / `m_choices.GetCount() > 0` / `No enum choices defined` の4文字列がすべて一致する警告だけ、ダイアログ表示を省略します。元の端末への警告出力は残し、その他のアサーションは通常のwxWidgets処理に渡します。

これは列挙型登録の不具合そのものを修正するものではありません。システムにインストールされたKiCadやwxWidgets、画像ローダ、プロジェクトの設計データは書き換えません。
将来のKiCad更新後は `/usr/bin/kicad snake_pcb.kicad_pro` で回避策なしの起動を確認できます。回避策が不要になったら、`~/.zshrc` の `BEGIN KiCad startup workaround` から `END KiCad startup workaround` までを削除し、現在の端末で `unalias kicad` を実行してください。

参考: [KiCad 10で同じ警告が出る報告](https://gitlab.com/kicad/code/kicad/-/work_items/23797)、[KiKitでの警告再現報告](https://github.com/yaqwsx/KiKit/issues/912)。今回のGUI停止箇所は、このマシンのGDBバックトレースで確認したものです。
