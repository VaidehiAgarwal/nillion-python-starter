from nada_dsl import *

def nada_main():
    party1 = Party(name="Party1")
    my_int1 = SecretInteger(Input(name="my_int1", party=party1))
    my_int2 = SecretInteger(Input(name="my_int2", party=party1))

    # write the computation for your program here - use my_int1 and my_int2 as inputs
    # Example computation: adding my_int1 and my_int2
    result = my_int1 + my_int2

    # return the result of the computation as output
    return [Output(result, "my_output", party=party1)]
