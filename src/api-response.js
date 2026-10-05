export async function parseJsonResponse(response, fallbackMessage = 'The server returned an invalid response.') {
  try {
    return await response.json();
  } catch {
    const statusSuffix = Number.isInteger(response?.status) && response.status > 0
      ? ` (HTTP ${response.status})`
      : '';
    throw new Error(`${fallbackMessage}${statusSuffix}`);
  }
}
