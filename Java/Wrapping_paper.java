package daytwo;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class Wrapping_Paper {


	public static void main(String[] args) {
		new Wrapping_Paper().squareFeetOfWrappingPaper(new File("inputs/input2.txt"));;
	}

	public void squareFeetOfWrappingPaper (File file) {
		int totalArea = 0;
		int ribbon = 0; 
		try {
			Scanner scan = new Scanner(file);
			String line;
			while (scan.hasNextLine()) {
				line = scan.nextLine();
				String [] tokens = line.split("x");

				int	l = Integer.parseInt(tokens[0]);
				int	w = Integer.parseInt(tokens[1]);
				int	h = Integer.parseInt(tokens[2]);

	

				ribbon+=2*l+2*w+2*h - 2 * Math.max(h, Math.max(w, l));
				ribbon+=l*w*h;

				totalArea+=(2*l*w+2*w*h+2*h*l);
				totalArea+=Math.min(l*w, Math.min(w*h, h*l));

			}
			System.out.println("Total of wrapper: " + totalArea);
			System.out.println("Total of ribbon: " + ribbon);
			scan.close();

		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}

	}
}
