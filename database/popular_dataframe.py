import pandas as pd
import numpy as np

columns = ['ID', 'Nome', 'Sobrenome', 'Classe',
           'Raça', 'Nível', 'Pontos de vida',
           'Pontos de mana', 'Força', 'Destreza', 'Constituição',
           'Inteligência', 'Sabedoria', 'Carisma']

df = pd.DataFrame(columns=columns)

nomes = [
    'Aaren', 'Arion', 'Auron', 'Bane', 'Beric', 'Bjorn', 'Caius', 'Connor', 'Darius',
    'Evander', 'Finnegan', 'Gabriel', 'Gideon', 'Grayson', 'Hagen', 'Hector', 'Henry', 'Ian',
    'Isaac', 'Jaxon', 'Kai', 'Kaleb', 'Kian', 'Liam', 'Lucas', 'Magnus', 'Milo',
    'Nathan', 'Oliver', 'Owen', 'Parker', 'Rowan', 'Sebastian', 'Silas', 'Tristan', 'Val',
    'Xavier', 'Zachary',
    'Anya', 'Azura', 'Briar', 'Cassandra', 'Celina', 'Cora', 'Delilah', 'Elora', 'Freya',
    'Gemma', 'Gwendolyn', 'Hazel', 'Imogen', 'Iris', 'Keira', 'Leila', 'Lyra', 'Maia',
    'Mia', 'Naomi', 'Nora', 'Olivia', 'Penelope', 'Raven', 'Selene', 'Sophia', 'Sylvia',
    'Talia', 'Tessa', 'Violet', 'Willow'
]
classes = [
    'Bardo', 'Guerreiro', 'Ladino', 'Mago',
    'Clérigo', 'Druida', 'Monge', 'Paladino',
    'Arqueiro', 'Cavaleiro', 'Caçador', 'Templário',
    'Assassino', 'Bárbaro', 'Dançarino da Lâmina', 'Ninja',
    'Bruxo', 'Feiticeiro', 'Inquisidor', 'Mestre das Trevas',
    'Alquimista', 'Arquiteto', 'Barqueiro', 'Campeão',
    'Cozinheiro', 'Diplomata', 'Estrategista', 'Fiel',
    'Físico', 'Guardião', 'Herdeiro', 'Imperador',
    'Inventor', 'Ladrão', 'Mercenário', 'Menestrel',
    'Mercador', 'Mestre de Armas', 'Mestre de Espionagem', 'Mestre de Magia',
    'Mestre de Música', 'Mestre de Oficio', 'Mestre de Profissão', 'Mestre de Teatro',
    'Nobre', 'Oficial', 'Palhaço', 'Pesquisador',
    'Poeta', 'Protetor', 'Pugilista', 'Religioso',
    'Sacerdote', 'Savant', 'Senhor da Guerra', 'Soldado',
    'Terapeuta', 'Troubadour', 'Vigilante',
]
racas = [
    'Humano', 'Anão', 'Elfo', 'Draconato',
    'Halfling', 'Half-elf', 'Half-orc', 'Gnome',
    'Gnome das profundezas', 'Gnome das colinas', 'Gnome das florestas',
    'Elfo da floresta', 'Elfo da noite', 'Elfo da luz',
    'Drow', 'Eladrin', 'Sylvan',
    'Anão da montanha', 'Anão da terra', 'Anão da floresta',
    'Half-elf do sol', 'Half-elf da lua',
    'Half-orc da cidade', 'Half-orc da selva',
    'Halfling das planícies', 'Halfling das montanhas', 'Halfling das florestas',
    'Halfling das sombras',
    'Tiefling',
]

def popular_dataframe(df):
    # Gerar IDs aleatórios
    df['ID'] = np.arange(1, 1501)

    # Gerar nomes aleatórios
    df['Nome'] = ['{0}'.format(nome)
                   for nome in np.random.choice(
                       nomes,
                       size=1500,
                       replace=True)]
    
    # Gerar sobrenome aleatórios
    df['Sobrenome'] = ['{0}'.format(nome)
                   for nome in np.random.choice(
                       nomes,
                       size=1500,
                       replace=True)]

    # Gerar classes aleatórias
    df['Classe'] = np.random.choice(
        classes,
        size=1500,
        replace=True)

    # Gerar raças aleatórias
    df['Raça'] = np.random.choice(
        racas,
        size=1500,
        replace=True)

    # Gerar níveis aleatórios
    df['Nível'] = np.random.choice(range(1, 20), size=1500)

    # Gerar pontos de vida aleatórios
    df['Pontos de vida'] = np.random.randint(1, 100, size=1500)

    # Gerar pontos de mana aleatórios
    df['Pontos de mana'] = np.random.randint(1, 50, size=1500)

    # Gerar estatísticas básicas aleatórias
    for stat in ['Força', 'Destreza', 'Constituição', 'Inteligência',
                 'Sabedoria', 'Carisma']:
        df[stat] = np.random.randint(1, 20, size=1500)

    return df


df = popular_dataframe(df.copy())

df.to_excel('dados_de_jogadores.xlsx', index=None)
