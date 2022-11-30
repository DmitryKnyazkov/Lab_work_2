def pow_gen(base: int):
    schet = 0
    while base:     # TODO записать функцию-генератор
        result = base**schet
        yield result
        schet +=1

if __name__ == "__main__":
    pow_numbers = pow_gen(10)

    for _ in range(5):
        print(next(pow_numbers))
