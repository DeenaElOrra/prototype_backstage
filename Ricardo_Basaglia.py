import streamlit as st 
import openai
from openai import OpenAI 

client = OpenAI(api_key=st.secrets['OPENAI_API_KEY'])

if "openai_model" not in st.session_state:
    st.session_state['openai_model'] = 'gpt-4o'

st.set_page_config(
    page_title='Chat Bot Backstage',
    page_icon='🔷',
    layout = 'centered'
)

st.title('ChatBot Ricardo')
st.sidebar.success('Select a page above')

#initialize chat histry
if "historico_mensagens_basaglia" not in st.session_state:
    st.session_state.historico_mensagens_basaglia = []

for mensagem in st.session_state.historico_mensagens_basaglia:
    with st.chat_message(mensagem["role"]):
        st.markdown(mensagem["content"])

#caracteristicas texto linkedin
biografia_basa = 'Ricardo Basaglia é uma figura proeminente no setor de recrutamento e liderança no Brasil, conhecido por sua vasta experiência e impacto significativo na transformação de carreiras e vidas. Atualmente, ele ocupa o cargo de CEO do PageGroup no Brasil, liderando as operações da Michael Page, Page Personnel, Page Executive, Page Outsourcing e Page Interim. Formação Acadêmica e Início de Carreira.Ricardo Basaglia possui uma formação acadêmica robusta, com um Mestrado em Administração de Empresas pela FGV/EAESP e uma extensão em Behavioral Science of Management pela Universidade de Yale. Ele iniciou sua trajetória acadêmica em Processamento de Dados na ETEC e no Centro Universitário Rio Preto, e posteriormente fez uma especialização na PUC-Campinas. Basaglia também estudou em renomadas instituições internacionais, como a Harvard Business School e a Yale School of Management.Sua carreira profissional começou na área de tecnologia, onde ele se destacou em projetos de transformação digital em grandes corporações. Aos 20 anos, Basaglia criou um portal de internet, que chamou a atenção de investidores interessados em comprar o projeto, marcando sua entrada no mercado corporativo.Trajetória ProfissionalApós ingressar no mercado corporativo, Ricardo Basaglia trabalhou no Sistema SETA de Ensino, participando de iniciativas de transformação digital. Em 2001, atuou como gerente de projetos de internet na Vivo e, em 2003, migrou para o setor comercial da Spread. Foi em 2007 que sua carreira deu uma guinada significativa, quando foi convidado para atuar como diretor executivo da Page Personnel, parte do PageGroup no Brasil. Como diretor executivo, Basaglia foi fundamental na expansão dos negócios e na abertura de novos escritórios pelo país. Sua habilidade em liderar e formar equipes fortes em diversos tipos de companhias o consolidou como o headhunter mais acompanhado do Brasil nas redes sociais. Em reconhecimento ao seu trabalho, ele foi promovido a CEO do PageGroup no Brasil, onde lidera as operações de todas as marcas do grupo.Contribuições e Impacto. Ricardo Basaglia é também autor do best-seller “Lugar de Potência: Lições de carreira e liderança de mais de 10 mil entrevistas, cafés e reuniões”, onde compartilha insights valiosos de sua extensa experiência. Além de seu trabalho no PageGroup, ele é Mentor em Gestão de Pessoas no G4 Educação e palestrante em diversos eventos sobre carreira e liderança. Basaglia acredita firmemente que o conhecimento só é transformador quando compartilhado. Ele se dedica a mostrar os comportamentos, habilidades, hábitos e crenças de grandes líderes do Brasil e do mundo, ajudando mais pessoas a alcançarem seu potencial máximo. Ele compartilha esses insights com mais de 3 milhões de pessoas através de suas redes sociais, colunas no Estadão e na Exame, na Rádio Eldorado, e no seu podcast “Lugar de Potência”. Filosofia de Liderança. A capacidade de adaptação é um dos principais ativos para qualquer profissional em um mundo dinâmico e imprevisível. Ricardo Basaglia enfatiza a importância da liderança em tempos de mudança, promovendo uma cultura de inovação dentro das organizações que inspira equipes a pensar fora da caixa. Ele acredita que a verdadeira transformação vem do impacto positivo na vida das pessoas, e isso guia sua abordagem em todas as suas iniciativas. Reconhecimentos e Futuro Ricardo Basaglia continua a ser uma figura influente no mundo corporativo, liderando a Michael Page, a maior empresa de recrutamento da América Latina, e contribuindo significativamente para a formação de líderes e profissionais em diversas indústrias. Sua visão estratégica e compromisso com o desenvolvimento de talentos garantem que ele continuará a ser um líder destacado e uma inspiração para muitos nos próximos anos. Essa biografia detalhada combina informações de várias fontes para fornecer uma visão abrangente sobre Ricardo Basaglia, destacando sua trajetória acadêmica, carreira, contribuições e filosofia de liderança.'

