import discord
from discord.ext import commands
import os
import random
from keep_alive import keep_alive

# インテントの設定（Developer PortalでONにする必要があります）
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'ログインしました: {bot.user.name}')
    await bot.change_presence(activity=discord.Game(name="ゆっくり回線鯖を監視中..."))

# ==========================================
# 実装済みの28個のコマンド
# ==========================================

# 1. ping
@bot.command()
async def ping(ctx):
    await ctx.send(f'🏓 Pong! 応答速度: {round(bot.latency * 1000)}ms')

# 2. hello
@bot.command()
async def hello(ctx):
    await ctx.send(f'こんにちは、{ctx.author.name}さん！ゆっくりしていってね！')

# 3. yukkuri
@bot.command()
async def yukkuri(ctx):
    await ctx.send('饅頭舐めんな！ゆっくりしていってね！！！')

# 4. kaisen (回線速度ジョーク)
@bot.command()
async def kaisen(ctx):
    speed = random.randint(1, 10000)
    await ctx.send(f'📡 {ctx.author.name}の現在の回線速度は... 概算 {speed} Mbpsです！')

# 5. serverinfo
@bot.command()
async def serverinfo(ctx):
    guild = ctx.guild
    await ctx.send(f'【{guild.name}】\nメンバー数: {guild.member_count}人\n作成日: {guild.created_at.strftime("%Y/%m/%d")}')

# 6. userinfo
@bot.command()
async def userinfo(ctx, member: discord.Member = None):
    member = member or ctx.author
    await ctx.send(f'👤 名前: {member.name}\n🆔 ID: {member.id}\n📅 参加日: {member.joined_at.strftime("%Y/%m/%d")}')

# 7. avatar
@bot.command()
async def avatar(ctx, member: discord.Member = None):
    member = member or ctx.author
    await ctx.send(member.display_avatar.url)

# 8. say
@bot.command()
async def say(ctx, *, text: str):
    await ctx.message.delete()
    await ctx.send(text)

# 9. dice
@bot.command()
async def dice(ctx):
    await ctx.send(f'🎲 サイコロを振りました！出目: {random.randint(1, 6)}')

# 10. coin
@bot.command()
async def coin(ctx):
    result = random.choice(['表', '裏'])
    await ctx.send(f'🪙 コイントスの結果: **{result}**')

# 11. omikuji
@bot.command()
async def omikuji(ctx):
    results = ['大吉', '中吉', '小吉', '吉', '末吉', '凶', '大凶']
    await ctx.send(f'⛩️ 今日の運勢は... **{random.choice(results)}**！')

# 12. member
@bot.command()
async def member(ctx):
    await ctx.send(f'👥 現在のサーバー参加人数は {ctx.guild.member_count} 人です！')

# 13. botinfo
@bot.command()
async def botinfo(ctx):
    await ctx.send('🤖 私は「ゆっくり回線鯖」専属のBOTです。Renderで稼働しています！')

# 14. rules
@bot.command()
async def rules(ctx):
    await ctx.send('📜 サーバーのルールを守って、仲良くゆっくりしましょう！')

# 15. invite
@bot.command()
async def invite(ctx):
    await ctx.send('🔗 招待リンクが必要な場合は管理者にお問い合わせください。')

# 16. choose
@bot.command()
async def choose(ctx, *options):
    if not options:
        await ctx.send('選択肢をスペース区切りで入力してください！ 例: !choose りんご みかん')
        return
    await ctx.send(f'🤔 うーん... **{random.choice(options)}** にしましょう！')

# 17. 8ball
@bot.command(name="8ball")
async def eightball(ctx, *, question: str):
    responses = ['間違いなくそうです。', 'おそらくそうです。', '五分五分ですね。', '今は言えません。', '絶対に違います。']
    await ctx.send(f'質問: {question}\n答え: 🎱 {random.choice(responses)}')

# 18. hug
@bot.command()
async def hug(ctx, member: discord.Member):
    await ctx.send(f'🫂 {ctx.author.name} が {member.name} をハグしました！')

# 19. pat
@bot.command()
async def pat(ctx, member: discord.Member):
    await ctx.send(f'✋ {ctx.author.name} が {member.name} をなでなでしました！')

# 20. version
@bot.command()
async def version(ctx):
    await ctx.send('🏷️ v1.0.0 (Render Edition)')

# 21. echo
@bot.command()
async def echo(ctx, *, text: str):
    await ctx.send(f'エコー: {text}')

# 22. math
@bot.command()
async def math(ctx, a: int, op: str, b: int):
    if op == '+': await ctx.send(f'🧮 {a+b}')
    elif op == '-': await ctx.send(f'🧮 {a-b}')
    elif op == '*': await ctx.send(f'🧮 {a*b}')
    elif op == '/': 
        await ctx.send(f'🧮 {a/b}' if b != 0 else 'ゼロで割ることはできません！')
    else: 
        await ctx.send('対応していない演算子です。+, -, *, / を使ってください。')

# 23. joke
@bot.command()
async def joke(ctx):
    jokes = ['布団が吹っ飛んだ！', 'アルミ缶の上にあるみかん', 'ネコが寝ころんだ！']
    await ctx.send(f'🤣 {random.choice(jokes)}')

# 24. praise
@bot.command()
async def praise(ctx, member: discord.Member = None):
    member = member or ctx.author
    await ctx.send(f'✨ {member.name}、今日も最高にかっこいいぞ！天才！')

# 25. scold
@bot.command()
async def scold(ctx, member: discord.Member = None):
    member = member or ctx.author
    await ctx.send(f'💢 {member.name}！もうちょっとしっかりしなさい！')

# 26. weather
@bot.command()
async def weather(ctx):
    w = random.choice(['晴れ☀️', '曇り☁️', '雨☔', '雪⛄', '雷雨⛈️'])
    await ctx.send(f'今日のゆっくり回線鯖周辺の天気は、たぶん {w} です！')

# 27. status
@bot.command()
async def status(ctx):
    await ctx.send('🟢 サーバーシステム: オールグリーン！異常なし！')

# 28. bye
@bot.command()
async def bye(ctx):
    await ctx.send(f'おやすみなさい、{ctx.author.name}さん。またゆっくりしに来てね。')

# ==========================================
# 起動処理
# ==========================================

# Webサーバーを起動してスリープ回避
keep_alive()

# 環境変数からトークンを取得してBOTを起動
TOKEN = os.environ.get('DISCORD_TOKEN')
if TOKEN:
    bot.run(TOKEN)
else:
    print("エラー: DISCORD_TOKENが設定されていません。")
