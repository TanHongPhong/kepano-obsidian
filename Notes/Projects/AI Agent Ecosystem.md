---
categories:
  - "[[Projects]]"
  - "[[AI Agent]]"
type: ["[[Bot for Community]]", "[[Product]]"]
org: ["[[UEH]]"]
start: 2026-05-07
year: 2026
url: https://github.com/tan-hong-phong/bot-for-community
status: "[[Planned]]"
---

# AI Bot Ecosystem - Hermes & OpenClaw (Bot for Community)

## Trạng Thái Hiện Tại
- **Giai đoạn:** Đang hoàn thiện Second Brain (Obsidian Vault)
- **Ưu tiên ngắn hạn:** Hoàn thành hệ thống quản lý tri thức cá nhân
- **Kế hoạch tiếp theo:** Chuyển sang phát triển các bot trong hệ sinh thái

## Hệ Sinh Thái Kỹ Thuật

### Frameworks
- **Hermes:** CLI/Gateway cho work-ops (Core của hệ sinh thái)
- **OpenClaw:** Gateway mode, pairing device

### Công Cụ Hỗ Trợ
- Claude Code (Anh - AI Assistant)
- Codex (OpenAI coding agent)
- Antigravity (Refactor code, build UI)

### Infrastructure
- Self-hosted: VPS
- Container: Docker
- OS: Linux CLI (WSL Ubuntu 24.04)
- API: Gemini API (lưu ý lỗi quota 429)

### UI/UX Concept
- **Phong cách:** Uranus
- **Style:** Tối giản, Dark mode
- **Màu sắc:** Xanh dương/ngọc premium
- **Yêu cầu:** Sạch, hiện đại, không hoạt hình
- **Giao diện:** Web-chat tối ưu cho luồng hội thoại

## Danh Mục Sản Phẩm (MVP Roadmap)

### 1. Bot Sinh Viên (Student-Ops)
| Bot | Chức năng | Status |
|-----|-----------|--------|
| **Hermes (Core)** | CLI/Gateway work-ops, quản lý deadline | 🔲 Planned |
| **Thesis Bot** | Hỗ trợ tìm kiếm, tóm tắt tài liệu học thuật | 🔲 Planned |
| **Deadline Bot** | Quản lý tiến độ, nhắc lịch tự động | 🔲 Planned |
| **Study Ops Bot** | Kết hợp quản lý tri thức (Obsidian) với AI | 🔲 Planned |

### 2. Bot Freelancer/SME
| Bot | Chức năng | Status |
|-----|-----------|--------|
| **Proposal Assistant** | Soạn thảo báo giá, hợp đồng nhanh | 🔲 Planned |
| **Follow-up Bot** | Tự động nhắc khách hàng theo workflow | 🔲 Planned |

## Mô Hình Kinh Doanh & Đóng Gói

### Hình Thức
- Bán Repo + Skill Pack + Setup Guide
- Người dùng tự chạy trên API key/VPS của họ
- **Lưu ý:** Hermes và các bot là MỘT dự án (Bot for Community)

### Giá Cả (SKU)
| Gói | Giá | Đối tượng |
|------|-----|------------|
| **Standard** | **690.000 VND** | Neo chính (cá nhân) |
| **Duo** | 590.000 - 990.000 VND | Nhóm nhỏ |

### Cam Kết
- Bảo hành kỹ thuật: 2-3 tháng
- ❌ Không cam kết vĩnh viễn (tránh rủi ro vận hành)

## Nguyên Tắc Phát Triển
- Giữ backend sạch, chỉ mod frontend
- Tập trung vào value-to-money
- Bỏ qua Enterprise giai đoạn này (tránh bẫy sa lầy chi phí)
- Ưu tiên hoàn thành Second Brain trước khi làm bot

## Tiến Độ Phát Triển

### Ngắn Hạn (Hiện Tại)
- [x] Setup Second Brain (Obsidian Vault)
- [ ] Hoàn thiện Obsidian Vault (Metadata, Templates, Links)
- [ ] Viết documentation cho Second Brain system

### Trung Hạn (Sau khi xong Second Brain)
- [ ] Setup Hermes core (CLI/Gateway)
- [ ] Integrate OpenClaw (Gateway mode)
- [ ] Build UI theo Uranus concept (Dark mode)
- [ ] Tích hợp Claude API & Gemini API
- [ ] Build Thesis Bot (ưu tiên đầu tiên)
- [ ] Build Deadline Bot
- [ ] Build Study Ops Bot
- [ ] Package & Pricing (Standard 690k VND)
- [ ] Viết Setup Guide & Skill Pack

### Dài Hạn
- [ ] Test với sinh viên thực tế
- [ ] Launch MVP 1.0
- [ ] Build Proposal Assistant & Follow-up Bot
- [ ] Mở rộng cho SME

## Liên Kết
- [[Hermes]] - Chi tiết dự án Bot for Community
- [[Evidence & Portfolio]] - Portfolio website
- [[Master Context]] - Context chung
- [[UEH]] - Nơi đang học tập
- [[Phong]] - Thông tin cá nhân
