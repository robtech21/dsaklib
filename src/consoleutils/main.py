def progress(style, prog):
    if style == 1:
        print(prog + "%")
    elif style == 2:
        progu = ''
        for 1 in prog:
            progu = i + "="
        print("<" + progu + ">")