# TVBox / 影视仓 自动化聚合订阅源

基于 GitHub Actions 每天自动化抓取全网优质 4K / 网盘 / 直链影视源，经过清洗去重后，自动分发到 Cloudflare 全球 CDN。

## 📺 影视仓 / TVBox 接口配置地址

复制以下链接直接填入电视软件：

- **🌟 全网精选聚合单仓接口**：
  `https://tvbox-live.pages.dev/tvbox.json`

- **📦 影视仓专用多仓接口**：
  `https://tvbox-live.pages.dev/multi.json`

- **🌐 网页版查看与一键复制**：
  `https://tvbox-live.pages.dev/`

## ⚙️ 自动化机制
- 每天北京时间凌晨 04:00 自动触发更新
- 自动剔除失效与重复源
- 纯云端无服务器运行，永久免费
