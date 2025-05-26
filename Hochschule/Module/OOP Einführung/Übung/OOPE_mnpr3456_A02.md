![[OOPE_Abgabe_02.excalidraw#^area=TeMWDiMkhWhSKnTWKx-Ha|100%]]

```java
public class Main {
	public static void main(String[] args) {
		int x = 80, y = 60;

		if(x < 100)
			if(y > 50)
				System.out.println("eins");
			else
				System.out.println("zwei");
		else
			System.out.println("drei");
	}
}
```

```output
eins
```

<div style='page-break-after: always;'></div>

![[OOPE_Abgabe_02.excalidraw#^area=kO3pOniJ9YO0QPK7Ko_wQ|100%]]

```java
public class Main {
	public static void main(String[] args) {
		int x = 110, y = 40;

		if(x < 100)
		{
			if(y > 50)
			System.out.println("eins");
		}
		else
		{
		System.out.println("zwei");
		System.out.println("drei");
		}
	}
}
```

```output
zwei
drei
```

<div style='page-break-after: always;'></div>

![[OOPE_Abgabe_02.excalidraw#^area=I4aczX-C21z5hs3fG6kjJ|100%]]

```java
public class Main {
	public static void main(String[] args) {
		// int t = 9;
		// int t = 20;
		// int t = 4;
		// int t = 7;
		int t = 16;

		if(t < 15)
			if(t > 7)
				System.out.println("eins");
			else
				System.out.println("zwei");
		else
			if(t < 18)
				System.out.println("drei");
		System.out.println("Ende");
	}
}
```

a)

```output
eins
Ende
```

b)

```output
Ende
```

c)

```output
zwei
Ende
```

d)

```output
zwei
Ende
```

e)

```output
drei
Ende
```

<div style='page-break-after: always;'></div>

![[OOPE_Abgabe_02.excalidraw#^area=RWjzh6_nnFHl2JRHwgqNM|100%]]

```java
public class Main {
	public static void main(String[] args) {
		//  int a = 3, b = 4, m = 1, n = 5;
		int a = 5, b = 3, m = 7, n = 4;

//		if(a < b)
//			if(m > n)
		if(a > b)
			if(m < n)
				System.out.println("schwarz");
			else
				System.out.println("rot");
		else
			if(m > n)
				System.out.println("gruen");
			else
				System.out.println("blau");
	}
}
```

a)

```output
rot
```

b)

```output
gruen
```

c)

- für a)

```output
blau
```

- für b)

```output
rot
```

d)

```java
public class Main {
	public static void main(String[] args) {
		//  int a = 3, b = 4, m = 1, n = 5;
		int a = 5, b = 3, m = 7, n = 4;

		if(m > n)
			if(a < b)
				System.out.println("schwarz");
			else
				System.out.println("gruen");
		else
			if(a < b)
				System.out.println("rot");
			else
				System.out.println("blau");
	}
}
```

<div style='page-break-after: always;'></div>

![[OOPE_Abgabe_02.excalidraw#^area=-Hp6F5cufIFKet7q154p9|100%]]

```java
public class Main {
	public static void main(String[] args) {
		// int n = 17;
		// int n = 25;
		// int n = 7;
		// int n = 0;
		int n = 9;

		if(n <= 10)
			if(n/3 < 2)
				System.out.println("eins");
			else if(n/3 >= 3)
				System.out.println("zwei");
			else
				System.out.println("drei");
		else if(n > 20)
			System.out.println("vier");
		else
			System.out.println("fuenf");
	}
}
```

a)

```output
fuenf
```

b)

```output
vier
```

c)

```output
drei
```

d)

```output
eins
```

e)

```output
zwei
```

<div style='page-break-after: always;'></div>

![[OOPE_Abgabe_02.excalidraw#^area=dakRNs0VgF7FSSh7w2C_w|100%]]

```java
public class Main {
	public static void main(String[] args) {
		switch(a)
		{
			case 3:
				result = a;
				break;
			case 6:
				result = a + 10;
				break;
			case 10:
				result = a + 20;
				break;
			default:
				result = a + 30;
				break;
		}
	}
}
```

<div style='page-break-after: always;'></div>

![[OOPE_Abgabe_02.excalidraw#^area=yiQtXzIEfR4tdQisimdKb|100%]]

```java
public class Main {
	public static void main(String[] args) {
		if(n == 39 || n == 15)
			System.out.println("gewonnen");
		else
			System.out.println("verloren");
	}
}
```

<div style='page-break-after: always;'></div>

![[OOPE_Abgabe_02.excalidraw#^area=B7DGUEsLhl9YaxWsENuZ2|100%]]

```java
public class Main {
	public static void main(String[] args) {
		// int n = 5;
		// int n = 4;
		int n = 8;

		switch(n)
		{
			case 1:
			case 3:
			case 4:
				System.out.println(n);
				break;
			case 2:
			case 5:
			case 6:
				System.out.println(n * 10);
				break;
			default:
				System.out.println(n * 100);
				break;
		}
	}
}
```

a)

```output
50
```

b)

```output
4
```

c)

```output
800
```

```java
public class Main {
	public static void main(String[] args) {
		// int n = 5;
		// int n = 4;
		int n = 8;

		switch(n)
		{
			case 1:
			case 3:
			case 4:
				System.out.println(n);
			case 2:
			case 5:
			case 6:
				System.out.println(n * 10);
			default:
				System.out.println(n * 100);
		}
	}
}
```

d)

```output
50
500
```

e)

```output
4
40
400
```

f)

```output
800
```

<div style='page-break-after: always;'></div>

![[OOPE_Abgabe_02.excalidraw#^area=PD8mgNpi4wrBCeq9YyYep|100%]]

```java
public class Main {
	public static void main(String[] args) {
		switch(ch)
		{
			case 'a':
			case 'b':
			case 'c':
				System.out.println("im Bereich \"abc\"");
				break;
			case 'g':
			case 'h':
				System.out.println("in der Mitte des Alphabets");
				break;
			case 'z':
				System.out.println("ein z, ein z, ...");
				break;
			default:
				System.out.println("andere Buchstaben");
				break;
		}
	}
}
```

<div style='page-break-after: always;'></div>

![[OOPE_Abgabe_02.excalidraw#^area=6nYC7sX6iPXuLa-9S-oG2|100%]]

```java
public class Main {
	public static void main(String[] args) {
		switch(n)
		{
			case 5, 6, 7:
				System.out.println("Bereich 2");
				break;
			default:
				System.out.println("Bereich 1");
				break;
		}
	}
}
```

<div style='page-break-after: always;'></div>

![[OOPE_Abgabe_02.excalidraw#^area=tHsC1cLih9MA_loSNUnYv|100%]]

```java
public class Main {
	public static void main(String[] args) {
		double x, y, z, val;

		if(x >= y && x <= z)
			val = z - y;
		else
			if(x < y)
				val = 0;
			else
				val = 1.0E25;
	}
}
```
