import random
def miller_rabin(n, k):
    if n == 2:
        return True

    if n % 2 == 0:
        return False

    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2
    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


def fermat_primality_test(p, s=5):
    if p == 2:
        return True
    if not p & 1:
        return False

    for i in range(s):
        a = random.randrange(2, p - 2)
        x = pow(a, p - 1, p)
        if x != 1:
            return False
    return True


def gen_q():
    pr = generate_primes(300, 1)

    q = pr[0]
    print("Q: " + str(q))
    if is_prime_q(q):
        return q


def is_prime_q(q):
    if fermat_primality_test(q):
        if miller_rabin(q, 40):
            return True
        else:
            return False
    else:
        return False


def generate_primes(n=512, k=1):
    assert k > 0
    assert n > 0 and n < 4096
    x = random.getrandbits(n)

    primes = []

    while k > 0:
        if miller_rabin_primality_test(x, s=7):
            primes.append(x)
            k = k - 1
        x = x + 1
    return primes


def miller_rabin_primality_test(p, s=5):
    if p == 2:
        return True
    if not (p & 1):
        return False

    p1 = p - 1
    u = 0
    r = p1

    while r % 2 == 0:
        r >>= 1
        u += 1

    assert p - 1 == 2 ** u * r

    def witness(a):
        z = square_and_multiply(a, r, p)
        if z == 1:
            return False

        for i in range(u):
            z = square_and_multiply(a, 2 ** i * r, p)
            if z == p1:
                return False
        return True

    for j in range(s):
        a = random.randrange(2, p - 2)
        if witness(a):
            return False

    return True


def square_and_multiply(x, k, p=None):
    b = bin(k).lstrip('0b')
    r = 1
    for i in b:
        r = r ** 2
        if i == '1':
            r = r * x
        if p:
            r %= p
    return r

def reconstruct_secret(shares):
    for p in range(len(shares)):
        shares[p] = shares[p][:-1]
    sums = 0

    for j, share_j in enumerate(shares):
        xj, yj = share_j
        prod_numerator = 1
        prod_denominator = 1

        for i, share_i in enumerate(shares):
            xi, _ = share_i
            if i != j:
                prod_numerator *= xi
                prod_denominator *= (xi - xj)

        prod = (yj * prod_numerator) // prod_denominator
        sums += prod

    return sums


def polynom(x, coefficients):
    point = 0

    for coefficient_index, coefficient_value in enumerate(coefficients[::-1]):
        point += x ** coefficient_index * coefficient_value
    return point


def coeff(t, secret,FIELD_SIZE):
    coeff = [random.randrange(0, FIELD_SIZE) for _ in range(t - 1)]
    coeff.append(secret)
    return coeff


def generate_shares(n, m, secret,FIELD_SIZE):
    coefficients = coeff(m, secret,FIELD_SIZE)
    shares = []

    for i in range(1, n + 1):
        x = random.randrange(1, FIELD_SIZE)
        shares.append((x, polynom(x, coefficients)))

    return shares


def letter_to_number(letter):
    return ord(letter)


def number_to_letter(number):
    return chr(number)


def int_from_bytes(s):
    acc = 0
    for b in s:
        acc = acc * 256
        acc += b
    return acc


def bytes_from_int(n):
    s = bytearray()
    while n > 0:
        s.append(n % 256)
        n //= 256
    return bytes(reversed(s))

