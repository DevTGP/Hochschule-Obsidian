![[Hochschule/Module/OOP Einführung/Übung/OOPE_Abgabe_03.excalidraw.md#^area=u3mq9Zt__HAz5E4qaCxB5|100%]]

```java
public class Main {
	public static void main(String[] args) {
		int i = 1;
		while(i <= 5)
		{
			System.out.print(i*i + " ");
			i += 1;
		}
	}
}
```

<div style='page-break-after: always;'></div>

![[Hochschule/Module/OOP Einführung/Übung/OOPE_Abgabe_03.excalidraw.md#^area=oySvcPtAIowyBOD4VbBO1|100%]]

```java
public class Main {
	public static void main(String[] args) {
		int i = 10;
		while(i >= 2)
		{
			System.out.print(i*i + " ");
			i -= 2;
		}
	}
}
```

<div style='page-break-after: always;'></div>

![[Hochschule/Module/OOP Einführung/Übung/OOPE_Abgabe_03.excalidraw.md#^area=GKGbhvscYWy30l_OQAna8|100%]]

```java
public class Main {
	public static void main(String[] args) {
		int n = 0, i = 1;
		while(i < 8)
		{
			n += i;
			i += 2;
		}
		System.out.println(n);
	}
}
```

```output
16
```

| i   | n   |
| --- | --- |
| 1   | 0   |
| 3   | 1   |
| 5   | 4   |
| 7   | 9   |
| 9   | 16  |

$n=16$

<div style='page-break-after: always;'></div>

![[Hochschule/Module/OOP Einführung/Übung/OOPE_Abgabe_03.excalidraw.md#^area=SfOlyvgiNzqQPXrW2IpNd|100%]]

```java
public class Main {
	public static void main(String[] args) {
		int n = 0, jahr = 1980;
		while(jahr <= 1989)
		{
			if(jahr % 4 == 0)
			{
				n++;
			}
			jahr++;;
		}
		System.out.println(n);
	}
}
```

```output
3
```

| jahr | n   |
| ---- | --- |
| 1980 | 0   |
| 1981 | 1   |
| 1982 | 1   |
| 1983 | 1   |
| 1984 | 1   |
| 1985 | 2   |
| 1986 | 2   |
| 1987 | 2   |
| 1988 | 2   |
| 1989 | 3   |
| 1990 | 3   |

$n=3$

<div style='page-break-after: always;'></div>

![[Hochschule/Module/OOP Einführung/Übung/OOPE_Abgabe_03.excalidraw.md#^area=zQKLsNDFPGcIYm43OnX3N|100%]]

```java
public class Main {
	public static void main(String[] args) {
		int i = 5;
		do
		{
			System.out.print(i*i + " ");
			i--;
		}
		while(i > 0);
	}
}
```

```output
25 16 9 4 1
```

| i   | print() |
| --- | ------- |
| 5   |         |
| 4   | 25      |
| 3   | 16      |
| 2   | 9       |
| 1   | 4       |
| 0   | 1       |

$\text{ print(): 25 16 9 4 1}$

<div style='page-break-after: always;'></div>

![[Hochschule/Module/OOP Einführung/Übung/OOPE_Abgabe_03.excalidraw.md#^area=tjJ3qHqdXQMXBYRzinl_5|100%]]

```java
public class Main {
	public static void main(String[] args) {
		int i = 5;
		do
		{
			i--;
			System.out.print(i*i + " ");
		}
		while(i > 0);
	}
}
```

```output
16 9 4 1 0
```

| i   | print() |
| --- | ------- |
| 5   |         |
| 4   | 16      |
| 3   | 9       |
| 2   | 4       |
| 1   | 1       |
| 0   | 0       |

$\text{ print(): 16 9 4 1 0}$

<div style='page-break-after: always;'></div>

![[Hochschule/Module/OOP Einführung/Übung/OOPE_Abgabe_03.excalidraw.md#^area=Q4pRYpjyxNIgoJ0c22-KJ|100%]]

a)

```java
public class Main {
	public static void main(String[] args) {
		int i = 1;
		while(i <= 5);  // ";" gehört hier nicht hin
		{
			System.out.println(i);
			i++;
		}
	}
}
```

b)

```java
public class Main {
	public static void main(String[] args) {
		int i = 9;
		do
		// "{"
			System.out.println(i);
			i--;
		// "}", der Bereich muss in geschweifte Klammern gesetzt werden
		while(i > 0);
	}
}
```

<div style='page-break-after: always;'></div>

![[Hochschule/Module/OOP Einführung/Übung/OOPE_Abgabe_03.excalidraw.md#^area=IlgvPhOtsCtd71ZXTIoXg|100%]]

```java
public class Main {
	public static void main(String[] args) {
		int sum = 0, i = 1;
		while(i <= 10)
		{
			if(i % 2 == 0)
				sum += i;
			i++;
		}
		System.out.println(sum);
	}
}
```

```output
30
```

<div style='page-break-after: always;'></div>

![[Hochschule/Module/OOP Einführung/Übung/OOPE_Abgabe_03.excalidraw.md#^area=G6t6W_ZY3ALezucLAnJBe|100%]]

```java
public class Main {
	public static void main(String[] args) {
		int fact = 1, i = 1;
		do
		{
			fact *=i;
			i++;
		} while(i < 6);
		System.out.println(fact);
	}
}
```

```output
120
```

<div style='page-break-after: always;'></div>

![[Hochschule/Module/OOP Einführung/Übung/OOPE_Abgabe_03.excalidraw.md#^area=xRUbBCZC2rZg21obrrxAc|100%]]

```java
public class Main {
	public static void main(String[] args) {
		int i = 10;
		while(i <= 100)
		{
			System.out.println(i);
			i++;
		}
	}
}
```

<div style='page-break-after: always;'></div>

![[Hochschule/Module/OOP Einführung/Übung/OOPE_Abgabe_03.excalidraw.md#^area=hWXIj9At0VYvNBtlZ0hIY|100%]]

```java
public class Main {
	public static void main(String[] args) {
		int i = 10, wert = 250;
		while(wert > 0)
		{
			wert -= i*i;
			i--;
		}
		System.out.println(i);

		i = 10; wert = 250;
		do
		{
			wert -= i*i;
			i--;
		} while(wert > 0);
		System.out.println(i);
	}
}
```

<div style='page-break-after: always;'></div>

![[Hochschule/Module/OOP Einführung/Übung/OOPE_Abgabe_03.excalidraw.md#^area=EowFPeyJYjv4fqr6GKs1-|100%]]

a)

```java
public class Main {
	public static void main(String[] args) {
		int i = 1;
		while(i <= 8)
		{
			System.out.print(i +  " ");
			i += 2;
		}
	}
}
```

```output
1 3 5 7
```

b)

```java
public class Main {
	public static void main(String[] args) {
		int i = 4, k;
		do
		{
			k = 2*i;
			System.out.print(k + " ");
			i--;
		} while (i >= 0);
	}
}
```

```output
8 6 4 2 0
```

<div style='page-break-after: always;'></div>

![[Hochschule/Module/OOP Einführung/Übung/OOPE_Abgabe_03.excalidraw.md#^area=7MR0bLkkhmbqFY_QaKkd3|100%]]

```java
public class Main {
	public static void main(String[] args) {
		int n = 0, i = 5;
		while(i > 0)
		{
			n += 2*i;
			i--;
		}
		System.out.println(n);
	}
}
```

```output
30
```

| i   | n   |
| --- | --- |
| 5   | 0   |
| 4   | 10  |
| 3   | 18  |
| 2   | 24  |
| 1   | 28  |
| 0   | 30  |

$n=30$

<div style='page-break-after: always;'></div>

![[Hochschule/Module/OOP Einführung/Übung/OOPE_Abgabe_03.excalidraw.md#^area=vUEHb1-52bN_LbQkeOC4k|100%]]

```java
public class Main {
	public static void main(String[] args) {
		int n = 0, i = 1;
		do
		{
			n += 10;
			i++;
		} while(i <= 5);
		System.out.println(n);
	}
}
```

```output
50
```

| i   | n   |
| --- | --- |
| 1   | 0   |
| 2   | 10  |
| 3   | 20  |
| 4   | 30  |
| 5   | 40  |
| 6   | 50  |

$n=50$

<div style='page-break-after: always;'></div>

![[Hochschule/Module/OOP Einführung/Übung/OOPE_Abgabe_03.excalidraw.md#^area=8kkwn8R8jVRY0cd2WZOQ0|100%]]

a)

```java
public class Main {
	public static void main(String[] args) {
		int t = 6;
		while(t > 3)
		{
			System.out.println(t);
			t--;
		}
		System.out.println(t);
	}
}
```

```output
6
5
4
3
```

b)

```java
public class Main {
	public static void main(String[] args) {
		int t = 6;
		do
		{
			System.out.println(t);
			t--;
		} while(t > 3);
		System.out.println(t);
	}
}
```

```output
6
5
4
3
```

<div style='page-break-after: always;'></div>

![[Hochschule/Module/OOP Einführung/Übung/OOPE_Abgabe_03.excalidraw.md#^area=bB7NwPrzeiIp1QIr_szhy|100%]]

a)

```java
public class Main {
	public static void main(String[] args) {
		int sum = 0, i = 2;
		while(i <= 20) // inklusive 20
		{
			if(i % 2 == 0)
				sum += i;
			i++;
		}
		System.out.println(sum);
	}
}
```

```output
110
```

b)

```java
public class Main {
	public static void main(String[] args) {
		int sum = 0, i = 1;
		do
		{
			sum += i;
			i++;
		} while(sum <= 500);
		System.out.println(sum);
	}
}
```

```output
528
```

c)

```java
public class Main {
	public static void main(String[] args) {
		int n = 10;
		while(n > 0)
		{
			if(n % 2 == 0)
				System.out.println(n*n);
			n--;
		}
	}
}
```

```output
100
64
36
16
4
```

<div style='page-break-after: always;'></div>

![[Hochschule/Module/OOP Einführung/Übung/OOPE_Abgabe_03.excalidraw.md#^area=xu6uG1VadOnMMsefP-iOG|100%]]

a)

```java
public class Main {
	public static void main(String[] args) {
		int i = 14;
		while(i <= 22)
		{
			System.out.print(i + " ");
			i += 2;
		}
	}
}
```

```output
14 16 18 20 22
```

b)

```java
public class Main {
	public static void main(String[] args) {
		int i = 7;
		while(i <= 11)
		{
			System.out.print(2*i + " ");
			i++;
		}
	}
}
```

```output
14 16 18 20 22
```

<div style='page-break-after: always;'></div>

![[Hochschule/Module/OOP Einführung/Übung/OOPE_Abgabe_03.excalidraw.md#^area=veREOxgkCQnoNXZQHhXVM|100%]]

a)

```java
public class Main {
	public static void main(String[] args) {
		boolean stop = false;
		int i;
		while(stop = false)
		{
			i = TastaturEingabe.readInt("i: ");
			if(i != 7)
				System.out.println(i*i);
			else
				stop = true;
		}
	}
}
```

Die Schleife wird so lange iteriert, bis eine $7$ eingegeben wird.
Jede Iteration wird die Quadratzahl von $i$ ausgegeben.

b)

```java
public class Main {
	public static void main(String[] args) {
		int i = 10;
		while(i > 0)
		{
			System.out.print(i);
			i++;
		}
	}
}
```

Endlosscheife, da $i$ größer $0$ ist und inkrementiert wird.
Jede Iteration wird der aktuelle Wert von $i$ erhöht wird.

<div style='page-break-after: always;'></div>

![[Hochschule/Module/OOP Einführung/Übung/OOPE_Abgabe_03.excalidraw.md#^area=MpGbxyn8NEu7C9Aoy0KYm|100%]]

```java
public class Main {
	public static void main(String[] args) {
		int i = 10;
		while(i >= 1)
		{
			System.out.print(i + " ");
			i--;
		}
	}
}
```

```java
public class Main {
	public static void main(String[] args) {
		for(int i = 10; i >= 1; i--)
		{
			System.out.print(i + " ");
		}
	}
}
```

![[Hochschule/Module/OOP Einführung/Übung/OOPE_Abgabe_03.excalidraw.md#^area=I9arScHkD-1a5or7Wiile|100%]]

```java
public class Main {
	public static void main(String[] args) {
		for(int i = 1; i < 10; i++)
		{
			System.out.println(i+5);
		}
	}
}
```

```java
public class Main {
	public static void main(String[] args) {
		int i = 1;
		while(i < 10)
		{
			System.out.println(i+5);
			i++;
		}
	}
}
```

<div style='page-break-after: always;'></div>

![[Hochschule/Module/OOP Einführung/Übung/OOPE_Abgabe_03.excalidraw.md#^area=TYsKoQthP-7ApWgg197Fz|100%]]

```java
public class Main {
	public static void main(String[] args) {
		int i = 1, sum = 0;
		while(i <= 15)
		{
			sum += i;
			i += 2;
		}
		System.out.println(sum);
	}
}
```

```java
public class Main {
	public static void main(String[] args) {
		int sum = 0;
		for(int i = 1; i <= 15; i += 2)
		{
			sum += i;
		}
		System.out.println(sum);
	}
}
```

<div style='page-break-after: always;'></div>

![[Hochschule/Module/OOP Einführung/Übung/OOPE_Abgabe_03.excalidraw.md#^area=1dH7ux_G36e6qLNA_EwdB|100%]]

a)

```java
public class Main {
	public static void main(String[] args) {
		for(int i = 1; i < 5; i++)
		{
			System.out.println(i*10);
		}
	}
}
```

```output
10
20
30
40
```

| i   | print() |
| --- | ------- |
| 1   | 10      |
| 2   | 20      |
| 3   | 30      |
| 4   | 40      |

b)

```java
public class Main {
	public static void main(String[] args) {
		for(int i = 5; i > 0; i--)
		{
			System.out.println(i*i);
		}
	}
}
```

```output
25
16
9
4
1
```

| i   | print() |
| --- | ------- |
| 5   | 25      |
| 4   | 16      |
| 3   | 9       |
| 2   | 4       |
| 1   | 1       |

<div style='page-break-after: always;'></div>

![[Hochschule/Module/OOP Einführung/Übung/OOPE_Abgabe_03.excalidraw.md#^area=NETokH7H2tih1WRpz3tGh|100%]]

a)

```java
public class Main {
	public static void main(String[] args) {
		int count = 0;
		for(int i = 1; i <= 5; i++)
		{
			for(int j = 1; j <= 3; j++)
			{
				count++;
			}
		}
	}
}
```

| i   | j   | count |
| --- | --- | ----- |
| 1   | 1   | 1     |
| 1   | 2   | 2     |
| 1   | 3   | 3     |
| 2   | 1   | 4     |
| 2   | 2   | 5     |
| 2   | 3   | 6     |
| 3   | 1   | 7     |
| 3   | 2   | 8     |
| 3   | 3   | 9     |
| 4   | 1   | 10    |
| 4   | 2   | 11    |
| 4   | 3   | 12    |
| 5   | 1   | 13    |
| 5   | 2   | 14    |
| 5   | 3   | 15    |

$count=15$

b)

```java
public class Main {
	public static void main(String[] args) {
		int count = 0;
		for(int i = 1; i <= 3; i++)
		{
			for(int j = 0; j < i; j++)
			{
				count++;
			}
		}
	}
}
```

| i   | j   | count |
| --- | --- | ----- |
| 1   | 0   | 1     |
| 2   | 0   | 2     |
| 2   | 1   | 3     |
| 3   | 0   | 4     |
| 3   | 1   | 5     |
| 3   | 2   | 6     |

$count=6$

<div style='page-break-after: always;'></div>

![[Hochschule/Module/OOP Einführung/Übung/OOPE_Abgabe_03.excalidraw.md#^area=UhpPv__bGZK7HERdH3wTA|100%]]

```java
public class Main {
	public static void main(String[] args) {
		int i, j;
		for(i = 1, j = 5; i + 2*j > 9; i++, j--)
		{
			System.out.println(2*i + 3*j);
		}
	}
}
```

```output
17
16
```

<div style='page-break-after: always;'></div>

![[Hochschule/Module/OOP Einführung/Übung/OOPE_Abgabe_03.excalidraw.md#^area=PvYYn3WRlaBcCIx7ExeUg|100%]]

a)

```java
public class Main {
	public static void main(String[] args)
	{
		for(int i = 1; i <= 5; i++)
			System.out.println(i);
	}
}
```

Kein Fehler vorhanden.

b)

```java
public class Main {
	public static void main(String[] args)
	{
		for(int i = 10; i > 0; i++)
			System.out.println(i);
	}
}
```

Endlosschleife, da $i > 0$ ist und inkrementiert wird.

<div style='page-break-after: always;'></div>

![[Hochschule/Module/OOP Einführung/Übung/OOPE_Abgabe_03.excalidraw.md#^area=ORsuzZv-o31MYGmkU0niP|100%]]

```java
public class Main {
	public static void main(String[] args) {
		for(int n = 5; n < 25; n++)
		{
			System.out.println(n);
			n = TastaturEingabe.readInt("n: ");
		}
	}
}
```

```output
5
11
23
7
24
```

<div style='page-break-after: always;'></div>

![[Hochschule/Module/OOP Einführung/Übung/OOPE_Abgabe_03.excalidraw.md#^area=eGOZejg-oWZdCijRdpcfZ|100%]]

```java
import utilities.TastaturEingabe;

public class loop27 {
	public static void main(String[] args) {
		long n, p;

		n = TastaturEingabe.readLong("Bitte eine ganze Zahl eingeben: ");
		for(int p = 1; p < n; p*=2)
			System.out.print(p + " ");
		System.out.println();
	}
}
```

a)
$n=40$

```output
1 2 4 8 16 32
```

b)
$n=50$

```output
1 2 4 8 16 32
```

c)
$n=100$

```output
1 2 4 8 16 32 64
```

Das Programm gibt alle Zweierpotenzen aus, welche kleiner sind als das Eingegebene $n$.

<div style='page-break-after: always;'></div>

![[Hochschule/Module/OOP Einführung/Übung/OOPE_Abgabe_03.excalidraw.md#^area=3WBSp8fFghTDmyNVyWcx8|100%]]

a)

```java
public class Main {
	public static void main(String[] args) {
		for(int i = 1; i <= 3; i++)
			for(int j = 1; j < 5; j++)
				System.out.print('*');
	}
}
```

b)

```java
public class Main {
	public static void main(String[] args) {
		for(int i = 3; i < 5; i++)
			for(int j = 6; j > 0; j--)
				System.out.print('*');
	}
}
```

c)

```java
public class Main {
	public static void main(String[] args) {
		for(int i = 1; i < 8; i += 2)
			for(int j = 2; j < 9; j += 3)
				System.out.print('*');
	}
}
```

<div style='page-break-after: always;'></div>

![[Hochschule/Module/OOP Einführung/Übung/OOPE_Abgabe_03.excalidraw.md#^area=1h7HXLIZZxKGbZovCbN8n|100%]]

a)

```java
public class Main {
	public static void main(String[] args) {
		int i, j, k;
		i = 0;
		while(i <= 10)
		{
			j = 1;
			while(j < i)
			{
				System.out.print('*');
				j++;
			}
			i++;
		}
	}
}
```

```output
45 '*' ausgegeben.
```

b)

```java
public class Main {
	public static void main(String[] args) {
		int i, j, k;
		for(i = 0; i < 3; i++)
			for(j = 0; j < 3; j++)
				for(k = 0; k < 2; k++)
					System.out.print('*');
	}
}
```

```output
18 '*' ausgegeben.
```

<div style='page-break-after: always;'></div>

![[Hochschule/Module/OOP Einführung/Übung/OOPE_Abgabe_03.excalidraw.md#^area=4PfGWxvpxv4GOboA2v7c0|100%]]

a)

```java
public class Main {
	public static void main(String[] args) {
		int i, j, k, sum;
		for(sum = 0, i = 0, k = 8; i < k; i++, k--)
			sum += 2*i + k;
		System.out.println(sum);
	}
}
```

```output
38
```

b)

```java
public class Main {
	public static void main(String[] args) {
		int i, j, k, sum;
		for(i = 0, j = 1; i*j < 100; i++, j *= 10)
			System.out.println(i * j);
	}
}
```

```output
0
10
```

<div style='page-break-after: always;'></div>

![[Hochschule/Module/OOP Einführung/Übung/OOPE_Abgabe_03.excalidraw.md#^area=YBuBRy7YCb8DjuEvG8cmA|100%]]

```java
public class Main {
	public static void main(String[] args) {
		int i, n;
		n = TastaturEingabe.readInt("n: ");

		for(i = 1; i < 10; i++)
		{
			if(i % 4 == 0)
				continue;
			else if(i == n)
				break;
			else
				System.out.println(i + " ");
		}
	}
}
```

a)
$n=7$

```output
1
2
3
5
6
```

b)
$n=4$

```output
1
2
3
5
6
7
9
```

c)
$n=9$

```output
1
2
3
5
6
7
```

<div style='page-break-after: always;'></div>

![[Hochschule/Module/OOP Einführung/Übung/OOPE_Abgabe_03.excalidraw.md#^area=4rlasPxyirDAmBIG2gGr-|100%]]

```java
public class Main {
	public static void main(String[] args) {
		int i = 0, sum = 0;

		while(i < 8)
		{
			if(i % 2 == 1)
			{
				i++;
				continue;
			}
			else
			{
				sum += i;
				i++;
			}
		}
		System.out.println(sum);
	}
}
```

```output
12
```

<div style='page-break-after: always;'></div>

![[Hochschule/Module/OOP Einführung/Übung/OOPE_Abgabe_03.excalidraw.md#^area=ocnoz0-BQxVapkEc6xgxo|100%]]

```java
public class Main {
	public static void main(String[] args) {
		i = 0;
		while(i < 10)
		{
			n = TastaturEingabe.readInt("n: ");
			if(n == 6)
				break;
			if(n % 3 == 0)
				continue;
			if(n < 8)
			{
				System.out.println(n*n);
			}
			else
			{
				System.out.println(n);
			}
			i++;
		}
	}
}
```
