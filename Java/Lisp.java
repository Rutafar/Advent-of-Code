private void findFloor(File file){

		int floor = 0; 

		BufferedReader reader;
		try {
			reader = new BufferedReader(
					new InputStreamReader(
							new FileInputStream(file),
							Charset.forName("UTF-8")));
			int counter=0;
			int c;
			boolean first=true;
			while((c = reader.read()) != -1) {
				char character = (char) c;
				if(floor == -1 && first) {
					first=false;
					System.out.println("Santa entered the basement at: " + counter);
				}
					if (character == '(') {
						floor++; 
					} else{
					if(character == ')'){
						floor--;
					}
					counter++;	  
				}
			System.out.println("Santa is on the " + floor + "th floor");
			reader.close();
		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
