const FOCUSABLE_SELECTOR = 'a[href], button:not([disabled]), input:not([disabled]), select:not([disabled]), textarea:not([disabled]), [tabindex]:not([tabindex="-1"])';

export function focusDialogFirstControl(dialog) {
  const firstControl = dialog?.querySelector(FOCUSABLE_SELECTOR);
  firstControl?.focus();
}

export function restoreDialogFocus(element) {
  element?.focus?.();
}

export function trapDialogTabKey(event) {
  if (event.key !== 'Tab') return;

  const dialog = event.currentTarget;
  const controls = Array.from(dialog.querySelectorAll(FOCUSABLE_SELECTOR));
  if (controls.length === 0) {
    event.preventDefault();
    dialog.focus();
    return;
  }

  const firstControl = controls[0];
  const lastControl = controls[controls.length - 1];
  const activeElement = dialog.ownerDocument.activeElement;

  if (event.shiftKey && (activeElement === firstControl || !dialog.contains(activeElement))) {
    event.preventDefault();
    lastControl.focus();
  } else if (!event.shiftKey && (activeElement === lastControl || !dialog.contains(activeElement))) {
    event.preventDefault();
    firstControl.focus();
  }
}
