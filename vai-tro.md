# Phần mở đầu của từng vai trò

Tệp này là phần **viết tay** của trang web, và là chỗ DUY NHẤT trong thư mục
`guide/` được phép mang câu chữ không có trong tài liệu nguồn.

Vì sao cần: tài liệu nguồn viết theo *việc cần làm*, nên ba vai trò **Trưởng bộ
phận**, **Sale Admin** và **Ban lãnh đạo** không có mục `##` nào của riêng
mình — phần việc của họ nằm rải trong các mục nói về luồng duyệt. Mở trang web
ra mà phần mang tên vai trò mình trống trơn thì người đọc kết luận là phần mềm
không có gì cho họ.

Cách viết:

- `## <mã vai trò>` mở một vai trò. Mã phải khớp cột thứ nhất của bảng `VAI_TRO`
  trong `build.py`.
- `### <tiêu đề>` là một mục của vai trò ấy. Mỗi mục được đánh số và vào mục lục
  đúng như mục lấy từ tài liệu nguồn — `build.py` không phân biệt hai nguồn.
- Chữ nằm trước `###` đầu tiên là đoạn dẫn, đứng ngay dưới tên vai trò.
- Các mục viết tay đứng **trước** các mục lấy từ tài liệu nguồn.

**Không chép nội dung từ tài liệu nguồn vào đây** — dẫn sang bằng một câu là đủ.
Chép sang là dựng ra bản thứ hai của cùng một luật, và hai bản sẽ lệch nhau.

## tdv

Bạn là người **mở đầu** mọi hồ sơ. Không ai lập hồ sơ CSBH thay bạn được, và
sau khi gửi duyệt thì cũng không ai sửa nội dung thay bạn được — hồ sơ phải đi
một vòng trả lại mới về tay bạn.

### Việc của bạn

| Việc | Ở đâu |
|---|---|
| Lập khách hàng, đính giấy tờ pháp lý | *Khách hàng* → **Tạo khách hàng** |
| Lập hồ sơ CSBH, nhập từng dòng sản phẩm | *Hồ sơ CSBH* → **Lập hồ sơ** |
| Chọn văn bản mẫu, chọn Trưởng bộ phận và Kế toán, gửi duyệt | Nút **Gửi duyệt** trên màn hình hồ sơ |
| Sửa lại khi bị trả về, rồi gửi lại | *Việc của tôi* trên trang Tổng quan |

**Dải thẻ của bạn**: Yêu cầu chỉnh sửa · Sắp quá hạn · Quá hạn · Đang chờ ·
Đang có hiệu lực · Từ chối.

Khối *Việc của tôi* của bạn gồm **cả hồ sơ Nháp** chưa gửi duyệt, không chỉ hồ
sơ bị trả lại — hồ sơ đang viết dở cũng là việc của bạn. Vì vậy dải thẻ không có
ô *Nháp* riêng.

> **Hai thứ đóng băng lúc bạn bấm *Gửi duyệt***: giá cùng ngưỡng chiết khấu của
> từng dòng, và thông tin khách hàng in trên bản CSBH. Đọc kỹ bản A4 trong hộp
> thoại gửi duyệt — đó là lần cuối nội dung còn sửa được mà không phải đi một
> vòng trả lại.

### Riêng bạn mới làm được

Ba việc dưới đây không vai trò nào khác thay được, **kể cả Quản trị hệ thống**:

- **Xoá một khách hàng** bạn phụ trách. Quan hệ với khách hàng là việc của người
  phụ trách họ.
- **Xoá một hồ sơ** của bạn, ở *Nháp*, *Yêu cầu chỉnh sửa* hoặc *Từ chối*.
- **Đính kèm và gỡ giấy tờ hồ sơ**, lúc hồ sơ còn sửa được.

> Đổi lại, có một việc **bạn không làm được**: đổi *Trình dược viên phụ trách*
> của một khách hàng. Đó là quyền của Sale Admin và Quản trị hệ thống.

## tbp

Bạn là **chữ ký đầu tiên** trên hồ sơ. Hồ sơ chỉ tới bàn bạn khi Trình dược
viên đích danh chọn tên bạn ở bước gửi duyệt — Trưởng bộ phận khác không nhìn
thấy hồ sơ ấy và cũng không mở được.

### Ba nút, và chỉ ba nút

Mở một hồ sơ đang ở *Chờ TBP duyệt*, dải thao tác ở góc trên bên phải có đúng ba
lựa chọn:

