;>; Input two numbers into cells 0 and 1
< move to 0
[
>>+ increment cell 2
>+ increment cell 3
<<<- decrement cell 0
]
>>> move to 3
[
<<<+ increment 0
>>>- decrement 3
]
<< move to 1
[
>>+ increment cell 3
>+ increment cell 4
<<<- decrement cell 1
]
>>> move to 4
[
<<<+ increment 1
>>>- decrement 4
]
< move to 3
[
<+ increment 2
>- decrement 3
]
< move to 2
: print result