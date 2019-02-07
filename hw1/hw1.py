#!/usr/bin/python3
#
# Author: Zach McKee
# Course: CPSC 326, Spring 2019
# Assignment: 1
# Description:
#   Basic program that takes a file of "commands" of the form:
#     left n;
#     right n;
#     up n;
#     down n;
#   where n is an integer, and computes the resulting Euclidean
#   distance.
#----------------------------------------------------------------------

import sys
import math


class DistanceCalculator(object):
    """Computes the Euclidean distance from a file of basic moves"""

    def __init__(self, input_stream):
        self.input_stream = input_stream
        self.x = 0
        self.y = 0
        self.__parse()          

        
    def __peek(self):
        """Returns next character keeping it in the stream"""
        pos = self.input_stream.tell()
        symbol = self.input_stream.read(1)
        self.input_stream.seek(pos)
        return symbol

    
    def __read(self, n):
        """Reads n characters from the stream"""
        return self.input_stream.read(n)

    
    def __parse_space(self):
        """Reads sequence of whitespace characters"""
        while self.__peek().isspace():
            self.__read(1)

            
    def __parse_command(self):
        """Reads and returns a sequence of non whitespace characters"""
        command = ''
        while not self.__peek().isspace():
            command += self.__read(1)
        return command

    
    def __parse_num(self):
        """Reads an integer string from the stream"""
        num = ''
        # TODO: read the int string into the num variable
        #Keep adding digits to num as long as digits are seen
        while self.__peek().isdigit() or self.__peek() == '-' :
            num += self.__read(1)
        try:
            return int(num)
        except Exception:
            raise Exception("invalid number '%s'" % num)

    
    def __parse(self):
        """Reads commands from input stream, updating x and y coordinates"""
        # TODO: implement this method using __parse_space(),
        # __parse_command(), __parse_num(), __read(), and __peek()
        while self.__peek() != '':  #Keep parsing until peek returns '' (EOF)
            self.__parse_space()    #Parse spaces before a command
            command = self.__parse_command()
            if not self.__valid_command(command):
                sys.exit('Invalid command detected "%s"' % command)
            self.__parse_space()        #Parse the space between the number
            amount = self.__parse_num() #and the command
            if command == 'up':
                self.y += amount
            elif command == 'down':
                self.y -= amount
            elif command == 'right':
                self.x += amount
            elif command == 'left':
                self.x -= amount
            
            self.__parse_space()
            #Removes semicolon if one is present
            #Else exits the program
            if self.__peek() == ';':
                self.__read(1)
            else:
                sys.exit('Missing semicolon after command "%s %s"' % (command, str(amount)))
            self.__parse_space()    #Parse spaces after a command

    def __valid_command(self, command):
        """Returns if a given commmand is valid or not"""
        if command == 'left' or command == 'right' or command == 'up' or command == 'down':
            return True
        else :
            return False 
 
    def distance(self):
        """Returns the final Euclidean distance from moves in input stream"""
        return math.sqrt(self.x**2 + self.y**2)
        
    
def main(filename):
    try:
        f = open(filename, 'r') 
        d = DistanceCalculator(f)
        print('Euclidean distance: %.2f' % d.distance())
        f.close()
    except FileNotFoundError:
        sys.exit('invalid filename %s' % filename)
    except Exception as e:
        f.close()
        sys.exit(e)
            

if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit('Usage: %s file' % sys.argv[0])
    main(sys.argv[1])