linkedin_1 = '"Sua voz nunca será mais importante que seu ouvido. Um líder que se blinda e não ouve seus liderados, deixando a vaidade tomar conta, por mais experiente que seja, está adotando a receita do seu próprio fim. Aqui vão 3 práticas que você precisa aderir para estimular a voz do seu time:--1. Corra atrás. Ninguém vai te dar feedback, seus liderados têm medo. Estimule-os. Pergunte como pode melhorar. Isso te ajuda a encontrar pontos cegos que, sozinho, você não perceberia.--2. Não leve para o ringue. Não interrompa, não queira se justificar.  Escute, por mais que não concorde, e no final faça essas perguntas: - Quais comportamentos você não gosta que eu tenha e acha que devo melhorar? - ‘’O que eu deveria parar e começar a fazer?’’--3. Ambiente seguro. Garanta que seus liderados se sintam confiantes para falar abertamente, sem medo. Mostra que você não só valoriza o feedback deles, como trabalha para melhorar o ponto levantado.Faça com que eles tenham vontade e confiança em poder falar abertamente e que isso não vai gerar um problema futuramente. Jogue o jogo abertamente. Sei que esse tipo de conversa nunca é fácil, eu mesmo demorei para entender que quem dá feedback também precisa estar preparado para receber. Falo sobre isso na minha aula no programa presencial G4 Gestão de Pessoas. Você aprenderá diretamente comigo, Vabo e Bernardinho as práticas de gestão e liderança das empresas que mais crescem no país.'

linkedin_2 = "Se existe um conselho senso comum que não acredito é “siga o seu sonho”. Sonhos têm como premissa a fantasia e não apego à realidade. E isso não é um problema. O erro está em resumir sua realidade aos sonhos. Sendo mais pragmático: não siga seus sonhos, procure uma atividade em que você é diferenciado. Tão alegre quanto quem realiza o que sonha na carreira é aquela pessoa que se destaca no que se propõe. Seguir nossos sonhos não significa muito, pois nem sempre somos excepcionais em tudo o que queremos. Porém, ao buscar uma atividade onde nos destacamos, encontramos um lugar para crescer e sermos protagonistas de nossas vidas. É onde nossos talentos naturais podem nos levar além do comum. Espero que você seja alguém de sorte, que seu maior talento esteja ligado ao seu sonho de criança. Se como a maioria das pessoas esse não for o caso, faça os dois e brilhe!"

linkedin_3 = "Se você quer agradar todo mundo, não seja líder. Venda sorvete. Os maiores lideres são aqueles que sabem dar feedback. Afinal, um executivo que não conversa com seus liderados e não joga o jogo abertamente, por mais experiente que seja, pode estar adotando a receita para o fracasso. Por isso, considere esses pontos na hora da reunião de 1:1 com seu liderado > --1. Jogue limpo Feedback não é elogio, nem todos são agradáveis, mas todos têm valor. Não enrole e jogue o jogo abertamente.-- 2. Esqueça o sanduíche. 70% dos candidatos saem de uma reunião sem saber o que foi elogio e o que foi reclamação. Afinal, a maioria dos líderes dão feedback “sanduíche”, entregam um elogio, depois uma critica e para fechar a reunião com um bom astral fazem mais um feedback positivo. Não funciona.--3. Monte um plano. Depois do feedback o candidato está ansioso para melhorar.Explique o contexto e foque no que deve ser feito dali para frente. Coloque prazos. Mostre o resultado que ele vai ter se alcançar aqueles pontos. Um feedback bem recebido e trabalhado pode destravar novas oportunidades na carreira. Sei que esse tipo de conversa nunca é fácil, tive que aprender muito para me tornar um líder que entrega resultados acima da média. Se você quer aprender sobre contratação, gestão de time, e as práticas de liderança das grandes empresas, participe do G4 Gestão de Pessoas. São 3 dias de conteúdos e mentorias para aprender a liderar times de alta performance."

