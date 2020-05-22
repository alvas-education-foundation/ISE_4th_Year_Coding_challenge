// Class that contains methods for Database manipulation

import java.awt.*;
//import javax.swing.*;
import java.awt.event.*;
import java.util.*;
import java.io.*;


public class FullDataBaseGenerator
{

	// Method that takes a String (from the film time cb)
	// And returns a String of the name of the text file it belongs to
	public static String returnFileName(String input)

	{
		String timeFileName  = input;

		if (input.equals("1.00 PM"))
		{
			timeFileName = "SEAT DATABASE 1.00 PM.txt";
		}
		else if (input.equals("3.00 PM"))
		{
			timeFileName= "SEAT DATABASE 3.00 PM.txt";
		}
		else if (input.equals("5.00 PM"))
		{
			timeFileName= "SEAT DATABASE 5.00 PM.txt";
		}
		else if (input.equals("7.00 PM"))
		{
			timeFileName = "SEAT DATABASE 7.00 PM.txt";
		}
		else if (input.equals("9.00 PM"))
		{
			timeFileName= "SEAT DATABASE 9.00 PM.txt";
		}

		return timeFileName;
	}


	// Method that generates a fresh database
	public void FullDataBaseGeneration(String file_name)
	{
		// Name of database (calculated by 'returnFileName' method)
		String name = file_name;

		// Get ArrayList cointaining values for every seat
		ArrayList <Integer> input = seatNumberCalculate();

		// Name of database
		String selectedTime = returnFileName(name);

		File selectedTimeFile = new File(selectedTime);

		try{
		// if the file exists, do not create a new file (leave existing file alone)
		if (selectedTimeFile.exists() == true)
		{
			return;
		}
		}catch (Exception ex){
		System.err.println(ex.getMessage());
		}

		// if the file doesnt exist..
		try{

			// create a new file with the correct name
			selectedTimeFile.createNewFile();

			// Start dependencies for file reading
			FileInputStream fs = new FileInputStream(selectedTimeFile.toString());
			DataInputStream in = new DataInputStream(fs);
			BufferedReader br = new BufferedReader(new InputStreamReader(in));

			//Start dependancy for file writing
			String stringLine;
			BufferedWriter fw1 = new BufferedWriter(new FileWriter(selectedTime));

			// Write a ; to the file (this is needed to add some content to replace)
			fw1.write(";");
			// Close this write dependancy
			fw1.close();

			// While there are Lines left to be read
		  	while ((stringLine = br.readLine()) != null)
		  	{
				// Create dependencies for writing to same file
				BufferedWriter fw = new BufferedWriter(new FileWriter(selectedTime));
				int x=0;
				// Iterate through the new edited array (orginal array minus selected seat)
				while(x < input.size())
				{
					// Rewrite every line of the text file with each entry in the new array
					String line = input.get(x).toString();
					fw.write(line + ";");
					x++;
				}
				//Close the file writing dependency
				fw.close();
			}

			}catch (Exception ex){
	  				System.err.println(ex.getMessage());}

	}



		// Method for returning an array of the available seats, for passing into the Main class
		public static ArrayList<Integer> AvailableSeatsArrayReturn(String file_name)
		{
			ArrayList<Integer> temp = new ArrayList<Integer>();

			String name = file_name;
			String selectedTime = returnFileName(name);
			File selectedTimeFile = new File(selectedTime);



			if (selectedTimeFile.exists())
			{

				try{

	 			FileInputStream fs = new FileInputStream(selectedTimeFile.toString());
	  			DataInputStream in = new DataInputStream(fs);
	  			BufferedReader br = new BufferedReader(new InputStreamReader(in));
	  			String stringLine;

	  			while ((stringLine = br.readLine()) != null)
	  			{
	  				String[] array = stringLine.split(";");

					// For every object in the array, built from items in the text file
	  				for (int i=0; i < array.length; i++)
	  				{
						// Convert the item to an integer
		  				Integer num = Integer.parseInt(array[i]);

		  				// Add Item to arraylist to be rerturned
		  				temp.add(num);
	  				}
	  			}

	  			in.close();

	    			}catch (Exception ex){System.err.println(ex.getMessage());}

			}
			return temp;
		}





}