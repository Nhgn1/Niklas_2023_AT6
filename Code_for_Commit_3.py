class DataValidator:
    def validate_and_convert(self, input_list):
        # Initialize the list for valid integers
        valid_integers = []

        for item in input_list:
            if item.isdigit():  # Check if the string is a positive integer
                valid_integers.append(int(item))  # Convert to integer and add to list

        return valid_integers
    
    
