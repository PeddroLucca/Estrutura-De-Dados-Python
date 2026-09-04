# Ajuste os métodos abaixo push_aux, pop_aux e get_min para que # seja possível
# encontrar o elemento mínimo de uma pilha simplesmente buscando no topo (peek) da pilha min_stack.

from stack import Stack

if __name__ == "__main__":
    main_stack = Stack()
    min_stack = Stack()

    def push_aux(data):
        main_stack.push(data)
        if min_stack.is_empty() or data <= min_stack.peek():
            min_stack.push(data)

    def pop_aux():
        data = main_stack.pop()
        if not min_stack.is_empty() and data == min_stack.peek():
            min_stack.pop()
        return data

    def get_min():
        return min_stack.peek()


    # Testes
    print("\nEmpilhando: 5, 3, 7, 2, 8")
    push_aux(5)
    print(f"Min atual: {get_min()}")

    push_aux(3)
    print(f"Min atual: {get_min()}")

    push_aux(7)
    print(f"Min atual: {get_min()}")

    push_aux(2)
    print(f"Min atual: {get_min()}")

    push_aux(8)
    print(f"Min atual: {get_min()}")

    print("\nDesempilhando e mostrando o mínimo:")
    pop_aux()
    print(f"Min atual: {get_min()}")

    pop_aux()
    print(f"Min atual: {get_min()}")

    pop_aux()
    print(f"Min atual: {get_min()}")

    pop_aux()
    print(f"Min atual: {get_min()}")

    pop_aux()
    try:
        print(get_min())
    except IndexError as e:
        print(f"Erro esperado: {e}")