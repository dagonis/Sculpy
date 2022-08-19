import argparse
import webbrowser
import yaml

from dataclasses import dataclass
from datetime import datetime

today = datetime.today()

@dataclass
class Line:
    raw_line: str
    
    def __post_init__(self) -> None:
        self.line_type = self.raw_line[0]
        self.line_text = self.raw_line[1:]

    def create_omnifocus_item(self, configuration: dict, default_note: bool) -> bool:
        project = configuration[self.line_type]['project']
        note = f"Added by Sculpy on {today}" if default_note else ""
        webbrowser.open(f"omnifocus:///add?name={self.line_text}&note={note}&project={project}&context=Sculpy,Blah")
        return True    

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("file", type=str, help="The file you want to parse items from")
    parser.add_argument("--config", type=str, default="config.yaml", help="Pass in a custom configuration")
    parser.add_argument("--remove_processed_lines", "-r", action="store_true", help="Remove the lines that were processes from the notes file.")
    parser.add_argument("--default_note", action='store_true', help="Apply a default note to each new item.")
    args = parser.parse_args()
    config = yaml.safe_load(open(args.config).read())
    with open(args.file, 'r', encoding="utf-8") as input_file:
        for line in input_file:
            l = Line(line.strip())
            l.create_omnifocus_item(config, args.default_note)

if __name__ == '__main__':
    main()

