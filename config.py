import os

# ==========================================
# 1. CẤU HÌNH ĐƯỜNG DẪN THƯ MỤC (PATHS)
# ==========================================
# Khai báo sẵn các thư mục để các file khác gọi ra dùng, tránh gõ sai chính tả
RAW_DIR = 'Scrawl_html'
OUT_DS1_DIR = 'Dataset 1'
OUT_DS2_DIR = 'Dataset 2'

# ==========================================
# 2. BỘ TỪ KHÓA TÌM KIẾM (KEYWORDS)
# ==========================================
# Dùng để quét và phân loại nhóm khách hàng cho Dataset 2
KEYWORDS_N234 = {
    'Hành chính': ['cơ quan', 'hành chính', 'sự nghiệp'],
    'Sản xuất': ['sản xuất', 'bán trực tiếp'],
    'Kinh doanh': ['kinh doanh', 'dịch vụ']
}

# ==========================================
# 3. ÁNH XẠ FILE HTML & ĐỊNH TUYẾN BÓC TÁCH (MAPPINGS)
# ==========================================
# Chứa tham số để vượt qua các bẫy cấu trúc ẩn của từng file HTML
# table_idx: Vị trí của bảng chứa giá tiền (đã cộng hao phí các bảng tiêu đề ẩn)
# price_col: Vị trí cột chứa con số giá tiền trong bảng đó
FILE_MAPPINGS = {
    'hanoi.html': {
        'name': 'Hà Nội', 
        'table_idx': 1, 
        'price_col': 3
    }, 
    'haiphong.html': {
        'name': 'Hải Phòng', 
        'table_idx': 1, 
        'price_col': 3
    },
    'danang.html': {
        'name': 'Đà Nẵng', 
        'table_idx': 2, 
        'price_col': 2
    },
    'cantho.html': {
        'name': 'Cần Thơ', 
        'table_idx': 1, 
        'price_col': 2
    },
    'hochiminhcity.html': {
        'name': 'BR-VT', 
        'table_idx': 2, 
        'price_col': 2
    }
}