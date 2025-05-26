![[LA_Aufgabensammlung_01.excalidraw#^area=2Uva_pmhP2g4BZdk1jRlm|100%]]

#### **Zu zeigen:**

1. $v + w \in \text{Span}(v_1, \dots, v_m)$
2. $\lambda v \in \text{Span}(v_1, \dots, v_m)$

---

### **Beweis:**

Da $v, w \in \text{Span}(v_1, \dots, v_m)$, gibt es Skalare $a_1, \dots, a_m \in \mathbb{R}$ und $b_1, \dots, b_m \in \mathbb{R}$, sodass:
$v = a_1 v_1 + a_2 v_2 + \dots + a_m v_m$
$w = b_1 v_1 + b_2 v_2 + \dots + b_m v_m$

---

**1. Additivität:**

$v + w = (a_1 + b_1)v_1 + (a_2 + b_2)v_2 + \dots + (a_m + b_m)v_m$
$\to$ Linearkombination von $v_1, \dots, v_m$ $\to$ also $v + w \in \text{Span}(v_1, \dots, v_m)$

---

**2. Skalarmultiplikation:**

$\lambda_{v} = \lambda (a_1 v_1 + \dots + a_m v_m) = (\lambda_{a_1}) v_1 + \dots + (\lambda_{a_m}) v_m$

$\to$ ebenfalls Linearkombination von $v_1, \dots, v_m$ $\to$ also $\lambda_{v} \in \text{Span}(v_1, \dots, v_m)$

---

Der Spann ist abgeschlossen unter Addition und Skalarmultiplikation $\to$ **ein Untervektorraum**.
Die Aussage ist damit bewiesen.

### **q.e.d.**
