#Task1:kiểm tra an toàn nhiệt độ 
def tem_freezer(Celsius):
    if Celsius>-18:
        print("chương trình cảnh báo nguy cơ mất an toàn thực phẩm.")
        print(f"Vì nó cao hơn -18°C khoảng {Celsius -(-18)}°C")
    else:
        print("tủ đông của bạn hoạt động an toàn")

nhiet_do = float(input("yêu cầu bạn nhập số Celsius trong tủ lạnh nhà bạn: "))   
tem_freezer(nhiet_do)

#task2:phân loại vé xem phim
def film_ticket(classify):
        if classify=="vip":
            print("ghế cao cấp kèm đồ ăn nhẹ free.")
        elif classify=="standard":
            print("ghế tiêu chuẩn.")
        elif classify=="student":
            print("vé ưu đãi dành cho sinh viên(có thẻ sinh viên).")
        elif classify=="child":
            print("vé ưu đãi dành cho trẻ em dưới 12 tuổi.")
        else:
            print("Invalid ticket type")
enter_film_ticker = input("yêu cầu bạn nhập loại vé xem phim của bạn: ")
classify = enter_film_ticker.strip().lower()
film_ticket(classify)

#task3:Đánh giá chỉ số khối cơ thể(BMI)
def body():
    print("===Đây là kết quả của chúng tôi===\n")
weight = float(input("Yêu cầu bạn khai báo cân nặng của bạn (kg):"))
height = float(input("Yêu cầu bạn khai báo chiều cao của bạn (m):"))
bmi=weight/height**2
if bmi < 18.5:
    print("Gầy")
    print("Bạn nên tăng cân để có sức khỏe tốt hơn.")
elif bmi < 25:
    print("Bình Thường")
    print("Bạn đang trong tình trạn sức khỏe ổn định cân bằng.")
elif bmi < 30:
    print("Thừa cân")
    print("Bạn nên kiểm soát chế độ ăn uống và tập thể dụng thường xuyên hơn")
else:
    print("Béo Phì")
    print("Bạn nên tham khảo ý kiến từ bác sĩ và có chế độ ăn uống rõ ràng")
    print(f"Vì Chỉ số BMI của bạn là:{bmi:.2f}")

body()


#task4: Đánh giá chất lượng tốc độ Internet
def Internet():
    print("===Đánh giá chất lượng Internet(Mbps)===\n")
    speed = float(input("yêu cầu bạn nhập khai báo: "))
    if speed < 10:
        print("kém")
    elif speed < 49:
        print("Trung bình")
    elif speed < 99:
        print("tốt")
    elif speed >= 100:
        print("xuất sắc")

Internet()

#task5:5. So sánh hiệu suất nhiên liệu
def fuel_efficiency(distance,fuel):
# Công thức: Hiệu suất = (nhiên liệu / quãng đường) × 100
    efficiency = (fuel/distance) *100
    return efficiency

def main():
    print("=== ĐÂY LÀ KẾT QUẢSO SÁNH HIỆU SUẤT NHIÊN LIỆU ===\n")
print("\nphương tiện số 1")
distance1 = float(input("hãy cho tôi biết quảng đường đã đi(km):"))
fuel1 = float(input("hãy cho tôi biết nhiên liệu đã tiêu thụ(lít):"))
print("\nphương tiện số 2")
distance2 = float(input("hãy cho tôi biết quảng đường đã đi(km):"))
fuel2 = float(input("hãy cho tôi biết nhiên liệu đã tiêu thụ(lít):"))
#tính hiệu xuất của 2 phương tiện
efficiency1 = fuel_efficiency(distance1,fuel1)
efficiency2 = fuel_efficiency(distance2,fuel2)
# Hiển thị kết quả
print("\n=== KẾT QUẢ ===")
print(f"Phương tiện 1: {efficiency1:.1f} lít/100km")
print(f"Phương tiện 2: {efficiency2:.1f} lít/100km")

print("\n=== ĐÁNH GIÁ ===")
if efficiency1 < efficiency2:
    print("Phương tiện 1 tiết kiệm nhiên liệu hơn!")
    saving = efficiency2 - efficiency1
    print(f"Tiết kiệm hơn {saving:.2f} lít/100km")
elif efficiency2 < efficiency1:
    print("Phương tiện 2 tiết kiệm nhiên liệu hơn!")
    saving = efficiency1 - efficiency2
    print(f"Tiết kiệm hơn {saving:.2f} lít/100km")
else:
    print("Cả 2 phương tiện có hiệu suất nhiên liệu như nhau!")
#chạy hàm
main()

#task6: An toàn tải trọng thang máy
def kiem_tra_tai_trong():
    trong_luong = float(input("Nhập tổng trọng lượng trong thang máy (kg): "))

    if trong_luong > 600:
        vuot_qua = trong_luong - 600
        print(f"Cảnh báo: Thang máy quá tải {vuot_qua} kg!")
    else:
        print("Tải trọng an toàn.")

# chạy hàm
kiem_tra_tai_trong()

#task7:Cấp độ khóa học trực tuyến
def cap_do_khoa_hoc():
    level = input("Nhập cấp độ khóa học trong các lựa chọn sau(cơ bản,trung cấp, nâng cao,chuyên gia): ").strip().lower()

    if level == "cơ bản":
        print("Khóa học dành cho người mới bắt đầu.")
    elif level == "trung cấp":
        print("Khóa học dành cho người đã có nền tảng.")
    elif level == "nâng cao":
        print("Khóa học chuyên sâu.")
    elif level == "chuyên gia":
        print("Khóa học cấp độ chuyên gia.")
    else:
        print("Invalid course level")
cap_do_khoa_hoc()

#task8:Đánh giá huyết áp
def danh_gia_huyet_ap():
    tam_thu = int(input("Nhập huyết áp tâm thu: "))
    tam_truong = int(input("Nhập huyết áp tâm trương: "))

    if tam_thu < 120 and tam_truong < 80:
        print("Huyết áp bình thường")
    elif 120 <= tam_thu < 130 and tam_truong < 80:
        print("Huyết áp tăng")
    elif 130 <= tam_thu < 140 or 80 <= tam_truong < 90:
        print("Huyết áp cao độ 1")
    else:
        print("Huyết áp cao độ 2")
danh_gia_huyet_ap()

#task9: Phân loại điểm thi
def phan_loai_diem():
    diem = float(input("Nhập điểm thi (0–100): "))
    if diem >= 90:
        print("Xếp loại A")
    elif diem >= 80:
        print("Xếp loại B")
    elif diem >= 70:
        print("Xếp loại C")
    elif diem >= 60:
        print("Xếp loại D")
    else:
        print("Xếp loại F")
phan_loai_diem()