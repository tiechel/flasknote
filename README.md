Flask Note
==========

Development Build
```
flask run
```

Production Build (UNIX only)
```
gunicorn flasknote:app
```

Deploy on heroku
```
heroku login -i
heroku git:remote --app <application name>
git push heroku master
```


# Migration

```
$ # 初期化
$ flask db init
$ # マイグレーション作成
$ flask db migrate
$ # マイグレーション適用
$ flask db upgrade
$ # ダウングレード
$ flask db downgrade
```