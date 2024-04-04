from time import sleep
from rich import print
from rich.console import Console
from rich.__main__ import make_test_card


console = Console(record=True)

style = "bold yellow"

with console.status('Calculando...', spinner='dots10'):
    sleep(5)
    console.log('Calculo realizado!', style=style)

with console.status('Contabilizando...', spinner='bouncingBall'):
    sleep(8)
    console.log('Contabilização realizada!')

with console.status('Salvando...', spinner='point'):
    sleep(8)
    console.log('[green bold]Concluído')
