# Hướng Dẫn Sử Dụng Obsidian Vault Cho Sinh Viên UEH

## Tổng Quan Sau Khi Dọn Dẹp

Vault này đã được làm sạch:
- ✅ Đã xóa toàn bộ nội dung cá nhân của Kepano (Daily notes, References, Clippings cũ)
- ✅ Giữ lại toàn bộ Templates trong thư mục `Templates/`
- ✅ Giữ lại cấu trúc Categories trong thư mục `Categories/`
- ✅ Tạo sẵn note mẫu: `[[Phong]]`, `[[UEH]]`, `[[Hermes]]`

---

## Cách Sử Dụng Hàng Ngày

### 1. Tạo Daily Note (Quan trọng nhất)
- **Cách 1:** Nhấn `Ctrl+P` → gõ "Daily note" → Enter
- **Cách 2:** Nhấn nút "Open today's note" trên ribbon trái
- **Kết quả:** Tạo file `Daily/2026-05-07.md` tự động theo template

Dùng Daily note để:
- Ghi chép bài học hôm nay
- Tracking tiến độ dự án Hermes/Thesis
- Note lại các ý tưởng mới về AI/SCM

### 2. Tạo Note Người Mới (Giảng viên, Bạn học, Đối tác)
```
1. Vào thư mục References/
2. Chuột phải → New note → Đặt tên (VD: "Nguyen Van A")
3. Nhấn Ctrl+P → "Templates: Insert template" → Chọn "People Template"
```
Hoặc nói với anh: *"Tạo People note cho giảng viên X"*

### 3. Ghi Chép Cuộc Họp (Meetings)
Dùng khi họp nhóm, gặp mentor, phỏng vấn:
```
1. Tạo note mới trong Notes/ (VD: "2026-05-07 Meeting with Mentor")
2. Chèn "Meeting Template"
3. Điền thông tin:
   - date: 2026-05-07
   - people: [[Mentor Name]]
   - org: [[UEH]]
   - topics: [[AI]], [[Thesis]]
```

### 4. Quản Lý Dự Án (Projects)
Dùng cho Hermes, Thesis, Freelance projects:
```
1. Tạo note trong Notes/Projects/ (VD: "Hermes.md")
2. Dùng "Project Template"
3. Cập nhật status: [[In Progress]] → [[Completed]]
```

### 5. Lưu Bài Viết Hay (Clippings)
Khi đọc được bài hay về SCM/AI:
```
1. Tạo note trong Clippings/
2. Dùng "Clipping Template"
3. Điền url, author, topics
```

---

## Các Lệnh Nói Với Anh (Claude)

Anh có thể giúp bạn tạo note nhanh:

| Yêu cầu | Anh sẽ làm |
|---------|------------|
| "Tạo Daily note hôm nay" | Tạo note ngày hiện tại |
| "Tạo People note cho giảng viên Y" | Tạo note người với template |
| "Tạo Project note cho Thesis" | Tạo note dự án với template |
| "Tạo Clipping từ URL này" | Tạo note lưu bài viết |
| "Tìm tất cả note về AI" | Tìm kiếm liên kết `[[AI]]` |
| "Liên kết note X với Y" | Thêm `[[Y]]` vào note X |

---

## Cấu Trúc Thư Mục Quan Trọng

```
📁 Vault Root
├── 📁 Templates/          # Template files (KHÔNG XÓA)
├── 📁 Categories/         # Phân loại note (KHÔNG XÓA)
├── 📁 Daily/              # Ghi chú hàng ngày (tự tạo)
├── 📁 Notes/              # Ghi chú cá nhân, dự án
│   └── 📁 Projects/       # Các dự án lớn (Hermes, Thesis...)
├── 📁 References/         # People, Places, Organizations
├── 📁 Clippings/          # Bài viết, tài liệu hay
└── 📁 .claude/            # Hướng dẫn cho AI (đã có sẵn)
    ├── TEMPLATE_GUIDE.md  # Chi tiết cách dùng template
    └── USAGE_GUIDE.md     # File này (hướng dẫn tổng quan)
```

---

## Tips Cho Sinh Viên UEH

1. **Liên kết là sức mạnh:** Dùng `[[Tên note]]` để liên kết mọi thứ
   - VD: Trong note `[[Hermes]]`, hãy thêm `[[AI Agent]]`, `[[UEH]]`

2. **Dùng Tags cho tìm kiếm nhanh:**
   - `#0🌲` - Evergreen notes quan trọng
   - `#thesis` - Liên quan luận văn
   - `#hermes` - Liên quan dự án Hermes

3. **Daily Notes là trung tâm:**
   - Mỗi tối dành 5 phút tạo Daily note cho ngày mai
   - Ghi lại 3 việc quan trọng cần làm (Next Actions)

4. **Projects tracking:**
   - Mỗi dự án 1 note
   - Cập nhật `status:` khi có thay đổi
   - Dùng checklist `- [ ]` cho tasks

---

## Checklist Bắt Đầu

- [x] Đã xóa nội dung Kepano
- [x] Đã tạo note `[[Phong]]`
- [x] Đã tạo note `[[UEH]]`
- [x] Đã tạo note `[[Hermes]]`
- [ ] Tạo Daily note hôm nay (2026-05-07)
- [ ] Tạo note `[[Thesis]]` cho luận văn
- [ ] Thêm giảng viên hướng dẫn vào References/
- [ ] Tạo Clipping đầu tiên từ bài viết hay

---

**Bắt đầu thôi!** Mở Obsidian và tạo Daily note đầu tiên cho ngày hôm nay.
Anh sẵn sàng hỗ trợ bạn xây dựng Second Brain chuyên nghiệp. 🚀
