class UserInputValidator:
    def validate_positive_integers(list):
        final_list = []
        for string in list:
            if string.isdigit():
                final_list.append(string)

        return print(f"The list contains {len(final_list)} integer(s) ")

c1 = UserInputValidator
c2 = UserInputValidator

list_of_strings = ["sun", "1973", "-3", "weather", "3.14", "24", "200"]
c1.validate_positive_integers(list_of_strings)
c2.validate_positive_integers(list_of_strings)