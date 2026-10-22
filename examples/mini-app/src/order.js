import { clampQuantity, discountRate, roundCurrency } from './math.js';
/** Training fixture: fake prices, no customer records. */
export function summarizeOrder({ unitPrice, quantity, member = false }) {
  if (!Number.isFinite(unitPrice) || unitPrice < 0) throw new RangeError('invalid unitPrice');
  const subtotal = roundCurrency(unitPrice * clampQuantity(quantity));
  const discount = roundCurrency(subtotal * discountRate(subtotal, member));
  return { subtotal, discount, total: roundCurrency(subtotal - discount) };
}
