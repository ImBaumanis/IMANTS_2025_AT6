class UserInputValidator:
    def validate_positive_integers(list):
        final_list = []
        for string in list:
            if string.isdigit():
                final_list.append(string)

        return print(f"The list contains {len(final_list)} integer(s) ")