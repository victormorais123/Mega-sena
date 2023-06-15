import random
from twilio.rest import Client

# Configurações da conta Twilio
account_sid = "ACe574d4470e2f2639b84e7349ccc20231"
auth_token = "472e06106703491e13edb0e0fcb6953b"
twilio_number = "14302345330"

# Função para enviar SMS
def enviar_sms(destinatario, mensagem):
    client = Client(account_sid, auth_token)
    try:
        message = client.messages.create(
            body=mensagem,
            from_=twilio_number,
            to=destinatario
        )
        print("SMS enviado com sucesso!")
        print("SID da mensagem:", message.sid)
    except Exception as e:
        print("Erro ao enviar SMS:", str(e))

# Exemplo de uso
numero_destinatario = "+5554999837827"
texto_mensagem = "Acertei  numeros"

enviar_sms(numero_destinatario, texto_mensagem)


def gerarRandomNumeros():
    numeros = random.sample(range(1,61), 6)
    return numeros
