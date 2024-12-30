// Seleciona o botão para adicionar metas
const addGoalButton = document.querySelector('.add-goal-btn');

// Seleciona o container onde as metas serão exibidas
const goalsSection = document.querySelector('.goals-section');

// Função para criar uma nova meta
function createGoal(title, description) {
    // Cria o elemento do cartão de meta
    const goalCard = document.createElement('div');
    goalCard.classList.add('goal-card');

    // Adiciona o título da meta
    const goalTitle = document.createElement('h3');
    goalTitle.textContent = title;
    goalCard.appendChild(goalTitle);

    // Adiciona a descrição da meta
    const goalDescription = document.createElement('p');
    goalDescription.textContent = description;
    goalCard.appendChild(goalDescription);

    // Adiciona o cartão à seção de metas
    goalsSection.appendChild(goalCard);
}

// Evento para adicionar uma nova meta ao clicar no botão
addGoalButton.addEventListener('click', () => {
    const title = prompt('Digite o título da sua nova meta:');
    const description = prompt('Digite uma breve descrição da meta:');

    if (title && description) {
        createGoal(title, description);
    } else {
        alert('Por favor, preencha os dois campos para adicionar uma nova meta.');
    }
});

// Evento para expandir e recolher as metas ao clicar
goalsSection.addEventListener('click', (event) => {
    // Verifica se clicou em um cartão de meta
    const clickedCard = event.target.closest('.goal-card');
    if (clickedCard) {
        // Alterna a classe "expanded" para expandir ou recolher
        clickedCard.classList.toggle('expanded');
    }
});
