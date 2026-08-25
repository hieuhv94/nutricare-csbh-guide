"""
BẢNG BIÊN TẬP: bỏ phần viết cho người phát triển ra khỏi trang web.

Tài liệu nguồn `impl/docs/03-HUONG-DAN-SU-DUNG.md` là tài liệu bàn giao, đọc
theo từng chặng sửa: nó mang nhãn ngày (`mới 23/08`, `sửa 21/08`) và những đoạn
kể **phần mềm trước đây thế nào**. Đúng cho người theo dõi quá trình sửa, thừa
với trình dược viên đang cần biết bấm nút nào.

Trang web bỏ hai thứ ấy. Tài liệu nguồn KHÔNG đụng tới.

Ba loại việc, và ranh giới giữa chúng là câu hỏi *đoạn này nói về cái gì*:

  BỎ    đoạn kể phần mềm ngày trước ra sao — "Trước đây ô tự chèn dấu chấm…"
  VIẾT  đoạn vừa kể chuyện cũ vừa nói luật hiện hành — giữ vế thứ hai
  GIỮ   đoạn giải thích vì sao phần mềm HIỆN TẠI bắt làm thế. Người dùng cần
        đúng những đoạn ấy lúc thắc mắc, nên chúng ở lại nguyên.

Cách khớp: viết `tim` thành MỘT dòng. `build.py` khớp qua mọi kiểu xuống dòng,
thụt đầu dòng và dấu `>` của trích dẫn, nên không phải chép lại cách ngắt dòng
của tài liệu nguồn. Đổi lại, mỗi mục phải khớp **đúng một lần**: sửa câu ấy ở
tài liệu nguồn thì lượt dựng kế tiếp DỪNG và nói ra mục nào không còn khớp, chứ
không lặng lẽ xuất bản đoạn cũ.

`thay = ""` nghĩa là bỏ hẳn.
"""

