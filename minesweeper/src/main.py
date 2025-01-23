from src.services.file_service import write_file
from src.services.mine_sweeper_service import create_mine_fields


def main():
    fields = create_mine_fields('../public/mines.txt')
    output = ""
    for field in fields:
        output += field.__str__()
    write_file("../public/minesweeper_output.txt", output)

main()