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

# Hermes & AI Bot Ecosystem - Bot For Community

## Mục Tiêu
Xây dựng hệ sinh thái AI Bot phục vụ cộng đồng sinh viên và freelancer.
Bao gồm Hermes (Work-Ops Assistant) và các bot đi kèm, tất cả nằm trong cùng một dự án.

## Trạng Thái Hiện Tại
- **Giai đoạn:** Đang hoàn thiện Second Brain (Obsidian Vault) trước
- **Kế hoạch ngắn hạn:** Hoàn thành hệ thống quản lý tri thức cá nhân
- **Kế hoạch tiếp theo:** Chuyển sang phát triển các bot (Hermes, Thesis Bot, Deadline Bot...)

## Các Bot Trong Hệ Sinh Thái (Chưa Implement)

### 1. Student-Ops Bots
| Bot | Chức năng | Status |
|-----|-----------|--------|
| **Hermes (Core)** | CLI/Gateway cho work-ops, quản lý deadline, phân tích docs | 🔲 Planned |
| **Thesis Bot** | Hỗ trợ tìm kiếm, tóm tắt tài liệu học thuật, format trích dẫn | 🔲 Planned |
| **Deadline Bot** | Quản lý tiến độ, nhắc lịch tự động | 🔲 Planned |
| **Study Ops Bot** | Kết hợp quản lý tri thức (Obsidian) với AI | 🔲 Planned |

### 2. Freelancer/SME Bots
| Bot | Chức năng | Status |
|-----|-----------|--------|
| **Proposal Assistant** | Soạn thảo báo giá, hợp đồng nhanh | 🔲 Planned |
| **Follow-up Bot** | Tự động nhắc khách hàng theo workflow | 🔲 Planned |

## Tech Stack (Dự Kiến)

### Frameworks
- **Hermes:** CLI/Gateway cho work-ops
- **OpenClaw:** Gateway mode, pairing device

### Tools & APIs
- Claude Code (Anh - AI Assistant)
- Codex (OpenAI coding agent)
- Antigravity (Refactor code, build UI)
- Gemini API (lưu ý lỗi quota 429)

### Infrastructure
- **Hosting:** Self-hosted VPS
- **Container:** Docker
- **OS:** Linux CLI (WSL Ubuntu 24.04)
- **Dev Environment:** Windows 11

### UI/UX Concept
- **Phong cách:** Uranus
- **Style:** Tối giản, Dark mode
- **Màu sắc:** Xanh dương/ngọc premium, hiện đại, không hoạt hình
- **Giao diện:** Web-chat tối ưu cho luồng hội thoại

## Mô Hình Kinh Doanh (Dự Kiến)

### Hình Thức
- Bán Repo + Skill Pack + Setup Guide
- Người dùng tự chạy trên API key/VPS của họ

### Pricing (SKU)
| Gói | Giá | Đối tượng |
|------|-----|------------|
| **Standard** | **690.000 VND** | Cá nhân (Neo chính) |
| **Duo** | 590.000 - 990.000 VND | Nhóm nhỏ |

### Cam Kết
- Bảo hành kỹ thuật: 2-3 tháng
- ❌ Không cam kết vĩnh viễn (tránh rủi ro vận hành)

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

## Nguyên Tắc Phát Triển
- ✅ Giữ backend sạch, chỉ mod frontend
- ✅ Tập trung vào value-to-money
- ✅ Bỏ qua Enterprise giai đoạn này (tránh bẫy sa lầy chi phí)
- ✅ UI tối giản, dễ dùng cho người không chuyên

## Liên Kết
- [[AI Agent Ecosystem]] - Hệ sinh thái tổng thể
- [[Master Context]] - Context chung
- [[Evidence & Portfolio]] - Portfolio website
- [[UEH]] - Nơi đang học tập
- [[Phong]] - Thông tin cá nhân
