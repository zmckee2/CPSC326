same_gen(X,Y) :- child_of(X,P), child_of(Y,P), X != Y.
same_gen(X,Y) :- child_of(C,X), child_of(C,Y), X != Y.
same_gen(X,Y) :- child_of(X,P), child_of(Y,R), same_gen(P,R), X != Y.
same_gen(X,Y) :- child_of(C,X), child_of(R,Y), same_gen(C,R), X != Y.
#show same_gen/2.