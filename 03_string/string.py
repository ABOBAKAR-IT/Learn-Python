chai = "Masala Chai"
print(chai)
firstChar = chai[0]
print(firstChar)

slice_chai = chai[0:6]
print(slice_chai)

number_list = "123456789"

print(number_list[3:]) # 456789

print(number_list[:7]) # 1234567

print(number_list[0:9:2]) # 13579 0 indicate start index 9 indicate last index and 2 indicate skip value

print(chai.upper())

print(chai.lower())

chai = "    Masala Chai      "
print(chai)

print(chai.strip()) # remove extra space

print(chai.lstrip()) # remove left space


print(chai.rstrip()) # remove right space

print(chai.replace("M","T"))


chai = "Lemon, Ginger, Masala, Mint"

print(chai.split()) #  split use to convert string into list

print(chai.split(', '))


chai = "Masala chai"

print(chai.find("chai")) # find use to find index of string
print(chai.find("Chai")) # -1 indicate string not found

print(chai.index("chai")) # index use to find index of string


chai_type = "masala chai"
quantity = 2
order = "I ordered {} cups of {} chai"
print(order.format(quantity,chai_type))

order = f"I ordered {quantity} cups of {chai_type} chai"
print(order)


chai_variety = ["Lemon","Masala","Genger","Mint"]

print("".join(chai_variety)) # output LemonMasalaGengerMint
print(" ".join(chai_variety)) # output Lemon Masala Genger Mint
print("-".join(chai_variety)) # output Lemon-Masala-Genger-Mint

print(len(chai))


for letter in chai:
    print(letter)


chai = "He said, \"Masal chai si awesome\" "

print(chai)

chai = "Masla \n chai"
print(chai)

chai = r"Masala \n chai"
print(chai) # output Masala \n chai

chai = "c:\\user\\pwd"
print(chai) # output c:\user\pwd