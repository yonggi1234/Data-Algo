def remove_card(a, b, n):
    for i in a:
        if n - i in b:
            a.remove(i)
            b.remove(n - i)
            return True
    return False

def solution(coin, cards):
    n = len(cards)
    my_cards = cards[0 : n//3]
    ans = 1
    draw = []

    for t in range(n//3, n, 2): 
        draw.append(cards[t])
        draw.append(cards[t + 1])
                
        if remove_card(my_cards, my_cards, n + 1):
            ans += 1
        elif remove_card(my_cards, draw, n + 1) and coin > 0:
            coin -= 1
            ans += 1
        elif remove_card(draw, draw, n + 1) and coin > 1:
            coin -= 2
            ans += 1
        else:
            break
    
    return ans
    