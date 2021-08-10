# ROI = (Doanh thu - Chi phí)/Chi phí
#Viết chương trình cho phép người dùng nhập vào Doanh thu và Chi phí và sản xuất ra tỉ lệ ROI cho người dùng, dồng thời hãy cho biết nên hay không nên đầu tư dự án khi biết ROI (Giả sử mức tối thiểu ROI 0.75 thì mới đầu tư)

def ROI(dt,cp):
    return (dt - cp) / cp

def GoiYDauTu(roi):
    if roi >= 0.75:
        return "Nên đầu tư"
    else:
        return "Không nên đầu tư"
print("Chương trình tính ROI")
dt = int(input("Nhập doanh thu: "))
cp = int(input("Nhập chi phí: "))
roi = ROI(dt,cp)
print("Tỉ lệ ROI =", roi)
print("==>", GoiYDauTu(roi))
  
