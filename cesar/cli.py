from inspect import ArgSpec
from unittest import result
from cesar import encripta, decripta
from argparse import ArgumentParser

parser = ArgumentParser(description="Cifra de Cesar")
parser.add_argument('frase', help='pharse to be encrypted/decrypted', type=str)
parser.add_argument('-n', help='Rotation value', default=13, type=int, required=False)
parser.add_argument('-d', help='Decrypte', required=False, action='store_true')

def cli():
    args = parser.parse_args()
    if args.d:
        result = decripta(args.frase, args.n)
    else:
        result = encripta(args.frase, args.n)

    print(f'Entrada: {args.frase}')
    print(f'Saida: {result}')

cli()

#stoped at 52' 34''