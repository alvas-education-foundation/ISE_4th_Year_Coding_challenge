5. Write a JAVA program which implements RMI.
HelloInterface.java
import java.rmi.*;
public interface HelloInterface extends Remote
{
public String getMessage() throws RemoteException;
public void display() throws RemoteException;
}
HelloServerImpl.java
import java.rmi.*;
import java.rmi.server.*;
public class HelloServerImpl extends UnicastRemoteObject implements HelloInterface
{
public HelloServerImpl() throws RemoteException
{
}
public String getMessage() throws RemoteException
{
return "This is simple RMI program";
}
public void display() throws RemoteException
{
System.out.println("Hai how are you ");
}
public static void main (String args[])
{
try{
HelloServerImpl Server = new HelloServerImpl();
Naming.rebind("rmi://localhost:1099/Server",Server);
}catch(Exception e){}
}
}
HelloClient.java
import java.rmi.*;
public class HelloClient
{
public static void main(String args[])
{
try{
HelloInterface Server = (HelloInterface)Naming.lookup("rmi://localhost:1099/Server");
String msg = Server.getMessage();
System.out.println(msg);
Server.display();
}catch(Exception e){}
}
}


