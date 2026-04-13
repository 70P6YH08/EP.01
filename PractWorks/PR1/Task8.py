a = int(input())

hour = a // 3600
minute = a % 3600 // 60
second = a % 3600 % 60

print(f"{hour if hour < 24 else hour - 24}:{minute}:{second}")