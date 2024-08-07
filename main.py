import discord
from discord.ext import commands
import json
import sys
import requests
import base64
import io
import yt_dlp as youtube_dl
import ffmpeg
import pytesseract
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
import os
import asyncio
from dotenv import load_dotenv
import urllib.parse
import urllib.request
import re

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Windowsの場合。適宜変更

# config.json からトークンを読み込む
with open('config.json') as f:
    config = json.load(f)

# トークンを変数に格納
TOKEN = config['TOKEN']

client = discord.Client(intents=discord.Intents.all())

# グローバル変数
voice_clients = {}

ytdl_options = {
    'format': 'bestaudio/best',
    'noplaylist': True,
}

ffmpeg_options = {
    'options': '-vn -ar 48000 -ac 2 -ab 192k',
}



bot = commands.Bot(command_prefix="g!", intents=discord.Intents.all())
bot.remove_command("help")


intents = discord.Intents.default()
intents.members = True  
intents.message_content = True



@bot.event
async def on_ready():
    print("✅Botは正常に起動しました")
    print(bot.user.name)
    print("Python", sys.version)  
    print("discord.py", discord.__version__)  
    print('------')
    await bot.change_presence(activity=discord.Game(name="/help"))
    
    # 参加しているサーバーの一覧を表示
    print("参加しているサーバー:")
    for guild in bot.guilds:
        print(f"サーバー名: {guild.name}, サーバーID: {guild.id}")
    
    try:
        synced = await bot.tree.sync()    
        print(f"{len(synced)}個のコマンドを同期しました")
    except Exception as e:
        print(e)
        
class SaveImageButton(discord.ui.Button):
    def __init__(self, image_url):
        super().__init__(label="画像を保存", style=discord.ButtonStyle.primary)
        self.image_url = image_url

    async def callback(self, interaction: discord.Interaction):
        try:
            response = requests.get(self.image_url)
            response.raise_for_status()

            image = io.BytesIO(response.content)
            file = discord.File(image, filename="skin.png")
            await interaction.response.send_message(file=file, content="画像を保存しました。")
        except requests.RequestException as e:
            embed = discord.Embed(title="⛔画像ダウンロードエラー", description=f"画像のダウンロード中にエラーが発生しました: {e}", color=0xff0000)
            await interaction.response.send_message(embed=embed)
        except Exception as e:
            embed = discord.Embed(title="⛔エラー", description=f"エラーが発生しました: {e}", color=0xff0000)
            await interaction.response.send_message(embed=embed)

@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    try:
        await member.kick(reason=reason)
        embed = discord.Embed(title="✅ユーザーをサーバーから追放しました", description=f"{member} がサーバーから追放されました", color=0x00ff00)
        await ctx.send(embed=embed)
    except discord.Forbidden:
        embed = discord.Embed(title="⛔エラー", description="このコマンドを実行するための十分な権限がありません。\nあなたのロールよりも相手のロールの方が高い、または相手が同じロールを持っているか、\n「管理者」または「メンバーをキック」権限が不足している可能性があります。", color=0xff0000)
        await ctx.send(embed=embed)
    except Exception as e:
        embed = discord.Embed(title="⛔エラー", description=f"コマンドの実行中にエラーが発生しました: {e}", color=0xff0000)
        await ctx.send(embed=embed)
    await ctx.message.delete()

@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    try:
        await member.ban(reason=reason)
        embed = discord.Embed(title="✅ユーザーをサーバーから禁止しました", description=f"{member} がサーバーから禁止されました\n理由: {reason}", color=0x00ff00)
        await ctx.send(embed=embed)
    except discord.Forbidden:
        embed = discord.Embed(title="⛔エラー", description="このコマンドを実行するための十分な権限がありません。\nあなたのロールよりも相手のロールの方が高い、または相手が同じロールを持っているか、\n「管理者」または「メンバーをBAN」権限が不足している可能性があります。", color=0xff0000)
        await ctx.send(embed=embed)
    except Exception as e:
        embed = discord.Embed(title="⛔エラー", description=f"コマンドの実行中にエラーが発生しました: {e}", color=0xff0000)
        await ctx.send(embed=embed)
    await ctx.message.delete()

@bot.command()
async def botinfo(ctx):
    embed = discord.Embed(title=bot.user.name, timestamp=ctx.message.created_at, color=discord.Colour.green())
    embed.add_field(name="🤖BotVersion", value="1.10.5", inline=True)
    embed.add_field(name="🖥️Python", value=sys.version, inline=True)
    embed.add_field(name="🛠️discord.py", value=discord.__version__, inline=True)
    embed.add_field(name="❓Support", value="準備中")
    await ctx.send(embed=embed)
    await ctx.message.delete()

@bot.tree.command(name="ping", description="Pongを返します")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message("Pong!")

