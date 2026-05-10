## Danh Sách Bằng Chứng

```dataview
TABLE without id
file.name as "Dự án/Bằng chứng",
type as "Loại",
org as "Tổ chức",
status as "Trạng thái"
FROM "Notes/Projects" OR "Notes"
WHERE contains(type, "Portfolio") OR contains(type, "Evidence")
SORT start DESC
```

---

**Tags:** #evidence #portfolio #overview
