def calcular_checksum(mensagem):
    checksum = 0
    for char in mensagem:
        checksum += ord(char)
    return checksum

def verificar_checksum(mensagem,checksum):
    checksum_calculado = calcular_checksum(mensagem)
    return checksum_calculado == checksum

mensagem = input("digite a mensagem para ser enviada:")
checksum_enviado = calcular_checksum(mensagem)
print(f"Checksum enviado: {checksum_enviado}")