Flask Note
===============

Development Build

```:bash
flask run
```

Production Build (UNIX only)

```:bash
gunicorn flasknote:app
```

Deploy on heroku

```:bash
heroku login -i
heroku git:remote --app <application name>
git push heroku master
```

Migration
---------------

```:json
# 初期化
flask db init
# マイグレーション作成
flask db migrate
# マイグレーション適用
flask db upgrade
# ダウングレード
flask db downgrade
```

settings.json
---------------

VS Code用の設定を覚え書き

```:json
{
    "files.trimTrailingWhitespace": true,
    "files.insertFinalNewline": true,
    "python.pythonPath": "venv\\Scripts\\python.exe",
    "python.linting.pylintEnabled": false,
    "python.linting.flake8Enabled": true,
    "python.linting.flake8Args": [
        "--max-line-length=160",
        "--ignore="
    ],
    "python.analysis.disabled": [
        "inherit-non-class"
    ],
}
```
