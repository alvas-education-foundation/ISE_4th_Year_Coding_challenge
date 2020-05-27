
4. Write a JAVA Program which uses FileInputStream / FileOutPutStream Classes.
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.InputStream;
import java.io.OutputStream;
public class Prog8 {
public static void main(String[] args) throws Exception {
FileInputStream fis = new FileInputStream("in.txt");
FileOutputStream fos = new FileOutputStream("out.txt");
int c;
while ((c = fis.read()) != -1) {
System.out.print((char) c);
fos.write(c);
}
fis.close();
fos.close();
}
}