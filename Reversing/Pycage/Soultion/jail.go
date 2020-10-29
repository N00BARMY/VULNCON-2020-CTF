package main


import(

    "fmt"
    "math"
      )


var g=  [5]float64{ 23 , 46 , 69, 92, 115}
var h= [5]float64{ 2, 2, 2 , 2, 2}

func one(){
	c:= math.Pow(g[0] , h[0])
	d:= math.Pow(g[1], h[1])
	e:= math.Pow(g[2] , h[2])
	f:= math.Pow(g[3] , h[3])
	i:= math.Pow(g[4] , h[4])
		var codeone string = "cageone"
                if codeone == "cage"{
					var checkone , checktwo , checkthree , checkfour , checkfive  float64
					fmt.Println("Enter the magic code : \n")
					fmt.Scanln(&checkone)
					if checkone == c{
								fmt.Println("0xd4")
							}
					fmt.Println("Enter the magic code : \n")
					fmt.Scanln(&checktwo)
					if checktwo == d{
								fmt.Println("t4")
						}
					fmt.Println("Enter the magic code : \n")
					fmt.Scanln(&checkthree)
					if checkthree == e{
								fmt.Println("by")
							}
					fmt.Println("Enter the magic code :\n")
					fmt.Scanln(&checkfour)
					if checkfour == f{
								fmt.Println("te")
							}
					fmt.Println("Enter the magic code :\n")
					fmt.Scanln(&checkfive)
					if checkfive == i{
								fmt.Println("s1")
							}else{
								fmt.Println("You might have landed the wrong place")
							}
		}else{
			fmt.Println("You might have landed the wrong place")
		}
 }

func main(){
		fmt.Println("Welcome to the cage , scopes will help you out for sure")
		one();
	}


