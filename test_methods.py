import methods
 
def test_area():
    # given a width of 2 and a height of 5
    width = 2
    height = 5

    # when we calculate the area
    output = methods.area_of_rectangle(width, height)

    # then the area should be 10
    assert output == 10
 
def test_perimeter():
    # given a width of 2 and a height of 5
    width = 2
    height = 5

    # when we calculate the perimeter
    output = methods.perimeter_of_rectangle(width, height)
    
    # then the perimeter should be 14
    assert output == 14

def teste_soma():
    # dado os numeros 2 e 4
    num1 = 2
    num2 = 4

    # quando calculamos a soma
    output = methods.soma(num1, num2)

    # o resultado deve ser 6
    assert output == 6

def teste_subtracao():
    # dado os numeros 40 e 25
    num1 = 40
    num2 = 25
    
    # quando calculamos a subtracao
    output = methods.subtracao(num1, num2)

    # o resultado deve ser 15
    assert output == 15

def teste_multiplicacao():
    # dado os numeros 5 e 9
    num1 = 5
    num2 = 9

    # quando calculamos a subtracao
    output = methods.multiplicacao(num1, num2)

    # o resultado deve sert 45
    assert output == 45

def teste_divisao():
    # dado os numeros 40 e 4
    num1 = 40
    num2 = 4

    # quando calculamos a divisao
    output = methods.divisao(num1, num2)

    # o resultado deve ser 10
    assert output == 10