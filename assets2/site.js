/**
 * Docsynecx v2 - Accessible Navigation & Interactive Components
 * - Keyboard accessible mega-menus (Esc key to close, click outside)
 * - Accessible mobile menu drawer with ARIA controls
 */

document.addEventListener('DOMContentLoaded', () => {
  // 1. Mobile Menu Drawer
  const mobBtn = document.querySelector('.mob-btn');
  const mobDrawer = document.querySelector('.mob-drawer');

  if (mobBtn && mobDrawer) {
    mobBtn.addEventListener('click', () => {
      const isOpen = mobDrawer.classList.toggle('open');
      mobBtn.setAttribute('aria-expanded', String(isOpen));
      document.body.style.overflow = isOpen ? 'hidden' : '';
    });

    // Close mobile drawer when clicking any link inside it
    mobDrawer.querySelectorAll('a').forEach(link => {
      link.addEventListener('click', () => {
        mobDrawer.classList.remove('open');
        mobBtn.setAttribute('aria-expanded', 'false');
        document.body.style.overflow = '';
      });
    });
  }

  // 2. Keyboard Access for Mega-menus
  const dropdownItems = document.querySelectorAll('.mi.d');

  dropdownItems.forEach(item => {
    const trigger = item.querySelector('button.nav-btn, a');
    const panel = item.querySelector('.pn');

    if (!trigger || !panel) return;

    // Close on Escape key
    item.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') {
        panel.style.display = 'none';
        trigger.focus();
        setTimeout(() => panel.style.display = '', 200);
      }
    });
  });

  // Global Escape key closes all mobile menus
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && mobDrawer && mobDrawer.classList.contains('open')) {
      mobDrawer.classList.remove('open');
      mobBtn.setAttribute('aria-expanded', 'false');
      document.body.style.overflow = '';
      mobBtn.focus();
    }
  });
});
