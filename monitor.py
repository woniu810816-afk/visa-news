import datetime

def get_intelligence():
    targets = [
        {"name": "🇺🇸 美国 USCIS 新闻", "url": "https://www.uscis.gov/news/news-releases"},
        {"name": "🇺🇸 签证排期表 (Visa Bulletin)", "url": "https://travel.state.gov/content/travel/en/legal/visa-law0/visa-bulletin.html"},
        {"name": "🇨🇦 加拿大 IRCC 邀请动态", "url": "https://www.canada.ca/en/immigration-refugees-citizenship/services/immigrate-canada/express-entry/submit-profile/rounds-invitations.html"}
    ]
    html_items = ""
    for t in targets:
        html_items += f"<div class='item'><strong>{t['name']}</strong><br><a href='{t['url']}' target='_blank'>点击查看官方公告原文 →</a></div>"
    return html_items

now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
content = get_intelligence()

html_template = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>全球移民动态监控</title>
    <style>
        body {{ font-family: -apple-system, sans-serif; background-color: #f4f7f9; padding: 15px; color: #333; line-height: 1.6; }}
        .card {{ background: white; border-radius: 12px; padding: 20px; box-shadow: 0 4px 15px rgba(0,0,0,0.05); margin-bottom: 20px; }}
        h1 {{ color: #0056b3; font-size: 22px; text-align: center; margin-bottom: 5px; }}
        .time {{ text-align: center; color: #999; font-size: 12px; margin-bottom: 20px; }}
        .item {{ background: #f8f9fa; padding: 12px; margin: 10px 0; border-radius: 8px; border-left: 5px solid #0056b3; }}
        .vip-card {{ background: linear-gradient(135deg, #2c3e50 0%, #000000 100%); color: white; border-radius: 12px; padding: 25px; text-align: center; }}
        .highlight {{ color: #ffc107; font-weight: bold; }}
        a {{ color: #0056b3; text-decoration: none; font-size: 14px; }}
    </style>
</head>
<body>
    <h1>🚀 移民 & 数字游民情报站</h1>
    <p class="time">AI 机器人自动巡视时间: {now}</p>

    <div class="card">
        <h3 style="margin-top:0;">📍 官方动态实时监控</h3>
        {content}
    </div>

    <div class="vip-card">
        <h3 style="margin-top:0;">💎 深度情报与私域库</h3>
        <p style="font-size:14px; opacity:0.9;">获取 NIW 获批案例对比、排期预测及<br><span class="highlight">《NIW 申请底层逻辑库》</span>完整报告</p>
        <hr style="opacity:0.2; margin:15px 0;">
        <div style="font-size:16px; margin-bottom:10px;">👇 请扫码或搜索关注公众号</div>
        <div style="font-size:20px; font-weight:bold; color:#ffc107;">自由飞翔的蜗牛</div>
        <p style="font-size:12px; margin-top:10px; opacity:0.8;">后台回复 <span style="background:white; color:black; padding:2px 5px; border-radius:3px; font-weight:bold;">加微信</span> 获取主理人联系方式</p>
    </div>

    <p style="text-align:center; color:#ccc; font-size:11px; margin-top:30px;">技术支持：GitHub 自动化机器人</p>
</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_template)
