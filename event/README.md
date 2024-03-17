## モデル

### Event

`Event`モデルは、イベントの基本情報を表します。以下のフィールドを持ちます：

- `title`: イベントのタイトル（文字列）
- `description`: イベントの説明（テキスト）
- `location`: イベントの開催場所（文字列）
- `repeat_rule`: 繰り返しのルールを保存するフィールド（文字列）

### EventInstance

`EventInstance`モデルは、`Event`の個別の開催インスタンスを表します。以下のフィールドを持ちます：

- `event`: 関連する`Event`への外部キー
- `start_time`: イベントの開始日時（日時）
- `end_time`: イベントの終了日時（日時）
- `status`: イベントのステータス（選択肢：'scheduled'または'cancelled'）

### RecurrenceRule

`RecurrenceRule`モデルは、イベントの繰り返しルールを表します。以下のフィールドを持ちます：

- `event`: 関連する`Event`への外部キー
- `frequency`: 繰り返しの頻度（選択肢：'NONE'、'CUSTOM'、'DAILY'、'WEEKLY'、'BIWEEKLY'、'MONTHLY'、'YEARLY'）
- `interval`: 繰り返しの間隔（正の整数）
- `weekdays`: 曜日ベースの繰り返しルールで使用される曜日（文字列）
- `month_day`: 月ベースの繰り返しルールで使用される日（整数）
- `month`: 年ベースの繰り返しルールで使用される月（整数）
- `occurrence`: 第N曜日の繰り返しルールで使用される出現回数（選択肢：1、2、3、4、-1）
- `weekday`: 第N曜日の繰り返しルールで使用される曜日（選択肢：0〜6）
- `custom_dates`: カスタム日付の繰り返しルールで使用される日付（JSON形式）
- `end_date`: 繰り返しの終了日（日付）

### EventRole

`EventRole`モデルは、イベントに対するユーザーの役割を表します。以下のフィールドを持ちます：

- `event`: 関連する`Event`への外部キー
- `user`: 関連する`User`への外部キー
- `role`: ユーザーの役割（選択肢：'organizer'または'staff'）

## 繰り返しルール

RecurrenceRuleモデルが対応している繰り返しルール

1. 設定なし（NONE）：繰り返しルールを設定しない場合。
2. カスタム（CUSTOM）：カスタム日付を使用して繰り返しルールを設定する場合。custom_datesフィールドにJSON形式で日付のリストを指定。
3. 毎日（DAILY）：毎日繰り返すルール。intervalフィールドで間隔を指定可能。
4. 毎週（WEEKLY）：毎週繰り返すルール。intervalフィールドで間隔を、weekdaysフィールドで曜日を指定可能。
5. 隔週（BIWEEKLY）：隔週で繰り返すルール。intervalフィールドで間隔を、weekdaysフィールドで曜日を指定可能。
6. 毎月（MONTHLY）：毎月繰り返すルール。以下の2つの方法で指定可能：
   - month_dayフィールドで日付を指定。
   - occurrenceフィールドで第N週目（第1、第2、第3、第4、最終）を、weekdayフィールドで曜日を指定。
7. 毎年（YEARLY）：毎年繰り返すルール。monthフィールドで月を、month_dayフィールドで日付を指定。

以上が、RecurrenceRuleモデルが対応している繰り返しルールのまとめです。これらのルールを組み合わせることで、様々な繰り返しパターンを表現できます。end_dateフィールドを使用することで、繰り返しの終了日を指定することも可能です。