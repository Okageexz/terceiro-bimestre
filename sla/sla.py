class Perfil():
    def _init_(self, id, nome, nome_da_conta, email, senha):
        self._id = id
        self._nome = nome
        self._nome_da_conta = nome_da_conta
        self._email = email
        self._senha = senha
        self._curtidas = 0

    def get_nome_da_conta(self):
        return self._nome_da_conta
    
    def get_curtidas(self):
        return self._curtidas
    
    def set_curtidas(self):
        self._curtidas += 1

perfil_douglas = Perfil(1, "Douglas Silva", "@douglinha", "douglas@exemplo.com", "douglas@12")

for i in range(1, 11):
    perfil_douglas.set_curtidas()

print(f"\nO Perfil {perfil_douglas.get_nome_da_conta()} tem um numero de curtidas igual a {perfil_douglas.get_curtidas()}")