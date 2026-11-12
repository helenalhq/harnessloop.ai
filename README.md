# HarnessLoop 企业官网 · Revision 3

五个主页面：主页、工作原理、数据与知识工厂、实践与研究、关于与合作。另有开发预览隐私说明。

## 开发与运行
- 无第三方运行依赖，HTML/CSS/JS 静态站。
- 修改 `build.py` 中的中文正文与共享框架、`en_content.py` 中的英文正文；v3 首页与联系增强位于 `refine.py`。执行 `python3 build.py` 生成页面。
- 样式与交互源码：`dist/assets/style.css`、`dist/assets/app.js`。
- 检查：`npm test`、`node --check dist/assets/app.js`。
- 本地预览：`python3 -m http.server 4173 --directory dist`，然后打开 `http://localhost:4173`。
- 其他本地环境可用任意静态 HTTP 服务器将 `dist` 作为根目录。不可用 file:// 代替服务器。

## 已实现
- 完整中英文、冷白与墨蓝的系统工程视觉、双闭环架构与实质交付清单。
- 五页导航、850px 响应式布局与移动导航。
- 合成采购资料的三阶段可交互演示，可键盘左右/Home/End切换。
- 本地需求简报生成及复制，无后端、不发送、不持久化。
- 研究笔记展开/收起，页面跳转与无障碍焦点。

## 边界与上线前待办
- 未公开部署，未连接 harnessloop.ai，未改 DNS 或生产。
- 全站 robots 禁止抓取并带 noindex，正式发布前需审查并调整。
- 所有演示合成，所有方法/服务方向不代表已完成生产能力。
- 没有虚构客户、认证、性能提升或合作背书。
- 已添加 contact@harnessloop.ai mailto 链接；未配置或验证邮箱收信。简报仍只在本地生成，打开邮件客户端后由用户自行检查、发送。
- 正式运营主体、联系渠道和正式隐私政策待用户确认。
- 未配置生产 canonical、sitemap、分析工具或认证。

## 检查记录
- `npm test`：12 路由静态文件、站内链接与资源路径、预览索引限制、双语交互及语言选择测试通过。
- JavaScript 语法检查通过。
- 云浏览器：主页视觉检查通过，五页导航通过；演示原始提取/质量检查/候选改进及反复切换通过；表单有效字段生成和重复生成通过；研究笔记展开通过。
- 390px 宽度浏览器 iframe 视口已验证首页布局、移动菜单展开、页面切换及演示切换；不等同真实手机设备测试。
- 剪贴板路径实现含失败提示，本轮云浏览器已验证英文简报复制成功。

## 双语与视觉优化（2026-11-12）
- 中英文各六页，中文沿用根路由，英文位于 `/en/`。英文文案见 `en_content.py`。
- 页首切换保留同一页面，并仅在本地存储 `harnessloop-language` 偏好。首次首页按浏览器语言选择；直接语言链接不强制跳转。无存储权限时仍可切换。
- 暖白纸面、墨色与砖红注释，首页以合成采购资料的一个具体错误取代发光轨道装饰。
- 两种语言的表单、演示、状态提示、导航、元描述、无障碍标签和隐私说明完整覆盖。简报仅在当前页面内生成，切换语言/刷新不会保留。
- `npm test` 覆盖 12 路由、链接、英文无中文正文、双语演示/简报、安全文本输出和语言选择逻辑；JS 语法检查通过。
- 云浏览器验证：中英页面切换保留路由，英文三阶段演示、简报生成及复制成功；390px iframe 下英文导航展开、进入数据工厂、两语言切换及演示步骤键盘操作成功。不是物理手机测试。
- 本轮未部署、未改域名/DNS，原私有 Site 配置保持不变。

## 第三轮优化（2026-11-12）
- 首屏重聚焦定制 Harness 与受控进化，架构图取代采购纸张视觉；首页以服务方向、完整改进案例、试点交付物组织。
- 重写样式表，不叠加第三层覆盖；桌面/移动使用统一栅格、强排版与信号蓝。
- 中英联系页、全站页脚显示指定邮箱。简报可生成编码安全的邮件草稿链接，不自动发送、不保存输入。
- 演示增加 tabpanel/ARIA 关联、roving tabindex；候选尚未验证，不再显示绿色成功状态。
- 自动测试通过；本轮云浏览器确认桌面中文首屏、英文联系页、本地简报生成/复制/编码邮件草稿、390px iframe 首页布局/菜单展开/页面跳转/双语演示/键盘操作。不是物理手机测试。

## V4: evidence-led evolution demo
Homepage has a bilingual five-stage conceptual animation with a synthetic procurement example. It is not a real run or a claim of measured performance. Candidate A preserves source units; candidate B's inference is rejected for lacking evidence. Release remains conditional on validation and human approval.
- Stage buttons pause autoplay; Next cycles deterministically; Play resumes.
- Reduced-motion starts paused and pauses SVG motion. Visibility changes suspend timers.
- No external animation dependency, no network calls, no input collection.
- `npm test` includes bilingual/reduced-motion/state-transition tests.
