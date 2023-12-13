class DataValidator:
    def validate_and_convert(self, input_list):
        valid_integers = []

        for item in input_list:
            if item.isdigit():  
                valid_integers.append(int(item)) 

        return valid_integers
    
    