@bot.tree.command(name="help", description="ヘルプを表示します")
async def help_command(interaction: discord.Interaction):
    embed = discord.Embed(title="Help", color=discord.Colour.red())
    embed.add_field(name="/help", value="ヘルプを表示します")
    embed.add_field(name="g!reply", value=f"{bot.user.name}が正常に動作しているかを確認します")
    embed.add_field(name="g!serverinfo", value="サーバーの情報を表示します")
    embed.add_field(name="/ping", value="Pongを返します")
    embed.add_field(name="g!kick @user", value="指定したユーザーをサーバーから追放します")
    embed.add_field(name="g!ban @user", value="指定したユーザーをサーバーから禁止します")
    embed.add_field(name="g!botinfo", value=f"{bot.user.name}の情報を表示します")
    embed.add_field(name="g!userinfo @user", value="ユーザーの情報を取得します")
    embed.add_field(name="g!avatar @user", value="ユーザーのアバターを表示します")
    embed.add_field(name="g!mcskin <mcid>", value="Minecraftスキンを表示します")
    embed.add_field(name="g!idinvite <guildid>", value="サーバーidからサーバーの招待リンクを生成します")
    embed.add_field(name="g!play <URL>", value="指定したURLの音楽を再生します。")
    embed.add_field(name="g!stop", value="再生中の音楽を停止します。")
    embed.add_field(name="g!tts <text>", value="指定したテキストを音声で再生します。")
    await interaction.response.send_message(embed=embed)

@bot.command()
async def reply(ctx):
    await ctx.send(f"✅現在{bot.user.name}は正常に動作しています!")
    await ctx.message.delete()

@bot.command()
async def serverinfo(ctx):
    guild = ctx.message.guild
    roles = [role for role in guild.roles]
    text_channels = [text_channel for text_channel in guild.text_channels]
    embed = discord.Embed(title="ServerInfo", description=guild.name, timestamp=ctx.message.created_at, color=discord.Colour.green())
    embed.set_thumbnail(url=ctx.guild.icon.url)
    embed.add_field(name="チャンネル数", value=f"{len(text_channels)}", inline=True)
    embed.add_field(name="ロール", value=f"{len(roles)}", inline=True)
    embed.add_field(name="サーバーブースター", value=guild.premium_subscription_count, inline=True)
    embed.add_field(name="メンバー数", value=guild.member_count, inline=True)
    embed.add_field(name="サーバー設立日", value=guild.created_at, inline=True)
    await ctx.send(embed=embed)
    await ctx.message.delete()

@bot.command()
async def userinfo(ctx, member: discord.Member = None):
    if member is None:
        await ctx.send("⛔ユーザーを指定してください。例: `g!userinfo @ユーザー`")
        return
    
    embed = discord.Embed(title=f"{member.name}の情報", color=0x00ff00)
    embed.set_thumbnail(url=member.avatar.url)
    embed.add_field(name="メンション", value=member.mention, inline=True)
    embed.add_field(name="名前", value=member.name, inline=True)
    embed.add_field(name="ユーザーID", value=member.id, inline=True)
    embed.add_field(name="アカウント作成日", value=member.created_at.strftime('%Y-%m-%d'), inline=True)
    embed.add_field(name="サーバー参加日", value=member.joined_at.strftime('%Y-%m-%d'), inline=True)
    roles = [role.mention for role in member.roles[1:]]  # 最初のロールは @everyone なので除外
    embed.add_field(name="ロール", value=", ".join(roles) if roles else "ロールなし", inline=False)
    await ctx.send(embed=embed)
    await ctx.message.delete()

@bot.command()
async def avatar(ctx, member: discord.Member = None):
    if member is None:
        member = ctx.author
    
    embed = discord.Embed(title=f"{member.name}のアバター", color=0x00ff00)
    embed.set_image(url=member.avatar.url)
    await ctx.send(embed=embed)

@bot.command()
@commands.has_permissions(administrator=True)  # 管理者権限が必要
async def idinvite(ctx, server_id: int):
    try:
        guild = bot.get_guild(server_id)
        if guild is None:
            await ctx.send("⛔指定されたサーバーが見つかりません。")
            return

        invite = await guild.text_channels[0].create_invite(max_age=3600, unique=True)  # 有効期限を1時間に設定
        invite_link = invite.url

        try:
            await ctx.author.send(f"✅以下がサーバーの招待リンクです:\n{invite_link}")
            await ctx.send("✅招待リンクをDMで送信しました。")
        except discord.Forbidden:
            await ctx.send("⛔DMを送信できません。DMがブロックされているか、DMを受け取る設定になっていない可能性があります。")
    except discord.Forbidden:
        await ctx.send("⛔この操作を実行する権限がありません。")
    except Exception as e:
        await ctx.send(f"⛔エラーが発生しました: {e}")

