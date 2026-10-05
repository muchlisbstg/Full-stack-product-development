export function isConnectionSetupLocked(busy, connection) {
  return busy || connection === 'checking';
}
