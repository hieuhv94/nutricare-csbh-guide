# Hướng dẫn sử dụng CSBH — trang web

Bản web của tài liệu **Hướng dẫn sử dụng phần mềm Chính sách bán hàng**
(Công ty Cổ phần Dinh dưỡng Nutricare), xuất bản qua GitHub Pages.

## Nguồn sự thật

Nội dung đến từ **`impl/docs/03-HUONG-DAN-SU-DUNG.md`** của kho
`sale-policy-tools`. Thư mục này là một submodule của kho ấy.

**Không sửa câu chữ trong `index.html`** — nó được dựng lại và ghi đè mỗi lần
chạy `build.py`. Sai chỗ nào thì sửa ở tài liệu nguồn rồi dựng lại.

| Tệp | Vai trò |
|---|---|
| `build.py` | Bộ dựng. Đổi Markdown sang HTML, **chia tài liệu theo sáu vai trò**, và biên tập lại cho người dùng cuối |
| `bien_tap.py` | Bảng biên tập: bỏ nhãn ngày và các đoạn kể phần mềm trước đây thế nào |
| `vai-tro.md` | Phần **viết tay**: mở đầu và các mục riêng của từng vai trò. Chỗ duy nhất được mang câu chữ không có trong tài liệu nguồn |
| `style.css` | Giao diện. Sáng/tối theo cài đặt máy người đọc, có bản in |
| `index.html` | **Sinh ra, không sửa tay** |
| `nguon.md` | Bản chép của tài liệu nguồn ở lượt dựng gần nhất, để kho này đứng một mình vẫn đọc và so được lịch sử |

## Dựng lại

```bash
python3 build.py      # chạy trong thư mục này, cần impl/docs/ ở thư mục cha
```

Không phụ thuộc thư viện ngoài, không cần Docker — chỉ Python 3 có sẵn.
Chạy xong thì mở `index.html` bằng trình duyệt để soát trước khi commit.

## Phép chia theo vai trò

Trang web có hai phần:

- **Phần A — phần chung**: những gì ai đăng nhập cũng gặp.
- **Phần B — sáu vai trò**: Trình dược viên · Trưởng bộ phận · Kế toán ·
  Sale Admin · Ban lãnh đạo · Quản trị hệ thống.

Phép chia khai ở hai bảng đầu `build.py`:

- `TUYEN` — mục `##` nào của tài liệu nguồn thuộc vai trò nào.
- `CHUYEN` — mục `###` nằm nhầm nhà, chuyển sang đúng vai trò.

**Mục mới không khai ở đâu thì rơi vào phần chung**, chứ không biến mất. Thêm
một mục vào tài liệu nguồn thì kiểm lại hai bảng ấy.

Ba vai trò — Trưởng bộ phận, Sale Admin, Ban lãnh đạo — **không có mục `##` nào
của riêng mình** trong tài liệu nguồn, vì tài liệu ấy viết theo *việc cần làm*
chứ không theo vai trò. Phần của họ viết tay trong `vai-tro.md`.

## Viết cho người dùng, không phải người phát triển

Tài liệu nguồn là tài liệu bàn giao, đọc theo từng chặng sửa: nó mang nhãn ngày
(`mới 23/08`, `sửa 21/08`) và những đoạn kể **phần mềm trước đây thế nào**. Đúng
cho người theo dõi quá trình sửa, thừa với trình dược viên đang cần biết bấm nút
nào. Trang web bỏ hai thứ ấy; tài liệu nguồn giữ nguyên.

Phép biên tập nằm ở `bien_tap.py`, và nó **tự canh mình**:

- Mỗi mục trong bảng `SUA` phải khớp **đúng một lần**. Sửa câu ấy ở tài liệu
  nguồn thì lượt dựng kế tiếp DỪNG và nói ra mỏ neo nào không còn khớp.
- Dựng xong, `DAU_HIEU` quét lại bản đã biên tập — cả `vai-tro.md`. Còn sót
  "Trước đây", "đã bỏ", một nhãn ngày hay một lệnh `make` thì DỪNG, kèm số dòng.

Nghĩa là thêm một đoạn "Trước đây…" vào tài liệu nguồn ở chặng sau sẽ **làm hỏng
lượt dựng**, chứ không lặng lẽ lên trang web.

Giữ lại các khối giải thích **vì sao phần mềm hiện tại bắt làm thế** — người
dùng cần đúng những đoạn ấy lúc thắc mắc.

## Xuất bản

GitHub Pages phục vụ thẳng nhánh `main` của kho này. Commit `index.html` là
trang đổi theo — không có bước dựng nào chạy trên máy chủ, và `.nojekyll` tắt
Jekyll để tệp được phục vụ nguyên trạng.
