# -*- coding: utf-8 -*-

import telepot

from carona import *

class Bot(telepot.Bot):
    
    def __init__(self, token):
        super(Bot, self).__init__(token)
        self.caronas = []
        
        self.msgErro = "Não entendi"
        self.regras = """
	***************Preencha o Formulário abaixo********
	Formulário: http://goo.gl/forms/OsTKcSLW2O
	Este documento descreve como o grupo costuma funcionar para não ficar muito bagunçado. São conselhos baseados no bom senso e experiência adquirida.
	-Nome e foto: libere a exibição do nome e foto no Telegram. Isso oferece mais segurança para os motoristas. Caso não exiba, existe grande chance de você ser removido por engano considerado inativo. 
	-Horários: Ao oferecer carona para ir ao fundão, diga o horário que você pretende chegar no fundão. Ao oferecer carona para voltar ao Méier, diga o horário que você pretende sair do fundão. 
	-Carona para o dia seguinte: espere um horário que não atrapalhe quem está  pedindo carona para voltar da faculdade. Sugestão: ofereça após as 19h
	-Valor: Não é pagamento, ninguém é obrigado a pagar como também ninguém é obrigado a dar carona. É uma ajuda de custos. O valor que a maioria doa é 3,50. Alguns 4, outros 3. Sugiro o valor de 3,50 por passageiro, independente se for 1 ou 5 no carro, pra não gerar concorrência desnecessária. 
	-Não seja ganancioso, seu carro não é táxi. 
	-Não seja mesquinho, você está indo para a  faculdade no conforto e rapidez, colabore com o motorista. 
	-Ao oferecer ou pedir carona, utilize o verbo 'ir' se o sentido for meier-> Fundão e o verbo 'voltar' se o sentido for fundao-> Méier.
	-Participe ativamente do grupo: seja ativo e pegue ou ofereça caronas constantemente, caso contrário você estará tirando a vaga de alguém que pode precisar mais que você. 
	-Se for removido: não fique chateado. Se foi algum equívoco, fale com algum admin e te colocam de volta."
	"""

    def handle(self, msg):
        content_type, chat_type, chat_id = telepot.glance2(msg)
        
        if content_type != 'text':
            self.sender.sendMessage(self.msgErro)
            return

        text = msg['text'].strip().lower()
        command = text.split(' ')[0]

        if command == '/regras':
            self.sendMessage(chat_id, self.regras)

        elif command == '/ida':
            try:
                _, pessoa, horario = text.split(' ')
            except ValueError:
                self.sendMessage(chat_id, self.msgErro + " Formato: /ida <nome> <horario>")

            carona = Carona(pessoa, horario)
            self.caronas.append(carona)
            self.sendMessage(chat_id, 'Nova carona ' + str(carona))

        elif command == '/lista':
            if len(self.caronas) == 0:
                resp = "Não ha caronas"
            
            else:
                resp = ""
                for carona in self.caronas:
                    resp += str(carona) + "\n"

            self.sendMessage(chat_id, resp)
        
        else:
            self.sendMessage(chat_id, self.msgErro)





