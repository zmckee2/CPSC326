num_spoken(X, N) :- N = #count {Y : speaks_with(X,Y); Y: speaks_with(Y,X)}, person(X,_).
most_influence(X, N) :- N = #max {Y : num_spoken(_,Y)}, person(X,_), num_spoken(X,N).
#show most_influence/2.