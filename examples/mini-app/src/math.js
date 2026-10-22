export function clampQuantity(quantity) {
  if (!Number.isInteger(quantity) || quantity < 0) throw new RangeError('quantity must be a nonnegative integer');
  return quantity;
}
export function discountRate(subtotal, isMember) {
  if (subtotal < 0) throw new RangeError('subtotal must be nonnegative');
  return isMember && subtotal >= 100 ? 0.1 : 0;
}
export function roundCurrency(value){ return Math.round((value + Number.EPSILON) * 100) / 100; }
