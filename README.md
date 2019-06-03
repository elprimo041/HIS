# HIS
Human Information Science

ファイル構成
|---body.py		    …計測を行うプログラム群を制御し結果を記録する
|---tests.py		…計測を行う
|---menu.py		    …メニュー画面を表示する
|---evaluate.py		…計測結果を評価する
|
|---outlier.py		…実験結果から外れ値を除去する
|---chi2_test.py	…χ^2検定を行う
|
|---result		    …測定結果を保存する
|   |---row_data	…生データを保存する
|   |---data_clean	…外れ値が除去されたデータを保存する
|
|---music		    …測定中に再生する音声ファイルを保存する
|   |---mp3 files


必要なモジュール等
python(３系にて作成．２系では動作未確認)
psychopy
pygame

測定方法
body.pyを実行する
出力はresult/row_data/に保存される
追加で実験する場合以前の実行結果は消去されず、以前の実験結果に追加する形で保存される

外れ値を除去する方法
outlier.pyを実行し、測定時に入力したIDを入力する
出力はresult/data_clean/に保存される

測定結果の独立性を検定する方法
chi2_test.pyを実行し、測定時に入力したIDを入力する
出力はresult/に保存される。