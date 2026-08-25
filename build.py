#!/usr/bin/env python3
"""
Dựng trang hướng dẫn sử dụng (GitHub Pages) từ tài liệu nguồn.

    python3 build.py

Nguồn sự thật là `impl/docs/03-HUONG-DAN-SU-DUNG.md` của kho chính — KHÔNG sửa
câu chữ ở đây. Mỗi chặng đồng bộ tài liệu ấy thì chạy lại lệnh trên, trang web
đổi theo. Sửa thẳng vào `index.html` là mất trắng ở lượt dựng kế tiếp.

Việc script làm, ngoài chuyện đổi Markdown sang HTML, là **chia lại tài liệu
theo vai trò người dùng**: tài liệu nguồn viết theo *việc cần làm* nên các mục
của sáu vai trò nằm xen nhau, còn người mở trang web thì chỉ muốn đọc phần của
mình. Bảng `TUYEN` ở dưới là toàn bộ phép chia ấy, và nó cố ý để lộ ra: thêm một
mục vào tài liệu nguồn mà quên khai ở đây thì mục ấy rơi vào PHẦN CHUNG, chứ
không biến mất.

Hai tệp đầu vào:

  ../impl/docs/03-HUONG-DAN-SU-DUNG.md   nội dung, chép nguyên
  vai-tro.md                             phần mở đầu của từng vai trò, viết tay

Đầu ra: `index.html` và `nguon.md` (bản chép của tài liệu nguồn, để kho guide
đứng một mình vẫn đọc và so được lịch sử).
"""
from __future__ import annotations

import html
import re
import shutil
import sys
import unicodedata
from pathlib import Path

from bien_tap import BO_QUA, DAU_HIEU, SUA

THU_MUC = Path(__file__).resolve().parent
NGUON = THU_MUC.parent / "impl" / "docs" / "03-HUONG-DAN-SU-DUNG.md"
VAI_TRO_MD = THU_MUC / "vai-tro.md"
RA = THU_MUC / "index.html"
CHEP = THU_MUC / "nguon.md"

TIEU_DE = "Hướng dẫn sử dụng — Chính sách bán hàng"
MO_TA = (
    "Hướng dẫn sử dụng phần mềm Chính sách bán hàng của Công ty Cổ phần "
    "Dinh dưỡng Nutricare, chia theo sáu vai trò người dùng."
)

# --- Sáu vai trò -------------------------------------------------------------
#
# Thứ tự ở đây là thứ tự hồ sơ đi qua luồng duyệt, không phải thứ tự abc: người
# đọc tìm vai trò của mình bằng cách nhớ mình đứng ở đoạn nào của quy trình.
VAI_TRO = [
    ("tdv", "Trình dược viên", "TDV",
     "Lập khách hàng, lập hồ sơ CSBH, gửi duyệt, sửa khi bị trả lại."),
    ("tbp", "Trưởng bộ phận", "TBP",
     "Ký số duyệt, trả lại để chỉnh sửa, từ chối hồ sơ."),
    ("ke-toan", "Kế toán", "KT",
     "Tiếp nhận lần 1, xuất hợp đồng, tiếp nhận lần 2, yêu cầu in lại."),
    ("sale-admin", "Sale Admin", "SA",
     "In bản cứng, trình ký, scan và bàn giao hồ sơ."),
    ("ban-lanh-dao", "Ban lãnh đạo", "BLĐ",
     "Chỉ xem: báo cáo, hồ sơ, lịch sử. Không có nút ghi ở bất kỳ đâu."),
    ("quan-tri", "Quản trị hệ thống", "QT",
     "Người dùng, sản phẩm, chiết khấu, văn bản mẫu, nhật ký."),
]
TEN_VAI_TRO = {ma: ten for ma, ten, _, _ in VAI_TRO}

CHUNG = "chung"

# --- Phép chia tài liệu ------------------------------------------------------
#
# Khoá là số mục trong tài liệu nguồn (`## 6. Lập hồ sơ CSBH (TDV)` -> "6").
# Mục nào không khai ở đây thì thuộc PHẦN CHUNG.
TUYEN = {
    "5": "tdv",          # Lập khách hàng
    "6": "tdv",          # Lập hồ sơ CSBH
    "9": "ke-toan",      # Xuất hợp đồng
    "12": "quan-tri",    # Người dùng
    "13": "quan-tri",    # Sản phẩm, Chiết khấu, Văn bản mẫu
}

