import sys
from scraper import build_dataset1, build_dataset2
from visualizer import (
    show_all_charts, 
    show_single_chart, 
    draw_group_bar, 
    draw_heatmap, 
    draw_line_chart, 
    draw_dumbbell
)

def menu():
    while True:
        print("\n====================================================")
        print("📊 CHƯƠNG TRÌNH PHÂN TÍCH GIÁ NƯỚC LŨY TIẾN 5 TỈNH 📊")
        print("====================================================")
        print("0. Cập nhật dữ liệu (Chạy Scraper cào file HTML)")
        print("1. Nhóm không phải dân cư (Dataset 2)")
        print("   1.1 Group Bar Chart (So sánh tuyệt đối)")
        print("   1.2 Heatmap (Bản đồ nhiệt)")
        print("2. Nhóm dân cư (Dataset 1)")
        print("   2.1 Line Chart (Độ dốc giá lũy tiến)")
        print("   2.2 Dumbbell Chart (Mức độ an sinh xã hội)")
        print("3. Hiển thị toàn bộ 4 biểu đồ cùng lúc")
        print("4. Thoát chương trình")
        print("====================================================")
        
        choice = input("Nhập lựa chọn của bạn: ").strip()
        
    # Cập nhật lại phần if-elif này trong main.py
        if choice == '0':
            build_dataset1()
            build_dataset2()
        elif choice == '1.1':
            show_single_chart(draw_group_bar)
        elif choice == '1.2':
            show_single_chart(draw_heatmap)
        elif choice == '2.1':
            show_single_chart(draw_line_chart)
        elif choice == '2.2':
            show_single_chart(draw_dumbbell)
        elif choice == '3':
            show_all_charts()
        elif choice == '4':
            print("👋 Đã thoát chương trình!")
            sys.exit()
        else:
            print("❌ Lựa chọn không hợp lệ, vui lòng nhập lại!")
if __name__ == "__main__":
    menu()