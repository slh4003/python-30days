#bang he so doi don vi sang °F
don_vi_nhiet_do = {
    "c": 1,  # độ C
    "f": 5/9,  # độ F sang độ C
}
# Chọn đơn vị đầu vào
don_vi_dau_vao = input("Nhập đơn vị đầu vào (C, F): ").lower()
don_vi_dau_ra = input("Đổi kết quả sang đơn vị nào (C, F): ").lower()
# Nhập nhiệt độ với đơn vị đầu vào
nhiet_do = float(input(f"Nhập nhiệt độ ({don_vi_dau_vao}): "))
# Đổi sang độ C
if don_vi_dau_vao == "f":
    nhiet_do_c = (nhiet_do - 32) * don_vi_nhiet_do[don_vi_dau_vao]
else:
    nhiet_do_c = nhiet_do * don_vi_nhiet_do[don_vi_dau_vao]
# Đổi kết quả sang đơn vị đầu ra
if don_vi_dau_ra == "f":
    nhiet_do_dau_ra = (nhiet_do_c * 9/5) + 32
else:
    nhiet_do_dau_ra = nhiet_do_c / don_vi_nhiet_do[don_vi_dau_ra]
# In kết quả
print(f"\n Kết quả: ")
print(f" Nhiệt độ: {nhiet_do_dau_ra:.2f} {don_vi_dau_ra}")