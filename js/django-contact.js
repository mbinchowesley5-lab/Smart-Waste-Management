(function () {
  const form = document.querySelector('#contactForm');
  const notice = document.querySelector('#formNotice');
  if (!form) return;

  const csrfToken = () => document.cookie.split('; ').find(row => row.startsWith('csrftoken='))?.split('=')[1];

  form.addEventListener('submit', async () => {
    if (!form.checkValidity()) return;

    try {
      const response = await fetch('/contact/', {
        method: 'POST',
        headers: { 'X-CSRFToken': csrfToken() || '' },
        body: new FormData(form),
        credentials: 'same-origin',
      });

      if (!response.ok) throw new Error('Contact request was not accepted.');
      notice.textContent = 'Your details were validated. Message delivery will be enabled when PICKCAM support is connected.';
      notice.className = 'form-notice text-success';
    } catch (error) {
      notice.textContent = 'We could not process this message right now. Please try again later.';
      notice.className = 'form-notice text-danger';
    }
  });
})();
