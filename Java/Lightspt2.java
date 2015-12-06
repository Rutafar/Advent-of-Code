package day6;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class Lightspt2 {
	int[][] grid;
	
	public Lightspt2() {
		createGrid();
		readFile();
		countLights();
	}


	private void countLights() {
		int lights=0;
		for(int i=0; i<1000; i++){
			for(int j=0; j<1000; j++){
				lights+=grid[i][j];
			}
		}
		System.out.println(lights + " is the total brightness");
	}


	private void readFile() {
		try {
			Scanner s = new Scanner(new File("Inputs/Lights.txt"));
			while(s.hasNextLine()){
				String line = s.nextLine();
				if(line.contains("turn on"))
					turnOnLight(line);
				else if (line.contains("turn off"))
					turnOffLight(line);
				else if (line.contains("toggle"))
					ToggleLight(line);
			}
			s.close();
		} catch (FileNotFoundException e) {e.printStackTrace();}

	}


	private void ToggleLight(String line) {
		String[] nl = line.split("through");
		String sub= nl[0].substring(7);
		String [] start = sub.split(",");
		String[] end = nl[1].split(",");
		int start_x= Integer.parseInt(start[0].trim());
		int start_y= Integer.parseInt(start[1].trim());
		int end_x= Integer.parseInt(end[0].trim());
		int end_y=Integer.parseInt(end[1].trim());
		for(int i = start_x; i<=end_x; i++){
			for(int j=start_y; j<=end_y; j++){
				grid[i][j]+=2;
			}
			}
		}
	


	private void turnOffLight(String line) {
		String[] nl = line.split("through");
		String sub= nl[0].substring(9);
		String [] start = sub.split(",");
		String[] end = nl[1].split(",");
		int start_x= Integer.parseInt(start[0].trim());
		int start_y= Integer.parseInt(start[1].trim());
		int end_x= Integer.parseInt(end[0].trim());
		int end_y=Integer.parseInt(end[1].trim());
		for(int i = start_x; i<=end_x; i++){
			for(int j=start_y; j<=end_y; j++){
			if(grid[i][j]>0)
				grid[i][j]--;
			}
		}
	}


	private void turnOnLight(String line) {
		String[] nl = line.split("through");
		String sub= nl[0].substring(8);
		String [] start = sub.split(",");
		String[] end = nl[1].split(",");
		int start_x= Integer.parseInt(start[0].trim());
		int start_y= Integer.parseInt(start[1].trim());
		int end_x= Integer.parseInt(end[0].trim());
		int end_y=Integer.parseInt(end[1].trim());
		for(int i = start_x; i<=end_x; i++){
			for(int j=start_y; j<=end_y; j++){
				grid[i][j]++;
				}
		}
	}


	private void createGrid(){
		grid=new int[1000][1000];
		for(int i=0; i<1000; i++){
			for(int j=0; j<1000; j++){
				grid[i][j]=0;
			}
		}
	}



	public static void main(String[] args) {
		new Lightspt2();
	}
}