SUA: list[tuple[str, str]] = [
    # --- 1. Đăng nhập --------------------------------------------------------
    (
        'Trước đây phần mềm tin ngay phiên cũ lưu trên máy: nó dựng trang Tổng quan lên rồi mới phát hiện phiên đã chết, và bạn nhận một ô báo *phiên hết hạn* đè lên một trang trống mà mình chưa hề đăng nhập để vào. Nghỉ vài ngày rồi mở lại là gặp đúng cảnh ấy.',
        "",
    ),

    # --- 3. Bố cục màn hình --------------------------------------------------
    (
        '**Vì sao Đăng xuất không còn bày sẵn.** Trước đây nó là một nút đứng ngay cạnh thẻ tên — tức là sát ngay chỗ người ta bấm để vào xem thông tin của mình. Bấm trượt một lần là mất phiên **và mất cả biểu mẫu đang nhập dở**. Giờ nó cần hai cú bấm có chủ ý.',
        '**Vì sao Đăng xuất không bày sẵn.** Một nút Đăng xuất đứng ngay cạnh thẻ tên là đứng sát chỗ người ta bấm để xem thông tin của mình; bấm trượt một lần là mất phiên **và mất cả biểu mẫu đang nhập dở**. Nằm trong menu thì nó cần hai cú bấm có chủ ý.',
    ),
    (
        'Dòng cũ ghi trước ngày 22/08 để trống ô này — phần mềm **không tra bù** tên hiện tại vào một việc của quá khứ.',
        'Dòng nào để trống ô này thì cứ để trống — phần mềm **không tra bù** tên hiện tại vào một việc của quá khứ.',
    ),
    (
        '**Phần mềm không nói bừa khi chưa hỏi được máy chủ**. Trước đây vài chỗ tra hỏng mà màn hình vẫn trả lời dứt khoát — *"khách hàng chưa có CSBH nào"*, *"không có mục nào khớp"* — trong khi sự thật chỉ là lượt gọi ấy hỏng. Nay những chỗ đó nói đúng là chưa tra được, kèm nút thử lại.',
        '**Phần mềm không nói bừa khi chưa hỏi được máy chủ.** Một câu dứt khoát như *"khách hàng chưa có CSBH nào"* hay *"không có mục nào khớp"* chỉ hiện khi đã tra được thật. Lượt tra hỏng thì màn hình nói đúng là chưa tra được, kèm nút thử lại.',
    ),

    # --- 4. Trang tổng quan --------------------------------------------------
    (
        'Vì vậy dải thẻ không còn ô *Nháp* riêng: một con số ở trên rồi lại chính danh sách ấy ở dưới là bắt bạn đọc hai lần cùng một chuyện.',
        'Vì vậy dải thẻ không có ô *Nháp* riêng: một con số ở trên rồi lại chính danh sách ấy ở dưới là bắt bạn đọc hai lần cùng một chuyện.',
    ),
    (
        '**Vì sao gộp lại.** Trước đây đây là hai danh sách tách rời dùng chung một thanh phân trang — nên một trang có thể toàn hồ sơ lần 1 trong khi lần 2 nằm ở trang sau, và nửa dưới báo *"không có hồ sơ nào chờ tiếp nhận lần 2"* dù thật ra vẫn còn. Gộp lại thì thứ tự theo hạn đúng trên toàn danh sách, và việc gấp nhất luôn nằm ở đầu bất kể nó thuộc lần nào.',
        '**Vì sao một danh sách chứ không phải hai.** Tách đôi thì hai nửa dùng chung một thanh phân trang, nên một trang có thể toàn hồ sơ lần 1 trong khi lần 2 nằm ở trang sau. Xếp chung thì thứ tự theo hạn đúng trên toàn danh sách, và việc gấp nhất luôn nằm ở đầu bất kể nó thuộc lần nào.',
    ),
    (
        'Khối *Hoạt động gần đây* đã gỡ cùng lượt với mục menu *Nhật ký* — chuyện một hồ sơ đã đi qua tay ai thì *Lịch sử hồ sơ* trong chính hồ sơ ấy kể.',
        'Không có khối *Hoạt động gần đây*, cũng không có mục menu *Nhật ký* — chuyện một hồ sơ đã đi qua tay ai thì *Lịch sử hồ sơ* trong chính hồ sơ ấy kể.',
    ),

    # --- 5. Lập khách hàng ---------------------------------------------------
    (
        'Trước 20/08 mọi vai trò ghi đều tải lên được, cho mọi khách trong phạm vi của mình. Giấy tờ pháp lý là thứ TDV xin của khách và mang về — ba vai trò kia không cầm bản gốc bao giờ.',
        'Giấy tờ pháp lý là thứ Trình dược viên xin của khách và mang về — ba vai trò kia không cầm bản gốc bao giờ.',
    ),
    (
        '**Gỡ giấy tờ** là việc mới. Trước đó tải nhầm là nằm lại vĩnh viễn, và cách duy nhất để sửa là tải thêm bản đúng rồi để hai bản cạnh nhau — người đọc sau không biết bản nào dùng được.',
        '**Tải nhầm thì gỡ được.** Để hai bản cạnh nhau thì người đọc sau không biết bản nào dùng được.',
    ),
    (
        '**Ba ô Tỉnh/thành · Bệnh viện–điểm bán · Kênh bán đã bỏ.** Ngưỡng chiết khấu chỉ phụ thuộc nhóm sản phẩm và loại khách hàng, nên ba ô ấy không còn ảnh hưởng tới bất kỳ con số nào. Dữ liệu đã nhập của chúng không còn nữa; muốn lọc theo địa bàn thì dùng ô **Địa chỉ đăng ký**.',
        '**Không có ô Tỉnh/thành, Bệnh viện–điểm bán hay Kênh bán.** Ngưỡng chiết khấu chỉ phụ thuộc nhóm sản phẩm và loại khách hàng, nên ba ô ấy không ảnh hưởng tới con số nào. Muốn lọc theo địa bàn thì dùng ô **Địa chỉ đăng ký**.',
    ),

    # --- 6. Lập hồ sơ CSBH ---------------------------------------------------
    (
        'Trước đây ô tự chèn dấu chấm ngay giữa lúc gõ, và nó **hỏng khi bật bộ gõ tiếng Việt**: bộ gõ giữ bộ đệm riêng cho chữ đang gõ, ô nhập chèn thêm ký tự vào giữa là bộ đệm lệch, lượt sửa kế tiếp của bộ gõ ăn nhầm chữ số — gõ đủ bảy phím mà số tiền ra thiếu hoặc thừa số. Giờ ô không đụng vào chữ bạn đang gõ nữa, nên bật hay tắt bộ gõ cũng cho ra cùng một con số.',
        'Ô nhập **không đụng vào chữ bạn đang gõ**, nên bật hay tắt bộ gõ tiếng Việt cũng cho ra cùng một con số.',
    ),

    # --- 7. Luồng duyệt ------------------------------------------------------
    (
        'Trước 19/08, lần Trưởng bộ phận ký số sinh hai thư về cùng một giây cho kế toán, vì hệ thống ghi thêm một bước trung gian *TBP đã ký số* mà không ai nhìn thấy. Bước ấy đã bỏ: ký xong là hồ sơ sang thẳng *KT duyệt bản mềm*.',
        'Trưởng bộ phận ký xong thì hồ sơ sang thẳng *KT duyệt bản mềm*, không qua bước trung gian nào.',
    ),
    (
        'Trước đây mục này tên là *Nhật ký* và nằm ở một màn hình riêng, vào bằng một liên kết nhỏ dưới mã hồ sơ. Đổi tên vì phần mềm còn một *Nhật ký* nữa — nhật ký kiểm toán toàn hệ thống của Quản trị — và hai thứ khác hẳn phạm vi mà trùng tên thì luôn phải hỏi lại đang nói cái nào.',
        'Đừng nhầm nó với *Nhật ký* của Quản trị hệ thống: đó là nhật ký kiểm toán của **toàn hệ thống**, còn mục này chỉ kể một hồ sơ.',
    ),
    (
        'Địa chỉ cũ **vẫn dùng được**: liên kết trong những lá thư *để biết* đã gửi đi vẫn mở đúng nơi.',
        "",
    ),
    (
        'Hai loại dòng *Tải bản mềm CSBH* và *Tải bản hợp đồng* ghi trước 20/08 đã **xoá hẳn**: phần mềm chưa bàn giao nên chúng đều là dấu vết của bản demo và của các lượt chạy thử.',
        "",
    ),
    (
        '**Hộp xem tự khớp theo hình dáng tệp**. Trước đây hộp có một cỡ cố định cho mọi thứ, nên tờ A4 ngang thành một dải bẹp kẹp giữa hai vệt xám, còn ảnh chụp thì nằm lọt thỏm. Nay hộp mang đúng hình của thứ bên trong: bản mềm khổ ngang thì hộp rộng ra, ảnh dọc thì hộp cao lên, và hộp giãn tới hết chỗ màn hình cho phép.',
        '**Hộp xem tự khớp theo hình dáng tệp.** Bản mềm khổ ngang thì hộp rộng ra, ảnh dọc thì hộp cao lên, và hộp giãn tới hết chỗ màn hình cho phép.',
    ),
    (
        '**Không ai chọn mẫu ở đây nữa**. Trước đó hộp này hỏi bạn chọn mẫu trước khi xem. Mẫu giờ là một phần của hồ sơ: Trình dược viên chọn một lần lúc gửi duyệt, và từ đó **mọi người xem đúng một bản**.',
        '**Không ai chọn mẫu ở đây.** Mẫu là một phần của hồ sơ: Trình dược viên chọn một lần lúc gửi duyệt, và từ đó **mọi người xem đúng một bản**.',
    ),
    (
        'Vì sao đổi: mỗi mẫu có bố cục và **tập cột riêng** — một mẫu đủ mười cột để đối chiếu nội bộ, một mẫu bốn cột để đưa khách hàng. Khi ai xem cũng tự chọn thì hai người mở cùng một hồ sơ có thể thấy hai bảng giá khác nhau, và bản đem đi ký không nhất thiết là bản người lập đã đọc.',
        'Vì sao: mỗi mẫu có bố cục và **tập cột riêng** — một mẫu đủ mười cột để đối chiếu nội bộ, một mẫu bốn cột để đưa khách hàng. Nếu ai xem cũng tự chọn thì hai người mở cùng một hồ sơ sẽ thấy hai bảng giá khác nhau, và bản đem đi ký không nhất thiết là bản người lập đã đọc.',
    ),
    (
        '**Không còn hỏi khổ giấy nữa**. Khổ giấy nằm sẵn trong file mẫu mà Quản trị soạn: mẫu ngang thì bản mềm ra ngang. Hỏi riêng khổ giấy là bắt bạn ghép hai mảnh mà phần mềm ghép được — bạn chọn *bản trình bày*, còn khổ giấy đi theo nó.',
        '**Không có ô chọn khổ giấy.** Khổ giấy nằm sẵn trong file mẫu mà Quản trị soạn: mẫu ngang thì bản mềm ra ngang. Bạn chọn *bản trình bày*, còn khổ giấy đi theo nó.',
    ),

    # --- 9. Xuất hợp đồng ----------------------------------------------------
    (
        'Trước đây có hai nút, trong đó nút xuất tải thẳng về máy: nghĩa là đường duy nhất để biết hợp đồng trông thế nào lại là đường không cho nhìn trước, nên người ta tải, mở ra, thấy sai mẫu, rồi tải lại — mỗi lượt là một dòng trong *Lịch sử*.',
        "",
    ),
    (
        '**Đổi chủ.** Trước 20/08 mục này thuộc Sale Admin. Sale Admin không mất gì trong công việc hằng ngày: họ vẫn xuất hợp đồng và vẫn chọn mẫu nào lúc xuất — chỉ không tải mẫu lên nữa.',
        '**Sale Admin không tải mẫu lên**, nhưng vẫn xuất hợp đồng và vẫn chọn mẫu nào ở từng lượt xuất.',
    ),
    (
        '**Bảng sản phẩm của hợp đồng cũng do hệ thống dựng**. Trước đó nó là một bảng vẽ tay bốn cột với nhóm khoá `san_pham.`; giờ đặt `{{bang_san_pham}}` và **chọn cột** như mẫu hồ sơ. Cùng một cách làm cho cả hai loại mẫu, và tập cột đổi được mà không phải vẽ lại bảng.',
        '**Bảng sản phẩm của hợp đồng cũng do hệ thống dựng.** Đặt `{{bang_san_pham}}` và **chọn cột** như mẫu hồ sơ — cùng một cách làm cho cả hai loại mẫu, và tập cột đổi được mà không phải vẽ lại bảng.',
    ),
    (
        'Có sẵn một file mẫu hợp đồng để sửa: `templates/mau-hop-dong-a4-doc.docx` trong bộ mã.',
        'Phần mềm có sẵn một file mẫu hợp đồng để tải về sửa.',
    ),
    (
        '**Vì sao tách.** Trước đó cả hai nằm chung một khối tên *Bản cứng*, nên Trình dược viên mở một hồ sơ **Nháp** ra là thấy vùng kéo thả nằm dưới đúng cái tiêu đề ấy — đọc ra là *"tôi đang tải bản cứng lên lúc hồ sơ còn nháp"*, một câu vô lý: bản cứng là bản giấy đã ký, nó chưa tồn tại cho tới khi Sale Admin trình ký xong ở bước B8.',
        '**Vì sao hai khối riêng.** Bản cứng là bản giấy đã ký — nó chưa tồn tại cho tới khi Sale Admin trình ký xong ở bước B8. Để chung một khối thì Trình dược viên mở hồ sơ **Nháp** ra sẽ thấy vùng kéo thả nằm dưới đúng tiêu đề *Bản cứng*, đọc ra là *"tôi đang tải bản cứng lên lúc hồ sơ còn nháp"*, một câu vô lý.',
    ),
    (
        'Trước 20/08 cả bốn vai trò trong luồng đều tải lên và gỡ được. Bản scan là bản giấy có chữ ký khách hàng, do chính Sale Admin in ra, trình ký rồi scan lại',
        'Bản scan là bản giấy có chữ ký khách hàng, do chính Sale Admin in ra, trình ký rồi scan lại',
    ),

    # --- 10. Tìm kiếm và bộ lọc ---------------------------------------------
    (
        '**Vì sao chọn thay vì gõ.** Mã khách hàng và nhóm sản phẩm là mã có thật trong danh mục. Trước đây phải nhớ và gõ đúng; gõ sai một ký tự thì kết quả rỗng, và không có gì phân biệt *"không có hồ sơ nào"* với *"bạn gõ sai mã"*.',
        '**Vì sao chọn thay vì gõ.** Mã khách hàng và nhóm sản phẩm là mã có thật trong danh mục. Bắt gõ tay thì sai một ký tự là kết quả rỗng, và không có gì phân biệt *"không có hồ sơ nào"* với *"bạn gõ sai mã"*.',
    ),
    (
        'Ba tiêu chí cũ đã bỏ: **địa chỉ đăng ký**, **mã số thuế**, và **người đề nghị** (gộp vào *TDV phụ trách*).',
        "",
    ),

    # --- 11. Thống kê và xuất Excel -----------------------------------------
    (
        'Trang này trước mang tên *Báo cáo* và bày lại chính những con số của trang **Tổng quan**. Từ 22/08 nó trả lời một câu hỏi khác hẳn:',
        'Trang này trả lời một câu hỏi khác hẳn trang **Tổng quan**:',
    ),
    (
        'Địa chỉ cũ `/bao-cao` vẫn mở được và dẫn tới đúng màn hình này.',
        "",
    ),
    (
        'Trước đây nút nằm ở trang Thống kê, cách bộ lọc một màn hình, nên nó chỉ xuất được **tất cả** hồ sơ trong phạm vi.',
        "",
    ),
    (
        '**Bỏ hai cột *Số dòng sản phẩm* và *Tổng giá thu về***. Chúng là con số của cả hồ sơ nên lặp lại y nguyên trên mọi dòng của hồ sơ ấy, và cộng cả cột là cộng thừa gấp mấy lần. Không mất gì: số dòng là số dòng của hồ sơ trong file, còn tổng giá thu về là tổng cột *Giá thu về* — để Excel cộng hộ thì chính xác hơn.',
        '**Không có cột *Số dòng sản phẩm* và *Tổng giá thu về*.** Chúng là con số của cả hồ sơ nên sẽ lặp lại y nguyên trên mọi dòng của hồ sơ ấy, và cộng cả cột là cộng thừa gấp mấy lần. Không thiếu gì: số dòng đếm ngay trong file, còn tổng giá thu về là tổng cột *Giá thu về* — để Excel cộng hộ thì chính xác hơn.',
    ),
    (
        '*Chiết khấu cao nhất (%)* vẫn còn, vì nó là một phép **lớn nhất** chứ không phải phép cộng: lặp lại bao nhiêu lần thì giá trị lớn nhất của cột vẫn đúng.',
        'Cột *Chiết khấu cao nhất (%)* thì có, vì nó là một phép **lớn nhất** chứ không phải phép cộng: lặp lại bao nhiêu lần thì giá trị lớn nhất của cột vẫn đúng.',
    ),
    (
        'Khối cột này đứng **ở cuối**. Thứ tự 16 cột cũ giữ nguyên để công thức Excel bạn đã dựng trên file cũ không hỏng.',
        'Khối cột này đứng **ở cuối**, sau 16 cột thông tin hồ sơ.',
    ),

    # --- 12. Người dùng ------------------------------------------------------
    (
        'Nhãn thẻ **không còn con số đếm**. Danh sách do máy chủ cắt trang nên con số duy nhất màn hình biết là tổng *sau khi lọc* — dán nó lên nhãn thẻ thì nó tụt xuống mỗi lần bạn gõ vào ô tìm. Tổng vẫn nói ra, ở thanh phân trang dưới bảng.',
        'Nhãn thẻ **không có con số đếm**. Danh sách do máy chủ cắt trang nên con số duy nhất màn hình biết là tổng *sau khi lọc* — dán nó lên nhãn thẻ thì nó tụt xuống mỗi lần bạn gõ vào ô tìm. Tổng nói ra ở thanh phân trang dưới bảng.',
    ),
    (
        'Trước đây hai ô ấy nằm ở đây, và chúng đẻ ra một kiểu hỏng im lặng: gán nhầm một Kế toán vào ô người duyệt thì hồ sơ đi vào ngõ cụt — người đó không có thao tác *Ký số duyệt* nào để làm, hồ sơ đứng im tới lúc quá hạn và không màn hình nào nói vì sao. Bỏ trống ô ấy còn tệ hơn: Trình dược viên không gửi được hồ sơ nào cả, mà chỉ biết điều đó ở lần gửi đầu tiên.',
        'Gán cứng ở đây thì hỏng im lặng: gán nhầm một Kế toán vào ô người duyệt là hồ sơ đi vào ngõ cụt — người đó không có thao tác *Ký số duyệt* nào để làm, hồ sơ đứng im tới lúc quá hạn và không màn hình nào nói vì sao.',
    ),

    # --- 13. Văn bản mẫu, Sản phẩm, Chiết khấu -------------------------------
    (
        '**Không xoá được mẫu nữa**. Từ khi mẫu hồ sơ gắn vào hồ sơ lúc gửi duyệt, xoá một mẫu nghĩa là làm hỏng vĩnh viễn bản mềm của mọi hồ sơ đã dùng nó — mà hồ sơ thì khoá sửa từ lúc ấy, nên không ai chữa được.',
        '**Không xoá được mẫu.** Mẫu hồ sơ gắn vào hồ sơ lúc gửi duyệt, nên xoá một mẫu là làm hỏng vĩnh viễn bản mềm của mọi hồ sơ đã dùng nó — mà hồ sơ thì khoá sửa từ lúc ấy, nên không ai chữa được.',
    ),
    (
        '**Không còn ban hành, không còn nháp.** Mọi mẫu trong danh sách đều dùng được ngay — lưu được là dùng được.',
        '**Không có bước ban hành, không có bản nháp.** Mọi mẫu trong danh sách đều dùng được ngay — lưu được là dùng được.',
    ),
    (
        '(Trước 20/08 là 13 — mục *thông tin công ty* rời khỏi danh sách cùng lúc với khoá của nó, và giờ do người soạn tự chịu trách nhiệm.)',
        "",
    ),
    (
        '**Bỏ ép *Trạng thái* và *Thời gian duyệt***. Hai mục ấy **còn đổi** trong lúc hồ sơ đi qua luồng duyệt',
        '***Trạng thái* và *Thời gian duyệt* không bị ép.** Hai mục ấy **còn đổi** trong lúc hồ sơ đi qua luồng duyệt',
    ),
    (
        '**Bộ file mẫu soạn sẵn** trong thư mục `templates/` của bộ mã: `mau-ho-so-a4-doc.docx`, `mau-ho-so-a4-ngang.docx`, một bản **rút gọn** gần sát mức tối thiểu (từ 24/08 nó rộng hơn đúng hai ô: *Trạng thái* và *Thời gian duyệt*, hai mục vừa thôi bị ép), và `mau-hop-dong-a4-doc.docx`. Tải một file về, sửa câu chữ trong Word, rồi tải lên. Bản demo (`make demo-mau`) nạp sẵn ba file đầu; mẫu hợp đồng thì không, ai cần tự tải lên.',
        '**Bộ file mẫu soạn sẵn** đi kèm phần mềm: một mẫu CSBH khổ A4 dọc, một mẫu A4 ngang, một bản **rút gọn** gần sát mức tối thiểu, và một mẫu hợp đồng. Tải một file về, sửa câu chữ trong Word, rồi tải lên.',
    ),
    (
        'Đổi lại, phần mềm **không còn tự bảo đảm** mục *CPBH* của muc 11.1 có mặt trên bản A4 — bạn soạn mẫu, bạn quyết.',
        'Đổi lại, phần mềm **không tự bảo đảm** mục *CPBH* có mặt trên bản A4 — bạn soạn mẫu, bạn quyết.',
    ),
    (
        'Cả hai ô lọc chạy **ở máy chủ, trên toàn bộ danh mục**. Trước đây màn hình chỉ tải 200 sản phẩm đầu rồi lọc tại chỗ, nên vượt con số ấy là gõ đúng tên một mặt hàng có thật vẫn ra "không tìm thấy" — mà không gì báo cho bạn biết mình chỉ đang tìm trong một phần.',
        'Cả hai ô lọc chạy **ở máy chủ, trên toàn bộ danh mục** — không phải chỉ trong những dòng đang hiện trên màn hình.',
    ),
    (
        'Ô gõ tự do cũ khớp cả mã, cả phạm vi, cả con số ngưỡng đang hiện — nhưng nó chỉ tìm trong **200 dòng đầu**, nên vượt con số đó là gõ đúng mã vẫn ra "không tìm thấy". Hai ô chọn lọc trên **toàn bộ** bảng quy định.',
        'Hai ô chọn lọc trên **toàn bộ** bảng quy định, không phải chỉ trong những dòng đang hiện trên màn hình.',
    ),
    (
        'Cột **"Độ cụ thể"** đã bỏ. Nó là con số nội bộ để xếp thứ tự ưu tiên; cột *Áp dụng cho* ngay bên cạnh đã nói rõ dòng nào hẹp hơn dòng nào, và câu hỏi *"hồ sơ này lấy ngưỡng từ đâu"* giờ trả lời bằng cột *Id* cộng cột *QĐCK*.',
        'Không có cột *Độ cụ thể* — nó là con số nội bộ để xếp thứ tự ưu tiên. Cột *Áp dụng cho* ngay bên cạnh đã nói rõ dòng nào hẹp hơn dòng nào, còn câu hỏi *"hồ sơ này lấy ngưỡng từ đâu"* thì cột *Id* cộng cột *QĐCK* trả lời.',
    ),
    (
        '**Danh mục tra cứu đã bỏ.** Khối tỉnh/thành · bệnh viện · kênh bán dưới bảng quy định không còn: ngưỡng chỉ khớp theo **nhóm sản phẩm × loại khách hàng**, và ba danh mục ấy không còn ô nào để điền vào.',
        '**Không có danh mục tra cứu tỉnh/thành, bệnh viện hay kênh bán.** Ngưỡng chỉ khớp theo **nhóm sản phẩm × loại khách hàng**.',
    ),
    (
        '**Người ký đã gỡ khỏi phần mềm.** Yêu cầu cho chức năng này chưa đủ rõ: chưa xác định người ký dùng ở đâu trong luồng và ai gán cho hồ sơ nào. Sẽ dựng lại sau khi chốt yêu cầu.',
        "",
    ),

    # Hai chỗ dẫn sang muc 11.1 của tài liệu YÊU CẦU NGHIỆP VỤ — người dùng
    # không có tài liệu ấy trong tay, nên số mục không nói gì với họ.
    (
        'Khác đúng một chỗ: mẫu hợp đồng **không có mục bắt buộc nào**, vì muc 11.1 chỉ nói về bản CSBH A4.',
        'Khác đúng một chỗ: mẫu hợp đồng **không có mục bắt buộc nào** — danh sách mục bắt buộc chỉ áp cho bản CSBH A4.',
    ),
    (
        'Khác nhau ở luật: mẫu hồ sơ có mục bắt buộc theo muc 11.1, mẫu hợp đồng thì không có mục nào.',
        'Khác nhau ở luật: mẫu hồ sơ có mục bắt buộc, mẫu hợp đồng thì không có mục nào.',
    ),

    # "Xem **13.0** ở trên" — chỗ duy nhất dẫn sang mục khác mà KHÔNG có chữ
    # "mục" đứng trước, nên bộ dựng không nhận ra để đổi thành liên kết. Số mục
    # thì đã bị đánh lại, nên để nguyên là trỏ vào hư không.
    (
        'Xem **13.0** ở trên: một màn hình, hai thẻ',
        'Xem mục 13.0 ở trên: một màn hình, hai thẻ',
    ),

    # --- 16. Những gì hệ thống không làm -------------------------------------
    (
        '**Nhập dữ liệu CSBH cũ từ Excel** đang hoãn sang giai đoạn 2.',
        '**Không nhập được dữ liệu CSBH cũ từ Excel.**',
    ),
]

