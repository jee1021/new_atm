
# 입금, 출금 , 영수증 보기 , 종료


balance = 3000
while True:
    num = input ("사용하실 기능의 번호를 입력해주세요.(1.입금, 2.출금, 3.영수증 보기, 4.종료)")

    
    
    if num == "1" :
       deposit_amount = input("입금할 금액을 입력해주세요 : ")
       if deposit_amount.isdigit() and int(deposit_amount) > 0:
          balance_amount += int(deposit_amount)
          print("고객님이 입금하신 금액은 {deposit_amount}원이고, 현재잔액은{balance}원 입니다.")
       else:
           print("정신차리고, 제대로된 숫자형태로 금액을 입금액을 작성해줘!!")
    if num == "2" :
        pass
    if num == "3" :
        pass
    if num == "4" :
        print("서비스를 종료합니다")
        break