| Nút | Hồ sơ đi đâu | Có quay lại được không |
|---|---|---|
| **Ký số duyệt** | Sang thẳng *KT duyệt bản mềm* | Không. Ký xong bạn **không tham gia bước nào nữa** |
| **Trả lại chỉnh sửa** | Về tay Trình dược viên, ở *Yêu cầu chỉnh sửa* | Có — họ sửa rồi gửi lại, và có thể gửi cho Trưởng bộ phận khác |
| **Từ chối hồ sơ** | Đóng **vĩnh viễn** | Không. Không ai xoá được hồ sơ đã từ chối, kể cả Quản trị hệ thống |

Hai nút sau **bắt buộc nhập lý do**. Lý do ấy đi vào *Lịch sử hồ sơ* và không ai
sửa hay xoá được, kể cả bạn.

> **Hồ sơ bị trả lại rồi gửi lại thì chữ ký của bạn bị huỷ.** Hồ sơ đi lại toàn
> bộ vòng duyệt và phải được ký lại — có thể bởi một Trưởng bộ phận khác, nếu
> người lập chọn khác. Dấu ký cũ vẫn nằm trong *Lịch sử hồ sơ*.

### Đọc gì trước khi ký

- **Khối vàng phía trên bảng dòng sản phẩm.** Nó chỉ hiện khi hồ sơ đang lệch
  với danh mục hiện tại — giá đã đổi, quy định chiết khấu đã đổi hoặc bị xoá,
  sản phẩm đã vô hiệu hoá. Hồ sơ đã gửi duyệt thì **đóng băng số**, nên không có
  gì khác trên màn hình nói ra điều đó, và **không có thư báo nào cho việc này**.
- **Cột *Tỷ lệ CK* tô màu.** Đỏ là vượt ngưỡng; vàng là dòng ấy không có quy
  định chiết khấu nào phủ, nên **không có ngưỡng để đối chiếu**. Bấm dấu `?`
  cạnh con số để biết vượt bao nhiêu so với ngưỡng nào.
- **Vượt ngưỡng KHÔNG bị phần mềm chặn.** Nó chỉ được đánh dấu để bạn nhìn
  thấy — quyết định vẫn là của bạn.

### Màn hình của bạn

**Dải thẻ**: Chờ TBP duyệt · Sắp quá hạn · Quá hạn · Đang chờ · Đang có hiệu lực
· Từ chối. Cuối trang Tổng quan còn một bảng **hồ sơ theo từng trình dược
viên** — bấm một dòng là ra danh sách hồ sơ của người đó.

Ở màn hình *Thống kê*, bạn soi được **từng trình dược viên đã gửi hồ sơ tới bàn
bạn**: xếp hạng, cơ cấu chất lượng (ký thẳng · trả lại 1 lần · trả lại từ 2 lần
· từ chối · đang xử lý), và **số ngày sửa lại** — quãng từ lúc bạn trả lại tới
lúc họ gửi lại, ăn thẳng vào hạn 14 ngày của chính hồ sơ ấy. Nhịp mặc định của
bạn là **tuần**.

> **Bạn không xuất hợp đồng.** Nút *Xuất hợp đồng* không hiện với vai trò này ở
> bất kỳ hồ sơ nào — đó là việc của Kế toán và Sale Admin, sau khi tiếp nhận
> lần 1.

## ke-toan

Bạn cầm hồ sơ **hai lần**, ở hai đầu của đoạn giữa quy trình. Hai lần ấy là hai
màn hình khác nhau nhưng cùng một người: hồ sơ tiếp nhận lần 2 **tự về đúng
người đã nhận lần 1**, không ai chọn lại.

### Ba việc, theo thứ tự

1. **Tiếp nhận lần 1** — nhận bản mềm sau khi Trưởng bộ phận ký. Ở bước này bạn
   **chọn Sale Admin** sẽ in và trình ký bản cứng.
2. **Xuất hợp đồng** — mở được ngay sau khi tiếp nhận lần 1.
3. **Tiếp nhận lần 2** — nhận lại bản cứng đã ký và scan. **Đây là lúc CSBH bắt
   đầu có hiệu lực**, không phải lúc Trưởng bộ phận ký.

Ở cả hai lần bạn đều **trả lại chỉnh sửa** được, và hồ sơ về tay Trình dược viên
kèm lý do bạn ghi.

> **Bản cứng in sai thì đừng trả lại hồ sơ.** Ở lần 2 có riêng thao tác **yêu
> cầu in lại**: hồ sơ sang thẻ *Lỗi bản cứng* của Sale Admin, bản scan cũ **vẫn
> còn** để đối chiếu, và nội dung hồ sơ không phải đi lại vòng duyệt.

### Màn hình của bạn

