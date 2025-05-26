[

// Custom Stuff

    {trigger: "pagebreak", replacement: "<div style='page-break-after: always;'></div>\n", options: "tA"},
    {trigger: "linebreak", replacement: "<br>", options: "tA"},
    {trigger: "tablepipe", replacement: "│", options: "tmA"},

// Modes

    // Math mode
    {trigger: "mk", replacement: "$$0$", options: "t"},
    {trigger: "dm", replacement: "$$\n$0\n$$", options: "t"},

    // Code mode
    {trigger: "cb", replacement: "```$0\n```", options: "t"},
    {trigger: "codejava", replacement: "```java\npublic class Main {\n\tpublic static void main(String[] args) {\n\t\t$0\n\t}\n}\n\`\`\`", options: "tA"},
    {trigger: "codepy", replacement: "```python\n$0\n\`\`\`", options: "tA"},
        {trigger: "codeout", replacement: "```output\n$0\n\`\`\`", options: "tA"},

// Coding Blocks

    // Shortcuts
    {trigger: "sysout", replacement: "System.out.println(\"$0\");$1", options: "cA"},
    {trigger: "if", replacement: "if($0)\n\t\t{\t\t\t$1\n\t\t}", options: "cA"},
    {trigger: "\"", replacement: "\"$0\"$1", options: "cA"},
    {trigger: "\'", replacement: "\'$0\'$1", options: "cA"},
    {trigger: "switch", replacement: "switch($0)\n\t\t{\n\t\t\t$1\n\t\t}", options: "cA"},
    {trigger: "for", replacement: "for(int $0 = $1; $0 < $2; $0++)\n\t\t{\n\t\t\t$3\n\t\t}", options: "cA"},
    {trigger: "while", replacement: "while($0)\n\t\t{\n\t\t\t$1\n\t\t}", options: "cA"},

// Environments

    // Text environment
    {trigger: "(text|note|txt)", replacement: "\\text{ $0 }$1", options: "rmA"},
    {trigger: "sts", replacement: "_\\text{$0}", options: "mA"},

    // Math environments
    {trigger: "pmat", replacement: "\\begin{pmatrix}\n$0\n\\end{pmatrix}", options: "MA"},
    {trigger: "bmat", replacement: "\\begin{bmatrix}\n$0\n\\end{bmatrix}", options: "MA"},
    {trigger: "Bmat", replacement: "\\begin{Bmatrix}\n$0\n\\end{Bmatrix}", options: "MA"},
    {trigger: "vmat", replacement: "\\begin{vmatrix}\n$0\n\\end{vmatrix}", options: "MA"},
    {trigger: "Vmat", replacement: "\\begin{Vmatrix}\n$0\n\\end{Vmatrix}", options: "MA"},
    {trigger: "matrix", replacement: "\\begin{matrix}\n$0\n\\end{matrix}", options: "MA"},

    {trigger: "nl", replacement: "&\\\\", options: "MA"},

    {trigger: "pmat", replacement: "\\begin{pmatrix}$0\\end{pmatrix}", options: "nA"},
    {trigger: "bmat", replacement: "\\begin{bmatrix}$0\\end{bmatrix}", options: "nA"},
    {trigger: "Bmat", replacement: "\\begin{Bmatrix}$0\\end{Bmatrix}", options: "nA"},
    {trigger: "vmat", replacement: "\\begin{vmatrix}$0\\end{vmatrix}", options: "nA"},
    {trigger: "Vmat", replacement: "\\begin{Vmatrix}$0\\end{Vmatrix}", options: "nA"},
    {trigger: "matrix", replacement: "\\begin{matrix}$0\\end{matrix}", options: "nA"},

    {trigger: "cases", replacement: "\\begin{cases}\n$0\n\\end{cases}", options: "MA"},
    {trigger: "cases", replacement: "\\begin{cases}$0\\end{cases}$1", options: "mA"},
    {trigger: "align", replacement: "\\begin{align}\n$0\n\\end{align}", options: "MA"},
    {trigger: "array", replacement: "\\begin{array}\n$0\n\\end{array}", options: "MA"},
    {trigger: "beg", replacement: "\\begin{$0}\n$1\n\\end{$0}", options: "MA"},
    {trigger: "rbeg", replacement: "\\begin{align*}\n&$0\\\\\n\\end{align*}", options: "MA"},
    {trigger: "lbeg", replacement: "\\begin{flalign*}\n&$0\\\\\n\\end{flalign*}", options: "MA"},

// Symbols

    // Greek letters
    {trigger: "\\$(${GREEK})", replacement: "$\\[[0]]", options: "rmA"},
    {trigger: "\\s(${GREEK})", replacement: "\\[[0]]", options: "rmA"},

        // Automatically convert Greek letters in text to math.
        {trigger: "(${GREEK})([\\n\\s.,?!:'])", replacement: "$\\[[0]]$[[1]]", options: "rtAw"},


    // Sets
    {trigger: "GG", replacement: "\\mathbb{G}", options: "mA"},
    {trigger: "LL", replacement: "\\mathbb{L}", options: "mA"},
    {trigger: "PP", replacement: "\\mathbb{P}", options: "mA"},
    {trigger: "NN", replacement: "\\mathbb{N}", options: "mA"},
    {trigger: "ZZ", replacement: "\\mathbb{Z}", options: "mA"},
    {trigger: "FF", replacement: "\\mathbb{F}", options: "mA"},
    {trigger: "QQ", replacement: "\\mathbb{Q}", options: "mA"},
    {trigger: "Q+", replacement: "\\mathbb{Q}^+", options: "mA"},
    {trigger: "II", replacement: "\\mathbb{I}", options: "mA"},
    {trigger: "AA", replacement: "\\mathbb{A}", options: "mA"},
    {trigger: "TT", replacement: "\\mathbb{T}", options: "mA"},
    {trigger: "RR", replacement: "\\mathbb{R}", options: "mA"},
    {trigger: "*R", replacement: "{}^*\\mathbb{R}", options: "mA"},
    {trigger: "CC", replacement: "\\mathbb{C}", options: "mA"},
    {trigger: "HH", replacement: "\\mathbb{H}", options: "mA"},
    {trigger: "OO", replacement: "\\mathbb{O}", options: "mA"},
    {trigger: "SS", replacement: "\\mathbb{S}", options: "mA"},
    {trigger: "KK", replacement: "\\mathbb{K}", options: "mA"},

    // Math Symbols
        // Basic operations
        {trigger: "(ooo|infi)", replacement: "\\infty", options: "rmA"},
        {trigger: "sum", replacement: "\\sum_{${0:i}=${1:1}}^{${2:N}} $3", options: "mA"},
        {trigger: "prod", replacement: "\\prod_{${0:i}=${1:1}}^{${2:N}} $3", options: "mA"},
        {trigger: "lim", replacement: "\\lim_{ ${0:n} \\to ${1:\\infty} } $2", options: "mA"},

    	{trigger: "(°|rd)", replacement: "^{$0}$1", options: "rmA"},
        {trigger: "_", replacement: "_{$0}$1", options: "mA"},
        {trigger: "sq", replacement: "\\sqrt{ $0 }$1", options: "mA"},
        {trigger: "//", replacement: "\\frac{$0}{$1}$2", options: "mA"},
        {trigger: "invs", replacement: "^{-1}", options: "mA"},

        {trigger: /([^\\])(exp|log|ln)/, replacement: "[[0]]\\[[1]]", options: "rmA"},
        {trigger: "conj", replacement: "^{*}", options: "mA"},
        {trigger: "Re", replacement: "\\mathrm{Re}", options: "mA"},
        {trigger: "Im", replacement: "\\mathrm{Im}", options: "mA"},

        // Linear algebra
        {trigger: /([^\\])(det)/, replacement: "[[0]]\\[[1]]", options: "rmA"},
        {trigger: "trace", replacement: "\\mathrm{Tr}", options: "mA"},

    	    // N Matrix
    	    {trigger: /genv(\d+)/, replacement: (match) => {
    	    	const n = match[1];
    	    	if (n>25) n=25;

    	    	let arr = [];
    	    	for (let j = 0; j < n; j++) {
    	    		arr[j] = [1];
    	    	}

    	    	let output = arr.map(el => el.join(" & ")).join(" \\\\\n");
    	    	output = `\\begin{pmatrix}\n${output}\n\\end{pmatrix}`;
    	    	return output;
    	    }, options: "M"},

    		// M x N Matrix
    	    {trigger: /genm(\d+)x(\d+)/, replacement: (match) => {
    			const m = match[1];
    			const n = match[2];
    		    if (m>25) m=25;
    		    if (n>25) n=25;

    	    	let arr = [];
    	    	for (let j = 0; j < m; j++) {
    	    		arr[j] = [];
    	    		for (let i = 0; i < n; i++) {
    	    			arr[j][i] = 1;
    	    		}
    	    	}

    	    	let output = arr.map(el => el.join(" & ")).join(" \\\\\n");
    	    	output = `\\begin{pmatrix}\n${output}\n\\end{pmatrix}`;
    	    	return output;
    	    }, options: "M", description: "M x N", priority: 1},

    		// N x N Matrix
    	    {trigger: /genm(\d+)/, replacement: (match) => {
    			const n = match[1];
    		    if (n>25) n=25;

    	    	let arr = [];
    	    	for (let j = 0; j < n; j++) {
    	    		arr[j] = [];
    	    		for (let i = 0; i < n; i++) {
    	    			arr[j][i] = (i === j) ? 1 : 0;
    	    		}
    	    	}

    	    	let output = arr.map(el => el.join(" & ")).join(" \\\\\n");
    	    	output = `\\begin{pmatrix}\n${output}\n\\end{pmatrix}`;
    	    	return output;
    	    }, options: "M", description: "N x N identity matrix", priority: 1},


        // Trigonometry
        {trigger: /([^\\])(arcsin|sin|arccos|cos|arctan|tan|csc|sec|cot)/, replacement: "[[0]]\\[[1]]", options: "rmA"},
        {trigger: /\\(arcsin|sin|arccos|cos|arctan|tan|csc|sec|cot)([A-Za-gi-z])/, replacement: "\\[[0]] [[1]]", options: "rmA"},
        {trigger: /\\(sinh|cosh|tanh|coth)([A-Za-z])/, replacement: "\\[[0]] [[1]]", options: "rmA"},

        // Derivatives and integrals
        {trigger: "par", replacement: "\\frac{ \\partial ${0:y} }{ \\partial ${1:x} } $2", options: "m"},
        {trigger: /pa([A-Za-z])([A-Za-z])/, replacement: "\\frac{ \\partial [[0]] }{ \\partial [[1]] } ", options: "rm"},
        {trigger: "ddt", replacement: "\\frac{d}{dt} ", options: "mA"},

        {trigger: /([^\\])int/, replacement: "[[0]]\\int", options: "mA", priority: -1},
        {trigger: "\\int", replacement: "\\int $0 \\, d${1:x} $2", options: "m"},
        {trigger: "dint", replacement: "\\int_{${0:0}}^{${1:1}} $2 \\, d${3:x} $4", options: "mA"},
        {trigger: "oint", replacement: "\\oint", options: "mA"},
        {trigger: "iint", replacement: "\\iint", options: "mA"},
        {trigger: "iiint", replacement: "\\iiint", options: "mA"},
        {trigger: "oinf", replacement: "\\int_{0}^{\\infty} $0 \\, d${1:x} $2", options: "mA"},
        {trigger: "infi", replacement: "\\int_{-\\infty}^{\\infty} $0 \\, d${1:x} $2", options: "mA"},

        // More Symbols
        {trigger: "+-", replacement: "\\pm", options: "mA"},
        {trigger: "-+", replacement: "\\mp", options: "mA"},
        {trigger: "...", replacement: "\\dots", options: "mA"},
        {trigger: "(nabl)", replacement: "\\nabla", options: "rmA"},
        {trigger: "xx", replacement: "\\times", options: "mA"},
        {trigger: "(cdot)", replacement: " \\cdot $0", options: "rmA"},
        {trigger: "(//|div)", replacement: " \\div $0", options: "rmA"},
        {trigger: "para", replacement: "\\parallel", options: "mA"},
        {trigger: "perp", replacement: "\\perp", options: "mA"},
        {trigger: "kgv", replacement: "\\sqcup", options: "mA"},
        {trigger: "ggt", replacement: "\\sqcap", options: "mA"},

    // Logic Notation
    {trigger: "forall", replacement: "\\forall", options: "mA"},
    {trigger: "exists", replacement: "\\exists", options: "mA"},
    {trigger: "existone", replacement: "\\exists!", options: "mA"},
    {trigger: "nexists", replacement: "\\nexists", options: "mA"},
    {trigger: "(lightning|wider)", replacement: "↯", options: "rmA"},
    {trigger: "(blacksquare|qed)", replacement: "\\blacksquare", options: "rmA"},

        // Arrows
        {trigger: "<->", replacement: "\\leftrightarrow ", options: "mA"},
        {trigger: "(<>=|=<>|equal)", replacement: "\\Leftrightarrow ", options: "rmA"},
        {trigger: "->", replacement: "\\to", options: "mA"},
        {trigger: "!>", replacement: "\\mapsto", options: "mA"},
        {trigger: "=>", replacement: "\\implies", options: "mA"},
        {trigger: "=<", replacement: "\\impliedby", options: "mA"},

    // More operations
    {trigger: "([a-zA-Z])hat", replacement: "\\hat{[[0]]}", options: "rmA"},
    {trigger: "([a-zA-Z])bar", replacement: "\\bar{[[0]]}", options: "rmA"},
    {trigger: "([a-zA-Z])dot", replacement: "\\dot{[[0]]}", options: "rmA", priority: -1},
    {trigger: "([a-zA-Z])ddot", replacement: "\\ddot{[[0]]}", options: "rmA", priority: 1},
    {trigger: "([a-zA-Z])tilde", replacement: "\\tilde{[[0]]}", options: "rmA"},
    {trigger: "([a-zA-Z]+)und", replacement: "\\underline{[[0]]}", options: "rmA"},
    {trigger: "([a-zA-Z]+)vec", replacement: "\\vec{[[0]]}", options: "rmA"},
    {trigger: "([a-zA-Z]),\\.", replacement: "\\mathbf{[[0]]}", options: "rmA"},
    {trigger: "([a-zA-Z])\\.,", replacement: "\\mathbf{[[0]]}", options: "rmA"},
    {trigger: "\\\\(${GREEK}),\\.", replacement: "\\boldsymbol{\\[[0]]}", options: "rmA"},
    {trigger: "\\\\(${GREEK})\\.,", replacement: "\\boldsymbol{\\[[0]]}", options: "rmA"},

    {trigger: "hat", replacement: "\\hat{$0}$1", options: "mA"},
    {trigger: "bar", replacement: "\\bar{$0}$1", options: "mA"},
    {trigger: "dot", replacement: "\\dot{$0}$1", options: "mA", priority: -1},
    {trigger: "ddot", replacement: "\\ddot{$0}$1", options: "mA"},
    {trigger: "tilde", replacement: "\\tilde{$0}$1", options: "mA"},
    {trigger: "und", replacement: "\\underline{$0}$1", options: "mA"},
    {trigger: "vec", replacement: "\\vec{$0}$1", options: "mA"},

// Operators

    // Logic Operators
    {trigger: "(and|land)", replacement: "\\land", options: "rmA"},
    {trigger: "(\\sor|lor)", replacement: "\\lor", options: "rmA"},
    {trigger: "(not|neg)", replacement: "\\neg", options: "rmA"},
    {trigger: "xor", replacement: "\\oplus", options: "rmA"},
    {trigger: "(true|top)", replacement: "\\top", options: "rmA"},
    {trigger: "(false|false)", replacement: "\\bot", options: "rmA"},

    // Relational Operators
    	// Math
    	{trigger: "(===|ident)", replacement: "\\equiv", options: "rmA"},
    	{trigger: "(~~|~=)", replacement: "\\approx", options: "rmA"},
    	{trigger: "(!=|neq)", replacement: "\\neq", options: "rmA"},
    	{trigger: "(>=|geq)", replacement: "\\geq", options: "rmA"},
    	{trigger: "(<=|leq)", replacement: "\\leq", options: "rmA"},

    	// Set Operators
        {trigger: "(And|cap)", replacement: "\\cap", options: "rmA"},
        {trigger: "(Or)", replacement: "\\cup", options: "rmA"},
        {trigger: "(without|minusset|ohne)", replacement: "\\setminus", options: "rmA"},
        {trigger: "(In)", replacement: "\\in", options: "rmA"},
        {trigger: "(Notin)", replacement: "\\not\\in", options: "rmA"},
        {trigger: "(sub=|subeq)", replacement: "\\subseteq", options: "rmA"},
        {trigger: "(sup=|supeq)", replacement: "\\supseteq", options: "rmA"},
        {trigger: "subin", replacement: "\\subset", options: "mA"},
        {trigger: "supin", replacement: "\\supset", options: "mA"},
        {trigger: "(eset|emptyset)", replacement: "\\emptyset", options: "rmA"},
        {trigger: "set", replacement: "\\{ $0 \\}$1", options: "mA"},

        // Mächtigkeiten
        {trigger: "#", replacement: "\\#", options: "mA"},
        {trigger: "vert", replacement: "\\vert$0\\vert$1", options: "mA"},
        {trigger: "dvert", replacement: "\\vert\\vert$0\\vert\\vert$1", options: "mA"},

// Brackets

    {trigger: "avg", replacement: "\\langle $0 \\rangle $1", options: "mA"},
    {trigger: "norm", replacement: "\\lvert $0 \\rvert $1", options: "mA", priority: 1},
    {trigger: "Norm", replacement: "\\lVert $0 \\rVert $1", options: "mA", priority: 1},
    {trigger: "ceil", replacement: "\\lceil $0 \\rceil $1", options: "mA"},
    {trigger: "floor", replacement: "\\lfloor $0 \\rfloor $1", options: "mA"},
    {trigger: "(", replacement: "(${VISUAL})", options: "mA"},
    {trigger: "[", replacement: "[${VISUAL}]", options: "mA"},
    {trigger: "{", replacement: "{${VISUAL}}", options: "mA"},
    {trigger: "(", replacement: "($0)$1", options: "mA"},
    {trigger: "{", replacement: "{$0}$1", options: "mA"},
    {trigger: "[", replacement: "[$0]$1", options: "mA"},
    {trigger: "lr(", replacement: "\\left( $0 \\right) $1", options: "mA"},
    {trigger: "lr{", replacement: "\\left\\{ $0 \\right\\} $1", options: "mA"},
    {trigger: "lr[", replacement: "\\left[ $0 \\right] $1", options: "mA"},
    {trigger: "lr|", replacement: "\\left| $0 \\right| $1", options: "mA"},
    {trigger: "lra", replacement: "\\left< $0 \\right> $1", options: "mA"},

// Visual operations

    {trigger: "U", replacement: "\\underbrace{ ${VISUAL} }_{ $0 }", options: "mA"},
    {trigger: "O", replacement: "\\overbrace{ ${VISUAL} }^{ $0 }", options: "mA"},
    {trigger: "B", replacement: "\\underset{ $0 }{ ${VISUAL} }", options: "mA"},
    {trigger: "C", replacement: "\\cancel{ ${VISUAL} }", options: "mA"},
    {trigger: "K", replacement: "\\cancelto{ $0 }{ ${VISUAL} }", options: "mA"},
    {trigger: "S", replacement: "\\sqrt{ ${VISUAL} }", options: "mA"},
    {trigger: "T", replacement: "\\text{ ${VISUAL}$0 }$1", options: "mA"},
    {trigger: "<", replacement: "<${VISUAL}>$0", options: "vmA"},
    {trigger: ">", replacement: "<${VISUAL}>$0", options: "vmA"},

// Subscriptions

// Misc

    // Automatically convert standalone letters in text to math (except a, A, I).
    {trigger: /([^'äüöÄÜÖß])\b([B-HJ-Zb-z])\b([\n\s.,?!:'])/, replacement: "[[0]]$[[1]]$[[2]]", options: "tA"},


    // Automatically convert text of the form "x=2" and "x=n+1" to math.
    {trigger: /([A-Za-z]=\d+)([\n\s.,?!:'])/, replacement: "$[[0]]$[[1]]", options: "rtAw"},
    {trigger: /([A-Za-z]=[A-Za-z][+-]\d+)([\n\s.,?!:'])/, replacement: "$[[0]]$[[1]]", options: "tAw"},

]
