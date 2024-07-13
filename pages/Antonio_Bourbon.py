import streamlit as st
import openai
from openai import OpenAI 

st.title('ChatBot Antonio')

client = OpenAI(api_key=st.secrets['OPENAI_API_KEY'])

if "openai_model" not in st.session_state:
    st.session_state['openai_model'] = 'gpt-4o'

st.sidebar.success('Select a page above')

#initialize chat histry
if "historico_mensagens_bourbon" not in st.session_state:
    st.session_state.historico_mensagens_bourbon = []

for mensagem in st.session_state.historico_mensagens_bourbon:
    with st.chat_message(mensagem["role"]):
        st.markdown(mensagem["content"])

#caracteristicas texto linkedin
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

biografia_bourbon = """
                '✨ Jornada Inspiradora:'
                'Antônio Vezozzo possui carreira focada em estratégias no setor de serviços, especificamente em hotelaria. Deu os primeiros passos no coração do hotel, respirando negócios desde o início. Apesar do sonho inicial de seguir a carreira esportiva, a vida o guiou para o mundo da hotelaria quando um restaurante do Bourbon Curitiba Hotel & Suites cruzou seu caminho.'

                '🌐 Expansão e Inovação:'
                'Como líder na Bourbon Gastronomia, Antônio ampliou a equipe, desenhando processos e estratégias. Simultaneamente, a padronização tornou-se o seu desafio, solidificando a sua visibilidade e inspirando a criação da marca-mãe, Bourbon Hospitalidade.'

                'Competitividade e Sucesso:'
                'O espírito competitivo de Antônio impulsiona suas iniciativas de sucesso. Jovem, inovador, exala seriedade e credibilidade, sendo mais do que um simples líder: é a personificação da perseverança e do otimismo no cenário corporativo.''

                'Desafio e inspiração:'
                'A missão de Antônio vai além da hospitalidade, buscando ampliar redes e inspirar jovens a alcançarem grandes feitos. Valores como transparência, respeito, honestidade e cordialidade norteiam sua abordagem.'

                '#Inovação #Liderança #Hospitalidade #BourbonHospitalidade'
                'Vamos construir juntos um futuro melhor.'"""

linkedin_1b = """
                'Você já conheceu seus ídolos?'

                'Tive o privilégio de crescer com o meu.'

                'Dia 19 de Junho completou um ano de seu falecimento, meu avô, Alceu Ântimo Vezozzo, é uma fonte constante de inspiração para mim. '

                'Fundador da Bourbon Hotels & Resorts, seu percurso reflete não apenas o espírito empreendedor, mas uma visão perspicaz que continua a guiar a indústria hoteleira. '

                'Desde o início, em 1963, com a inauguração do primeiro hotel em Londrina, ele definiu padrões de excelência e cultivou um ambiente onde cada detalhe é pensado para melhorar a experiência do hóspede.'

                'Seu compromisso em construir negócios longevos e sua capacidade de antever as necessidades do mercado são lições que permanecem relevantes. '

                'Hoje, graças à sua fundação sólida e à continuidade de suas práticas inovadoras, a Rede Bourbon é um símbolo de qualidade e resiliência no setor hoteleiro. '

                'Mais do que edifícios ou locais, meu avô construiu espaços onde as pessoas podem encontrar conforto, e acolhimento, uma verdadeira celebração do que significa ser visionário nos negócios. A sua falta será eterna.'"""""

linkedin_2b = """ 
                'Na Rede Bourbon, a transformação de cada       empreendimento conforme a época do ano é uma arte que reflete nossa dedicação em manter cada propriedade vibrante e convidativa ao longo do ano. '

                'Um exemplo claro dessa dinâmica é o Arraiá do Bourbon Atibaia, onde o espírito das festas juninas toma conta do resort, oferecendo uma vivência rica e autêntica aos nossos hóspedes.'

                'Essas mudanças sazonais são vitais para a renovação contínua da experiência do cliente, permitindo-nos celebrar a diversidade cultural e manter nossos serviços relevantes. '

                'Por aqui, cada estação é uma nova oportunidade de encantar e engajar, garantindo que nossa hospitalidade não só atenda, mas também supere as expectativas dos hóspedes, mantendo o negócio dinâmico e atrativo.'"""

linkedin_3b = """"
                'O verdadeiro valor está na riqueza das experiências compartilhadas e na satisfação profunda que elas trazem.

                No coração de Atibaia, o Bourbon Atibaia Resort não é apenas um destino, mas uma jornada cultural imersiva em um ambiente acolhedor e atento a cada detalhe. 

                Em uma vasta área de 400 mil m², o resort combina uma impressionante infraestrutura de lazer e convenções com a tranquilidade da natureza, criando um espaço onde cada momento é desenhado para enriquecer a experiência de quem nos visita.

                A hospitalidade no Bourbon Atibaia vai além do tradicional. Aqui, a ênfase está em oferecer uma vivência autêntica e completa, desde o relaxamento no Mandí Nature SPA até a variada programação de lazer e a alta gastronomia nos restaurantes especializados.

                Cada atividade é uma porta aberta para novas descobertas, permitindo aos hóspedes não apenas descansar, mas também se conectar com novas experiências e criar memórias inesquecíveis. 

                É essa integração de serviços excepcionais com a atenção genuína aos interesses e bem-estar dos hóspedes que torna o Bourbon Atibaia um modelo de sucesso na indústria hoteleira.'
                """

