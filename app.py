import streamlit as st
from PIL import Image
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide", page_title="Douglas Winston")

st.title('Douglas Winston')
st.markdown('#### Data Product Manager')

data = [
        {'Ano': 2019, 'Gestão de Pessoas': 0.5, 'Entrega de Valor': 1.5, 'Dados e Analytics': 2.0, 'Criatividade e Soluções': 3.0, 'Gestão de Produto': 0.5},
        {'Ano': 2020, 'Gestão de Pessoas': 1.0, 'Entrega de Valor': 2.5, 'Dados e Analytics': 3.5, 'Criatividade e Soluções': 3.5, 'Gestão de Produto': 1.5},
        {'Ano': 2021, 'Gestão de Pessoas': 2.0, 'Entrega de Valor': 3.5, 'Dados e Analytics': 4.0, 'Criatividade e Soluções': 3.8, 'Gestão de Produto': 2.5},
        {'Ano': 2022, 'Gestão de Pessoas': 3.8, 'Entrega de Valor': 4.1, 'Dados e Analytics': 4.5, 'Criatividade e Soluções': 4.0, 'Gestão de Produto': 3.0},
        ]

df = pd.DataFrame(data)

df_melted = df.melt(id_vars=['Ano'],
                            value_vars=['Gestão de Pessoas',
                                        'Entrega de Valor',
                                        'Dados e Analytics',
                                        'Criatividade e Soluções',
                                        'Gestão de Produto'])


coluna_header = st.columns((2, 1, 2, 5), gap='small')

perfil = Image.open('perfil.jpeg')
personalidade = Image.open('personalidade.png')

coluna_header[0].image(perfil, width=350)

fig = px.line_polar(df_melted, r='value', theta='variable', color='Ano', color_discrete_sequence=px.colors.qualitative.G10, line_close=True, render_mode='SVG')

fig.update_layout(legend=dict(
    orientation="h",
    yanchor='middle',
    xanchor="center",
    x=0.5
))

fig.update_layout(
    template=None,
    polar = dict(
        radialaxis = dict(range=[0, 5], showticklabels=False, ticks=''),
        # angularaxis = dict(showticklabels=False, ticks='')
    )
)
coluna_header[2].write(fig)

colunas = st.columns(4)
colunas[0].markdown('São Paulo, SP')
colunas[1].markdown('+55 62 996990837')
colunas[2].markdown('douglas.winston.r@gmail.com')
colunas[3].markdown('[linkedin.com/in/douglas-winston](https://www.linkedin.com/in/douglas-winston/)')

html_componet = """<div style="text-align: center"> your-text-here </div>"""

st.markdown('### Experiência')
st.markdown("""
##### 2022, **Coordenador de Dados**, Recovery, São Paulo, SP (***1 ano e 4 meses)***

- Liderei um time excepcional a construir ferramentas baseadas em dados e inteligência artificial para a precificação de carteiras de créditos inadimplidos.
- A cada Sprint fizemos descoberta de produto, testes de funcionalidade com usuários especialistas e avaliações constantes da proposta de valor de cada funcionalidade.
- Utilizamos o máximo de processamento e tratamento de dados internos e de mercado para o treinamento de modelos estatísticos e computacionais robustos.
- Conseguimos com cada melhoria nas métricas dos modelos e usabilidade do produto, reduzir o risco de investimento de centenas de milhões de reais.
- Tenho orgulho de dizer que construímos uma das ferramentas mais avançadas do pais no que diz respeito a recuperação de crédito.

**Habilidades**: Product Management · Agile · Scrum · Python · PySpark · Power BI · Classification · Regression · Survival · Boosting · Neural Networks · Azure · Databricks · Streamlit
""")
st.markdown("""
##### 2021, **Cientista de Dados,** Carajás, Maceió, AL, (***1 ano***)

- Como consultor ajudei a mapear as etapas da jornada do cliente nas lojas online e físicas de produtos relacionados a construção, decoração e utensílios domésticos.
- Em reuniões semanais identifiquei e propus soluções de dados para guiar ações de comunicação com o cliente (CRM) usando a base de dados de 10 lojas online e físicas.
- Desenvolvi modelos de segmentação e classificação de clientes para identificar o tempo e a fase da construção na obra ou reforma do cliente.
- Elaborei painéis de acompanhamento com filtros interativos para que a gestão de vendas conseguisse segmentar os clientes de acordo com critérios de cada campanha de marketing.

**Habilidades**: Business Strategy · SQL · Qlik Sense · CRM · Customer Segmentation · Product Vision · Data Analysis · Python
""")
st.markdown("""
##### 2021, Cientista de Dados, Grupo Saga, Goiânia, GO, (1 ano)

- Construí e disseminei produtos de dados para as concessionárias automobilísticas de diversas marcas do Grupo Saga (Toyota, BMW, Volkswagen, entre outras).
- Realizei análises de evasão de clientes em revisões programadas, análises de recompra de veículos novos e propus uma segmentação da base de clientes por critérios do negócio.
- Construí também um processo de extração e recomendação de precificação de assinaturas de carros da concessionária com base nos preços concorrentes do mercado (Localiza, Movida, Porto Seguro).

**Habilidades**: Gestão de projetos · SQL · Google Cloud · Dataform · Data Scrapping · Amazon Athena · S3 · PySpark · Python
""")
st.markdown("""
##### 2020, Cientista de Dados, Acordo Certo, São Paulo, SP,  (1 ano e 2 meses)

- Liderei tecnicamente uma equipe de cientistas de dados com foco na construção de um processo de tomada de decisão de acionamentos de consumidores com inadimplência no mercado de crédito.
- Desenvolvi modelos de propensão de cadastro e de pagamento/acordo em um site estilo marketplace para a negociação de dívidas.
- Construí modelos de LTV para estimar o valor de recuperação de cada consumidor/cliente otimizando os custos com acionamentos nos canais de sms e e-mail.
- Avaliei métricas relevantes para o negócio como taxa de clique, quantidade de cadastros, quantidade de acordos, entre outros, correlacionando com o resultado dos modelos.

**Habilidades**: Google Cloud · Big Query · SQL · Dataform · Modelos de Propensão · Data Studio · Python
""")
st.markdown("""
##### 2019, Cientista de Dados, HP Transportes, Goiânia, GO, (1 ano e 4 meses)

- Extrai dados para processos de inteligência competitiva com objetivo de otimizar estratégias de marketing de serviço de MAAS (Mobility As A Service).
- Realizei diversas modelagens de dados geográficos para soluções de mobilidade urbana com foco na resolução de problemas relacionados ao transporte compartilhado na região metropolitana.
- Desenvolvi estudos de conceitos de centralidades urbanas no âmbito do transporte público.
- Construí um produto de dados para acompanhar e recomendar preços de viagens de serviços de aplicativos de transporte em toda região metropolitana (Uber e 99).

**Habilidades**: Qlik Sense · Google Earth · QGis · Data Scrappig · Automação de Processos (RPA) · Python
""")
st.markdown("""
##### 2018, Analista de Dados, Grupo Jaime Câmera, Goiânia, GO, (1 ano e 4 meses)

- Desenvolvi relatórios de SEO para os produtos importantes da filial da TV Globo em Goiânia, como o site de notícias Jornal O Popular e o site de classificados Classi.
- Construí visualizações e monitorei indicadores-chave de desempenho relacionadas ao tráfego de audiência orgânico e pago dos sites do grupo
- Realizei extrações e modelagem de dados de audiência de TV fornecidos pelo IBOPE

**Habilidades**: SEO · Web Development · React · Java Script · Microsoft Azure · Kantar Media · Python
""")
st.markdown("""
##### 2015, Pesquisador, Jacobs School of Engineering, San Diego, CA, (3 meses)

- Ajudei a construir uma plataforma de coleta de imagens em tempo real usando o Microsoft Kinect com o objetivo de monitorar ambientes hospitalares.
- Realizei estudos para o processamento de imagens de profundida usadas em algoritmos de detecção de movimento e queda para alertas sobre o estado do paciente.

**Habilidades**:  C# · Microsoft Kinect SDK · Image Processing
""")

