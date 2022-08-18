import argparse
import webbrowser
import yaml

from dataclasses import dataclass
from datetime import datetime
from typing import TypeVar

today = datetime.today()
line = TypeVar('Line')

@dataclass
class Line:
    raw_line: str
    
    def __post_init__(self) -> None:
        self.line_type = self.raw_line[0]
        self.line_text = self.raw_line[1:]

    def create_omnifocus_item(self) -> None:
        project = config[self.line_type].project

def create_omnifocus_item(line: line, configuration: dict) -> bool:
    project = configuration[line.line_type]['project']
    webbrowser.open(f"omnifocus:///add?name={line.line_text}&note=Added by Sculpy on {today}&project={project}&context=Sculpy,Blah")
    return True    

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("file", type=str, help="The file you want to parse items from")
    parser.add_argument("--config", type=str, default="config.yaml", help="Pass in a custom configuration")
    args = parser.parse_args()
    config = yaml.safe_load(open(args.config).read())
    with open(args.file, 'r', encoding="utf-8") as input_file:
        for _line in input_file:
            l = Line(_line.strip())
            print(l.__dict__)
            create_omnifocus_item(l, config)

if __name__ == '__main__':
    main()

