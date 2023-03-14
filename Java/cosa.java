package Java;
import java.util.Scanner;

public class cosa{
    public static void main(String args[]){
        Scanner entrada = new Scanner(System.in);
        int num1 = 0;
        int num2 = 0;
        int resultado = 0;

        System.out.println("Escribe un numero");
        num1 = entrada.nextInt();
        System.out.println("Escribe el segundo numero");
        num2 = entrada.nextInt();
        resultado = num1*num2;
        System.out.println("El resultado es "+ resultado);
    }
}