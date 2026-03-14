letter = '''
        Dear <|Name|>,
        You are selected!
        <|Date|>'''

print(letter.replace("<|Name|>","Asad").replace("<|Date|>","20 May,2027"))