**Dải thẻ**: KT duyệt bản mềm · KT duyệt bản cứng · Sắp quá hạn · Quá hạn · Đang
chờ · Đang có hiệu lực.

Khối *Việc của tôi* của bạn là **một danh sách duy nhất** gộp cả lần 1 lẫn lần
2, xếp theo hạn gần nhất trước, mỗi dòng có nhãn trạng thái riêng màu. Tách đôi
thì hai nửa dùng chung một thanh phân trang, nên việc gấp nhất có thể rơi xuống
trang sau.

Cuối trang Tổng quan có bảng **hồ sơ theo từng trình dược viên**. Nhịp mặc định
của màn hình *Thống kê* với bạn là **tuần**.

## sale-admin

Bạn là người **duy nhất chạm vào bản giấy**. Cả quy trình trước và sau bạn đều
là màn hình; đoạn của bạn là in ra, mang đi ký, rồi đưa trở lại vào phần mềm.

### Một vòng của bạn

1. Kế toán tiếp nhận lần 1 và chọn tên bạn — hồ sơ vào thẻ **Trình ký**.
2. In bản CSBH, trình Ban lãnh đạo ký, nhận lại bản giấy.
3. **Scan** và tải lên khối *Bản cứng* của hồ sơ.
4. Bàn giao — hồ sơ sang *KT duyệt bản cứng*.

**Hai thẻ của bạn trông giống nhau nhưng là hai việc khác hẳn:**

| Thẻ | Nghĩa | Việc phải làm |
|---|---|---|
| **Trình ký** | Kế toán vừa nhận bản mềm | In, trình ký, scan, tải lên |
| **Lỗi bản cứng** | Kế toán nhận bản cứng rồi **bắt in lại** | Đối chiếu bản scan cũ xem giấy hỏng ở đâu, in lại, **gỡ bản cũ và tải bản mới lên** |

Thẻ *Lỗi bản cứng* tô vàng vì đó là việc lẽ ra không phải làm.

### Bản cứng là của riêng bạn

**Chỉ bạn thêm và gỡ được bản cứng đã scan.** Bản scan là bản giấy mang chữ ký,
do chính bạn in ra và mang đi — không ai khác cầm nó trong tay. Ngược lại, bạn
**không** gỡ được giấy tờ mà Trình dược viên đã đính từ lúc lập hồ sơ, dù hai
khối nằm cạnh nhau trên cùng màn hình.

> **Ai đã tải bản scan xuống là một câu hỏi có câu trả lời.** Mỗi lượt tải bản
> cứng để lại một dòng trong *Lịch sử hồ sơ*, kèm tên người và thời điểm. Mở tệp
> bằng nút *Xem* thì không ghi gì.

Trang Tổng quan của bạn còn hiện **cảnh báo đỏ khi chưa có mẫu hợp đồng nào đang
áp dụng** — lúc đó Kế toán không xuất được hợp đồng.

### Hai việc ngoài luồng duyệt

- **Xuất hợp đồng** — bạn dùng được như Kế toán, sau khi hồ sơ qua tiếp nhận
  lần 1.
- **Đổi Trình dược viên phụ trách một khách hàng** — chỉ bạn và Quản trị hệ
  thống làm được. Đây không phải đổi một cái tên: **mọi hồ sơ của khách hàng ấy
  sang tay theo**, và người cũ thôi nhìn thấy họ.

> **Bạn không tải mẫu hợp đồng lên** — việc ấy thuộc Quản trị hệ thống. Nhưng
> bạn vẫn xuất hợp đồng và vẫn **chọn mẫu nào** ở từng lượt xuất.

## ban-lanh-dao

Vai trò này **chỉ đọc**. Không có nút ghi ở bất kỳ màn hình nào — không phải bị
ẩn đi, mà là không tồn tại: máy chủ từ chối mọi đường ghi của vai trò này.

### Bạn thấy nhiều hơn mọi người

- **Cả 11 trạng thái** trên dải thẻ, thay vì chỉ vài bước như các vai trò trong
  luồng.
- **Toàn bộ hồ sơ của công ty**, kể cả hồ sơ còn **Nháp** của người khác — bạn
  là vai trò duy nhất đọc được chúng.
- **Từng trình dược viên** ở màn hình *Thống kê*: xếp hạng, xu hướng sáu kỳ,
  biểu đồ **phân tán** (trục ngang số CSBH có hiệu lực, trục dọc tỷ lệ bị trả
  lại — vùng xanh nhạt là nơi nên nằm), và **chiết khấu bình quân theo nhóm sản
  phẩm** kèm số dòng vượt ngưỡng.
