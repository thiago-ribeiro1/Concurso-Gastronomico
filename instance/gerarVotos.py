import sqlite3
import random
from faker import Faker

# Caminho para o arquivo do banco de dados SQLite
db_path = 'E:/ATVD/ConcursoGastronomico/Concurso-Gastronomico/instance/database.db'  # Ajuste conforme necessário

# Conectar ao banco de dados SQLite
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Inicializar Faker para gerar nomes e números de telefone aleatórios
faker = Faker()

# Número de votos a gerar
num_votes = 100

# Lista predefinida de restaurantes
restaurants = ['bdc', 'seuManoel', 'pastelDaLiberdade', 'picanha200', 'saporeDItalia', 'dominos']

# Comentário a ser usado para todos os votos
comment = 'Random comment for testing purposes.'

# Gerar votos aleatórios
votes = []
for _ in range(num_votes):
    codAvaliacao = random.randint(100000, 999999)
    nome = faker.name()
    cpf = faker.random_number(digits=11, fix_len=True)
    telefone = faker.phone_number()
    atendimento_input = random.randint(1, 5)
    qualidade_input = random.randint(1, 5)
    apresentacao_input = random.randint(1, 5)
    restaurante = random.choice(restaurants)
    
    vote = (None, codAvaliacao, nome, cpf, telefone, comment, atendimento_input, qualidade_input, apresentacao_input, restaurante)
    votes.append(vote)

# Comando SQL para inserir votos na tabela 'voto'
insert_vote_sql = """
INSERT INTO voto (idNfe, codAvaliacao, nome, cpf, telefone, comentario, atendimento_input, qualidade_input, apresentacao_input, restaurante) 
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
"""

# Inserir votos no banco de dados
cursor.executemany(insert_vote_sql, votes)
conn.commit()

# Verificar se os votos foram inseridos
cursor.execute("SELECT COUNT(*) FROM voto;")
vote_count = cursor.fetchone()[0]

# Fechar a conexão com o banco de dados
conn.close()

print(f'Total de votos na tabela: {vote_count}')
