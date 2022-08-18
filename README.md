# Sculpy
Turn Notes (probably Markdown) into OmniFocus items

## Reasoning
I take a lot of notes throughout the day and at the end of the day I like to chop up my notes into next steps. This mainly means creating stuff for me to follow up on in my OmniFocus.

I was tinkering with the OmniFocus Application URL with @alexstockwell and figured I would apply a little bit of rigor to my notes and have something automatically create me items at the end of the day.

OmniFocus has an API, but it is in JavaScript and at this moment I can't really figure out how to use it.

## Requirements
- Desktop installation of OmniFocus 3
- Python 3.7 (or newer 🤷, this uses dataclasses)

## Installation
Right now just clone this down and run it. 

## Defaul Emoji/Project pairing
❓ Question Project

🤔 Think About Project

📖 Book Project

## Usage
`sculpy [-h] [--config CONFIG] file`

## Planned Features
Custom prefix/Emoji mapping config.

