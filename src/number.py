
x = 1
y = 2
z = 3

def add():
    '''
    加算
    '''
    n = x + y
    print(n)

def sub():
    '''
    減算
    '''
    n = x - y
    print(n)

def mul():
    '''
    乗算
    '''
    n = x * y
    print(n)

def div():
    '''
    除算
    '''
    n = x / y
    print(n)

def trancate_div():
    '''
    切り捨て除算
    '''
    n = x // y
    print(n)

def mod():
    '''
    剰余
    '''
    n = x % y
    print(n)

def operator_with_assign():
    '''
    複合代入演算子
    '''
    n = x
    n += y
    n -= y
    n *= y
    n /= y
    n //= y
    n %= y
    print(n)

def priority():
    '''
    計算の優先順位
    '''
    n = x + y * z
    print(n)

    n = (x + y) * z
    print(n)

def radix():
    '''
    2進数, 8進数, 10進数, 16進数
    '''
    binary = 0b10
    Binary = 0B10
    print(binary)
    print(Binary)

    oct = 0o10
    Oct = 0O10
    print(oct)
    print(Oct)

    decimal = 10
    print(decimal)

    hex = 0x10
    Hex = 0X10
    print(hex)
    print(Hex)


if __name__ == '__main__':
    add()
    sub()
    mul()
    div()
    trancate_div()
    mod()
    operator_with_assign()
    priority()
    radix()