@bot.command()
async def mcskin(ctx, gamertag: str):
    try:
        # Mojang APIを使用してUUIDを取得
        mojang_response = requests.get(f'https://api.mojang.com/users/profiles/minecraft/{gamertag}')
        mojang_response.raise_for_status()
        data = mojang_response.json()
        uuid = data.get('id')
        
        if not uuid:
            await ctx.send("⛔指定されたゲーマータグが見つかりません。")
            return
        
        # UUIDからスキンのURLを取得
        skin_response = requests.get(f'https://sessionserver.mojang.com/session/minecraft/profile/{uuid}?unsigned=false')
        skin_response.raise_for_status()
        profile_data = skin_response.json()
        textures = profile_data.get('properties', [])[0].get('value')
        textures_data = json.loads(base64.b64decode(textures))
        skin_url = textures_data['textures']['SKIN']['url']

        # 画像をダウンロードしてファイルとして送信
        response = requests.get(skin_url)
        response.raise_for_status()
        img_data = response.content

        # 画像のファイルを一時的に保存
        with open('skin_image.png', 'wb') as file:
            file.write(img_data)

        # ボタンの作成
        class SaveButton(discord.ui.View):
            def __init__(self):
                super().__init__()
                self.add_item(discord.ui.Button(label="保存", url="https://example.com/save_image"))

        # メッセージを送信
        with open('skin_image.png', 'rb') as file:
            await ctx.send(
                f"{gamertag}ここにMinecraftスキンの画像があります。",
                file=discord.File(file, 'skin_image.png'),
                view=SaveButton()
            )

    except requests.RequestException as e:
        await ctx.send(f"⛔ネットワークエラー: {e}")
    except KeyError as e:
        await ctx.send(f"⛔データ取得エラー: {e}")
    except Exception as e:
        await ctx.send(f"⛔エラーが発生しました: {e}")

@bot.command()
async def play(ctx, *url):
    global voice_clients
    try:
        url = " ".join(url)
        print(f"Requesting URL: {url}")
        
        voice_client = await ctx.author.voice.channel.connect()
        voice_clients[ctx.guild.id] = voice_client

        loop = asyncio.get_event_loop()
        ytdl = youtube_dl.YoutubeDL(ytdl_options)
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=False))

        if data is None:
            raise ValueError("⛔指定されたURLから動画の情報を取得できませんでした")

        if 'entries' in data:
            data = data['entries'][0]

        title = data.get('title') if data else 'unknown'
        print(f"✅{title}を再生中です")

        url2 = data['url']
        source = await discord.FFmpegOpusAudio.from_probe(url2, **ffmpeg_options)
        voice_clients[ctx.guild.id].play(source)
        embed = discord.Embed(title=f"✅{title}を再生中です", color=discord.Colour.green())
        await ctx.send(embed=embed)
        await ctx.message.delete()
    except Exception as e:
        embed = discord.Embed(title="⛔エラー", description=f"エラーが発生しました: {e}", color=0xff0000)
        await ctx.send(embed=embed)
        await ctx.message.delete()

@bot.command()
async def stop(ctx):
    global voice_clients
    try:
        voice_client = voice_clients.get(ctx.guild.id)
        if voice_client:
            await voice_client.disconnect()
            del voice_clients[ctx.guild.id]
            embed = discord.Embed(title="✅音楽の再生を停止しました", color=discord.Colour.green())
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title="⛔エラー", description="再生中の音楽がありません", color=0xff0000)
            await ctx.send(embed=embed)
        await ctx.message.delete()
    except Exception as e:
        embed = discord.Embed(title="⛔エラー", description=f"エラーが発生しました: {e}", color=0xff0000)
        await ctx.send(embed=embed)
        await ctx.message.delete()

@bot.command()
async def tts(ctx, *, message):
    try:
        url_encoded_message = urllib.parse.quote(message)
        url = f"http://translate.google.com/translate_tts?ie=UTF-8&client=tw-ob&q={url_encoded_message}&tl=ja"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}

        request = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(request) as response:
            audio_data = response.read()

        if os.path.exists("tts.mp3"):
            os.remove("tts.mp3")

        with open("tts.mp3", "wb") as file:
            file.write(audio_data)

        voice_channel = ctx.author.voice.channel
        if not voice_channel:
            await ctx.send("⛔まずボイスチャンネルに参加してください。")
            return

        voice_client = voice_clients.get(ctx.guild.id)
        if voice_client is None:
            voice_client = await voice_channel.connect()
            voice_clients[ctx.guild.id] = voice_client
        
        voice_client.play(discord.FFmpegPCMAudio("tts.mp3"))
        embed = discord.Embed(title="TTS", description=message, color=discord.Colour.green())
        await ctx.send(embed=embed)
        await ctx.message.delete()
    except Exception as e:
        embed = discord.Embed(title="⛔エラー", description=f"エラーが発生しました: {e}", color=0xff0000)
        await ctx.send(embed=embed)
        await ctx.message.delete()

bot.run(TOKEN)
