# Hướng Dẫn Sử Dụng Template - Obsidian Vault

## Phân Biệt: Template vs Nội Dung Cá Nhân

### Template (Giữ lại - Dùng cho Phong)
Nằm trong thư mục `Templates/`, dùng để tạo ghi chú mới với cấu trúc chuẩn:

| Template | Mục Đích | Cách Dùng |
|----------|-----------|-----------|
| `Daily Note Template.md` | Tạo ghi chú hàng ngày | Ctrl+P > "Daily note" |
| `People Template.md` | Quản lý thông tin người quen | Dùng khi tạo note mới cho người |
| `Meeting Template.md` | Ghi chép cuộc họp | Dùng sau mỗi buổi gặp đối tác |
| `Project Template.md` | Quản lý dự án SCM/AI | Tạo note mới cho mỗi dự án |
| `Clipping Template.md` | Lưu bài viết hay | Dùng khi clip nội dung từ web |
| `Evergreen Template.md` | Ghi chú ý tưởng lâu dài | Dùng cho các insight học thuật |

### Nội Dung Cá Nhân Kepano (Cần Thay Thế/Xóa)

**Thư mục cần xóa hoặc thay thế:**
- `Daily/2023-09-12.md`, `Daily/2023-09-30.md` - Lịch sử của Kepano
- `Notes/2023 Japan Trip.md` - Chuyến đi của Kepano
- `Notes/2023-09-12 Meeting with Steph.md` - Cuộc họp của Kepano
- `Notes/Minimal Theme.md` - Ghi chú về theme của Kepano
- `References/Kevin Kelly.md`, `References/Steph Ango.md` - Người quen của Kepano
- `References/Blade Runner.md`, `References/Futurama.md` - Sở thích cá nhân
- `Clippings/68 Bits of Unsolicited Advice.md` - Nội dung của Kepano

**Thư mục giữ lại (xóa nội dung cũ, giữ cấu trúc):**
- `Categories/` - Giữ cấu trúc, xóa liên kết đến Kepano
- `References/` - Xóa các file cũ, dùng Template để tạo mới cho Phong

---

## Cách Sử Dụng Template Cho Sinh Viên UEH

### 1. Daily Notes (Ghi chú hàng ngày)
```
Mở Obsidian > Ctrl+P > gõ "Daily note" > Enter
```
- Tự động tạo theo `Templates/Daily Note Template.md`
- Dùng để ghi chép hằng ngày, tracking tiến độ học tập/dự án

### 2. Tạo Note Người Mới (Giảng viên, Bạn học, Đối tác)
```
Chuột phải vào thư mục References > New note > Đổi tên
Hoặc dùng Template: Ctrl+P > "Templates: Insert template" > Chọn "People Template"
```
- Điền `org: [[UEH]]` hoặc `org: [[Shopee]]` tùy vào tổ chức
- Thêm meeting vào phần "Meetings" sẽ tự động hiển thị

### 3. Ghi Chép Cuộc Họp (Meetings)
```
Tạo note mới trong thư mục Notes > Chọn "Meeting Template"
```
- `date: {{date}}` - Tự động điền ngày
- `people: [[Tên người]]` - Liên kết với People note
- `org: [[UEH]]` - Tổ chức liên quan
- `topics: [[Supply Chain]], [[AI]]` - Chủ đề thảo luận

### 4. Quản Lý Dự Án (Project Template)
Dùng cho các dự án như Hermes, Thesis, Freelance:
```
Tạo note mới > Chọn "Project Template"
```
- `status: [[In Progress]]` hoặc `[[Completed]]`
- `topics: [[AI Agent]], [[Supply Chain]]`
- Ghi chú tiến độ, rủi ro, next steps

### 5. Lưu Bài Viết Hay (Clipping Template)
```
Tạo note mới trong Clippings > Chọn "Clipping Template"
```
- `url: https://...` - Link bài gốc
- `author: [[Tên tác giả]]` - Liên kết với People note
- `topics: [[AI]], [[Operations]]` - Phân loại
- `status: [[Read]]` hoặc `[[Unread]]`

### 6. Evergreen Notes (Ý tưởng dài hạn)
Dùng cho các insight học thuật, quy tắc nghề nghiệp:
```
Tạo note mới > Chọn "Evergreen Template"
```
- Tên note phải ngắn gọn, đúng 1 ý (VD: "SCM cần AI để tối ưu")
- Dùng để xây dựng hệ thống tri thức cá nhân

---

## Lưu Ý Quan Trọng

1. **Liên kết (Links)**: Dùng `[[]]` để liên kết các note (VD: `[[Hermes]]`, `[[UEH]]`)
2. **Categories**: Mỗi note nên có ít nhất 1 category từ thư mục `Categories/`
3. **Tags**: Dùng `#` cho tags nhanh (VD: `#0🌲` cho Evergreen quan trọng)
4. **Templates folder**: Tất cả template nằm trong `Templates/`, không sửa trừ khi cần thiết
5. **Base notes**: Một số template dùng `![[xxx.base]]` để embed danh sách tự động

---

## Checklist Thay Thế Nội Dung Kepano

- [ ] Xóa `Daily/2023-*.md` (2 files)
- [ ] Xóa `Notes/2023*.md` và `Notes/Minimal*.md` (3 files)
- [ ] Xóa `References/Kevin Kelly.md`, `References/Steph Ango.md`
- [ ] Xóa `References/Blade Runner.md`, `References/Futurama.md`
- [ ] Xóa `Clippings/68 Bits of Unsolicited Advice.md`, `Clippings/Buy wisely.md`
- [ ] Kiểm tra `Categories/` - Xóa liên kết cũ đến Kepano
- [ ] Tạo note mới `References/Phong.md` cho bản thân
- [ ] Tạo note `Projects/Hermes.md` dùng Project Template
- [ ] Tạo note `Projects/Thesis.md` quản lý luận văn

---

## Lệnh Nhanh Cho Claude

Khi cần tạo note mới, hãy nói:
- "Tạo Daily note hôm nay"
- "Tạo People note cho giảng viên X"
- "Tạo Project note cho Hermes dùng template"
- "Tạo Clipping từ URL này: ..."

Anh sẽ tự động dùng đúng template và điền thông tin phù hợp.
