def tinh_so_tho():
    # Nhập số tháng
    x = int(input("Nhập vào số tháng x: "))
    
    # Tính số lượng thỏ sau x tháng
    so_tho = 2 ** x  # Số lượng thỏ gấp đôi mỗi tháng
    
    # Hiển thị kết quả
    print(f"Trong rừng có: {so_tho} con thỏ")

# Gọi hàm
tinh_so_tho()
