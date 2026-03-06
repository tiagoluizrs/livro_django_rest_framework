# Importa o sinal para que ele seja registrado quando o pacote for carregado
from productManager.signals.EntryOutputSignal import create_history_entry_output
from productManager.signals.StockSignal import broadcast_stock_update
from productManager.signals.ClientSignal import notificar_novo_cliente
