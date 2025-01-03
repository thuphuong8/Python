from datetime import datetime

# Nhập vào họ tên
ho_ten = input("Nhập vào họ tên: ")

# Nhập vào năm sinh
nam_sinh = int(input("Nhập vào năm sinh: "))

# Lấy năm hiện tại
nam_hien_tai = datetime.now().year

# Tính tuổi
tuoi = nam_hien_tai - nam_sinh

# Chuyển họ tên thành chữ in hoa
ho_ten_in_hoa = ho_ten.upper()

# Hiển thị thông báo
print(f"Bạn \"{ho_ten_in_hoa}\" năm nay {tuoi} tuổi!")