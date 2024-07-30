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

ユーザーのアバターを取得して表示します

``g!mcskin <mcid>``

MCIDからMinecraftスキンを取得します ※Java Editionのみ

``g!idinvite <guildid>``

サーバーid(guildid)からサーバーの招待リンクを生成します

## グローバル版

[グローバル版導入](https://discord.com/oauth2/authorize?client_id=1264941322515644548&permissions=8&integration_type=0&scope=bot+applications.commands)

サーバーを選択をクリックして、botを入れたいサーバーをクリックします

![image](https://github.com/user-attachments/assets/27aae2a4-cf5d-4138-acdc-644486596dc6)

はいをクリックします

![image](https://github.com/user-attachments/assets/a67e3507-8d1f-4c94-ba5b-d5fdf1cac9af)

認証をクリックします

![image](https://github.com/user-attachments/assets/5b67742a-faae-4b3c-9398-f8519c89577f)

私は人間ですにチェックを入れます

![image](https://github.com/user-attachments/assets/ae32d55c-d54e-47f9-964f-04fc0b000900)

この画面が出たら導入は完了です。

![image](https://github.com/user-attachments/assets/3477f3c2-95bc-4e6f-9794-e3bba365dc32)

## ローカル版

### Botの作成

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

Reset Tokenをクリック

![image](https://github.com/user-attachments/assets/f4ad0eb0-75ff-4a1b-8a70-accd6ab7ca03)

Yes, do it!をクリック

![image](https://github.com/user-attachments/assets/567f49db-46c6-4d73-9928-262452a2b201)

この画面が出たらAuthの番号(6桁)を打つ

![image](https://github.com/user-attachments/assets/aa45da89-d299-4869-8ef3-47926352e23e)

Tokenが生成されるので、Copyを押します

##### このTokenは絶対に公開しないでください

##### このTokenは絶対に公開しないでください

##### このTokenは絶対に公開しないでください

大事なことなので3回書きました。

万が一公開してしまった場合は、Reset Tokenを押すところからやり直しです。

このtokenは後で使うので、メモ帳などに貼り付けて流失するおそれのない覚えやすい場所(Google Driveなど)に保存しておきます

![image](https://github.com/user-attachments/assets/4ccb4948-737c-4450-b6e4-5e49ca794713)

少し下にスクロールし、３つ並んでいるこのグレーのボタンをクリックして緑に変えます

![image](https://github.com/user-attachments/assets/38395faa-f9b8-450f-8600-e9a07eca5a15)

一番下らへんまでスクロールして、Bot PermissionにあるAdministratorにチェックを入れます

![image](https://github.com/user-attachments/assets/6bc0eeb6-8299-4e3d-8a67-8f0620f21138)

左側のOAuth2をクリック

![image](https://github.com/user-attachments/assets/435f0daa-829c-401b-83ba-928ca655ae1a)

下までスクロールしてOAuth2 URL Generator にあるbotとapplications.commandsにチェックを入れます

![image](https://github.com/user-attachments/assets/e6a56ef8-9c85-42ad-9fe6-f3d91c0821d9)

すると下にBOT PERMISSION が出てくるのでAdministratorにチェックを入れます

![image](https://github.com/user-attachments/assets/848781a6-ac56-43d1-82d4-10292438154c)

一番下のGENERATED URLの中にあるURLを選択して右クリックしてhttps://discord.com/oauth2/authorize?client_id...に移動をクリックします(URLの横のCopyではないので注意)

![image](https://github.com/user-attachments/assets/52b77f9d-b891-47f4-a316-e8fb7b51b1a0)

サーバーを選択をクリックして、botを入れたいサーバーをクリックします

![image](https://github.com/user-attachments/assets/27aae2a4-cf5d-4138-acdc-644486596dc6)

はいをクリックします

![image](https://github.com/user-attachments/assets/a67e3507-8d1f-4c94-ba5b-d5fdf1cac9af)

認証をクリックします

![image](https://github.com/user-attachments/assets/5b67742a-faae-4b3c-9398-f8519c89577f)

私は人間ですにチェックを入れます

![image](https://github.com/user-attachments/assets/ae32d55c-d54e-47f9-964f-04fc0b000900)

この画面が出たらbotの作成作業は完了です。お疲れ様でした。

![image](https://github.com/user-attachments/assets/3477f3c2-95bc-4e6f-9794-e3bba365dc32)

### コードの編集

```
{
  "TOKEN": "Token here"
}
```

Token hereを先ほど保存しておいたtokenに置き換えます

### 実行

コンソールで ``Python main.py`` を実行して起動します。
botのステータスがオンラインになったら起動完了です

## 注意

このソースコードはpython3.10.9で動作確認しています。他のバージョンでの動作は保証しません。

このソースコードは自由に改変できますが、改変して動かなくなったとしても我々は一切責任を負いません

このソースコードにはパッケージ"discord.py"と"ffmpeg-python","yt-dlp"を使用しています

起動する前にコンソールで pip install discord.py yt-dlp ffmpeg-python を実行してください。

Python入れてないのに動かそうとするおバカさんの相手はしません

以上です。いかがだったでしょうか(?) それではアディオス！
