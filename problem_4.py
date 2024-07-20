def get_list_of_squares_of_even_numbers(numbers):
   
    squares_of_even_numbers = [x ** 2 for x in numbers if x % 2 == 0]
    return squares_of_even_numbers

def slice_sublist_from_list(numbers, start_index, end_index):
    
    return numbers[start_index:end_index]

def main():

    numbers = list(map(int, input("Enter the list of integers: ").strip('[]').split(',')))
    
    
    squares_of_even_numbers = get_list_of_squares_of_even_numbers(numbers)
    print(f"List of squares of even numbers: {squares_of_even_numbers}")

    
    start_index = int(input("Enter start index: "))
    end_index = int(input("Enter end index: "))

    
    sliced_sublist = slice_sublist_from_list(numbers, start_index, end_index)
    print(f"sublist: {sliced_sublist}")

if __name__ == "__main__":
    main()
