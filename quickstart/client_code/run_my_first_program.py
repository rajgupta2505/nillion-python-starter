from nada_dsl import *

def nada_main():

    party1 = Party(name="Party1")

    my_int1 = SecretInteger(Input(name="my_int1", party=party1))
    my_int2 = SecretInteger(Input(name="my_int2", party=party1))
    my_int3 = SecretInteger(Input(name="my_int3", party=party1))

    # Perform a different operation, such as multiplication and addition
    product = my_int1 * my_int2
    new_int = product + my_int3

    return [Output(new_int, "my_output", party1)]
