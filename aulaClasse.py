class Aluno():
    def __init__(self, nome, idade, curso):
        self.nome =  nome
        self.idade = idade
        self.curso = curso
        self.ra = ""
       
    def apresentar(self):
        print(f"Olá, meu nome é {self.nome}, tenho {self.idade} anos e faço o curso de {self.curso}.")
        if(self.ra == ""):
            print("Esse aluno não tem RA.")
        else:
            print(f"O RA é: {self.ra}")


        nome = input('Qual seu nome?')
        idade = int(input('Qual sua idade?'))
        curso = input('Qual seu curso?')

        alun1 = Aluno(nome,idade,curso)
        alun1.apresentar()
        ra = input('Qual seu RA: ')
        alun1.ra = ra
        alun1.apresentar()
        print(f"O nome é: {alun1.nome}")
        
