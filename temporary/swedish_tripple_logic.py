p1 = vesko
p2 = sasho
p3 = geri

if game = p1 VS p2:
    if p1 win:
        p1 = right
        p3 = left
    elif p2 win:
        p2 = left
        p3 = right
if game = p1 VS p3
    if p1 win:
        p1 = right
        p2 = left
    elif p3 win:
        p3 = left
        p2 = right
if game = p2 VS p1:
    if p2 win:
        p2 = right
        p3 = left
    elif p1 win:
        p1 = left
        p3 = right
if game = p2 VS p3:
    if p2 win:
        p2 = right
        p1 = left
    elif p3 win:
        p3 = left
        p1 = right
if game = p3 VS p1:
    if p3 win:
        p3 = right
        p2 = left
    elif p1 win:
        p1 = left
        p2 = right
if game = p3 VS p2:
    if p3 win:
        p3 = right
        p1 = left
    elif p2 win:
        p2 = left
        p1 = right



