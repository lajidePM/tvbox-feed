#!/usr/bin/env python3
import urllib.request
import json
import os

# 精选几个长期维护、国内直连的高质量底座源（涵盖全网网盘、4K、直连采集）
RELIABLE_SOURCES = [
    {"name": "PG优质网盘", "url": "https://raw.githubusercontent.com/guxiangbin/tvbox2/main/PG.txt"},
    {"name": "ABC综合", "url": "https://raw.githubusercontent.com/guxiangbin/tvbox2/main/ABC.txt"}
]

HEADERS = {"User-Agent": "Mozilla/5.0"}

def main():
    print("🚀 开始获取高质量底座并聚合...")
    results = []
    for s in RELIABLE_SOURCES:
        try:
            req = urllib.request.Request(s["url"], headers=HEADERS)
            with urllib.request.urlopen(req, timeout=10) as resp:
                data = json.loads(resp.read().decode("utf-8", errors="ignore"))
                results.append(data)
                print(f"✅ 获取成功: {s['name']} (包含 {len(data.get('sites', []))} 个站点)")
        except Exception as e:
            print(f"❌ 获取失败: {s['name']} -> {e}")

    if not results:
        print("未获取到数据，退出")
        return

    base = results[0]
    merged_sites = []
    seen = set()

    for data in results:
        for site in data.get("sites", []):
            k = site.get("key")
            n = site.get("name")
            if not k or not n or n in seen:
                continue
            seen.add(n)
            merged_sites.append(site)

    final_tvbox = {
        "spider": base.get("spider", ""),
        "wallpaper": "https://bing.img.run/rand.php",
        "sites": merged_sites,
        "lives": base.get("lives", []),
        "parses": base.get("parses", []),
        "rules": base.get("rules", []),
        "doh": base.get("doh", [])
    }

    out_dir = "/tmp/tvbox-feed/public"
    os.makedirs(out_dir, exist_ok=True)
    out_file = os.path.join(out_dir, "tvbox.json")
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(final_tvbox, f, ensure_ascii=False, indent=2)

    print(f"✨ 成功生成清洗聚合配置: {out_file} (总计 {len(merged_sites)} 个精选去重站点)")

if __name__ == "__main__":
    main()
