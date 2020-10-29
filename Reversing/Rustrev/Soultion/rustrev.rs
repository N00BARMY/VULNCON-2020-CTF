pub fn crack1()

{
	let mut s = "checklen";
	let mut d = "variable";

	println!("Is it the important function ?");
	if s == "variable"
		{
			let mut s = String::with_capacity(10);
			
			s.insert(0, 'c');
			s.insert(1, 'h');
			s.insert(2, '4');
			s.insert(3, 'r');
			s.insert(4, 's');
			s.insert(5, 'g');
			s.insert(6, 'o');
			s.insert(7, 'b');
			s.insert(8, 'r');
			s.insert(9, 'r');
	      println!("{}" , s );

	}
 	if s == "checklen"
		{
			println!("Wrong Place my friend");
		}
}

pub fn lencheck()

{
	let panic = "into_bytes".to_string();
	let paniczero = "reserve_up".to_string();
	let strlen_panic = panic.len();
	let strlen_paniczero = paniczero.len();
	if strlen_panic == 9
			{
				crack1();
			}
	if strlen_paniczero == 11
			{
				println!("Check out for the perfect function");
			}
      else
		{
			println!("I would suggest you to go to the perfect re-write");
		}
}

fn main()

{
	let push = 0 ;
	let pop = 1;
		if pop != 1 
			{
				lencheck();
			}
	       if pop == 1 
			{
				println!("Crackmes Just got re defined");
			}
        else
		{
			println!(" Are you the one for whom the  flag is waiting for ?");
		}
}