linkedin_4 = "Quando alguém se apaixona pelas suas flores e não pelas suas raízes ficará completamente perdido quando o outono ou o inverno chegarem. Isso vale para relacionamentos amorosos, familiares, de amizade ou profissionais."

linkedin_5 = "Se preocupar com os outros é um dos maiores desperdícios de energia que você poderia ter.Sejamos honestos: os outros não se preocupam tanto assim com você. Mais do que isso, é que certo para um pode não ser para outro, tornando impossível a possibilidade de agradar a todos. Aos poucos, no anseio da popularidade, você se distancia dos seus sonhos. Aos poucos, deixa de ser você. E se ainda não consegui te convencer, nunca se esqueça: a opinião dos outros muda com frequência. Você não só vai desagradar muita gente, você vai desagradar gente que gostava de você e mudou de opinião. Talvez você discorde. Argumente que eu estou ficando velho e acho isso uma excelente colocação. Mas tudo bem, não me importo tanto assim com a opinião dos outros. "

linkedin_6 = "O segredo do sucesso vai além das habilidades técnicas. É sobre entender profundamente o ambiente ao seu redor. A cultura da empresa, suas regras e, principalmente, as pessoas que compõem esse universo são peças-chave. Investir tempo em compreender esse contexto aumenta sua eficiência e também direciona seus esforços para onde realmente importam. Analise, absorva e adapte-se. É assim que você não apenas sobrevive, mas prospera nesse ambiente desafiador.‌"


biografia_analise = """
                    - Contexto
                    - Experiências
                    - Trajetória Profissional
                    - Contribuições
                    - Impacto na Comunidade
                    - Competências
                    - Assuntos Dominados
                    - Formas de Agregar para o Leitor
                """
caracteristica_linkedin =  """
                - Escolha de Palavras: identifique as palavras e expressões frequentes e distintivas.
                - Complexidade Lexical: Medir a diversidade e a complexidade do vocabulário utilizado.
                - Estrutura das Frases: Analisar a estrutura gramatical das frases, incluindo o uso de frases curtas e longas.
                - Uso de Pontuação: Observar o uso de vírgulas, pontos, travessões, pontos de exclamação e interrogação.
                - Tom de Voz: Determinar se o tom é assertivo, reflexivo, sarcástico, etc.
                - Formalidade: Avaliar o nível de formalidade do texto.
                - Persuasividade: Analisar técnicas persuasivas, como apelos emocionais e argumentos lógicos.
                - Sentimento: Avaliar a polaridade (positiva, negativa, neutra) e a intensidade emocional do texto.
                - Temas e Tópicos: Identificar os principais temas e tópicos abordados no texto.
                - Figura de Linguagem: Detectar o uso de metáforas, símiles, ironias, hipérboles, etc.
                - Uso de Repetição: Identificar padrões de repetição de palavras e frases para ênfase.
                - Coerência: Avaliar a lógica e a fluidez das ideias apresentadas no texto.
                - Entonação: Estudar a entonação das frases.
                - Ritmo e Pausas: Analisar o ritmo da fala e o uso de pausas.
                - Marcas de Identidade: Detectar elementos que indicam a identidade pessoal ou profissional do autor.
                - Referências Pessoais: Observar menções a experiências pessoais, crenças, e valores.
            """

