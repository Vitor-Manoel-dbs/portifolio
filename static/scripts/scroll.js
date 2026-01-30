// Scroll suave para uma sessão específica
function irParaSessao(sessao) {
    const elemento = document.getElementById(sessao);
    if (elemento) {
        elemento.scrollIntoView({
            behavior: 'smooth'
        });
    }
}

// Função que mostra/esconde o menu
function controlaMenu() {
    const menu = document.getElementById('menu');
    if (!menu) return;

    // Ajuste fino: menu aparece após rolar 100px
    if (window.scrollY > 400) {
        menu.classList.add('aparecer');
    } else {
        menu.classList.remove('aparecer');
    }
}

// Eventos
window.addEventListener('scroll', controlaMenu);
window.addEventListener('load', controlaMenu);
