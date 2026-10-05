export const JSON_BODY_LIMIT = 1024 * 1024;

export function jsonBodyErrorHandler(error, _request, response, next) {
  if (error?.type === 'entity.too.large') {
    return response.status(413).json({ error: 'Request body exceeds the 1 MiB limit.' });
  }
  if (error?.type === 'entity.parse.failed') {
    return response.status(400).json({ error: 'Request body must be valid JSON.' });
  }
  if (error?.type === 'charset.unsupported') {
    return response.status(415).json({ error: 'Request body must use UTF-8 encoding.' });
  }
  if (error?.type === 'encoding.unsupported') {
    return response.status(415).json({ error: 'Unsupported request content encoding.' });
  }
  return next(error);
}
