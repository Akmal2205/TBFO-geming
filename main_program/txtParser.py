def txtParser():
    lines = [line.rstrip() for line in open('pda_ref.txt')]

    pda = []

    for line in lines:
        prod = [item.strip() for item in line.split(' ')]
        pda.append(prod)

    return pda