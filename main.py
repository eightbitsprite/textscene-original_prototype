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

# Truncated version of following regex:
#		(^@((?P<speaker>[\w]+) [\s]*
#		( \[(?P<emote>[\w]+) \]|)  
#			|!(?P<keyword>[\w]+)) [\s]* 
#		|[\s]*)
#		\b(?P<line>.[^#]+|) 
#		(\#(?P<time>([\d]+[\.]?|[\.])[\d]*)|) [.]*
regex = re.compile(r"""
	(
		^@(								#Specify speaker/emote OR keyword	
			(?P<speaker>[\w]+) [\s]*		#match specified 'speaker'
			(\[(?P<emote>[\w]+) \]|)			#if present, match 'emote'
				|							#OR
			!(?P<keyword>[\w]+)				#match specified 'keyword'
		) [\s]*
		| 								#Otherwise, ignore whitespace until...
	[\s]*)									
	(?P<line>.[^#]+						#matches the main 'line' group
		|
	)  					
	(\#
		(?P<time>([\d]+[\.]?|[\.])[\d]*)	#if present, match specified 'time'
		|
	) [.]*
	""", re.VERBOSE)

class scene:
	def __init__(self, sceneLines):
		self.lines = []
		for line in sceneLines:
			self.lines.append(vars(line).copy())

class sceneLine:
    def __init__(self, speaker, emote, line, keyword, time):
        self.speaker = "" if speaker is None else speaker
        self.emote = "" if emote is None else emote
        self.line = "" if line is None else line
        self.keyword = "" if keyword is None else keyword
        self.time = 1.0 if time is None else float(time)

    #def __repr__(self):

	def __str__(self):
		keyword = "" if self.keyword == "" else self.keyword + " "
		emote = "" if self.emote == "" else " (<i>" + self.emote + "</i>): "
		string = str(self.speaker) + emote + keyword + self.line
		return string

	def debugString(self):
		string =  "[SPEAKER: "+ str(self.speaker) + " (" + self.emote + ") "
		string += str(self.line) + " TIME:" + str(self.time) + " "
		string += "KEYWORD: " + str(self.keyword) + "]\n"
		return string



def read(infile):
	inputf = open(infile, "r")
	lines = [] 
	for line in inputf:
		if line[0] == "$":
			print "IGNORING: " + line
			continue
		pLine = line.rstrip()
		if (pLine):
			lines.append(pLine) 
	inputf.close()
	return lines

def process(lines):
	objects = []
	for line in lines:
		match_res = regex.match(line)
		if match_res:
			fields = match_res.groupdict()
			sLine = sceneLine(fields["speaker"],fields["emote"],
				fields["line"],fields["keyword"],fields["time"])
			objects.append(sLine)
	return objects

def write(scene, outfile, compact):
	outputf = open(outfile, "w") 
	lines = []
	for line in scene:
		lines.append(vars(line))
	fScene = {'lines':lines}
	if compact:
		json.dump(fScene, outputf)
	else:
		json.dump(fScene, outputf, indent=4, separators=(',', ': '))
	outputf.flush()
	outputf.close()
	return True

def processing(infile, outfile, compact):
	lines = read(infile)
	scene = process(lines)
	#for obj in objects:
		#print obj
		#print obj.debugString()
	result = write(scene, outfile, compact)
	return result

if __name__ == '__main__':
	if len(sys.argv) != 4:
		print "INPUT ERROR; try python main.py -[c(ompact)/p(retty)] [inputfile] [outputfile]"
	else:
		compact = True if sys.argv[1] == "-c" else False
		infile = sys.argv[2]
		outfile = sys.argv[3]
		result = processing(infile, outfile, compact)
		print "PROCESSING SUCCESSFUL" if result else "PROCESSING UNSUCCESSFUL"