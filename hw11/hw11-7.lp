 cycle(X) :- person(X,_), person(Y,_), person(Z,_), speaks_with(X,Y), speaks_with(Y,Z), speaks_with(Z,X).
 #show cycle/1.