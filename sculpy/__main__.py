import argparse
import webbrowser

from dataclasses import dataclass

@dataclass
class Line:
    raw_line: str
    
    def __post_init__(self) -> None:
        self.line_type = self.raw_line[0]
        self.line_text = self.raw_line[1:]

    def create_omnifocus_item(self) -> None:
        webbrowser.open(f"omnifocus:///add?name={self.line_text}")

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("file", type=str, help="The file you want to parse items from")
    parser.add_argument("--config", type=str, help="Pass in a custom configuration")
    args = parser.parse_args()
    with open(args.file, 'r', encoding="utf-8") as input_file:
        for line in input_file:
            l = Line(line.strip())
            l.create_omnifocus_item()

if __name__ == '__main__':
    main()