st.markdown('### Educação')
st.markdown(""" 
##### 2022, **Doutorado em Ciências da Computação,** Universidade Federal de Goiás, UFG, (**disciplinas concluídas**)
*SEO-RL: A Supervised Evolutionary Offline Reinforcement Learning Approach*

**Tópicos**: Aprendizado de Máquina, Aprendizado por Reforço, Redes Neurais e Computação Evolutiva
""")
st.markdown(""" 
##### 2020, **Mestrado em Ciências da Computação**, Universidade Federal de Goiás, UFG
*Evolutionary Approaches for Endmember Extraction in Hyperspectral Unmixing using Genetic Algorithms*

**Tópicos**: Processamento de Imagens, Computação Evolutiva, Aprendizado Supervisionado e Meta-heurísticas
""")
st.markdown(""" 
##### 2019, **Especialização em Desenvolvimento Web**, Universidade Federal de Goiás, UFG, (**disciplinas concluídas**)
*Aplicação Web e Mobile de serviço de sugestões de mobilidade direcionados as necessidades dos usuários focado em economia tempo e dinheiro*

**Tópicos**: Raspagem de Dados Web, Aplicação Web e Mobile, Visualização de Dados
""")
st.markdown(""" 
##### 2018, **Especialização em Business Intelligence**, Universidade Federal de Goiás, UFG
*Categorização Automática de Textos Não Supervisionada Aplicada a um Site de Notícias*

**Tópicos**: Categorização de Textos, Processamento de Linguagem Natural e Aprendizado Não Supervisionado
""")
st.markdown(""" 
##### 2016, **Bacharelado em Ciência da Computação,** Universidade Federal de Goiás, UFG
*Estudo e implementação do método de calibração de câmeras de Zhengyou Zhang*

**Tópicos**: Geometria Computacional, Calibração de Câmeras, Processamento de Imagens
""")
st.markdown(""" 
##### 2015, **Intercâmbio**, University of California San Diego, UCSD
*Hospital Patient Monitoring System*

**Tópicos**: Construção de Software, Processamento de Imagens
""")
st.markdown('### Trabalhos e Publicações')
st.markdown("""
- 2021, PulseRL: Enabling Offline Reinforcement Learning for Digital Marketing Systems via ConservativeQ-Learning
- 2020, A Systematic Mapping Study on Software Testing for Systems-of-Systems
- 2020, Selecting Important Features Interactions In A Click-Through-Rate Application Using Genetic Algorithms
- 2020, Adaptive Multilayer Perceptron
- 2019, A Multi-Objective Evolutionary Approach For Optimizing Pickup and Delivery Locations In A Demand Responsive Transport Service
- 2019, GAEEII: An Optimised Genetic Algorithm Endmember Extractor for Hyperspectral Unmixing
- 2018, Comparison of VCA and GAEE algorithms for Endmember Extraction
- 2018, TensorNet: Classificação de Protozoários
- 2013, Estudo de Ambiente Virtual para Simulação Multiagente de Usuários de Aplicativo Web
"""
)
