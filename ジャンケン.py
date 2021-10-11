import random
class Janken:
    def Glico(self):
        me = 0
        you = 0
        while True:
            
            jyanken_list = ["グー","チョキ","パー"]
            print("グー、チョキ、パー何かを入力")
            
            while True:
                choice = input()
                random_choice = jyanken_list[random.randrange(3)]     #グー = 0 チョキ = 1 パー = 2
                
                print("自分は"+choice)
                print("相手は"+random_choice)
                
                if choice == random_choice:
                    print("あいこ")
                else:
                    break
                #あいこの時に繰り返すためにwhile文を使ってます
            if choice =="グー"and random_choice =="チョキ":
                 print("勝ち")
                 print("グ〜リ〜コッ！　3歩進んだ")
                 me +=3
            elif choice =="チョキ"and random_choice =="パー":
                 print("勝ち")
                 print("チーヨーコーレーイート！　6歩進んだ")
                 me +=6
            elif choice =="パー"and random_choice =="グー":
                 print("勝ち")
                 print("パーイーナーツープール！　6歩進んだ")
                 me +=6
            if choice =="グー"and random_choice =="パー":
                print("負け")
                print("パーイーナーツープール！　相手は6歩進んだ")
                you +=6
            elif choice =="チョキ"and random_choice =="グー":
                print("負け")
                print("グ〜リ〜コッ！　相手は3歩進んだ")
                you +=3
            elif choice =="パー"and random_choice =="チョキ":
                print("負け")
                print("チーヨーコーレーイート！　相手は6歩進んだ")
                you +=6
            print("残り"+str(15-me)+"段")
            print(("相手は残り"+str(15-you)+"段"))
            #ゴールは15段です
            if me >=15:
              print("自分の勝ち！")
              break
            elif you >=15:
              print("相手の勝ち！")
              break
            #30段ピッタリじゃなくても終了します​
janken1 = Janken()
janken1.Glico()