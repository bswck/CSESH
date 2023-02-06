# ZAD 6
encoder = {
    'START': '11011010',
    'STOP': '11010110'
}

with open('cyfra_kodkreskowy.txt') as f:
    f.readline()
    for line in f.readlines():
        digit, val = line.split()
        encoder[digit] = val


def encode(number):
    digits = str(number)[::-1]
    odd_total = sum(map(int, digits[::2])) * 3
    even_total = sum(map(int, digits[1::2]))
    checksum_digit = str(10 - ((odd_total + even_total) % 10) % 10)
    return ''.join(
        map(encoder.get, str(number) + checksum_digit)
    ).join((encoder['START'], encoder['STOP']))
