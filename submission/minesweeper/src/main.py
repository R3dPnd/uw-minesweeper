from src.services.file_service import write_file
from src.services.mine_sweeper_service import create_mine_fields
from src.services.minefield_generation import generate_test_file

'''
    Description: Main function.
'''
def main():
    # Generate test file
    ai_fields = generate_test_file(10)
    
    # Create mine field input
    input_file_path = "../public/minesweeper_input.txt"
    write_file(input_file_path, ai_fields)
    
    # Create mine field output
    fields = create_mine_fields(input_file_path)
    output = ""
    for field in fields:
        output += field.__str__()
    write_file("../public/minesweeper_output.txt", output)

main()