//Method to Create a blank database of all the seats available
	public ArrayList<Integer> seatNumberCalculate()
	{
		// Variables to values for each block of seats
		int A = 0;
		int B = 0;
		int C  = 0;

		// ArrayList to hold the values
		ArrayList<Integer> al = new ArrayList<Integer>();

		// Add zero at the start of the array to act as a defauilt value for the cbs
		al.add(0);

		// Calculate the seatnumbers and add them into the array
		for (int i=0; i < 36; i++)
		{
			A = 101+i;
			al.add(A);
		}
		for (int i = 0; i < 40; i++)
		{
			B = 201+i;
			al.add(B);
		}
		for (int i = 0; i < 36; i++)
		{
			C = 301+i;
			al.add(C);
		}

		return al;
	}
