<html>

<title>CMC BH-30 Controller Web Menu</title>

<body>

<h2>CMC BH-30 Controller Web Menu</h2>

%if name == '80H':
    <h3>Last tuned to {{name}}</h3>
%elif name == '80L':
    <h3>Last tuned to {{name}}</h3>
%elif name == '40L':
    <h3>Last tuned to {{name}}</h3>
%elif name == '40H':
    <h3>Last tuned to {{name}}</h3>
%elif name == '20L':
    <h3>Last tuned to {{name}}</h3>
%elif name == '20H':
    <h3>Last tuned to {{name}}</h3>
%elif name == '15':
    <h3>Last tuned to {{name}}</h3>
%elif name == '10':
    <h3>Last tuned to {{name}}</h3>
%else:
    <h3>Select a band...</h3>
%end

<button onclick="window.location.href = '/80L/80L';">80L</button>
<button onclick="window.location.href = '/80H/80H';">80H</button>
<button onclick="window.location.href = '/40L/40L';">40L</button>
<button onclick="window.location.href = '/40H/40H';">40H</button>
<button onclick="window.location.href = '/20L/20L';">20L</button>
<button onclick="window.location.href = '/20H/20H';">20H</button>
<button onclick="window.location.href = '/15/15';">15</button>
<button onclick="window.location.href = '/10/10';">10</button>

</body>

</html>
