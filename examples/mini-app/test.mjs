import assert from 'node:assert/strict';
import { summarizeOrder } from './src/index.js';
assert.deepEqual(summarizeOrder({unitPrice:20, quantity:5, member:true}),{subtotal:100,discount:10,total:90});
assert.deepEqual(summarizeOrder({unitPrice:20, quantity:4, member:true}),{subtotal:80,discount:0,total:80});
assert.deepEqual(summarizeOrder({unitPrice:20, quantity:5, member:false}),{subtotal:100,discount:0,total:100});
assert.throws(()=>summarizeOrder({unitPrice:-1,quantity:1}),RangeError);
assert.throws(()=>summarizeOrder({unitPrice:10,quantity:1.2}),RangeError);
console.log('5 self-owned fixture tests passed');
