# -*- coding: utf-8 -*-
"""Jogo do Nim.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/172DYDmLagXJYRBgAx-xppcWzu0DVWIZV
"""

def  computador_escolhe_jogada ( n , m ):
    computadorRemover  =  1

    while  computadorRemover  !=  m :

        if ( n  -  computadorRemover ) % ( m  + 1 ) ==  0 :
            return  computadorRemover
        else:
            computadorRemover  =  computadorRemover  +  1

    return  computadorRemover
        
def  usuario_escolhe_jogada ( n , m ):
    jogadaValida  =  False
    while not jogadaValida:
        jogadorRemover  =  int ( input ( 'Quantas peças você vai tirar? ' ))
        if  jogadorRemover  >  m  or  jogadorRemover  <  1 :
            print ()
            print ( 'Opa! Jogada inválida! Tente de novo.' )
            print ()

        else:
            jogadaValida  =  True
    return jogadorRemover  
def  campeonato ():
    numeroRodada  =  1
    while  numeroRodada  <=  3 :
        print ()
        print ( '**** Rodada' , numeroRodada , '****' )
        print ()
        partida ()
        numeroRodada  +=  1
    print ()
    print ( 'Placar: Você 0 X 3 Computador' )


def  partida ():
    n  =  int ( input ( 'Quantas peças? ' ))

    m  =  int ( input ( 'Limite de peças por jogada? ' ))

    vezDoPC  =  False

    if  n  % ( m + 1 ) ==  0 :
        print ()
        print ( 'Voce começa!' )

    else:
        print ()
        print ( 'Computador começa!' )
        vezDoPC  =  True

    while  n  >  0 :
        if  vezDoPC :
            computadorRemover  =  computador_escolhe_jogada ( n , m )
            n  =  n  -  computadorRemover
            if  computadorRemover  ==  1 :
                print ()
                print ( 'O computador tirou uma peça' )
            else:
                print ()
                print ( 'O computador tirou' , computadorRemover , 'peças' )

            vezDoPC  =  False
        else:
            jogadorRemover  =  usuario_escolhe_jogada ( n , m )
            n  =  n  -  jogadorRemover
            if  jogadorRemover  ==  1 :
                print ()
                print ( 'Você tirou uma peça' )
            else:
                print ()
                print ( 'Você tirou' , jogadorRemover , 'peças' )
            vezDoPC  =  True
        if n  ==  1 :
            print ( 'Agora resta apenas uma peça no tabuleiro.' )
            print ()
        else:
            if  n  !=  0 :
                print ( 'Agora restam,' , n , 'peças no tabuleiro.' )
                print ()

    print ( 'Fim do jogo! O computador ganhou!' )

print ( 'Bem-vindo ao jogo do NIM! Escolha:' )
print ()

print ( '1 - para jogar uma partida isolada' )

tipoDePartida  =  int ( input ( 'Digite 1 para inciar' ))
tipoDePartida  ==  1 
print ()
