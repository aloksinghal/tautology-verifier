from statement_solver import check_tautology


def main():
    input_string = raw_input("Enter logical statement: ")
    is_tautology = check_tautology(input_string)
    print is_tautology

if __name__ == "__main__":
    main()
