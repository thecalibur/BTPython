# Viết hàm tính BMI

def BMI(height, weight):
    return weight / (height ** 2)

def PhanLoai(BMI):
    if BMI < 18.5:
        return "Gầy"
    elif BMI <= 24.9:
        return "Bình thường"
    elif BMI <= 29.9:
        return "Hơi béo"
    elif BMI < 34.9:
        return "Béo phì cấp độ 1"
    elif BMI < 39.9:
        return "Béo phì cấp độ 2"
    else:
        return "Béo phì cấp độ 3"

def NguyCoBenh(BMI):
    if BMI < 18.5:
        return "Thấp"
    elif BMI <= 24.9:
        return "Trung bình"
    elif BMI <= 29.9:
        return "Cao"
    elif BMI < 34.9:
        return "Cao"
    elif BMI < 39.9:
        return "Rất cao"
    else:
        return "Nguy hiểm"



print("Nhập vào chiều cao: ")
height = float(input())
print("Nhập vào cân nặng: ")
weight = float(input())
bmi = BMI(height, weight)
print ("BMI của bạn:", bmi)
print("Phân loại:", PhanLoai(bmi))
print("Nguy cơ bệnh:", NguyCoBenh(bmi))
