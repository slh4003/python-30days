# bảng hệ số đổi đơn vị sang mét
don_vi_sang_m = {
    "mm": 0.001,
    "cm": 0.01,
    "dm": 0.1,
    "m": 1,
    "km": 1000
}

# Chọn đơn vị đầu vào
don_vi_dau_vao = input("Nhập đơn vị đầu vào (mm, cm, dm, m, km): ").lower()
don_vi_dau_ra = input("Đổi kết quả sang đơn vị nào (mm, cm, dm, m, km): ").lower()

# Nhập chiều dài và chiều rộng với đơn vị đầu vào
dai = float(input(f"Nhập chiều dài ({don_vi_dau_vao}): "))
rong = float(input(f"Nhập chiều rộng ({don_vi_dau_vao}): "))
ban_kinh = float(input(f"Nhập bán kính hình tròn ({don_vi_dau_vao}): "))
duong_kinh = float(input(f"Nhập đường kính hình tròn ({don_vi_dau_vao}): "))

# Đổi sang mét
dai_m = dai * don_vi_sang_m[don_vi_dau_vao]
rong_m = rong * don_vi_sang_m[don_vi_dau_vao]
ban_kinh_m = ban_kinh * don_vi_sang_m[don_vi_dau_vao]
duong_kinh_m = duong_kinh * don_vi_sang_m[don_vi_dau_vao]

# Tính chu vi, diện tích (đơn vị mét)
chu_vi = 2 * (dai_m + rong_m)
dien_tich = dai_m * rong_m
chu_vi_hinh_tron = 2 * 3.14 * ban_kinh_m
dien_tich_hinh_tron = 3.14 * (ban_kinh_m ** 2)

# Đổi kết quả sang đơn vị đầu ra
chu_vi_dau_ra = chu_vi / don_vi_sang_m[don_vi_dau_ra]
dien_tich_dau_ra = dien_tich / (don_vi_sang_m[don_vi_dau_ra] ** 2)
chu_vi_hinh_tron_dau_ra = chu_vi_hinh_tron / don_vi_sang_m[don_vi_dau_ra]
dien_tich_hinh_tron_dau_ra = dien_tich_hinh_tron / (don_vi_sang_m[don_vi_dau_ra] ** 2)

# In kết quả
print(f"\n Kết quả: ")
print(f" Chu vi: {chu_vi_dau_ra:.2f} {don_vi_dau_ra}")
print(f" Diện tích: {dien_tich_dau_ra:.2f} {don_vi_dau_ra}²")
print(f" Chu vi hình tròn: {chu_vi_hinh_tron_dau_ra:.2f} {don_vi_dau_ra}")
print(f" Diện tích hình tròn: {dien_tich_hinh_tron_dau_ra:.2f} {don_vi_dau_ra}²")
