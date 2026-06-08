import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

plt.rcParams['font.family'] = 'Segoe UI'
sns.set_theme(style="whitegrid", font="Segoe UI")

def check_data():
    """Kiểm tra xem file CSV đã tồn tại chưa"""
    if not (os.path.exists('Dataset 2/khoi_kinh_te.csv') and 
            os.path.exists('Dataset 1/baseline_hocu_dothi.csv') and 
            os.path.exists('Dataset 1/welfare_ansinh_xh.csv')):
        print("❌ Lỗi: Không tìm thấy các file CSV sạch. Vui lòng chạy Cập nhật dữ liệu (Phím 0) trước!")
        return False
    return True

def draw_group_bar():
    df_n234 = pd.read_csv('Dataset 2/khoi_kinh_te.csv')
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(data=df_n234, x='Tinh_Thanh', y='Gia_Tien', hue='Nhom_Khach', palette='Set2', ax=ax)
    ax.set_title('So sánh Giá nước khối Cơ quan & Doanh nghiệp', fontsize=14, fontweight='bold', pad=15)
    ax.set_xlabel('Tỉnh / Thành phố')
    ax.set_ylabel('Giá tiền (VNĐ/m³)')
    ax.legend(title='Nhóm đối tượng', bbox_to_anchor=(1.02, 1), loc='upper left')
    for container in ax.containers:
        ax.bar_label(container, fmt='%.0f', padding=3, size=9)
    plt.tight_layout()

def draw_heatmap():
    df_n234 = pd.read_csv('Dataset 2/khoi_kinh_te.csv')
    fig, ax = plt.subplots(figsize=(10, 5))
    ma_tran = df_n234.pivot(index='Tinh_Thanh', columns='Nhom_Khach', values='Gia_Tien')[['Hành chính', 'Sản xuất', 'Kinh doanh']]
    sns.heatmap(ma_tran, annot=True, fmt=".0f", cmap='Reds', linewidths=1, linecolor='white', ax=ax)
    ax.set_title('Bản đồ nhiệt: Mức độ đắt đỏ của Giá nước ngoài sinh hoạt', fontsize=14, fontweight='bold', pad=15)
    ax.set_ylabel('')
    ax.set_xlabel('')
    plt.tight_layout()

def draw_line_chart():
    df_baseline = pd.read_csv('Dataset 1/baseline_hocu_dothi.csv')
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.lineplot(data=df_baseline, x='Bac_Tieu_Thu', y='Gia_Tien', hue='Tinh_Thanh', marker='o', markersize=8, linewidth=2.5, palette='Set1', ax=ax)
    ax.set_title('Độ dốc Chính sách giá nước lũy tiến (Khách hàng Đô thị - Bình thường)', fontsize=14, fontweight='bold', pad=15)
    ax.set_xlabel('Mốc khối lượng tiêu thụ', fontweight='bold')
    ax.set_ylabel('Giá tiền (VNĐ/m³)', fontweight='bold')
    ax.set_ylim(bottom=0)
    ax.legend(title='Tỉnh / Thành phố', bbox_to_anchor=(1.02, 1), loc='upper left')
    plt.tight_layout()

def draw_dumbbell():
    df_welfare = pd.read_csv('Dataset 1/welfare_ansinh_xh.csv')
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.vlines(x=df_welfare['Tinh_Thanh'], ymin=df_welfare['Gia_Tro_Cap'], ymax=df_welfare['Gia_Binh_Thuong'], color='grey', alpha=0.4, linewidth=5)
    ax.scatter(x=df_welfare['Tinh_Thanh'], y=df_welfare['Gia_Binh_Thuong'], color='crimson', s=200, label='Giá Đô thị (Bình thường)', zorder=3)
    ax.scatter(x=df_welfare['Tinh_Thanh'], y=df_welfare['Gia_Tro_Cap'], color='dodgerblue', s=200, label='Giá Trợ cấp (Yếu thế)', zorder=3)
    
    for i, row in df_welfare.iterrows():
        ax.text(row['Tinh_Thanh'], row['Gia_Binh_Thuong'] + 300, f"{row['Gia_Binh_Thuong']:,.0f}", ha='center', va='bottom', fontsize=10, fontweight='bold', color='crimson')
        ax.text(row['Tinh_Thanh'], row['Gia_Tro_Cap'] - 400, f"{row['Gia_Tro_Cap']:,.0f}", ha='center', va='top', fontsize=10, fontweight='bold', color='dodgerblue')
        
    ax.set_title('Mức độ hỗ trợ giá nước sinh hoạt cho nhóm yếu thế (Mốc 0-10m³)', fontsize=14, fontweight='bold', pad=25)
    ax.set_ylabel('Giá tiền (VNĐ/m³)')
    ax.set_ylim(0, 13000)
    ax.legend(bbox_to_anchor=(1.02, 1), loc='upper left', borderaxespad=0.)
    sns.despine(ax=ax)
    plt.tight_layout()

def show_single_chart(chart_func):
    """Kích hoạt và hiển thị 1 biểu đồ đơn lẻ"""
    if not check_data(): return
    chart_func()
    plt.show()

def show_all_charts():
    """Kích hoạt và hiển thị cả 4 biểu đồ cùng lúc"""
    if not check_data(): return
    draw_group_bar()
    draw_heatmap()
    draw_line_chart()
    draw_dumbbell()
    print("✅ Đã hiển thị toàn bộ biểu đồ thành công!")
    plt.show()