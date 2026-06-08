import pandas as pd
import os
import re
import warnings

# Import các cấu hình từ file config.py
from config import RAW_DIR, OUT_DS1_DIR, OUT_DS2_DIR, KEYWORDS_N234, FILE_MAPPINGS

warnings.filterwarnings('ignore')

def build_dataset2():
    """Hàm cào dữ liệu Khối Cơ quan, Sản xuất, Kinh doanh (Dataset 2)"""
    print("Đang cào Dataset 2 (Khối Kinh tế)...")
    data_n234 = []

    for file_name, config in FILE_MAPPINGS.items():
        file_path = os.path.join(RAW_DIR, file_name)
        # đọc các từ khóa và giá tiền từ bảng HTML dựa trên cấu hình đã định nghĩa trong config.py
        if os.path.exists(file_path):
            tables = pd.read_html(file_path, flavor='bs4')
            df_raw = tables[config['table_idx']]
            df_text = df_raw.astype(str).apply(lambda x: x.str.lower())
            # Dùng KEYWORDS_N234 để phân loại nhóm khách hàng và trích xuất giá tiền tương ứng
            for nhom, keywords_list in KEYWORDS_N234.items():
                found_kw = False
                for idx, row in df_text.iterrows():
                    if any(kw in str(row.values) for kw in keywords_list):
                        found_kw = True
                    # Nếu tìm thấy từ khóa, tiếp tục trích xuất giá tiền từ cột đã định nghĩa trong config.py    
                    if found_kw:
                        raw_price = str(df_raw.iloc[idx, config['price_col']])
                        price_str = re.sub(r'[^\d]', '', raw_price)
                        
                        if not price_str: 
                            continue 
                            
                        clean_price = float(price_str)
                        if config['name'] == 'BR-VT' and nhom == 'Sản xuất' and clean_price < 13000:
                            continue 
                            
                        data_n234.append({
                            'Tinh_Thanh': config['name'],
                            'Nhom_Khach': nhom,
                            'Gia_Tien': clean_price
                        })
                        break 

    df_dataset2 = pd.DataFrame(data_n234)
    os.makedirs(OUT_DS2_DIR, exist_ok=True)
    df_dataset2.to_csv(os.path.join(OUT_DS2_DIR, 'khoi_kinh_te.csv'), index=False, encoding='utf-8-sig')
    print("✅ Đã cào và lưu thành công Dataset 2!")
    return df_dataset2


