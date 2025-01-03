# Khởi tạo danh sách điểm
diem_lop = ['A', 'B', 'C', 'F', 'B', 'A', 'D', 'F', 'C', 'B']

# 1. Số sinh viên trong lớp
so_sinh_vien = len(diem_lop)
print(f"Số sinh viên trong lớp: {so_sinh_vien}")

# 2. Số sinh viên phải học lại môn này (điểm F)
hoc_lai = diem_lop.count('F')
print(f"Số sinh viên phải học lại môn này: {hoc_lai}")

# 3. Số sinh viên có điểm từ B trở lên (A hoặc B)
diem_tot = sum(1 for diem in diem_lop if diem in ['A', 'B'])
print(f"Số sinh viên có điểm từ B trở lên: {diem_tot}")

# 4. Tạo bảng điểm mới, loại bỏ sinh viên đầu tiên và cuối cùng
diem_moi = diem_lop[1:-1]
print(f"Bảng điểm mới sau khi loại bỏ sinh viên đầu tiên và cuối cùng: {diem_moi}")
