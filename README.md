# VRC Event Manager


VRC Event Managerは、Djangoで構築されたWebアプリケーションのバックエンドで、VRChatコミュニティ内でのイベントの作成、管理、告知を行います。

このシステムは、イベント登録、定期的なイベントの自動化、ソーシャルメディア連携（TwitterとDiscord）、Googleカレンダー同期などの機能を提供します。

## 機能

- ユーザー登録と認証
  - メールアドレスとパスワードによる認証
  - Googleアカウントでのログイン
- イベント管理
  - イベントの作成と管理
  - 各イベントに対してユーザーに役割（主催者とスタッフ）を割り当てる
  - 定期的なイベントの自動作成
  - **相談**:下記の機能はこの内容で良いのか
  - ユーザーはイベントリストを作成し、お気に入りのイベントを追跡
  - イベントリストは公開または非公開に設定
  - 他のユーザーはイベントリストを検索し、お気に入りのイベントを追跡
- ソーシャルメディア連携
  - TwitterとDiscordなどでのイベントの告知
  - 告知スケジュールと告知用テンプレートのカスタマイズ
  - **相談**:SNSが増えることを想定して設計するか、初めから特定のSNSに絞るか
- Googleカレンダー同期
  - イベントをGoogleカレンダーと自動同期
  - イベントの変更（作成、更新、削除）をGoogleカレンダーに反映
- 外部連携(API)
  - 条件を指定してイベント情報を取得できるAPIを公開
  - 技術学術系イベントまとめアセットなど外部サービスとの連携

#### 扱わないこと

- LT関係の機能は実装しない
- イベントの情報を作成、編集するAPIを公開するので各自で実装する

## 使用技術

- Django: バックエンド開発用のPythonWebフレームワーク
- Django REST Framework: Django用のAPI開発ツールキット
- MySQL: データ保存用のリレーショナルデータベース
- HTML/CSS/JavaScript: フロントエンド開発
- Google Calendar API: イベント同期用のGoogleカレンダーとの統合
- Twitter API: イベント告知用のTwitterとの統合
- Discord API: イベント告知用のDiscordとの統合

## インストール

1. リポジトリをクローンします：
   ```
   git clone https://github.com/noricha-vr/VRCEventManager.git
   ```

2. プロジェクトディレクトリに移動します：
   ```
   cd VRCEventManager
   ```

3. 仮想環境を作成して有効化します：
   ```
   python3 -m venv venv
   source venv/bin/activate
   ```

4. 必要な依存関係をインストールします：
   ```
   pip install -r requirements.txt
   ```

5. データベースをセットアップします：
   ```
   python manage.py migrate
   ```

6. スーパーユーザーアカウントを作成します：
   ```
   python manage.py createsuperuser
   ```

7. ソーシャルメディアとGoogleカレンダーのAPI認証情報を設定します(不要)：
   - Twitter、Discord、Googleカレンダーの API 認証情報を取得します
   - プロジェクト設定ファイルで対応する設定を更新します

8. 開発サーバーを起動します：
   ```
   python manage.py runserver
   ```

9. Webブラウザで `http://localhost:8000` にアクセスしてアプリケーションを使用します。

## 使用方法

- 新しいユーザーアカウントを登録するか、既存のアカウントでログインします
- 必要な詳細情報を入力して新しいイベントを作成します
- イベントに対してユーザーに役割（主催者とスタッフ）を割り当てます
- ソーシャルメディアプラットフォームの告知スケジュールとテンプレートを設定します
- システムは指定されたルールに基づいて定期的なイベントを自動的に作成します
- イベントの変更はGoogleカレンダーと同期されます

## 貢献

貢献は大歓迎です！問題を見つけたり、改善の提案がある場合は、Issueを開くかプルリクエストを送信してください。
