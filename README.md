# ガゾーヘンカン (GazoHenkan) - Easy Image Converter

<div align="center">

![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)
![Platform](https://img.shields.io/badge/platform-Windows%2011-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Python](https://img.shields.io/badge/python-3.11-blue.svg)

**Windows 11向けオフライン画像変換アプリケーション**  
JPG/PNG を AVIF形式に簡単変換！

</div>

## 📖 概要

ガゾーヘンカン（GazoHenkan）は、JPG/PNGファイルをAVIF形式に変換するWindows 11向けオフラインデスクトップアプリケーションです。直感的なGUIで初心者からプロまで簡単に使用できます。

### 🚀 主な機能

- ✅ **ドラッグ&ドロップ対応** - ファイルを簡単に追加
- ✅ **品質調整** - 10-100の範囲で品質を設定
- ✅ **ロスレス変換** - 品質を保持したファイル変換
- ✅ **プレビュー機能** - 変換前後の比較表示
- ✅ **バッチ処理** - 複数ファイルの一括変換
- ✅ **設定保存** - ユーザー設定の自動保存
- ✅ **EXE配布** - インストール不要

## 📋 システム要件

- **OS**: Windows 11 (22H2以降)
- **メモリ**: 4GB以上
- **ストレージ**: 100MB以上の空き容量
- **CPU**: Core i5相当以上推奨

## 📦 インストール・使用方法

### 🎯 EXEファイルで使用

1. [Releases](https://github.com/tatsuyamaru/GazoHenkan/releases)から最新版をダウンロード
2. `GazoHenkan.exe`をダブルクリック
3. インストール不要で即座に使用開始

### 🔧 Python環境で使用

```bash
# リポジトリをクローン
git clone https://github.com/tatsuyamaru/GazoHenkan.git
cd GazoHenkan

# 依存関係をインストール
pip install -r requirements.txt

# アプリケーションを実行
python -m src
```

## 🎯 使い方

### 基本的な流れ

1. **アプリケーションを起動**
2. **JPG/PNGファイルをドラッグ&ドロップ**でリストに追加
3. **品質設定**を調整（デフォルト: 80）
4. **出力フォルダ**を選択（デフォルト: `output`フォルダ）
5. **変換開始**ボタンをクリック
6. 変換完了まで待機

### 🛠️ 詳細設定

- **品質設定**: 10 から 100 まで調整可能
- **ロスレス**: チェックで画質劣化なしの変換
- **プレビュー**: 変換前後のファイルサイズ比較
- **バッチ処理**: 最大500ファイルまで対応

## 🔧 開発・技術情報

### 主要ライブラリ

- **Pillow** - 画像処理エンジン
- **pillow-avif-plugin** - AVIFフォーマット対応
- **Tkinter** - GUIフレームワーク
- **tkinterdnd2** - ドラッグ&ドロップ機能
- **tomli/tomli-w** - 設定ファイル管理

### プロジェクト構成

```
GazoHenkan/
├── src/              # ソースコード
│   ├── __main__.py   # エントリーポイント
│   ├── gui.py        # GUI関連コード
│   ├── converter.py  # 画像変換ロジック
│   └── utils.py      # ユーティリティ関数
├── assets/           # リソースファイル
├── output/           # 変換後画像の出力先
├── config.toml       # 設定ファイル
└── README.md         # このファイル
```

## ❓ よくある質問

### トラブルシューティング

**Q: 変換が失敗する**
- 対応ファイル形式（JPG/PNG）か確認
- ファイルが破損していないか確認
- 出力フォルダに書き込み権限があるか確認

**Q: EXEファイルが起動しない**
- Windows Defenderの除外設定を確認
- 管理者権限で実行してみる

**Q: 変換速度が遅い**
- ファイルサイズを確認
- 品質設定を下げる

## 🛣️ 今後の予定

- ✅ **WebP、HEIF、JPEG XL** 対応
- 🔄 **多言語UI** 日本語/英語切り替え
- ✅ **ログ機能** 変換履歴保存
- 🔄 **UI改善** より使いやすいインターフェース
- ✅ **配布パッケージ** 改善

## 🤝 コントリビューション

プルリクエストやバグレポートを歓迎します！

1. フォーク
2. フィーチャーブランチを作成 (`git checkout -b feature/amazing-feature`)
3. 変更をコミット (`git commit -m 'Add amazing feature'`)
4. ブランチにプッシュ (`git push origin feature/amazing-feature`)
5. プルリクエストを作成

## 📄 ライセンス

このプロジェクトは [MIT License](LICENSE) の下で公開されています。

## 📞 サポート・お問い合わせ

- **GitHub Issues**: [問題の報告](https://github.com/tatsuyamaru/GazoHenkan/issues)
- **GitHub Repository**: https://github.com/tatsuyamaru/GazoHenkan

---

<div align="center">

**🇯🇵 日本製の画像変換ツール**

Made with ❤️ in Japan

</div>