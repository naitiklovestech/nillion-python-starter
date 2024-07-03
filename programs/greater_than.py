from nada_dsl import *

def nada_main():
    # Define the parties involved in the computation
    party1 = Party(name="Party1")
    party2 = Party(name="Party2")
    
    # Define secret inputs from both parties
    A = SecretInteger(Input(name="A", party=party1))
    B = SecretInteger(Input(name="B", party=party2))
    C = SecretInteger(Input(name="C", party=party1))
    D = SecretInteger(Input(name="D", party=party2))
    
    # Perform the computation
    result = A * B + C > B * D
    
    # Output the result to a specified party
    return [Output(result, "my_output", party1)]

# Execute the NADA program
if __name__ == "__main__":
    result = nada_main()
    for output in result:
        print(output)
