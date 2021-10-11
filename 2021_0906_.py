# def is_leapyear(seireki):
#     if seireki % 400 == 0:
#         return True
#     elif seireki % 4 == 0:
#         if seireki % 100 == 0:
#             return False
#         else:
#             return True

# seireki = int(input("西暦を入力してください。うるう年であるかはん判断します。＞＞"))
# flag = is_leapyear(seireki)
# print("西暦{}年は".format(seireki), end="")
# if flag:
#     print("うるう年です。")
# else:
#     print("うるう年ではありません。")


# def take_bus():
#     print("バスに乗ります。")

# def walk():
#     print("ちょっと歩きます。")


# def run():
#     print("走ります。") 
#     walk()

# print("行ってきます。")
# walk();take_bus();run();run()
# print("ただいま。")


# def int_input(messege):
#     return int(input("{}を入力してください".format(messege)))

# def calc_payment(amount,people=2):
#     dnum=amount / people
#     pay = dnum // 100 * 100
#     if dnum > pay:
#         pay = int(pay+100)
#     payorg = amount - pay * (people-1)
#     return[int(pay),int(payorg)]
# def show_payment(pay,payorg,peple=2):
#     print("***支払額***")
#     print("１人当たり{}円({}人),幹事は{}円です".format(pay,peple-1,payorg))
# amount = int_input("支払い総額")
# peple = int_input("参加人数")
# pay_list = calc_payment(amount,peple)
# show_payment(pay_list[0],pay_list[1],peple)

userinfo = input("名前と血液型をカンマで区切って１行で入力＞＞")
[name , blood] = userinfo.split(",")
blood=blood.upper().split()
print("{}さんは{}型なので大吉です".format(name,blood))