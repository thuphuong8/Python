def xu_ly_doan_van():
    doan_van = "Nước Việt Nam là một, dân tộc Việt Nam là một. Sông có thể cạn núi có thể mòn, song chân lý ấy không bao giờ thay đổi. (HỒ CHÍ MINH, 1890 – 1969)"
    
    # 1. Đếm số ký tự trong đoạn văn
    so_ky_tu = len(doan_van)
    print(f"Số ký tự trong đoạn văn: {so_ky_tu}")
    
    # 2. Kiểm tra từ có xuất hiện hay không (không phân biệt hoa thường)
    tu_1 = "hồ chí minh".lower() in doan_van.lower()
    tu_2 = "non sông".lower() in doan_van.lower()
    print(f"Đoạn văn có chứa từ 'hồ chí minh': {tu_1}")
    print(f"Đoạn văn có chứa từ 'non sông': {tu_2}")
    
    # 3. Tách đoạn văn thành các câu bởi dấu '.'
    cac_cau = [cau.strip() for cau in doan_van.split('.') if cau.strip()]
    print("Các câu trong đoạn văn:")
    for i, cau in enumerate(cac_cau, start=1):
        print(f"Câu {i}: {cau}")
    
    # 4. Kiểm tra có ký tự nào khác ký tự chữ và số hay không
    ky_tu_khac = any(not (char.isalnum() or char.isspace()) for char in doan_van)
    print(f"Đoạn văn có ký tự nào khác chữ và số: {ky_tu_khac}")
    
    # 5. Thay thế 'Việt Nam' bằng 'VIỆT NAM'
    doan_van_moi = doan_van.replace("Việt Nam", "VIỆT NAM")
    print("Đoạn văn sau khi thay thế:")
    print(doan_van_moi)

# Gọi hàm
xu_ly_doan_van()
