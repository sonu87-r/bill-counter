#bill counter

bill_amt = int(input("Enter your bill amount and get discount:" ))
if (bill_amt >= 1000):
    print("yayy, you got 20% off","your total bill amout are:-",bill_amt-bill_amt*20/100 )
    print("dicount amount are:",bill_amt*20/100)
elif (bill_amt < 1000 and bill_amt > 500):
    print("wow, you got 10% dicount","your total bill amout are:-", bill_amt-bill_amt*10/100)
    print("dicount amount are:",bill_amt*10/100)

else:
    print("No, you should eat more")
    