# Bốn mục con nằm nhầm nhà trong tài liệu nguồn — chuyển sang đúng vai trò.
#
# Khoá là tiêu đề `###` SAU KHI đã gỡ nhãn ngày — `bien_tap_nguon()` chạy trước
# `cat()`, nên tiêu đề tới đây đã sạch. Để nguyên nhãn trong khoá thì không khoá
# nào khớp, mục rơi về phần chung và không có gì báo; vì thế `tuyen()` bắt buộc
# mọi khoá phải khớp đúng một mục.
CHUYEN = {
    # Nằm trong "3. Bố cục màn hình", nhưng chỉ Quản trị hệ thống vào được.
    "Nhật ký hệ thống": "quan-tri",
    # Nằm trong "9. Xuất hợp đồng", nhưng mẫu hợp đồng thuộc Quản trị hệ thống.
    "Mẫu hợp đồng (Quản trị hệ thống)": "quan-tri",
    # Hai mục này nói về màn hình hồ sơ — mọi vai trò đọc được hồ sơ đều dùng.
    "Xem và tải văn bản trên màn hình hồ sơ": CHUNG,
    "Giấy tờ hồ sơ và Bản cứng": CHUNG,
}

# --- Không dấu, để dựng neo --------------------------------------------------

def bo_dau(s: str) -> str:
    s = s.replace("đ", "d").replace("Đ", "D")
    s = unicodedata.normalize("NFD", s)
    return "".join(c for c in s if unicodedata.category(c) != "Mn")


def neo(s: str) -> str:
    s = bo_dau(s).lower()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    return s.strip("-") or "muc"


# --- Markdown ----------------------------------------------------------------

BAT_DAU_KHOI = re.compile(r"^(#{1,6}\s|>|\||```|---\s*$|[-*]\s|\d+\.\s)")

# Số mục cũ trong tài liệu nguồn -> (neo, nhãn để hiện, tiêu đề đầy đủ).
# Đổ đầy ở lượt một của `dung()`, đọc trong `inline()`.
THAM_CHIEU: dict[str, tuple[str, str, str]] = {}

# "mục 13.0" — chỉ bắt dạng CÓ DẤU. Tài liệu nguồn dẫn sang tài liệu yêu cầu
# nghiệp vụ bằng dạng KHÔNG DẤU ("muc 11.1", "muc 2.8"), và những chỗ ấy trỏ ra
# ngoài trang web này nên phải để nguyên.
DAN_MUC = re.compile(r"mục (\d+(?:\.\d+)*)")


def bien_tap_nguon(src: str) -> str:
    """Bỏ nhãn ngày và các đoạn kể chuyện cũ. Xem `bien_tap.py`."""
    # Nhãn ngày đi trước, để mọi mỏ neo trong bảng SUA viết theo câu chữ SẠCH —
    # không phải chép lại chỗ đặt nhãn, thứ đổi mỗi chặng.
    src = re.sub(r"[ \t]*`(mới|sửa)\s+\d{2}/\d{2}`", "", src)

    for tim, thay in SUA:
        # Khớp qua mọi kiểu xuống dòng, thụt đầu dòng và dấu `>` của trích dẫn:
        # tài liệu nguồn ngắt dòng thủ công ở cột 100, nên một câu nằm trên hai
        # ba dòng là chuyện thường.
        mau = re.compile(r"[\s>]+".join(re.escape(w) for w in tim.split()))
        n = len(mau.findall(src))
        if n != 1:
            sys.exit(
                f"build.py: mục biên tập khớp {n} lần, cần đúng 1 — tài liệu nguồn đã đổi.\n"
                f"  Mỏ neo: {tim[:90]}…\n"
                "  Mở impl/docs/03-HUONG-DAN-SU-DUNG.md, tìm đoạn ấy, rồi sửa mỏ neo\n"
                "  trong bien_tap.py cho khớp — hoặc bỏ mục ấy đi nếu đoạn văn không còn."
            )
        src = mau.sub(lambda _: thay, src, count=1)

    return don_dep(src)