# User input
prompt = st.chat_input("Digite algo para iniciar a conversa...")
if prompt:
    st.chat_message('user').markdown(prompt)
    st.session_state.historico_mensagens_basaglia.append({"role": "user", "content": prompt})

    response = openai.chat.completions.create(
        model= 'gpt-4o',
        temperature=0.7,
        messages=[
           {'role':'system', 'content':f"""'Você é a melhor agência de marketing de conteúdo estratégico para o Linkedin. Você sabe escrever os textos mais coesos, claros, explicativos, e objetivos para o seu cliente. A fim de gerar textos escritos customizados exatamente do jeito que o cliente se comunica, sobre os assuntos que ele aborda e de uma maneira que cative qualquer público leitor a ler, você deve considerar os seguintes aspectos:'
            '1. Entender quem é o cliente em análise. Para isso, o nome do cliente será informado e a sua biografia também. O nome do cliente é Ricardo Basaglia.Quando a biografia do cliente for informada, quero que considere esses aspectos ao reproduzir um texto igual a personalidade produziria: {biografia_analise}. A biografia do Ricardo Basaglia é a seguinte: {biografia_basa}' 
            '2. Aprender a escrever com as mesmas características que o cliente escreve. Para isso, serão fornecidos posts do LinkedIn do cliente como referência. Com base nesses posts de referência, quero que extraia as características seguintes {caracteristica_linkedin}. É importante você levar todas as características de escrita da personalidade em consideração ao gerar o texto,  a proporção de parágrafo por caractere nas referências de post fornecidas e a estrutura dos parágrafos e a sua quantidade. Além disso, comece o texto com uma oração curta e cativante ao leitor, depois elabore as ideias em primeira pessoa, num tom pessoal, e finalize a ideia em terceira pessoa, num contexto de aconselhar o leitor do que deve ser feito para evitar o fracasso. Os posts de referência são o seguinte: {linkedin_1}, {linkedin_2}, {linkedin_3}, {linkedin_4}, {linkedin_5}, {linkedin_6} .' 
            '3. Com base na consulta de todos esses dados, quero que escreva um texto com o numero de caracteres que for informado sobre e sobre o tema requisitado em forma de parágrafos. Por favor, respeite a quantidade de caracteres que deve ser utilizada como referência para produzir o texto. O texto gerado não pode ter um tom genérico, ele deve conter todas as características que o torna personalizado e customizado ao jeito de escrita do cliente. '
            '4. Finalmente, sugira novos assuntos que você ache pertinente esse cliente falar com base em todos os temas e tópicos já abordados. Evite sugerir assuntos que possam gerar polêmica.'"""},
            *st.session_state.historico_mensagens_basaglia
        ]
    )

    resposta = response.choices[0].message.content
    st.session_state.historico_mensagens_basaglia.append({"role": "assistant", "content": resposta})

    with st.chat_message('assistant'):
        st.markdown(resposta)








#  {'role':'system', 'content':f"""'Você é a melhor agência de marketing de conteúdo estratégico para o Linkedin. Você sabe escrever os textos mais coesos, claros, explicativos, e objetivos para o seu cliente. A fim de gerar textos escritos customizados exatamente do jeito que o cliente se comunica, sobre os assuntos que ele aborda e de uma maneira que cative qualquer público leitor a ler, você deve considerar os seguintes aspectos:'
#             '1. Entender quem é o cliente em análise. Para isso, o nome do cliente será informado e a sua biografia também. Quando a biografia do cliente for informada, quero que considere esses aspectos ao reproduzir um texto igual a personalidade produziria: {biografia_analise}. ' 
#             '2. Aprender a escrever com as mesmas características que o cliente escreve. Para isso, serão fornecidos posts do LinkedIn do cliente como referência. Com base nesses posts de referência, quero que extraia as características seguintes {caracteristica_linkedin}. É importante você levar todas as características de escrita da personalidade em consideração ao gerar o texto,  a proporção de parágrafo por caractere nas referências de post fornecidas e a estrutura dos parágrafos e a sua quantidade. Além disso, comece o texto com uma oração curta e cativante ao leitor, depois elabore as ideias em primeira pessoa, num tom pessoal, e finalize a ideia em terceira pessoa, num contexto de aconselhar o leitor do que deve ser feito para evitar o fracasso. ' 
#             '3. Com base na consulta de todos esses dados, quero que escreva um texto com o numero de caracteres que for informado sobre e sobre o tema requisitado em forma de parágrafos. Por favor, respeite a quantidade de caracteres que deve ser utilizada como referência para produzir o texto. O texto gerado não pode ter um tom genérico, ele deve conter todas as características que o torna personalizado e customizado ao jeito de escrita do cliente. '
#             '4. Finalmente, sugira novos assuntos que você ache pertinente esse cliente falar com base em todos os temas e tópicos já abordados. Evite sugerir assuntos que possam gerar polêmica.'"""}