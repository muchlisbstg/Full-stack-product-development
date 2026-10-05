export function shouldSubmitMessageOnEnter(event) {
  if (event?.key !== 'Enter' || event.shiftKey) return false;

  const isComposing = event.isComposing === true
    || event.nativeEvent?.isComposing === true
    || event.keyCode === 229
    || event.nativeEvent?.keyCode === 229;

  return !isComposing;
}
