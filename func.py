import random
from twilio.rest import Client

# Configurações da conta Twilio
account_sid = "SEU_ACCOUNT_SID"
auth_token = "SEU_AUTH_TOKEN"
twilio_number = "SEU_NUMERO_TWILIO"

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
numero_destinatario = ""
texto_mensagem = ""

enviar_sms(numero_destinatario, texto_mensagem)


def gerarRandomNumeros():
    numeros = random.randrange(1,60)
    return numeros
