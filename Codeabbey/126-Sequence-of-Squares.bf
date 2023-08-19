; input number in 0
#>$  copy input to 1
[ 
 > move to 2
 + increment by 1
 #>$  copy from 2 to 3
 #>$  copy from 3 to 4
 < move to 3
 [>[->+>+<<]>[-<+>]<<-]  multiply values in 3 and 4
 >[-]                    clear second cell
 >>[-<<<+>>>]<<<         move result to 3
 : print value
 << move to 1
 -
]