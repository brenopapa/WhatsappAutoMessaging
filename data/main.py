import lib
#lib functions:
#   - get_forecast_info()
#   - get_todays_emmissary()
#   - send_message(message_target, message)

print("##################################################")
print("#                Enviar mensagem ?               #")
print("##################################################")
option = input(" Responda S ou N: ")

if(option.upper() == "S"):
	message_target = "Família Papa"
	message = "Bom dia familia"

	lib.send_message(message_target, message)
else:
	print("Rotina Cancelada!")
