import numpy
while True:
    try:
        a = input("请输入血糖值mmol/l(正常值为7.0):")
        b = eval(a)*18.016
        print("您的血糖值mg/dl为: %5.3f." %b)
    except:
        break
print("程序正常退出。")