- Trang Tổng quan: **sức khoẻ luồng duyệt**, hồ sơ đang tắc ở bước nào, top 5
  trình dược viên.

Nhịp mặc định của màn hình *Thống kê* với bạn là **quý**; đổi sang tuần, tháng
hay năm bằng một cú bấm.

> **Bốn chỉ số hiệu quả đo việc chạy hồ sơ, KHÔNG đo doanh số.** Phần mềm không
> có dữ liệu bán hàng. *Tổng giá thu về* là tổng trên các tờ CSBH, không phải
> tiền đã bán được.

> **Hồ sơ Nháp chưa có bản mềm.** Mở một hồ sơ Nháp của người khác rồi bấm *Xem
> bản mềm*, phần mềm báo rằng hồ sơ chưa gửi duyệt nên chưa có bản mềm. Đó không
> phải lỗi: văn bản mẫu chỉ gắn vào hồ sơ lúc Trình dược viên gửi duyệt.

### Hai thứ bạn không có

- **Mục *Nhật ký*** hệ thống — đó là màn hình của Quản trị hệ thống. Chuyện một
  hồ sơ đã đi qua tay ai thì *Lịch sử hồ sơ* trong chính hồ sơ ấy kể, đầy đủ hơn
  và đúng phạm vi hơn.
- **Khối *Hoạt động gần đây*** trên trang Tổng quan — cũng không có, và cùng
  một lý do.

> **Chữ ký của bạn nằm ngoài phần mềm.** Ở bước B8, Sale Admin in bản CSBH ra
> giấy và mang tới cho bạn ký tay. Phần mềm không có bước nào cho việc ấy — nó
> chỉ nhận lại bản scan sau khi bạn đã ký.

## quan-tri

Bạn dựng và giữ **cái nền** mà năm vai trò kia đứng lên: tài khoản, danh mục sản
phẩm và giá, quy định chiết khấu, văn bản mẫu.

### Bạn đứng ngoài luồng duyệt

Không hồ sơ nào chờ bạn, và trang Tổng quan của bạn **không có con số hồ sơ
nào** — hồ sơ không thuộc phạm vi dữ liệu của vai trò này, nên mọi ô sẽ là 0 và
đọc ra nghĩa sai. Thay vào đó là thư hỏng chưa xử lý, số người dùng, số tài
khoản chưa kích hoạt hoặc đang bị khoá, số sản phẩm đang áp dụng, và nhật ký gần
đây.

Ở màn hình *Thống kê*, thay cho con số hồ sơ bạn có **hoạt động của hệ thống
theo kỳ**, đếm từ nhật ký, trong cửa sổ **6 tháng** gần nhất.

### Dựng một hệ mới, theo thứ tự này

| Bước | Việc | Vì sao phải trước |
|---|---|---|
| 1 | **Nhóm sản phẩm** | Chưa có nhóm nào thì nút *Tạo sản phẩm* không bấm được |
| 2 | **Sản phẩm**, rồi **đặt giá** cho từng cái | Sản phẩm chưa có giá thì không lập được hồ sơ với nó |
| 3 | **Quy định chiết khấu** | Không có thì dòng hồ sơ không có ngưỡng để đối chiếu |
| 4 | **Văn bản mẫu** | Có sẵn một mẫu mặc định cho mỗi khổ giấy, nên bước này hoãn được |
| 5 | **Tài khoản**: Trưởng bộ phận → Kế toán → Sale Admin → Trình dược viên | Trình dược viên chỉ **gửi** được hồ sơ khi đã có TBP và Kế toán **đã kích hoạt** để chọn |

Thứ tự này không bị phần mềm ép, nhưng đi khác thì phải quay lại.

> **Bạn không phát mật khẩu cho ai.** Tạo tài khoản không đặt mật khẩu; thư mời
> là đường duy nhất để tài khoản có mật khẩu. Đổi lại, **địa chỉ email phải
> đúng** — gõ nhầm thì thư mời vào hộp thư người khác, và người đó đặt được mật
> khẩu cho tài khoản ấy.

### Bốn việc bạn không làm được

Và không phải do thiếu quyền — phần mềm không có chức năng ấy cho bất kỳ ai:

- **Duyệt, ký hay xử lý bất kỳ hồ sơ nào.**
- **Xoá một khách hàng** — chỉ Trình dược viên phụ trách chính khách đó.
- **Xoá người dùng** — nhật ký kiểm toán tham chiếu tới tài khoản. Vô hiệu hoá
  là cách duy nhất để một tài khoản ngừng hoạt động.
- **Đổi vai trò của một tài khoản** — vô hiệu hoá tài khoản cũ kèm bàn giao, rồi
  tạo tài khoản mới.
