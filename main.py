import curses
from curses import wrapper
import time 
import random

def start_screen(stdscr):
    stdscr.clear()   
    stdscr.addstr("Wpm test")
    stdscr.addstr("\n Press a key to continue") 
    stdscr.refresh()
    stdscr.getkey()

def load_file():
    with open("text.txt", "r") as file:
        text = file.readlines()
    return random.choice(text).strip()

def wpm_test(stdscr,wpm=0):
    target_text = load_file()
    current_text = []

    stdscr.clear()   
    stdscr.addstr(target_text)
    stdscr.addstr(3,0,f"WPM:{wpm}")
    stdscr.refresh()
    start_time = time.time()
    stdscr.nodelay(True)
    i = 0


    while True:
        time_elapsed = max(time.time() - start_time,1) 
        wpm = round(len(current_text) / (time_elapsed / 60) / 5)
        stdscr.addstr(3,0,f"WPM:{wpm}")
    
        if i == len(target_text):
            stdscr.nodelay(False)
            break

        try:
            key = stdscr.getkey()
        except:
            continue
        
        current_text.append(key)

        if key in ("KEY_BACKSPACE",'\b',"\x7f"):
            i -= 1
        elif ord(key) == 27:
            break
        elif key == target_text[i]:
            stdscr.addstr(0,i,key,curses.color_pair(2))
            i += 1 
        else:
            stdscr.addstr(0,i,key,curses.color_pair(1))
            i += 1 

  

def main(stdscr):
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)

    start_screen(stdscr)

    while True:
        wpm_test(stdscr)
        stdscr.addstr(2,0,"Congrats The test is completed")
        key = stdscr.getkey()
        if ord(key) == 27:
            break


wrapper(main)
