% main predicate
main :- 
    % reads the input, passes it into the rev_list predicate, then writes it
    read(Input),
    rev_list(Input, Result),
    write(Result).

% Calls helper function to reverse the function and stores it in variable Result
rev_list(Input,Result) :-
    accRev(Input,[],Result).

% Takes the head and tail of the input, then recursively calls the predicate to store the reverse in variable R
accRev([H|T],A,R) :- 
    accRev(T,[H|A],R).
accRev([],A,A).