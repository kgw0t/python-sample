
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

def bool_to_int():
    '''
    bool型をint型に変換
    True は 1
    False は 0
    '''
    n = int(True)
    print(n)

    n = int(False)
    print(n)

def float_to_int():
    '''
    float型をint型に変換
    小数点以下は切り捨てられる
    '''
    n = int(98.6)
    print(n)

    n = int(1.0e4)
    print(n)

def str_to_int():
    '''
    str型をint型に変換
    '''
    n = '99'
    print(n)

    n = '-23'
    print(n)

    n = '+12'
    print(n)

    # ValueError
    # n = int('98.6')
    # n = int('1.0e4')

def auto_cast():
    '''
    演算時の自動的な型変換
    '''
    n = 4 + 7.0
    print(n)
    print(type(n))

    n = True + 2
    print(n)
    print(type(n))

    n = False + 5.0
    print(n)
    print(type(n))

def googol():
    '''
    10 ** 100のような大きい数
    オーバーフローせずに計算できる
    '''
    n = 10 ** 100
    print(n)

def bool_to_float():
    '''
    bool型をfloat型に変換
    '''
    n = float(True)
    print(n)

    n = float(False)
    print(n)

def int_to_float():
    '''
    int型をfloat型に変換
    '''
    n = float(98)
    print(n)

def str_to_float():
    '''
    str型をfloat型に変換
    '''
    n = float('98')
    print(n)

    n = float('98.6')
    print(n)

    n = float('-1.5')
    print(n)

    n = float('1.0e4')
    print(n)

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
    bool_to_int()
    float_to_int()
    str_to_int()
    auto_cast()
    googol()
    bool_to_float()
    int_to_float()
    str_to_float()
