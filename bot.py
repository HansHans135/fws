import discord
import json
import requests
from discord import option
bot = discord.Bot()

with open("setting.json", "r", encoding="utf-8")as f:
    setting = json.load(f)
domain_list = []
for i in setting["domains"]:
    domain_list.append(i)


class chk(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="確定", style=discord.ButtonStyle.green, custom_id="awa:start",)
    async def start(self, button: discord.ui.Button, interaction: discord.Interaction):
        for i in domain_list:
            if i in interaction.message.content:
                d=i
        id = setting["domains"][d]["id"]
        key = setting["domains"][d]["key"]
        ip = setting["ip"]
    
        # 創建
        url = f"https://api.cloudflare.com/client/v4/zones/{id}/dns_records"

        payload = {
            "content": ip,
            "name": interaction.message.content,
            "proxied": True,
            "type": "A",

        }
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"{key}",
        }

        response = requests.request("POST", url, json=payload, headers=headers)
        if response.json()["success"]:
            await interaction.response.send_message(f"已創建此網域\n http://{interaction.message.content}", ephemeral=True)
        else:
            try:
                ers=""
                for i in response.json()["errors"]:
                    ers+=i["message"]+"\n"
                embed=discord.Embed(title="錯誤內容",description=ers)
            except:
                embed=None
            await interaction.response.send_message("發生問題,請聯絡管理員",embed=embed, ephemeral=True)
        c = bot.get_channel(1122903057265590283)
        embed = discord.Embed(title=f"API紀錄", description=response.text)
        await c.send(f"剛剛`{interaction.user}`對`{interaction.message.content}`執行了操作", embed=embed)


@bot.event
async def on_ready():
    print(bot.user)


@bot.slash_command(description="創建一個子網域")
@option("text", description="網域名")
@option("domain", description="選擇你的網域", choices=domain_list)
async def new_domain(ctx: discord.ApplicationContext, text, domain):
    embed = discord.Embed(
        title="確認", description=f"你確定要將`{text}.{domain}`作為你的網域嗎\n**此操作不可返回**")
    await ctx.respond(f"{text}.{domain}", embed=embed, ephemeral=True, view=chk())


bot.run(setting["token"])
