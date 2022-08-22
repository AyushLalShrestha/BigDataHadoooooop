VIM cheat sheet: vim cheat-sheet
VIM most frequently used Commands:
:q  = quit vim
:q! = quit vim and ignore changes
:w = save document
:wq = save and quit
Shift + i = Jump to the beginning of the line in insert mode
Shift + a = Jump to the end of the line in insert mode
x = to delete the unwanted character
u = to undo the last the command and U to undo the whole line
CTRL-R = to redo
v = starts visual mode for selecting the lines and you can perform operation on that like d delete
v then $ = select and delete to theend of the line
$ = to go to the end of the line
0 = to move to the start of the line
/<pattern> = search <pattern> then press ‘ESC’ and press ‘n’ to find next match
% = find a matching ),], or }
dw = move the cursor to the beginning of the word to delete that word
2w = to move the cursor two words forward.
3e = to move the cursor to the end of the third word forward.
d<x>w = deletes x words eg. d2w
dd = to delete the line and 2dd to delete to line .number can be changed for deleting the number of consecutive words
The format for a change command is: operator [number] motion
-operator - is what to do, such as d for delete
- [number] - is an optional count to repeat the motion
- motion - moves over the text to operate on, such as w (word),
$ (to the end of line), etc.
p - puts or paste 
r - to replace the letter e.g press re to replace the letter with e
ce - to change until the end of a word (place the cursor on the u in lubw it will delete ubw )
ce - deletes the word and places you in Insert mode
G - to move you to the bottom of the file.
gg - to move you to the start of the file.
Type the number of the line you were on and then G


:s/old/new/g to substitute 'new' for 'old' where g is globally
/ backward search n to find the next occurrence and N to search in opposite direction
? forward search
:! to run the shell commands like :!dir, :!ls
:w - TEST (where TEST is the filename you chose.) . Save the file


:r - Filename will insert the content into the current file
R - to replace more than one character
y - operator to copy text using v visual mode and p to paste it
yw - (copy)yanks one word
o - opens a line below the cursor and start Insert mode.
O - opens a line above the cursor.
a - inserts text after the cursor.
A - inserts text after the end of the line.
e - command moves to the end of a word.
y - operator yanks (copies) text, p puts (pastes) it.
R - enters Replace mode until <ESC> is pressed.
ctrl-w to jump from one window to another



