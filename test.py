import decimal


a = decimal.Decimal('6.625')
b = float(a.quantize(decimal.Decimal('0.00'), rounding=decimal.ROUND_HALF_UP))
print(b)