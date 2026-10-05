const LIVE_REGION_ATTRIBUTES = Object.freeze({
  status: Object.freeze({
    role: 'status',
    'aria-live': 'polite',
    'aria-atomic': 'true',
  }),
  alert: Object.freeze({
    role: 'alert',
    'aria-live': 'assertive',
    'aria-atomic': 'true',
  }),
});

export function getLiveRegionAttributes(kind) {
  const attributes = LIVE_REGION_ATTRIBUTES[kind];
  if (!attributes) throw new TypeError(`Unknown live region kind: ${kind}`);
  return attributes;
}
