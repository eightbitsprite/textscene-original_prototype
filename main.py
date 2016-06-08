import json
import sys
import re

"""
This program is designed to turn a formatted text file into an array of sceneLine objects, 
which is then output into a json file for use in Javascript.

Formatted text syntax is as follows:
"@" indicates the beginning of a line. 
	- An alphanumeric word can be appended to the '@' to indicate the 'speaker', 
	if one exists. If a speaker does not exist, italics will be applied to the line.
		If so desired, an 'emote' can be added with " [<emote>]". This is 
		only possible if a speaker has been specified.
	- Alternatively, a keyword can be added in the format of "!<keyword>" to indicate 
	special behavior.

Any text after the '@' and its optional modifiers will be classified as a 'line'.

"#" is an optional character used to indicate a specific 'time' (in seconds) 
	that will elapse before the line will be displayed. Float numbers are allowed. 
	If a time is not specified, the sceneLine object will default to "1"
"""

class sceneLine:
    def __init__(self, line, speaker=None, emote=None, time=1.0):
        self.speaker = speaker
        self.emote = emote
        self.line = line
        self.time = time

    def __str__():
    	string =  "[SPEAKER: "+ str(self.speaker) + " (" + self.emote + ") "
    	string += str(self.line) + " TIME:" + str(self.time) + "\n"
    	return string


def read(infile):
	input = open(infile, "r")
	lines = [] 
	for line in input:
		pLine = line.rstrip()
		if (pLine):
			lines.append(pLine) 
	return lines

def process(lines):
	objects = []
	# Truncated version of following regex:
	#		^@((?P<speaker>[\w]+) [\s]*
	#		( \[(?P<emote>[\w]+) \]|)  
 	#			|!(?P<keyword>[\w]+) ) [\s]* 
	#		\b(?P<line>[^#]+|) 
	#		(\#(?P<time>[\d]+[\.]?[\d]*)|) [\s]*
	regex = re.compile(r"""
		^@
		(	
			(?P<speaker>[\w]+) [\s]*		#if speaker is specified, matches that
			(\[(?P<emote>[\w]+) \]|)		#then if emote is specified, matches that
				|!(?P<keyword>[\w]+)
		) [\s]*
		(?P<line>[^#]+)  						#matches the main 'line' group
		(\#(?P<time>[\d]+[\.]?[\d]*)|) [\s]*	#if time is specified, matches that
		""", re.VERBOSE)
	#for line in lines:


def processing(infile, outfile):
	lines = read(infile)
	print lines
	objects = process(lines)
	return False

if __name__ == '__main__':
	if len(sys.argv) != 3:
		print "INPUT ERROR; try python main.py [inputfile] [outputfile]"
	else:
		infile = sys.argv[1]
		outfile = sys.argv[2]
		result = processing(infile, outfile)
		print "PROCESSING SUCCESSFUL" if result else "PROCESSING UNSUCCESSFUL"