export function apiNotFoundHandler(request, response, next) {
  if (request.path === '/api' || request.path.startsWith('/api/')) {
    return response.status(404).json({ error: 'API endpoint not found.' });
  }
  return next();
}
