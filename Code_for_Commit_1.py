class Validator:
    def validate_and_convert(self, input_list):
        ints = []

        for item in input_list:
            if item.isdigit(): 
                ints.append(int(item)) 

        return ints
    
    