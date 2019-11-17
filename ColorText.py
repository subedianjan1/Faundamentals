import sys

#try:
color = sys.stdout.shell
#except AttributeError: raise RuntimeError("Use IDLE")

#And then use color.write(YourText,Color) for "printing":

color.write("Hello(Orange)\n","KEYWORD")
color.write("Hello(Green)\n","STRING")
color.write("Hello(Red)\n","COMMENT")
color.write("Hello(Purple)\n","BUILTIN")

'''
The "Colors" you can put are: SYNC, stdin, BUILTIN, STRING,
console, COMMENT, stdout, TODO, stderr, hit, DEFINITION, KEYWORD, ERROR, and sel.
'''
