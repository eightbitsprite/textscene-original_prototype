# textscene-original_prototype
prototype 'compiler' and interpreter for autonomous fiction markup language

This project takes significant inspiration from inkle studio's 'ink' text engine, and is similarly meant to turn formatted prose into something that can be easily manipulated by external programs. In contrast to ink, this program is designed around stageplay scripts; individual lines of dialogue are assigned a 'speaker' and an 'emotion' for that line. The pacing of each line can be indicated by a numeric value after the '#' symbol, and keywords which indicate a special action to be performed by the external program are denoted by '!' (keywords have not been implemented yet).

Included is a basic compiler that transforms a formatted file into a compiled JSON file, a sample input and output file, and a web page that will play a basic 'textscene' based off of the compiled test output.
