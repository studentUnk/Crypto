import java.util.*;

public class CifradoCesar{
	
	public static void main(String [] args){
		// Este codigo solo encripta letras a-z, del abecedario ingles
		Scanner scanner = new Scanner(System.in);
		//String m = "Encriptame con Cesar";
		System.out.println("Ingrese su mensaje a encriptar: ");
		String m = scanner.nextLine();
		System.out.println("Ingrese la clave Cesar: ");
		//int key = 15;
		int key = scanner.nextInt();
		int letters = 26;
		key %= letters; // Arreglame para evitar errores posteriores
		String mE = "";
		for(int i = 0; i < m.length(); i++){
			char c = m.charAt(i);
			int pos = c;
			if(m.charAt(i) >= 97){ // Identificar tipo de letra, mayuscula v minuscula
				pos -= 97;
			}else{
				pos -= 65;
			}
			if((m.charAt(i) >= 65 && m.charAt(i) <= 90) || (m.charAt(i) >= 97 && m.charAt(i) <= 122)){
				pos = ((pos+key)%letters); // Circulo modulo letters, encriptado
				if(Character.isUpperCase(m.charAt(i))){ // 65
					pos += 65;
				}else{ // 97
					pos += 97;
				}
				mE = mE.concat(Character.toString((char)pos)); // Agregar caracter encriptado
			} else{
				mE = mE.concat(Character.toString(c)); // No se encripta
			}
		}
		System.out.println("Mensaje = " + m);
		System.out.println("Cifrado Cesar = " + mE);
		// Descifrar
		String mD = "";
		for(int i = 0; i < mE.length(); i++){
			char c = mE.charAt(i);
			int pos = c;
			if(mE.charAt(i) >= 97){
				pos -= 97;
			}else{
				pos -= 65;
			}
			if((mE.charAt(i) >= 65 && mE.charAt(i) <= 90) || (mE.charAt(i) >= 97 && mE.charAt(i) <= 122)){
				//pos = ((pos-key)%letters);
				pos -= key; // Retroceso de suma Cesar
				pos = pos % letters; // Circulo modulo letters
				if(pos < 0){ pos = letters+pos;} // Ajustar valores negativos
				if(Character.isUpperCase(mE.charAt(i))){ // 65
					pos += 65;
				}else{ // 97
					pos += 97;
				}
				mD = mD.concat(Character.toString((char)pos)); // Agregar letra desencriptada
			} else{
				mD = mD.concat(Character.toString(c)); // No se encripto
			}
		}
		//System.out.println("Mensaje cifrado = " + m);
		System.out.println("Descifrado Cesar = " + mD);
	}
}