# 犬年齢計算機
dog_name = input("What is your dog's name?")
input_dog_age = input("What is your dog's age?")

#intに変換
dog_age = int(input_dog_age)
#犬の年齢の7倍で人間の年齢に換算できる
human_age = dog_age * 7

print(human_age)
print('Your dog ', dog_name, ' is <', human_age, '> years old in human years')
