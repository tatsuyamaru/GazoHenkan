# ガゾーヘンカン (GazoHenkan) - Claude引き継ぎ用ドキュメント

## プロジェクト概要
ガゾーヘンカン（GazoHenkan）は、JPG/PNGをAVIF形式に変換するWindows 11向けオフラインデスクトップアプリケーションです。将来的にWebP、HEIF、JPEG XLなど他の画像形式への拡張も視野に入れています。

## 開発環境
- **言語**: Python 3.11
- **主要ライブラリ**:
  - `Pillow`: 画像処理（AVIF変換含む）
  - `pillow-avif-plugin`: PillowのAVIFサポート
  - `Tkinter`: GUIフレームワーク
  - `tkinterdnd2`: ドラッグ＆ドロップ機能
  - `tomli`, `tomli-w`: TOML形式での設定保存・読み込み
  - `PyInstaller`: アプリケーションのEXE化
- **動作環境**: Windows 11 (22H2以降)、完全オフライン動作

## フォルダ構成
```
GazoHenkan/
├── src/
│   ├── __main__.py  # アプリケーションのエントリーポイント
│   ├── gui.py       # GUI関連のコード（Tkinter, tkinterdnd2）
│   ├── converter.py # 画像変換処理のロジック（Pillow）
│   └── utils.py     # ユーティリティ関数（設定の保存・読み込み）
├── assets/          # アプリアイコンなどのリソース
│   └── icon.ico     # (未作成)
├── dist/            # PyInstallerによるEXEファイルの出力先
│   └── GazoHenkan/  # --onedir モードで生成されるフォルダ
│       └── GazoHenkan.exe
├── output/          # 変換後の画像のデフォルト出力先
├── README.md        # プロジェクトの概要と使い方
├── requirements.txt # 必要なPythonライブラリのリスト
├── config.toml      # アプリケーションの設定ファイル（品質、出力先など）
├── Gemini.md        # Gemini CLIでの開発履歴・概要
├── 構想.md          # 初期企画・仕様書
└── CLAUDE.md        # このファイル（Claude引き継ぎ用）
```

## 実装済み機能
- ✅ **基本的なGUI**: Tkinterによるウィンドウ、ロゴ表示
- ✅ **ドラッグ＆ドロップ**: JPG/PNGファイルのリストボックスへの追加、非対応形式のエラー表示
- ✅ **品質設定**: 品質スライダー (10-100, デフォルト80)
- ✅ **ロスレス変換**: ロスレス/ロッシー切り替えチェックボックス
- ✅ **出力フォルダ選択**: `output`フォルダをデフォルトとし、ユーザーが変更可能
- ✅ **画像変換**: リスト内のJPG/PNGファイルをAVIFに変換（`converter.py`）
- ✅ **進捗表示**: プログレスバーとステータスラベルによる変換進捗の表示
- ✅ **設定の保存と読み込み**: TOML形式 (`config.toml`) で品質、ロスレス設定、出力フォルダを保存・自動読み込み
- ✅ **プレビュー機能**: 選択したファイルの変換前後の画像、ファイルサイズ、圧縮率を別ウィンドウで表示
- ✅ **EXE化**: PyInstallerによる実行可能ファイル (`dist/GazoHenkan/GazoHenkan.exe`) の生成（`--onedir`モード）

## 最近の修正（2025-07-13）
- ✅ **変換エラーの修正**: `converter.py`の`convert_to_avif`関数の引数を修正（output_dir → output_path）
- ✅ **エラーハンドリング強化**: AVIF形式サポートの確認とデバッグログの追加
- ✅ **メモリリーク対策**: 画像処理後の`img.close()`呼び出しを追加

## 未実装・検討事項
- ⏳ **アイコンの追加**: アプリケーションアイコン (`assets/icon.ico`) の作成とEXEへの組み込み
- ⏳ **バッチ処理の強化**: フォルダ選択による一括変換機能の改善
- ⏳ **予想ファイルサイズ表示**: 変換前のファイルサイズ推定機能
- ⏳ **多言語対応**: 日本語/英語UI切り替え機能の本格実装
- ⏳ **ログ機能**: 変換履歴のファイルへの保存
- ⚠️ **pillow-avif-plugin依存**: AVIFサポートには`pip install pillow-avif-plugin`が必要

## アプリケーションの実行
```bash
# 開発モードで実行
python -m src

# EXE化
pyinstaller --name GazoHenkan --onedir --windowed src/__main__.py
```

## 主要ファイルの役割
- `src/__main__.py`: アプリケーションのエントリーポイント
- `src/gui.py`: GUI関連のコード（Tkinter, tkinterdnd2）
- `src/converter.py`: 画像変換処理のロジック（Pillow）
- `src/utils.py`: ユーティリティ関数（設定の保存・読み込み）
- `config.toml`: アプリケーションの設定ファイル（品質、出力先など）

## 開発時の注意点
- Windows 11 (22H2以降) での動作を想定
- 完全オフライン動作を維持
- 初心者からプロまで使いやすいUIを心がける
- MITライセンスでの公開予定
- 最大500ファイルまでの処理を想定
- メモリ効率を考慮した画像処理（`img.close()`の適切な実行）

## テスト方法
1. JPG/PNGファイルをドラッグ&ドロップしてリストに追加されることを確認
2. 品質設定を変更してAVIF変換が正しく動作することを確認
3. プレビュー機能で変換前後のファイルサイズが表示されることを確認
4. 設定が `config.toml` に正しく保存・読み込まれることを確認

## 今後の開発方針
1. 基本機能の安定化とバグ修正
2. パフォーマンス向上（大量ファイル処理時）
3. 他の画像形式（WebP、HEIF、JPEG XL）への拡張
4. UIの改善とユーザビリティ向上
5. 配布用パッケージの整備