def don_dep(src: str) -> str:
    """Dọn dấu vết của những đoạn vừa bị bỏ.

    Bỏ một đoạn nằm trong trích dẫn thì cái vỏ `>` của nó ở lại: một dòng `>`
    rỗng đầu khối, hoặc hai dòng `>` rỗng dính nhau. Markdown không thấy đó là
    lỗi — nó dựng ra một khối trích dẫn mở đầu bằng khoảng trắng.
    """
    src = re.sub(r"(?m)[ \t]+$", "", src)
    dong = src.split("\n")

    def rong_trich(d: str) -> bool:
        return re.fullmatch(r"[ \t]*>[ \t]*", d) is not None

    def la_trich(d: str) -> bool:
        return d.lstrip().startswith(">")

    ra: list[str] = []
    for i, d in enumerate(dong):
        if rong_trich(d):
            sau = dong[i + 1] if i + 1 < len(dong) else ""
            # Rỗng ở đầu khối, ở cuối khối, hoặc dính vào một dòng rỗng khác.
            if not ra or rong_trich(ra[-1]) or not la_trich(ra[-1]):
                continue
            if not la_trich(sau) or rong_trich(sau):
                continue
        ra.append(d)

    return re.sub(r"\n{3,}", "\n\n", "\n".join(ra))


def quet_con_sot(src: str, ten: str = "tài liệu nguồn") -> None:
    """Còn dấu hiệu chữ viết cho người phát triển thì DỪNG, kèm số dòng.

    Quét CẢ phần viết tay: một luật chỉ áp cho tài liệu nguồn là một luật sẽ bị
    lách ngay ở tệp mà người sửa trang web gõ nhiều nhất.
    """
    sot: list[str] = []
    for k, d in enumerate(src.split("\n"), start=1):
        if any(bq in d for bq in BO_QUA):
            continue
        for dh in DAU_HIEU:
            if re.search(dh, d):
                sot.append(f"  dòng {k}: [{dh}] {d.strip()[:96]}")
                break
    if sot:
        sys.exit(
            f"build.py: còn sót chữ viết cho người phát triển trong {ten}:\n"
            + "\n".join(sot)
            + "\n  Khai thêm mục vào bảng SUA của bien_tap.py, hoặc vào BO_QUA nếu\n"
            "  chỗ ấy dùng đúng những chữ đó mà không phải kể chuyện cũ."
        )


def chu_thuan(t: str) -> str:
    """Tiêu đề rút về chữ trơn, để dùng làm nhãn liên kết và thuộc tính title."""
    t = re.sub(r"`[^`]*`", "", t)
    return re.sub(r"\s+", " ", t.replace("*", "")).strip()


def _thoat(s: str) -> str:
    return html.escape(s, quote=False)


def nhan_manh(s: str) -> str:
    """`**đậm**` và `*nghiêng*`, lồng nhau được.

    Không dùng biểu thức chính quy: tài liệu nguồn có `**Thẻ *Đang chờ***` —
    một cụm đậm kết thúc CÙNG CHỖ với cụm nghiêng bên trong nó. Cặp regex
    "đậm trước, nghiêng sau" cắt cụm ấy thành `<strong>Thẻ *Đang chờ</strong>*`
    rồi đẻ ra thẻ chéo nhau, thứ trình duyệt tự vá mỗi nơi một kiểu.

    Nên quét một lượt trái sang phải với một ngăn xếp: mỗi dãy dấu sao vừa có
    thể đóng cụm đang mở, vừa có thể mở cụm mới; ưu tiên đóng. Dãy nào không
    làm được gì thì nhả ra thành dấu sao thật.
    """
    ra: list[str] = []
    ngan: list[str] = []
    i, n = 0, len(s)
    while i < n:
        if s[i] != "*":
            ra.append(s[i])
            i += 1
            continue
        j = i
        while j < n and s[j] == "*":
            j += 1
        dai = j - i
        # Dấu sao dính vào chữ ở bên trái thì đóng được; dính vào chữ ở bên
        # phải thì mở được. Đây là phép "flanking" rút gọn của CommonMark, đủ
        # cho tập ký hiệu mà tài liệu nguồn dùng.
        truoc = s[i - 1] if i > 0 else " "
        sau = s[j] if j < n else " "
        dong_duoc = not truoc.isspace()
        mo_duoc = not sau.isspace()
        while dai > 0:
            if dong_duoc and ngan:
                the = ngan[-1]
                can = 2 if the == "strong" else 1
                if dai >= can:
                    ra.append(f"</{the}>")
                    ngan.pop()
                    dai -= can
                    continue
            if mo_duoc:
                the = "strong" if dai >= 2 else "em"
                ra.append(f"<{the}>")
                ngan.append(the)
                dai -= 2 if the == "strong" else 1
                continue
            ra.append("*" * dai)
            dai = 0
        i = j
    # Dấu sao lẻ trong tài liệu nguồn: đóng nốt cho HTML còn hợp lệ, và kêu lên
    # để người sửa tài liệu biết mình vừa gõ thiếu một dấu.
    while ngan:
        the = ngan.pop()
        ra.append(f"</{the}>")
        print(f"build.py: CẢNH BÁO — thiếu dấu đóng <{the}> ở: {s[:70]!r}", file=sys.stderr)
    return "".join(ra)