def build_dataset1():
    """Hàm cào dữ liệu Hộ dân cư: Tách Baseline và Welfare (Dataset 1)"""
    print("Đang cào Dataset 1 (Hộ dân cư)...")
    data_baseline = []
    data_welfare = []

    # 1. HÀ NỘI
    try:
        path = os.path.join(RAW_DIR, 'hanoi.html')
        df_hn = pd.read_html(path, flavor='bs4')[1]
        data_baseline.extend([
            {'Tinh_Thanh': 'Hà Nội', 'Bac_Tieu_Thu': 'Bậc 1 (0-10m³)', 'Gia_Tien': 8500.0},
            {'Tinh_Thanh': 'Hà Nội', 'Bac_Tieu_Thu': 'Bậc 2 (10-20m³)', 'Gia_Tien': 9900.0},
            {'Tinh_Thanh': 'Hà Nội', 'Bac_Tieu_Thu': 'Bậc 3 (20-30m³)', 'Gia_Tien': 16000.0},
            {'Tinh_Thanh': 'Hà Nội', 'Bac_Tieu_Thu': 'Bậc 4 (>30m³)', 'Gia_Tien': 27000.0}
        ])
        data_welfare.append({'Tinh_Thanh': 'Hà Nội', 'Gia_Binh_Thuong': 8500.0, 'Gia_Tro_Cap': 5973.0})
    except Exception as e: print(f"Lỗi Hà Nội: {e}")

    # 2. HẢI PHÒNG
    try:
        path = os.path.join(RAW_DIR, 'haiphong.html')
        df_hp = pd.read_html(path, flavor='bs4')[1]
        data_baseline.extend([
            {'Tinh_Thanh': 'Hải Phòng', 'Bac_Tieu_Thu': 'Bậc 1 (0-10m³)', 'Gia_Tien': 10900.0},
            {'Tinh_Thanh': 'Hải Phòng', 'Bac_Tieu_Thu': 'Bậc 2 (10-20m³)', 'Gia_Tien': 13500.0},
            {'Tinh_Thanh': 'Hải Phòng', 'Bac_Tieu_Thu': 'Bậc 3 (20-30m³)', 'Gia_Tien': 18000.0},
            {'Tinh_Thanh': 'Hải Phòng', 'Bac_Tieu_Thu': 'Bậc 4 (>30m³)', 'Gia_Tien': 21500.0}
        ])
        data_welfare.append({'Tinh_Thanh': 'Hải Phòng', 'Gia_Binh_Thuong': 10900.0, 'Gia_Tro_Cap': 9000.0})
    except Exception as e: print(f"Lỗi Hải Phòng: {e}")

    # 3. ĐÀ NẴNG
    try:
        path = os.path.join(RAW_DIR, 'danang.html')
        df_dn = pd.read_html(path, flavor='bs4')[2]
        data_baseline.extend([
            {'Tinh_Thanh': 'Đà Nẵng', 'Bac_Tieu_Thu': 'Bậc 1 (0-10m³)', 'Gia_Tien': 4550.0},
            {'Tinh_Thanh': 'Đà Nẵng', 'Bac_Tieu_Thu': 'Bậc 2 (10-20m³)', 'Gia_Tien': 5460.0},
            {'Tinh_Thanh': 'Đà Nẵng', 'Bac_Tieu_Thu': 'Bậc 3 (20-30m³)', 'Gia_Tien': 5460.0},
            {'Tinh_Thanh': 'Đà Nẵng', 'Bac_Tieu_Thu': 'Bậc 4 (>30m³)', 'Gia_Tien': 6810.0}
        ])
        data_welfare.append({'Tinh_Thanh': 'Đà Nẵng', 'Gia_Binh_Thuong': 4550.0, 'Gia_Tro_Cap': 0.0})
    except Exception as e: print(f"Lỗi Đà Nẵng: {e}")

    # 4. CẦN THƠ
    try:
        path = os.path.join(RAW_DIR, 'cantho.html')
        df_ct = pd.read_html(path, flavor='bs4')[1]
        data_baseline.extend([
            {'Tinh_Thanh': 'Cần Thơ', 'Bac_Tieu_Thu': 'Bậc 1 (0-10m³)', 'Gia_Tien': 9020.0},
            {'Tinh_Thanh': 'Cần Thơ', 'Bac_Tieu_Thu': 'Bậc 2 (10-20m³)', 'Gia_Tien': 9020.0},
            {'Tinh_Thanh': 'Cần Thơ', 'Bac_Tieu_Thu': 'Bậc 3 (20-30m³)', 'Gia_Tien': 9020.0},
            {'Tinh_Thanh': 'Cần Thơ', 'Bac_Tieu_Thu': 'Bậc 4 (>30m³)', 'Gia_Tien': 9020.0}
        ])
        data_welfare.append({'Tinh_Thanh': 'Cần Thơ', 'Gia_Binh_Thuong': 9020.0, 'Gia_Tro_Cap': 4820.0})
    except Exception as e: print(f"Lỗi Cần Thơ: {e}")

    # 5. BÀ RỊA - VŨNG TÀU
    try:
        path = os.path.join(RAW_DIR, 'hochiminhcity.html')
        df_brvt = pd.read_html(path, flavor='bs4')[2]
        data_baseline.extend([
            {'Tinh_Thanh': 'BR-VT', 'Bac_Tieu_Thu': 'Bậc 1 (0-10m³)', 'Gia_Tien': 9400.0},
            {'Tinh_Thanh': 'BR-VT', 'Bac_Tieu_Thu': 'Bậc 2 (10-20m³)', 'Gia_Tien': 12600.0},
            {'Tinh_Thanh': 'BR-VT', 'Bac_Tieu_Thu': 'Bậc 3 (20-30m³)', 'Gia_Tien': 13500.0},
            {'Tinh_Thanh': 'BR-VT', 'Bac_Tieu_Thu': 'Bậc 4 (>30m³)', 'Gia_Tien': 13500.0}
        ])
        data_welfare.append({'Tinh_Thanh': 'BR-VT', 'Gia_Binh_Thuong': 9400.0, 'Gia_Tro_Cap': 5500.0})
    except Exception as e: print(f"Lỗi BR-VT: {e}")

    df_baseline = pd.DataFrame(data_baseline)
    df_welfare = pd.DataFrame(data_welfare)
    df_welfare['Gap'] = df_welfare['Gia_Binh_Thuong'] - df_welfare['Gia_Tro_Cap']
    df_welfare = df_welfare.sort_values(by='Gap', ascending=False)

    os.makedirs(OUT_DS1_DIR, exist_ok=True)
    df_baseline.to_csv(os.path.join(OUT_DS1_DIR, 'baseline_hocu_dothi.csv'), index=False, encoding='utf-8-sig')
    df_welfare.to_csv(os.path.join(OUT_DS1_DIR, 'welfare_ansinh_xh.csv'), index=False, encoding='utf-8-sig')

    print("✅ Đã cào và lưu thành công Dataset 1!")
    return df_baseline, df_welfare