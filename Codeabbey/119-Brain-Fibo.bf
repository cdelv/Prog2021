; input N 
>>>;>; (N | 0 | 0 | f0 | f1)
[
	<<+<+ increment 1 and 2
	>>>-
]
<<<< move to 0  (N | f1 | f1 | f0 | 0)
[
	>>> move to 3
	[
		<<+ increment 1 (N | f1 plus f0 | f1 | 0)
		>>-
	]
	< move to 2
	[
		>+ increment 3 (N | f1 plus f0 | 0 | f1)
		<-
	]
	< move to 1
	[
		>>>+ increment 4 (N | 0 | 0 | f1 | f1 plus f0)
		<<<-
	]
	>>> move to 4
	[
		<<+<+ increment 1 and 2 (N | f1 plus f0 | f1 plus f0 | f1 | 0)
		>>>-
	]
	<<<: print f1 plus f2
	<- decrement 0
]