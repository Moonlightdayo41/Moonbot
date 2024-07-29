# Moonbot
多機能なdiscordbotです

## コマンド一覧

``/help``

ヘルプを表示します

``g!reply``

BOTが正常に動作しているかを確認します

``g!serverinfo``

サーバーの情報を表示します

``/ping``

Pongを返します

``g!kick @user``

指定したユーザーをサーバーから追放します

``g!ban @user``

指定したユーザーをサーバーから禁止します

``g!botinfo``

BOTの情報を表示します

``g!userinfo @user``

ユーザーの情報を取得します

``g!avatar @user``

ユーザーのアバターを表示します

``g!mcskin <mcid>``

Minecraftスキンを表示します

``g!idinvite``

サーバーidからサーバーの招待リンクを生成します

## 使い方

### OAuth2

[discord.dev](https://discord.com/developers/)を開きます

New Application をクリックします

![image](https://github.com/user-attachments/assets/f2bcda08-d234-4eef-b778-8813200f6786)


Name*に任意の名前を入力して

By clicking Create, you agree to the Discord Developer Terms of Service and Developer Policy.にチェックを入れます
Createをクリックします

![image](https://github.com/user-attachments/assets/94187e65-d395-4918-8740-98c73b31e5c1)

この画面が出たら、アイコンや名前、説明を自由にカスタマイズしてみてください(必須ではない)

![image](https://github.com/user-attachments/assets/806c46ef-9aad-47fc-8d72-974186f52e1c)

カスタマイズが終わったら、左のBotをクリックします

![image](https://github.com/user-attachments/assets/48f7b3c8-3269-458f-9bbb-f42ce9ccc2d6)



### コードの編集

```
{
  "TOKEN": "Token here"
}
```

Token hereをbotのtokenに置き換えます

### 実行

コンソールで ``Python main.py`` を実行して起動します。
botのステータスがオンラインになったら起動完了です
