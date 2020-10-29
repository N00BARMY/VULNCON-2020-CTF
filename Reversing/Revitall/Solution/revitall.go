package main

import "fmt"


func check(str string) (result string) { 
    for _, v := range str { 
        result = string(v) + result 
    } 
    return
} 

func fake1(){

	var fakeflag string = "vulncon{fak1sm}"

      strRev := check(fakeflag)
     fmt.Println(strRev)
	a:= 3
	b:= 4
	if a ==b{
		flag1()
	}else
	{
		fake2()
	}		
}

func flag1(){
	x:= "0x8888"
	y:= "0xccs0s"
        if x == y{
	strone := []string{"g" , "0" , "p", "h" ,"3" ,"r" ,"_" ,"a"}
	i:= 8
	for i<=8{
		fmt.Println(strone)
		i++
		}
		check:= "0x000null"
		check2:= "0x0000void"
		if check == check2{
			flag2()
			}else
		{
			fake2()
		}
	}else
	{
		reverse:= "g0ph3rs"
		strRev1 := check(reverse)
		fmt.Println(strRev1)
	}
}

func fake2(){
	var faketwo string = "vulncon{onemorefake}"
	strRev2 := check(faketwo)
	fmt.Println(strRev2)
	}

func flag2(){
		c:= "vulncon0"
		d:= "vulnconx001"
	if c == d{
		strtwo := []string{"d" , "d" , "r" , "3" , "s" , "s" ,"_" , "1"}
		j:= 8
		for j<=8{
			fmt.Println(strtwo)
			j++
			}
	}else
	{
		 notokay:= "ddr3ss_1"
		strRev2 := check(notokay)
		fmt.Println(strRev2)
		}
}

func main() {




	var x string = "0x056husio" 


	var y *string


	y = &x 


	var  compare = "string"
	var setone  *string


	setone = &compare
	    

		if setone != y{
			
				fake1()
			}else
                                               
		{
        fmt.Println("Make sure to have a look at the compare statements :) ")
    }
}

