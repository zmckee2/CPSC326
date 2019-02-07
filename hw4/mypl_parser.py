# Author: Zach McKee
# Course: CPSC 326, Spring 2019
import mypl_error as error
import mypl_lexer as lexer
import mypl_token as token

class Parser(object):

    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = None

    def parse(self):
        """succeeds if program is syntatically well-formed"""
        self.__advance()
        self.__stmts()
        self.__eat(token.EOS, 'expecting end of file')

    def __advance(self):
        self.current_token = self.lexer.next_token()

    def __eat(self, tokentype, error_msg):
        if self.current_token.tokentype == tokentype:
            self.__advance()
        else:
            self.__error(error_msg)

    def __error(self, error_msg):
        s = error_msg + ', found "' + self.current_token.lexeme + '" in parser'
        l = self.current_token.line
        c = self.current_token.column
        raise error.MyPLError(s, l, c)

    #Begin of recursive decent functions
    def __stmts(self):
        """<stmts> ::= <stmt> <stmts> | e"""
        if self.current_token.tokentype != token.EOS:
            self.__stmt()
            self.__stmts()

    def __stmt(self):
        """<stmt> ::= <sdecl> | <fdecl> | <bstmt>"""
        if self.current_token.tokentype == token.STRUCTTYPE:
            self.__sdecl()
        elif self.current_token.tokentype == token.FUN:
            self.__fdecl()
        else:
            self.__bstmt()
    
    def __bstmts(self):
        """<bstmts> ::= <bstmt> <bstmts> | e"""
        #Tokens that can start a bstmt
        types = [token.VAR, token.SET, token.IF, token.WHILE, token.LPAREN]
        types.extend([token.STRINGVAL, token.INTVAL, token.BOOLVAL,token.RETURN])
        types.extend([token.FLOATVAL, token.NIL, token.NEW, token.ID])
        if self.current_token.tokentype in types:
            self.__bstmt()
            self.__bstmts()

    def __bstmt(self):
        """<bstmt> ::= <vdecl> | <assign> | <cond> | <while> | <expr> SEMICOLON | <exit>"""
        if self.current_token.tokentype == token.VAR:
            self.__vdecl()
        elif self.current_token.tokentype == token.SET:
            self.__assign()
        elif self.current_token.tokentype == token.IF:
            self.__cond()
        elif self.current_token.tokentype == token.WHILE:
            self.__while()
        elif self.current_token.tokentype == token.RETURN:
            self.__exit()
        else:
            self.__expr()
            self.__eat(token.SEMICOLON, 'expecting a ";"')

    def __sdecl(self):
        """<sdecl> ::= STRUCT ID <vdecls> END"""
        self.__eat(token.STRUCTTYPE, "expecting a struct")
        self.__eat(token.ID, "expecting an identifyer")
        self.__vdecls()
        self.__eat(token.END, "expecting end")

    def __vdecls(self):
        """<vdecls> ::= <vdecl> <vdecls> | e"""
        if self.current_token.tokentype == token.VAR:
            self.__vdecl()
            self.__vdecls()

    def __fdecl(self):
        """<fdecl> ::= FUN (<type>|NIL) ID LPAREN <params> RPAREN <bstmts> END"""
        self.__eat(token.FUN, "expecting fun keyword")
        if self.current_token.tokentype == token.NIL:
            self.__advance()
        else:
            self.__type()
        self.__eat(token.ID, "expecting an identifyer")
        self.__eat(token.LPAREN, 'expecting a "("')
        self.__params()
        self.__eat(token.RPAREN, 'expecting a ")"')
        self.__bstmts()
        self.__eat(token.END, "expecting end")
                       
    def __params(self):
        """<params> ::= ID COLON <type> (COMMA ID COLON <type>)* | e"""
        if self.current_token.tokentype == token.ID:
            self.__advance()
            self.__eat(token.COLON, 'expecting a ":"')
            self.__type()
            while self.current_token.tokentype == token.COMMA:
                self.__advance()
                self.__eat(token.ID, "expecting an identifyer")
                self.__eat(token.COLON, 'expecting a ":"')
                self.__type()

    def __type(self):
        """<type> ::= ID | INTTYPE | FLOATTYPE | BOOLTYPE | STRINGTYPE"""
        types = [token.ID, token.INTTYPE, token.FLOATTYPE, token.BOOLTYPE]
        types.append(token.STRINGTYPE)
        if self.current_token.tokentype in types:
            self.__advance()
        else:
            s = 'expected a type, found"' + self.current_token.lexeme + '" in parser'
            l = self.current_token.line
            c = self.current_token.column
            raise error.MyPLError(s, l, c)


    def __exit(self):
        """<exit> ::= RETURN (<expr> | e) SEMICOLON"""
        self.__eat(token.RETURN, 'expecting a "return" keyword')
        types = [token.LPAREN,token.STRINGVAL, token.INTVAL, token.BOOLVAL]
        types.extend([token.FLOATVAL, token.NIL, token.NEW, token.ID])
        if self.current_token.tokentype in types:
            self.__expr()
        self.__eat(token.SEMICOLON, 'expecting a ";"')

    def __vdecl(self):
        """<vdecl> ::= VAR ID <tdecl> ASSIGN <expr> SEMICOLON"""
        self.__eat(token.VAR, "expecting var keyword")
        self.__eat(token.ID, "expecting an identifier")
        self.__tdecl()
        self.__eat(token.ASSIGN, 'expectring a "="')
        self.__expr()
        self.__eat(token.SEMICOLON, 'expecting a ";"')

    def __tdecl(self):
        if self.current_token.tokentype == token.COLON:
            self.__advance()
            self.__type()

    
    def __assign(self):
        """<assign> ::= SET <lvalue> ASSIGN <expr> SEMICOLON"""
        self.__eat(token.SET, 'expecting a "set" keyword')
        self.__lvalue()
        self.__eat(token.ASSIGN, 'expectring a "="')
        self.__expr()
        self.__eat(token.SEMICOLON, "Expecting a semicolon")

    def __lvalue(self):
        """<lvalue> ::= ID (DOT ID)*"""
        self.__eat(token.ID, "expecting an identifier")
        while self.current_token.tokentype == token.DOT:
            self.__eat(token.DOT, 'expecting a "."')
            self.__eat(token.ID, "expecting an identifier")

    def __cond(self):
        """<cond> ::= IF <bexpr> THEN <bstmts> <condt> END"""
        self.__eat(token.IF, 'expecting an "if" keyword')
        self.__bexpr()
        self.__eat(token.THEN, 'expecting a "then" keyword')
        self.__bstmts()
        self.__condt()
        self.__eat(token.END, 'expecting an "end" keyword')

    def __condt(self):
        """<condt> ::= ELIF <bexpr> THEN <bstmts> <condt> | ELSE <bstmts> | e"""
        if self.current_token.tokentype == token.ELIF:
            self.__advance()
            self.__bexpr()
            self.__eat(token.THEN, 'expecting a "then" keyword')
            self.__bstmts()
            self.__condt()
        elif self.current_token.tokentype == token.ELSE:
            self.__advance()
            self.__bstmts()

    def __while(self):
        """<while> ::= WHILE <bexpr> DO <bstmts> END"""
        self.__eat(token.WHILE, 'expecting a "while" keyword')
        self.__bexpr()
        self.__eat(token.DO, 'expecting a "do" keyword')
        self.__bstmts()
        self.__eat(token.END, 'expecting an "end" keyword')

    def __expr(self):
        """<expr> ::= (<rvalue> | LPAREN <expr> RPAREN) (<mathrel> <expr> | e)"""
        if self.current_token.tokentype == token.LPAREN:
            self.__advance()
            self.__expr()
            self.__eat(token.RPAREN, 'expecting a ")"')
        else:
            self.__rvalue()
        types = [token.PLUS, token.MINUS, token.DIVIDE, token.MULTIPLY]
        types.append(token.MODULO)
        if self.current_token.tokentype in types:
            self.__mathrel()
            self.__expr()
        

    def __mathrel(self):
        """<mathrel> ::= PLUS | MINUS | DIVIDE | MULTIPLY | MODULO"""
        types = [token.PLUS, token.MINUS, token.DIVIDE, token.MULTIPLY, token.MODULO]
        if self.current_token.tokentype in types:
            self.__advance()
        else:
            s = 'expected a math operator, found "' + self.current_token.lexeme + '" in parser'
            l = self.current_token.line
            c = self.current_token.column
            raise error.MyPLError(s, l, c)

    def __rvalue(self):
        """<rvalue> ::= STRINGVAL | INTVAL | BOOLVAL | FLOATVAL | NIL | NEW ID | <idrval>"""
        types = [token.STRINGVAL, token.INTVAL, token.BOOLVAL]
        types.extend([token.FLOATVAL, token.NIL])
        if self.current_token.tokentype == token.NEW:
            self.__advance()
            self.__eat(token.ID, "expecting an identifier")
        elif self.current_token.tokentype == token.ID:
            self.__idrval()
        elif self.current_token.tokentype in types:
            self.__advance()
        else:
            s = 'expected a rvalue found"' + self.current_token.lexeme + '" in parser'
            l = self.current_token.line
            c = self.current_token.column
            raise error.MyPLError(s, l, c)

    def __idrval(self):
        """<idrval> ::= ID (DOT ID)* | ID LPAREN <exprlist> RPAREN"""
        self.__eat(token.ID, "expecting an identifier")
        if self.current_token.tokentype == token.LPAREN:
            self.__advance()
            self.__exprlist()
            self.__eat(token.RPAREN, 'expecting a ")"')
        else:
            while self.current_token.tokentype == token.DOT:
                self.__advance()
                self.__eat(token.ID, "expecting an identifier")

    def __exprlist(self):
        """<exprlist> ::= <expr> (COMMA <expr>)* | e"""
        types = [token.LPAREN,token.STRINGVAL, token.INTVAL, token.BOOLVAL]
        types.extend([token.FLOATVAL, token.NIL, token.NEW, token.ID])
        if self.current_token.tokentype in types:
            self.__expr()
            while self.current_token.tokentype == token.COMMA:
                self.__advance()
                self.__expr()

    def __bexpr(self):
        """<bexpt> ::= <expr> <bexprt> | NOT <bexpr> <bexprt> |"""
        """            LPAREN <bexpr> RPAREN <bconnct>"""
        if self.current_token.tokentype == token.LPAREN:
            self.__advance()
            self.__bexpr()
            self.__eat(token.RPAREN, 'expecting a ")"')
            self.__bconnct()
        elif self.current_token.tokentype == token.NOT:
            self.__advance()
            self.__bexpr()
            self.__bexprt()
        else:
            self.__expr()
            self.__bexprt()

    def __bexprt(self):
        """<bexprt> ::= <boolrel> <expr> <bconnct> | <bconnct>"""
        types = [token.EQUAL, token.LESS_THAN, token.LESS_THAN_EQUAL]
        types.extend([token.GREATER_THAN_EQUAL, token.GREATER_THAN])
        types.append(token.NOT_EQUAL)
        if self.current_token.tokentype in types:
            self.__boolrel()
            self.__expr()
            self.__bconnct()
        else:
            self.__bconnct()

    def __bconnct(self):
        """<bconnct> ::= AND <bexpr> | OR <bexpr> | e"""
        if self.current_token.tokentype == token.AND:
            self.__advance()
            self.__bexpr()
        elif self.current_token.tokentype == token.OR:
            self.__advance()
            self.__bexpr()

    def __boolrel(self):
        """<boolrel> ::= EQUAL | LESS_THAN | GREATER_THAN | LESS_THAN_EQUAL |"""
        """              GREATER_THAN_EQUAL | NOT_EQUAL"""
        types = [token.EQUAL, token.LESS_THAN, token.LESS_THAN_EQUAL]
        types.extend([token.GREATER_THAN_EQUAL, token.GREATER_THAN])
        types.append(token.NOT_EQUAL)
        if self.current_token.tokentype in types:
            self.__advance()
        else:
            s = 'expected a conditional operator, found "' + self.current_token.lexeme + '" in parser'
            l = self.current_token.line
            c = self.current_token.column
            raise error.MyPLError(s, l, c)