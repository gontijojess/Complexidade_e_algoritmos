import sys
sys.stdout.reconfigure(encoding='utf-8')

def returnChar(string):
    new_char = [char for char in string if not char.isspace()]
    print(new_char)

returnChar('Sítio do pica-pau amarelo \n 2023')