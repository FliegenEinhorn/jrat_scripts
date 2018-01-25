import java.io.*;
import sun.security.rsa.RSAPrivateCrtKeyImpl;

import java.security.InvalidKeyException;
import java.security.NoSuchAlgorithmException;
import java.security.interfaces.RSAPrivateKey;
import javax.crypto.BadPaddingException;
import javax.crypto.Cipher;
import javax.crypto.IllegalBlockSizeException;
import javax.crypto.NoSuchPaddingException;
import java.security.spec.RSAPrivateCrtKeySpec;


public class deserialization
{

    public static void main(String[] args) throws FileNotFoundException,IOException,ClassNotFoundException,
            NoSuchAlgorithmException, NoSuchPaddingException, InvalidKeyException, IllegalBlockSizeException,
            BadPaddingException
    {
        File fichier = new File("./FetsLunule");

        ObjectInputStream ois =  new ObjectInputStream(new FileInputStream(fichier)) ;
        sun.security.rsa.RSAPrivateCrtKeyImpl m = (sun.security.rsa.RSAPrivateCrtKeyImpl)ois.readObject() ;
        System.out.print("Fetslunule");
        System.out.println("\n") ;
        System.out.print("modulus : "+m.getModulus());
        System.out.println("\n") ;
        System.out.print("PublicExponent : "+m.getPublicExponent());
        System.out.println("\n") ;
        System.out.print("Private Exponent : " + m.getPrivateExponent());
        System.out.println("\n") ;
        System.out.print("PrimeP : "+ m.getPrimeP());
        System.out.println("\n") ;
        System.out.print("PrimeQ : " + m.getPrimeQ());
        System.out.println("\n") ;
        System.out.print("PrimeExponentP : " + m.getPrimeExponentP());
        System.out.println("\n") ;
        System.out.print("PrimeExponentQ : " + m.getPrimeExponentQ());
        System.out.println("\n") ;
        System.out.print("CrtCoefficient : " + m.getCrtCoefficient());
    }
}

