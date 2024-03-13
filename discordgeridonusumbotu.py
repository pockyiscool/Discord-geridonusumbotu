import discord
from discord.ext import commands
koruma2 = "Doğal Kaynakların Korunması: Geri dönüştürme, doğal kaynakların tükenmesini engeller.Geri dönüşüm endüstrisi, ekonomiye katkı sağlar ve istihdam yaratırEv atıklarını geri dönüştürmek, sürdürülebilir bir gelecek için önemli bir adımdır."

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def Koruma(ctx):
    await ctx.send(koruma2)
    
@bot.command()
async def Geridönüşüme_katkı_sağlamak_için_ne_yapmalıyım(ctx):
    await ctx.send(f'Yağların geri dönüştürülmesi, çevresel etkilerini azaltmanın yanı sıra kaynakları korumak ve atık yönetimini daha sürdürülebilir hale getirmek için önemlidir. Bu nedenle, kullanılmış yağları doğru şekilde toplamak ve geri dönüştürmek, her bireyin ve toplumun sorumluluğudur.')

@bot.command()
async def isim(ctx):
    await ctx.send(f'mesaj')


@bot.command()
async def geridonusum (ctx):
    await ctx.send("""
        Geri dönüşüm, kullanılmış malzemelerin yeni ürünler oluşturmak için tekrar işlenmesidir. 
        Bu süreç, doğal kaynakların korunmasına, atık miktarının azaltılmasına ve çevre kirliliğinin önlenmesine yardımcı olur.
        En yaygın geri dönüştürülen malzemeler arasında kağıt, cam, plastik ve metal bulunur.
        """)
       




bot.run("token")
