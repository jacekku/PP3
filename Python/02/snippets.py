def safe_input(prompt_string="",except_string="Please enter a number",convert_to_int=False):
    """Prompt the user to input a number, don't stop until a valid number is provided"""
    output=""
    while(type(output) is not float):
        try:
            output=float(input(prompt_string))
        except ValueError:
            print(except_string)
    return int(output) if convert_to_int else output


def input_of_length(length=255,prompt="",exact_length=False,wrong_length_string="Wrong length"):
    """
    Prompt the user to input a string of certain length

    length -- upper length limit

    prompt -- what to ask user in the input prompt
    
    exact_length -- does the returned string have to be exactl length?

    wrong_length_string -- what to print when user typed in string of wrong length 

    """


    output=""
    while(not output or len(output)>length or (exact_length and len(output)<length)):
        output=input(prompt)
    return output




def get_unique_value(tab,function,*args):
    """
    This function takes an iterable and tries to return a value that is not in the iterable.
    Useful for non repeating chains of random numbers

    tab = iterable to check against eg.:[1,2,3,4]

    function = function to call and check the return value with tab eg.: randint

    *args = arguments to pass to function eg.: [1,49] >> randint(1,49)
    """
    n=function(*args)
    while(n in tab):
        n=function(*args)
    return n