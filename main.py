import json
import sys
import re

"""
This program is designed to turn a formatted text file into an array of sceneLine objects, 
which is then output into a json file for use in Javascript.

Formatted text syntax is as follows:
"@" indicates the beginning of a line of dialogue.
	- An alphanumeric word should be appended to the '@' to indicate the 'speaker'.
		If so desired, an 'emote' can be added with " [<emote>]". This is 
		only possible if a speaker has been specified.
	- Alternatively, a keyword can be added in the format of "!<keyword>" to indicate 
	special behavior.

Any text after the '@' and its optional modifiers will be classified as a 'line'.

If the current line is not a line of dialogue, this line is assumed to be a scene or 
action description and italics will be applied.

"#" is an optional character used to indicate a specific 'time' (in seconds) 
	that will elapse before the line will be displayed. Float numbers are allowed. 
	If a time is not specified, the sceneLine object will default to "1"

"$" is a comment character. Any line beginning with "$" will be absent from the final output.
"""

class sceneLine:
    def __init__(self, line, speaker=None, emote=None, time=1.0, keyword=None):
        self.speaker = speaker
        self.emote = emote
        self.line = line
        self.time = time
        self.keyword = keyword

    def __str__():
    	string =  "[SPEAKER: "+ str(self.speaker) + " (" + self.emote + ") "
    	string += str(self.line) + " TIME:" + str(self.time) + "\n"
    	return string


def read(infile):
	input = open(infile, "r")
	lines = [] 
	for line in input:
		if line[0] == "$":
			print "IGNORING: " + line
			continue
		pLine = line.rstrip()
		if (pLine):
			lines.append(pLine) 
	return lines

def process(lines):
	objects = []
	# Truncated version of following regex:
	#		(^@((?P<speaker>[\w]+) [\s]*
	#		( \[(?P<emote>[\w]+) \]|)  
 	#			|!(?P<keyword>[\w]+)) [\s]* 
	#		|[\s]*)
	#		\b(?P<line>.[^#]+|) 
	#		(\#(?P<time>[\d]+[\.]?[\d]*)|) [.]*
	regex = re.compile(r"""
		(
			^@(									
				(?P<speaker>[\w]+) [\s]*		#if speaker is specified, matches that
				(\[(?P<emote>[\w]+) \]|)		#then if emote is specified, matches that
					|
				!(?P<keyword>[\w]+)				#if keyword is specified, matches that
			) [\s]*
			| 
		[\s]*)
		(?P<line>.[^#]+|)  						#matches the main 'line' group
		(\#(?P<time>[\d]+[\.]?[\d]*)|) [.]*		#if time is specified, matches that
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