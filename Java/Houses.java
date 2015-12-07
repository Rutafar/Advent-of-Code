package daythree;

import java.awt.Point;
import java.io.BufferedReader;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStreamReader;
import java.nio.charset.Charset;
import java.util.HashSet;
import java.util.Set;

public class Houses {

	public static void main(String[] args) {
		new Houses().numberOfHouses(new File("inputs/input3.txt"));
	}

	private void numberOfHouses (File file) {
		BufferedReader reader;
		try {
			reader = new BufferedReader(
					new InputStreamReader(
							new FileInputStream(file),
							Charset.forName("UTF-8")));

			Set<Point> houses = new HashSet<Point>();
			boolean isSanta=true;
			int santa_x=0;
			int santa_y=0;
			int robot_x=0;
			int robot_y=0;
			Point init = new Point(santa_x,santa_y);
			houses.add(init);
			int c;
			while((c = reader.read()) != -1) {
				char character = (char) c;
				switch (character) {
				case '^':
					if (isSanta)
						santa_y++;
					else
						robot_y++;
					break;
				case 'v':
					if (isSanta)
						santa_y--;
					else
						robot_y--;
					break;

				case '<':
					if (isSanta)
						santa_x--;
					else
						robot_x--;
					break;

				case '>':
					if (isSanta)
						santa_x++;
					else
						robot_x++;
					break;

				}
				if (isSanta){
					houses.add(new Point(santa_x,santa_y));
					isSanta=false;
				}else{
					houses.add(new Point(robot_x,robot_y));
					isSanta=true;
				}
			}
			System.out.println("Number of houses with presents: " + houses.size());
		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}

	}

}