linkedin_4b = """"
                'A experiência que vai além da culinária e se entrelaça com a cultura. 

                Isso é proporcionar uma experiência de verdade, é o que buscamos em cada detalhe dos empreendimentos da Bourbon Gastronomia, como no Bourbon Bistrot, localizado em Curitiba/PR.

                Comandado pelo chef Eduardo Richard, semifinalista do MasterChef Brasil e apaixonado pela cozinha francesa, nosso bistrô é um convite para conhecer a França através dos sabores. 

                Aqui, a gastronomia é uma porta para a cultura, oferecendo aos nossos  clientes uma imersão autêntica que transcende o tradicional conceito de hospitalidade.

                Cada prato do Bourbon Bistrot reflete a essência da França, com toques de sofisticação em preparações descomplicadas que capturam o espírito parisiense. 

                Essa conexão culinária enriquece a experiência dos visitantes e reafirma nosso compromisso com uma hospitalidade que valoriza a autenticidade e a cultura.'
                """

linkedin_5b = """
                Na indústria hoteleira, a tecnologia tem se tornado fundamental para melhorar a personalização e o conforto durante as estadas. 

                Quartos inteligentes equipados com automação de temperatura, iluminação personalizada e sistemas de entretenimento controlados via voz ou aplicativos oferecem aos hóspedes alto nível de conveniência. 

                Adicionalmente, check-ins e check-outs por dispositivos móveis agilizam os processos e aumentam a satisfação dos hóspedes. Uma das facilidades atreladas a isso é a possibilidade de utilização do smartphone como chave da acomodação. 

                Essas inovações não apenas otimizam as operações hoteleiras, mas também garantem que cada visita seja adaptada às preferências individuais do hóspede, proporcionando uma experiência genuinamente personalizada e confortável. 

                Assim, a tecnologia na hospitalidade está redefinindo o modo como os serviços são entregues, com foco no conforto e na personalização para enriquecer cada momento da estada.
                """

linkedin_6b = """
                A cada prato servido e sorriso compartilhado, a equipe de nossa cozinha personifica a dedicação e a paixão que definem a verdadeira hospitalidade. Nos bastidores, uma orquestra culinária trabalha em harmonia. Cada membro traz habilidades específicas e um compromisso inabalável com a qualidade, criando experiências gastronômicas inesquecíveis.

                Nossa cozinha é um palco onde a arte e a precisão se encontram para encantar os hóspedes. Ingredientes cuidadosamente selecionados são transformados em obras de arte comestíveis. 

                Este vídeo captura o espírito de nossa equipe, cuja dedicação nos bastidores assegura uma experiência extraordinária para cada hóspede.
                """
# User input
prompt = st.chat_input("Digite algo para iniciar a conversa...")
if prompt:
    st.chat_message('user').markdown(prompt)
    st.session_state.historico_mensagens_bourbon.append({"role": "user", "content": prompt})

    response = openai.chat.completions.create(
        model= 'gpt-4o',
        temperature=0.7,
        messages=[
            {'role':'system', 'content':f"""'Você é a melhor agência de marketing de conteúdo estratégico para o Linkedin. Você sabe escrever os textos mais coesos, claros, explicativos, e objetivos para o seu cliente. A fim de gerar textos escritos customizados exatamente do jeito que o cliente se comunica, sobre os assuntos que ele aborda e de uma maneira que cative qualquer público leitor a ler, você deve considerar os seguintes aspectos:'
            '1. Entender quem é o cliente em análise. Para isso, o nome do cliente será informado e a sua biografia também. O nome do cliente é Antonio Bourbon.Quando a biografia do cliente for informada, quero que considere esses aspectos ao reproduzir um texto igual a personalidade produziria: {biografia_analise}. A biografia do Antonio Bourbon é a seguinte: {biografia_bourbon}' 
            '2. Aprender a escrever com as mesmas características que o cliente escreve. Para isso, serão fornecidos posts do LinkedIn do cliente como referência. Com base nesses posts de referência, quero que extraia as características seguintes {caracteristica_linkedin}. É importante você levar todas as características de escrita da personalidade em consideração ao gerar o texto,  a proporção de parágrafo por caractere nas referências de post fornecidas e a estrutura dos parágrafos e a sua quantidade. Além disso, comece o texto com uma oração curta e cativante ao leitor, depois elabore as ideias em primeira pessoa, num tom pessoal, e finalize a ideia em terceira pessoa, num contexto de aconselhar o leitor do que deve ser feito para evitar o fracasso. Os posts de referência são o seguinte: {linkedin_1b}, {linkedin_2b}, {linkedin_3b}, {linkedin_4b}, {linkedin_5b}, {linkedin_6b} .' 
            '3. Com base na consulta de todos esses dados, quero que escreva um texto com o numero de caracteres que for informado sobre e sobre o tema requisitado em forma de parágrafos. Por favor, respeite a quantidade de caracteres que deve ser utilizada como referência para produzir o texto. O texto gerado não pode ter um tom genérico, ele deve conter todas as características que o torna personalizado e customizado ao jeito de escrita do cliente. '
            '4. Finalmente, sugira novos assuntos que você ache pertinente esse cliente falar com base em todos os temas e tópicos já abordados. Evite sugerir assuntos que possam gerar polêmica.'"""},
            *st.session_state.historico_mensagens_bourbon
        ]
    )

    resposta = response.choices[0].message.content
    st.session_state.historico_mensagens_bourbon.append({"role": "assistant", "content": resposta})

    with st.chat_message('assistant'):
        st.markdown(resposta)








