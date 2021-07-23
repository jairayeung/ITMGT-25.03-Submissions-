def get_product(code):
    item = products[code]
    return item
get_product("espresso")


def get_property(code, property_):
    detail = products[code][property_]
    return detail

get_property("espresso", "name")


def main():
    orders = []
    while True:
        order = input("Enter your order and quantity: ")
        if order =="/":
            break
        else:
            orders.append(order.split(','))

    without_repeats= [i[0] for i in orders]
    without_repeats = list(set(without_repeats))
    without_repeats.sort()

    final_list = []
    for item in without_repeats:
        item_qty = [item,0]
        for x in orders:
            if x[0] == item:
                item_qty[1] += int(x[1])

        final_list.append(item_qty)


    with open ('receipt.txt','w') as receipt:
        receipt.write("""
==
CODE\t\t\tNAME\t\t\tQUANTITY\t\t\tSUBTOTAL

        """)

    subtotal = 0
    for code in final_list:
        total = int(code[1])*get_property(code[0], 'price')
        subtotal += total
        name = get_property(code[0],'name')
        with open ('receipt.txt','a') as receipt:
            receipt.write('\n'+f'{code[0]}\t\t\t{name}\t\t\t{code[1]}\t\t\t\t{total}')

    with open ('receipt.txt','a+') as receipt:
        receipt.write(f'''

Total:\t\t\t\t\t\t\t\t\t\t{subtotal}
==
        ''')

        receipt.seek(0)
        print(receipt.read())


main()