# Dấu hiệu của chữ viết cho người phát triển. Sau khi biên tập xong, `build.py`
# quét lại bản đã sửa: còn sót dấu nào thì DỪNG, kèm số dòng.
#
# Đây là cái chốt giữ cho bảng trên khỏi mục: tài liệu nguồn thêm một đoạn
# "Trước đây…" ở chặng sau mà không ai khai vào đây thì lượt dựng kế tiếp kêu,
# chứ không lặng lẽ đẩy nó lên trang web.
DAU_HIEU = [
    r"Trước đây",
    r"Trước đó",
    r"Trước \d{2}/\d{2}",
    r"Từ \d{2}/\d{2}",
    r"đã bỏ",
    r"đã gỡ",
    r"cũ đã",
    r"Vì sao đổi",
    r"`(mới|sửa) \d{2}/\d{2}`",
    r"make demo",
    r"bộ mã",
    r"muc \d+\.\d+",
]

# Chỗ dùng đúng những chữ trên nhưng KHÔNG phải kể chuyện cũ. Khai ở đây để
# phép quét bỏ qua — kèm lý do, vì một danh sách miễn trừ không có lý do thì
# lượt sau không ai dám xoá khỏi nó.
BO_QUA = [
    # "Bỏ trống một ô nghĩa là mọi giá trị" — nói về cách khai quy định chiết
    # khấu, không phải về một ô đã bị gỡ khỏi phần mềm.
    "Bỏ trống một ô nghĩa là",
    # Ngày ở đây là ngày hiệu lực của giá, do người dùng khai — không phải mốc
    # sửa phần mềm.
    "Giá hiện hành là dòng mới nhất",
]