def inline(s: str) -> str:
    """Markdown một dòng: `code`, **đậm**, *nghiêng*, [chữ](địa chỉ)."""
    kho: list[str] = []

    def cat(chuoi: str) -> str:
        kho.append(chuoi)
        return f"\x00{len(kho) - 1}\x00"

    # Dấu gạch chéo ngược đứng trước ký tự đặc biệt: giữ nguyên ký tự ấy.
    s = re.sub(r"\\([*_`\[\]|\\])", lambda m: cat(_thoat(m.group(1))), s)

    # Nhãn ngày (`sửa 21/08`) không tới được đây: `bien_tap_nguon()` đã gỡ hết
    # trước khi cắt mục, và `quet_con_sot()` canh cho không sót cái nào.
    s = re.sub(r"`([^`]+)`", lambda m: cat(f"<code>{_thoat(m.group(1))}</code>"), s)
    s = _thoat(s)
    s = nhan_manh(s)
    s = re.sub(
        r"\[([^\]]+)\]\(([^)\s]+)\)",
        lambda m: f'<a href="{html.escape(m.group(2), quote=True)}">{m.group(1)}</a>',
        s,
    )

    def dan(m: re.Match[str]) -> str:
        d = THAM_CHIEU.get(m.group(1))
        if not d:
            return m.group(0)
        n, nhan, day_du = d
        return (
            f'<a class="dan-muc" href="#{n}" '
            f'title="{html.escape(day_du, quote=True)}">mục {html.escape(nhan)}</a>'
        )

    s = DAN_MUC.sub(dan, s)
    return re.sub(r"\x00(\d+)\x00", lambda m: kho[int(m.group(1))], s)


def khoi(dong: list[str], trong_trich: bool = False) -> str:
    """Đổi một dãy dòng Markdown thành HTML. Gọi đệ quy cho trích dẫn và danh sách."""
    ra: list[str] = []
    i, n = 0, len(dong)

    while i < n:
        d = dong[i]

        if not d.strip():
            i += 1
            continue

        # Khối mã
        if d.lstrip().startswith("```"):
            i += 1
            than: list[str] = []
            while i < n and not dong[i].lstrip().startswith("```"):
                than.append(dong[i])
                i += 1
            i += 1
            ra.append("<pre><code>" + _thoat("\n".join(than)) + "</code></pre>")
            continue

        # Đường kẻ ngang
        if re.match(r"^---\s*$", d):
            ra.append("<hr>")
            i += 1
            continue

        # Tiêu đề. Bên trong trích dẫn nó là tiêu đề của chính khối cảnh báo ấy,
        # không phải một mục của tài liệu — nên không vào mục lục.
        m = re.match(r"^(#{1,6})\s+(.*)$", d)
        if m:
            chu = inline(m.group(2))
            if trong_trich:
                ra.append(f'<p class="tieu-de-trich">{chu}</p>')
            else:
                ra.append(f"<h5>{chu}</h5>")
            i += 1
            continue

        # Trích dẫn
        if d.startswith(">"):
            than = []
            while i < n and dong[i].startswith(">"):
                than.append(re.sub(r"^>\s?", "", dong[i]))
                i += 1
            ra.append("<blockquote>" + khoi(than, True) + "</blockquote>")
            continue

        # Bảng
        if d.lstrip().startswith("|"):
            hang = []
            while i < n and dong[i].lstrip().startswith("|"):
                hang.append(dong[i].strip())
                i += 1
            ra.append(bang(hang))
            continue

        # Danh sách
        m = re.match(r"^([-*]|\d+\.)\s+(.*)$", d)
        if m:
            co_so = "ol" if m.group(1)[0].isdigit() else "ul"
            muc: list[list[str]] = []
            while i < n:
                m2 = re.match(r"^([-*]|\d+\.)\s+(.*)$", dong[i])
                loai = "ol" if (m2 and m2.group(1)[0].isdigit()) else "ul"
                if not m2 or loai != co_so:
                    break
                than = [m2.group(2)]
                i += 1
                # Dòng tiếp theo thuộc về mục này chừng nào nó còn thụt vào,
                # kể cả khi cách một dòng trống.
                while i < n:
                    if dong[i].strip() and not dong[i].startswith("  "):
                        break
                    if not dong[i].strip():
                        j = i
                        while j < n and not dong[j].strip():
                            j += 1
                        if j >= n or not dong[j].startswith("  "):
                            break
                        than.extend([""] * (j - i))
                        i = j
                        continue
                    than.append(dong[i][2:])
                    i += 1
                muc.append(than)
            ben_trong = "".join(f"<li>{khoi(t, trong_trich)}</li>" for t in muc)
            ra.append(f"<{co_so}>{ben_trong}</{co_so}>")
            continue

        # Đoạn văn
        than = []
        while i < n and dong[i].strip():
            if than and BAT_DAU_KHOI.match(dong[i]):
                break
            than.append(dong[i].strip())
            i += 1
        ra.append("<p>" + inline(" ".join(than)) + "</p>")

    return "".join(ra)


