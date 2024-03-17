
```bash
# テーブル更新
 python manage.py makemigrations && python manage.py migrate      
```
```bash
# ER図のdotファイルを作成
python manage.py graph_models -a --dot > er_diagram.dot
```