appears_in_one(X) :- person(X,_), appears_in(X, episode1).
appears_in_one(X) :- droid(X,_), appears_in(X, episode1).
appears_in_two(X) :- appears_in(X, episode2), appears_in_one(X).
appears_in_three(X) :- appears_in(X, episode3), appears_in_two(X).
appears_in_four(X) :- appears_in(X, episode4), appears_in_three(X).
appears_in_five(X) :- appears_in(X, episode5), appears_in_four(X).
appears_in_six(X) :- appears_in(X, episode6), appears_in_five(X).
appears_in_seven(X) :- appears_in(X, episode7), appears_in_six(X).
appears_in_all(Y) :- person(X,Y), appears_in_seven(X).
appears_in_all(Y) :- droid(X,Y), appears_in_seven(X).
#show appears_in_all/1.