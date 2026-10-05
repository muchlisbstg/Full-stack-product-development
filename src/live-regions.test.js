import test from 'node:test';
import assert from 'node:assert/strict';
import { getLiveRegionAttributes } from './live-regions.js';

test('announces connection updates politely as a complete status', () => {
  assert.deepEqual(getLiveRegionAttributes('status'), {
    role: 'status',
    'aria-live': 'polite',
    'aria-atomic': 'true',
  });
});

test('announces chat failures assertively as a complete alert', () => {
  assert.deepEqual(getLiveRegionAttributes('alert'), {
    role: 'alert',
    'aria-live': 'assertive',
    'aria-atomic': 'true',
  });
});

test('rejects unsupported live-region kinds', () => {
  assert.throws(() => getLiveRegionAttributes('unknown'), /Unknown live region kind/);
});
