def handle_index(listq: list) -> list:
    try:
        for n in range(0,len(listq) + 1):
         print(listq[n], end=" ")
    except (IndexError, ValueError) as e:
        print(f"\nError:{e}")


list = [123.41,14,11,22]
handle_index(list)