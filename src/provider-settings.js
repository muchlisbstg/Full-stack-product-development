export function isConnectionSetupLocked(busy, connection) {
  return busy || connection === 'checking';
}

export function resetConnectionForProviderConfigChange({
  setModels,
  setConnection,
  setConnectionMessage,
}) {
  setModels([]);
  setConnection('idle');
  setConnectionMessage('');
}

export function markProviderAsResponding({ setConnection, setConnectionMessage }) {
  setConnection('connected');
  setConnectionMessage('Connected and responding.');
}
