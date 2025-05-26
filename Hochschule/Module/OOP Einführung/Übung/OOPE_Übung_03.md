![[OOPE_Übung_03.excalidraw#^area=IUc-mO5jwDVnOuFVEyv37|100%]]

a)

```java
public class Main {
	public static void main(String[] args) {
		String output = "";

		for(int i = 1;i < 10;i++)
		{
			output += i;
			System.out.println(output);
		}
	}
}
```

b)

```java
public class Main {
	public static void main(String[] args) {
		String output = "";

		for(int i = 1;i < 10;i++)
		{
			output += i;
			System.out.println(String.format(" ".repeat(9-output.length()) + output));
		}
	}
}
```

<div style='page-break-after: always;'></div>

![[OOPE_Übung_03.excalidraw#^area=Oj-3nZQfTSSHIvmcH9d5T|100%]]

a)

```java
public class Main {
	public static void main(String[] args) {
		long zahl = 523453982L;

		String binaer_zahl = Long.toBinaryString(zahl);
		int n = binaer_zahl.replace("0", "").length();
		System.out.println("Die Zahl " + zahl + " hat " + n + " 1en.");
	}
}
```

b)

```java
public class Main {
	public static void main(String[] args) {
		long zahl = 523453982L;

		String binaer_zahl = Long.toBinaryString(zahl);
		int n = binaer_zahl.replace("1", "").length();
		System.out.println("Die Zahl " + zahl + " hat " + n + " 0en.");
	}
}
```

<div style='page-break-after: always;'></div>

![[OOPE_Übung_03.excalidraw#^area=Ejb7A3w9WtZR0_rfu7rMg|100%]]

a)

```java
public class Main {
	public static void main(String[] args) {
		String string_zahl = "590522";

		int zahl = Integer.parseInt(string_zahl);

		System.out.println(zahl);
	}
}
```

b)

```java
public class Main {
	public static void main(String[] args) {
		String string_zahl = "101111";
		String string_basis = "2";

		int zahl = 0;
		int basis = Integer.parseInt(string_basis);

		for(int i = 0; i < string_zahl.length(); i++)
		{
			zahl += Math.pow(basis, i) * (string_zahl.charAt(string_zahl.length() - i - 1) - '0');
		}

		System.out.println(zahl);
	}
}
```
