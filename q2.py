def sortCards(cards_list):
    stack = []
    while cards_list:
        card = cards_list.pop()
        position = 0
        while position < len(stack) and stack[position] < card:
            position += 1
        stack.insert(position, card)
    return stack

cards_list = [7, 3, 10, 1, 2, 12, 8, 5, 6, 11, 4, 9, 13]
cartas_ordenadas = sortCards(cards_list)
print(cartas_ordenadas)