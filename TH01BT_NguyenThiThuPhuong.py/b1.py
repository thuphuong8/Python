def chia_keo():
    # Nhập số kẹo của cô
    N = int(input("Nhập số kẹo của cô: "))
    
    # Nhập số học sinh trong lớp
    M = int(input("Nhập số học sinh trong lớp: "))
    
    # Tính số kẹo mỗi học sinh nhận và số kẹo còn lại
    keo_moi_hoc_sinh = N // M  # Mỗi học sinh nhận được
    keo_con_lai = N % M        # Số kẹo còn lại
    
    # Hiển thị kết quả
    print(f"Mỗi học sinh nhận được: {keo_moi_hoc_sinh} cái kẹo.")
    print(f"Cô còn lại: {keo_con_lai} cái kẹo.")

# Gọi hàm
chia_keo()