def _o(hang: str) -> list[str]:
    return [c.strip() for c in hang.strip().strip("|").split("|")]


def bang(hang: list[str]) -> str:
    dau = _o(hang[0])
    than = hang[2:] if len(hang) > 1 and re.match(r"^[\s|:\-]+$", hang[1]) else hang[1:]
    ra = ["<div class='cuon-bang'><table><thead><tr>"]
    ra += [f"<th>{inline(c)}</th>" for c in dau]
    ra.append("</tr></thead><tbody>")
    for h in than:
        ra.append("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in _o(h)) + "</tr>")
    ra.append("</tbody></table></div>")
    return "".join(ra)


# --- Cắt tài liệu nguồn thành từng mục ---------------------------------------

class Muc:
    def __init__(self, cap: int, tieu_de: str):
        self.cap = cap                # 2 = `##`, 3 = `###`
        self.tieu_de = tieu_de        # còn nguyên Markdown
        self.dong: list[str] = []
        self.dich = CHUNG
        self.so = ""                  # số mục trong tài liệu nguồn, nếu có
        self.neo = ""
        self.sach = ""                # tiêu đề đã bỏ số mục cũ
        self.nhan = ""                # số hiệu mới: "A4", "B1.2" — chỉ mục cấp 2


def cat(van_ban: str) -> list[Muc]:
    """Cắt theo `##` và `###`. Bỏ phần mở đầu trước mục 1."""
    ra: list[Muc] = []
    trong_ma = False
    for d in van_ban.splitlines():
        if d.lstrip().startswith("```"):
            trong_ma = not trong_ma
        m = None if trong_ma else re.match(r"^(#{2,3})\s+(.*)$", d)
        if m:
            ra.append(Muc(len(m.group(1)), m.group(2).strip()))
        elif ra:
            ra[-1].dong.append(d)
    return ra


def tuyen(muc: list[Muc]) -> None:
    """Gán vai trò cho từng mục: `###` theo mục cha, trừ khi khai ở CHUYEN."""
    hien = CHUNG
    for m in muc:
        if m.cap == 2:
            so = re.match(r"^(\d+)\.\s+", m.tieu_de)
            m.so = so.group(1) if so else ""
            hien = TUYEN.get(m.so, CHUNG)
            m.dich = hien
        else:
            m.dich = CHUYEN.get(m.tieu_de, hien)

    # Khoá không khớp mục nào nghĩa là tiêu đề trong tài liệu nguồn đã đổi. Nếu
    # im lặng thì mục ấy rơi về phần chung — một vai trò mất một mục mà không
    # ai biết, đúng kiểu hỏng chỉ lộ ra khi có người đi tìm.
    co = {m.tieu_de for m in muc if m.cap == 3}
    lac = [k for k in CHUYEN if k not in co]
    if lac:
        sys.exit(
            "build.py: khoá CHUYEN không khớp mục nào trong tài liệu nguồn:\n"
            + "\n".join(f"  {k!r}" for k in lac)
            + "\n  Tiêu đề mục ấy đã đổi. Sửa khoá trong build.py cho khớp,\n"
            "  hoặc bỏ khoá đi nếu mục không còn."
        )

    thua = [k for k in TUYEN if k not in {m.so for m in muc if m.cap == 2}]
    if thua:
        sys.exit(f"build.py: khoá TUYEN không khớp mục nào: {', '.join(thua)}.")


def don_tieu_de(t: str) -> str:
    """Bỏ số mục của tài liệu nguồn — sau khi chia lại theo vai trò thì thứ tự
    số cũ không còn liền mạch, và một dãy 1, 2, 3, 4, 7, 8 đọc ra như bị thiếu."""
    t = re.sub(r"^\d+(\.\d+)*\.\s+", "", t)
    # "5. Lập khách hàng (TDV)" -> tên vai trò trong ngoặc đã thừa, vì mục này
    # nằm sẵn trong phần của vai trò ấy.
    t = re.sub(r"\s*\((TDV|Kế toán và Sale Admin|Quản trị hệ thống|chỉ Quản trị hệ thống)\)", "", t)
    return t.strip()


# --- Phần mở đầu viết tay cho từng vai trò -----------------------------------

def doc_vai_tro() -> dict[str, tuple[str, list[Muc]]]:
    """Đọc `vai-tro.md` -> {mã vai trò: (đoạn dẫn, các mục)}.

    Mục viết tay ra `Muc(cap=2)` y như mục lấy từ tài liệu nguồn, nên chúng đi
    qua đúng một đường đánh số, đặt neo và dựng mục lục. Ba vai trò không có mục
    `##` nào trong tài liệu nguồn — Trưởng bộ phận, Sale Admin, Ban lãnh đạo —
    nhờ vậy vẫn có mục lục riêng thay vì một thẻ rỗng.
    """
    if not VAI_TRO_MD.exists():
        sys.exit(f"build.py: không thấy {VAI_TRO_MD.name} — phần viết tay của trang.")
    tho: dict[str, list[str]] = {}
    ma = None
    for d in VAI_TRO_MD.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^##\s+([a-z-]+)\s*$", d)
        if m:
            ma = m.group(1)
            if ma not in TEN_VAI_TRO:
                sys.exit(
                    f"build.py: vai-tro.md khai vai trò '{ma}' không có trong bảng "
                    f"VAI_TRO. Mã hợp lệ: {', '.join(TEN_VAI_TRO)}."
                )
            tho[ma] = []
        elif ma is not None:
            tho[ma].append(d)

    ra: dict[str, tuple[str, list[Muc]]] = {}
    for k, dong in tho.items():
        dan: list[str] = []
        muc: list[Muc] = []
        for d in dong:
            m = re.match(r"^###\s+(.*)$", d)
            if m:
                muc.append(Muc(2, m.group(1).strip()))
            elif muc:
                muc[-1].dong.append(d)
            else:
                dan.append(d)
        ra[k] = ("\n".join(dan), muc)

    for k, (dan, muc) in ra.items():
        quet_con_sot("\n".join([dan] + [m.tieu_de for m in muc]
                                + [d for m in muc for d in m.dong]),
                     f"vai-tro.md, phần '{k}'")

    thieu = [ma for ma in TEN_VAI_TRO if ma not in ra]
    if thieu:
        sys.exit(f"build.py: vai-tro.md thiếu phần mở đầu của: {', '.join(thieu)}.")
    return ra


# --- Dựng trang --------------------------------------------------------------

def dung() -> str:
    if not NGUON.exists():
        sys.exit(
            f"build.py: không thấy tài liệu nguồn {NGUON}.\n"
            "  Chạy script này từ trong kho chính (thư mục guide là một submodule\n"
            "  của kho sale-policy-tools) — nó cần impl/docs/ ở thư mục cha."
        )
    shutil.copyfile(NGUON, CHEP)
    goc = bien_tap_nguon(NGUON.read_text(encoding="utf-8"))
    quet_con_sot(goc)

    muc = cat(goc)
    tuyen(muc)
    mo_dau = doc_vai_tro()

    # Gom theo vai trò, giữ nguyên thứ tự xuất hiện trong tài liệu nguồn.
    gio: dict[str, list[Muc]] = {CHUNG: []}
    for ma, _, _, _ in VAI_TRO:
        gio[ma] = []
    for m in muc:
        gio[m.dich].append(m)

    # Mục viết tay đứng TRƯỚC mục lấy từ tài liệu nguồn: chúng nói "việc của bạn
    # là gì", còn tài liệu nguồn nói "làm thế nào".
    for ma, (_, muc_tay) in mo_dau.items():
        gio[ma] = muc_tay + gio[ma]

    than: list[str] = []
    muc_luc: list[tuple[str, str, str, list[tuple[str, str]]]] = []
    da_dung: set[str] = set()

    def dat_neo(goi_y: str) -> str:
        g = neo(goi_y)
        n, k = g, 2
        while n in da_dung:
            n, k = f"{g}-{k}", k + 1
        da_dung.add(n)
        return n

    # LƯỢT MỘT: đặt neo và số hiệu mới cho MỌI mục, trước khi dựng thân bài.
    #
    # Phải làm trước vì tài liệu nguồn dẫn chéo sang nhau bằng số mục cũ
    # ("xem mục 11"), mà số ấy vừa bị chia lại theo vai trò nên không còn đúng.
    # Có bảng tra sẵn thì `inline()` đổi được chúng thành liên kết thật — người
    # đọc bấm là tới, và không còn con số nào để lệch.
    for ma_gio, tien_to in [(CHUNG, "A")] + [
        (ma, f"B{k}.") for k, (ma, *_) in enumerate(VAI_TRO, start=1)
    ]:
        stt = 0
        for m in gio[ma_gio]:
            m.sach = don_tieu_de(m.tieu_de)
            m.neo = dat_neo(f"{tien_to}-{m.sach}")
            if m.cap == 2:
                stt += 1
                m.nhan = f"{tien_to}{stt}"
            so = re.match(r"^(\d+(?:\.\d+)*)\.\s", m.tieu_de)
            if so:
                THAM_CHIEU[so.group(1)] = (
                    m.neo,
                    m.nhan or f"“{chu_thuan(m.sach)}”",
                    chu_thuan(m.sach),
                )

    # LƯỢT HAI: dựng thân bài.
    def ve(ds: list[Muc]) -> list[tuple[str, str]]:
        """Dựng HTML cho một nhóm mục, trả về mục lục con của nhóm ấy."""
        con: list[tuple[str, str]] = []
        for m in ds:
            if m.cap == 2:
                con.append((m.neo, m.sach))
                than.append(
                    f'<section class="muc" id="{m.neo}">'
                    f'<h3><a class="lien-neo" href="#{m.neo}">'
                    f'<span class="stt">{m.nhan}</span>{inline(m.sach)}</a></h3>'
                )
            else:
                than.append(
                    f'<section class="muc-con" id="{m.neo}">'
                    f'<h4><a class="lien-neo" href="#{m.neo}">{inline(m.sach)}</a></h4>'
                )
            than.append(khoi(m.dong))
            than.append("</section>")
        return con

    # PHẦN CHUNG
    than.append('<section class="phan" id="phan-chung">')
    than.append(
        '<h2><span class="nhan-phan">Phần A</span>Phần chung — mọi vai trò</h2>'
        "<p class='dan'>Những gì ai đăng nhập cũng gặp: cách vào phần mềm, bố cục "
        "màn hình, luồng duyệt mười bước, tìm kiếm, thống kê. Đọc một lượt phần này "
        "trước, rồi sang phần của vai trò mình.</p>"
    )
    con_chung = ve(gio[CHUNG])
    than.append("</section>")
    muc_luc.append(("phan-chung", "Phần A · Phần chung", "Mọi vai trò", con_chung))

    # PHẦN RIÊNG
    than.append('<section class="phan" id="phan-rieng">')
    than.append(
        '<h2><span class="nhan-phan">Phần B</span>Phần riêng theo vai trò</h2>'
        "<p class='dan'>Sáu vai trò, sáu phần. Bạn chỉ cần đọc phần mang tên vai trò "
        "của mình — phần mềm cũng chỉ bày cho bạn đúng những màn hình ấy.</p>"
    )
    for k, (ma, ten, _, tom) in enumerate(VAI_TRO, start=1):
        n = dat_neo(f"vai-tro-{ma}")
        than.append(f'<section class="phan-vai-tro" id="{n}">')
        than.append(
            f'<h3 class="ten-vai-tro"><a class="lien-neo" href="#{n}">'
            f'<span class="stt">B{k}</span>{html.escape(ten)}</a></h3>'
            f'<p class="dan">{html.escape(tom)}</p>'
        )
        than.append(khoi(mo_dau[ma][0].splitlines()))
        con = ve(gio[ma])
        than.append("</section>")
        muc_luc.append((n, f"Phần B{k} · {ten}", tom, con))
    than.append("</section>")

    return trang("".join(than), muc_luc)


def trang(than: str, muc_luc) -> str:
    # Mục lục ở đầu trang: mỗi phần một thẻ, bên trong là các mục của phần ấy.
    the = []
    for n, ten, tom, con in muc_luc:
        ds = "".join(f'<li><a href="#{c}">{inline(t)}</a></li>' for c, t in con)
        the.append(
            f'<article class="the-ml">'
            f'<a class="ten-the" href="#{n}">{html.escape(ten)}</a>'
            f'<p class="tom">{html.escape(tom)}</p>'
            f"<ul>{ds}</ul></article>"
        )

    ben = []
    for n, ten, _, con in muc_luc:
        ds = "".join(f'<li><a href="#{c}">{inline(t)}</a></li>' for c, t in con)
        ben.append(f'<li><a class="ben-phan" href="#{n}">{html.escape(ten)}</a><ul>{ds}</ul></li>')

    return f"""<!doctype html>
<html lang="vi">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(TIEU_DE)}</title>
<meta name="description" content="{html.escape(MO_TA)}">
<link rel="stylesheet" href="style.css">
</head>
<body>
<a class="bo-qua" href="#noi-dung">Bỏ qua, tới nội dung</a>

<header class="dau-trang">
  <div class="trong">
    <p class="cong-ty">Công ty Cổ phần Dinh dưỡng Nutricare</p>
    <h1>Hướng dẫn sử dụng<span>phần mềm Chính sách bán hàng</span></h1>
    <p class="dan-dau">Viết theo <strong>việc bạn cần làm</strong>, không theo màn hình.
    Phần chung dành cho mọi người; sáu phần còn lại, mỗi phần một vai trò.</p>
  </div>
</header>

<nav class="chon-vai-tro" aria-label="Chọn vai trò">
  <div class="trong">
    <p class="hoi">Bạn đăng nhập bằng vai trò nào?</p>
    <div class="luoi-vai-tro">
      {"".join(
        f'<a class="the-vai-tro" href="#vai-tro-{ma}">'
        f'<span class="viet-tat">{html.escape(vt)}</span>'
        f'<span class="ten">{html.escape(ten)}</span>'
        f'<span class="viec">{html.escape(tom)}</span></a>'
        for ma, ten, vt, tom in VAI_TRO)}
    </div>
  </div>
</nav>

<div class="than trong">
  <aside class="ben" aria-label="Mục lục bên">
    <p class="ben-tieu-de">Mục lục</p>
    <ul>{"".join(ben)}</ul>
  </aside>

  <main id="noi-dung">
    <section class="muc-luc" id="muc-luc">
      <h2>Mục lục</h2>
      <div class="luoi-ml">{"".join(the)}</div>
    </section>
    {than}
    <footer class="chan">
      <p>Tài liệu này dựng tự động từ <code>impl/docs/03-HUONG-DAN-SU-DUNG.md</code>
      của kho mã nguồn. Thấy chỗ nào sai thì sửa ở tài liệu ấy rồi dựng lại —
      sửa thẳng vào trang web sẽ mất ở lượt dựng kế tiếp.</p>
      <p>Phần mềm Chính sách bán hàng · Công ty Cổ phần Dinh dưỡng Nutricare</p>
    </footer>
  </main>
</div>

<a class="len-dau" href="#" aria-label="Về đầu trang">↑</a>
<script>
// Tô đậm mục đang đọc ở mục lục bên. Không có thư viện nào, và trang vẫn dùng
// được đầy đủ khi tắt JavaScript — đây chỉ là chỉ dẫn vị trí.
(function () {{
  var lien = {{}};
  document.querySelectorAll('.ben a[href^="#"]').forEach(function (a) {{
    lien[a.getAttribute('href').slice(1)] = a;
  }});
  var dich = Object.keys(lien).map(function (id) {{ return document.getElementById(id); }})
                   .filter(Boolean);
  if (!dich.length || !('IntersectionObserver' in window)) return;
  var dang = null;
  var mat = new IntersectionObserver(function (muc) {{
    muc.forEach(function (m) {{
      if (!m.isIntersecting) return;
      var a = lien[m.target.id];
      if (!a || a === dang) return;
      if (dang) dang.classList.remove('dang-doc');
      a.classList.add('dang-doc');
      dang = a;
    }});
  }}, {{ rootMargin: '-80px 0px -70% 0px' }});
  dich.forEach(function (d) {{ mat.observe(d); }});
}})();
</script>
</body>
</html>
"""


if __name__ == "__main__":
    RA.write_text(dung(), encoding="utf-8")
    print(f"build.py: đã dựng {RA.relative_to(THU_MUC)} ({RA.stat().st_size:,} byte)")
    print(f"build.py: đã chép nguồn sang {CHEP.relative_to(THU_MUC)}")
